#Para provar a Lei dos Grandes Números e Teorema Central do Limite simule 1000 lançamentos de moeda em Python. 
#Verifique nas animações que a taxa de sucessos ("caras"/"coroas + caras") converge com o tempo para 0.5.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definir parâmetros da simulação
n_lancamentos = 1000
n_simulacoes = 5  # Número de curvas
p = 0.5  # Probabilidade de sucesso (cara)

# Simular os lançamentos para cada simulação
lancamentos = np.random.binomial(1, p, (n_simulacoes, n_lancamentos))
taxa_sucessos = np.cumsum(lancamentos, axis=1) / np.arange(1, n_lancamentos + 1)

# Calcular a média amostral
media_amostral = np.mean(taxa_sucessos, axis=0)

# Configurar a animação
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Configuração do gráfico da taxa de sucessos
ax1.set_xlim(0, n_lancamentos)
ax1.set_ylim(0, 1)
ax1.set_xlabel("Número de Lançamentos")
ax1.set_ylabel("Taxa de Sucessos")
ax1.set_title("Taxa de Sucessos por Número de Lançamentos")

# Configuração do gráfico da média amostral
ax2.set_xlim(0, n_lancamentos)
ax2.set_ylim(0, 1)
ax2.set_xlabel("Número de Lançamentos")
ax2.set_ylabel("Média Amostral")
ax2.set_title("Média Amostral")

# Criar múltiplas linhas, uma para cada simulação
lines = [ax1.plot([], [], lw=2)[0] for _ in range(n_simulacoes)]
colors = plt.cm.jet(np.linspace(0, 1, n_simulacoes))  # Paleta de cores

# Aplicar as cores diferentes às linhas
for line, color in zip(lines, colors):
    line.set_color(color)

# Linha da média amostral
linha_media, = ax2.plot([], [], color='black', lw=2)

def update(frame):
    # Atualizar os dados das linhas de taxa de sucesso
    for i, line in enumerate(lines):
        line.set_data(np.arange(1, frame + 1), taxa_sucessos[i, :frame])
    
    # Atualizar os dados da linha da média amostral
    linha_media.set_data(np.arange(1, frame + 1), media_amostral[:frame])
    
    return lines + [linha_media]

ani = FuncAnimation(fig, update, frames=n_lancamentos, blit=True, interval=10, repeat=False)

# Adicionar histograma das médias amostrais ao final
plt.figure(figsize=(8, 4))
plt.hist(media_amostral, bins=30, edgecolor='black', alpha=0.7)
plt.xlabel("Taxa de Sucessos")
plt.ylabel("Frequência")
plt.title("Distribuição das Médias Amostrais")

plt.show()
