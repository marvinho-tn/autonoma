import pandas as pd

# Carregar o CSV em um DataFrame do Pandas
df = pd.read_csv("dados.csv")

# Criar as colunas xrav e yrav a partir de outras colunas existentes
df["xrav"] = df["sensor1"]
df["yrav"] = df["sensor2"]

# Converter as colunas relevantes em valores numéricos
df["xrav"] = df["xrav"].astype(float)
df["yrav"] = df["yrav"].astype(float)

# Mapear as outras colunas para variáveis
sensor1 = df["xrav"].values
sensor2 = df["yrav"].values
sensor3 = df["sensor3"].astype(float).values
latitude = df["latitude"].astype(float).values
longitude = df["longitude"].astype(float).values
acao = df["acao"].astype(int).values
recompensa = df["recompensa"].astype(int).values

# Mapear as colunas com valores string para variáveis
imagem_path = df["imagem_path"].values
anotacao_path = df["anotacao_path"].values
estado_trafego = df["estado_trafego"].values

# Exibir os valores das variáveis
print("sensor1:", sensor1)
print("sensor2:", sensor2)
print("sensor3:", sensor3)
print("imagem_path:", imagem_path)
print("anotacao_path:", anotacao_path)
print("latitude:", latitude)
print("longitude:", longitude)
print("acao:", acao)
print("recompensa:", recompensa)
print("estado_trafego:", estado_trafego)