from mpi4py import MPI
import numpy as np

# Inicializar o ambiente MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Definir o tamanho do array a ser processado
n = 1000000

# Gerar um array de números aleatórios
if rank == 0:
    data = np.random.rand(n)
    print(f"Gerando array de tamanho {n} no processo {rank}")

# Distribuir o array entre os processos
data_split = np.array_split(data, comm.size)

# Processar o array em cada processo
result = np.zeros_like(data)
for i in range(len(data_split)):
    if rank == i:
        result[i*len(data_split[i]):(i+1)*len(data_split[i])] = np.sum(data_split[i])

# Agregar os resultados dos processos
result_agg = comm.allreduce(result, op=MPI.SUM)

# Imprimir o resultado final
if rank == 0:
    print(f"Resultado final: {result_agg}")

# Finalizar o ambiente MPI
comm.Finalize()