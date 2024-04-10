import gym
import tensorflow as tf
import tensorflow_addons as tfa
import numpy as np
import matplotlib.pyplot as plt

# Definir o ambiente
env = gym.make('CartPole-v1')
state_size = env.observation_space.shape[0]
action_size = env.action_space.n

# Construir a rede neural
model = tf.keras.Sequential([
    tf.keras.layers.Dense(24, input_shape=(state_size,), activation='relu'),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(action_size, activation='linear')
])

model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(lr=0.001))

# Parâmetros do agente
gamma = 0.95
epsilon = 1.0
epsilon_min = 0.01
epsilon_decay = 0.995
episodes = 1000

# Função de escolha da ação
def choose_action(state):
    if np.random.rand() <= epsilon:
        return env.action_space.sample()
    return np.argmax(model.predict(state)[0])

# Loop de treinamento
for episode in range(episodes):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    done = False
    total_reward = 0

    while not done:
        action = choose_action(state)
        next_state, reward, done, _ = env.step(action)
        next_state = np.reshape(next_state, [1, state_size])
        total_reward += reward

        target = reward + gamma * np.amax(model.predict(next_state)[0])
        target_f = model.predict(state)
        target_f[0][action] = target

        model.fit(state, target_f, epochs=1, verbose=0)
        state = next_state

    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

    print(f'Episode: {episode + 1}, Total Reward: {total_reward}')

env.close()
