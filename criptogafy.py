
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. DADOS E MODELO MATEMÁTICO
# ==========================================

primeira_amostra = [
    6.5, 7, 5, 8, 7.5, 5.5, 6, 9,
    7, 6.5, 4, 8.5, 7, 6
]

segunda_amostra = [
    7, 8, 8, 5.5, 7.5, 6.5, 8, 7, 6, 5
]

# Calculando média e desvio padrão
media = np.mean(primeira_amostra)
desvio = np.std(primeira_amostra, ddof=1)

print("MODELO DE PREVISÃO DO TEMPO DE SONO")
print("-----------------------------------")
print(f"Média: {media:.2f} horas")
print(f"Desvio padrão: {desvio:.2f} horas")

# ==========================================
# 2. SIMULANDO UMA POPULAÇÃO
# ==========================================

distribuicao = np.random.normal(
    loc=media,
    scale=desvio,
    size=100000
)

print(f"\nPopulação simulada: {len(distribuicao)} pessoas")

# ==========================================
# 3. ANALISANDO INTERVALOS
# ==========================================

limite_68_min = media - desvio
limite_68_max = media + desvio

limite_95_min = media - 2 * desvio
limite_95_max = media + 2 * desvio

limite_997_min = media - 3 * desvio
limite_997_max = media + 3 * desvio

print("\nINTERVALOS ESTATÍSTICOS")

print(f"68%: {limite_68_min:.2f} até {limite_68_max:.2f}")
print(f"95%: {limite_95_min:.2f} até {limite_95_max:.2f}")
print(f"99,7%: {limite_997_min:.2f} até {limite_997_max:.2f}")

# ==========================================
# 4. VALIDANDO COM A SEGUNDA AMOSTRA
# ==========================================

segunda_amostra_np = np.array(segunda_amostra)

faixa = (
    (segunda_amostra_np >= limite_68_min) &
    (segunda_amostra_np <= limite_68_max)
)

valor_observado = faixa.mean() * 100

print("\nVALIDAÇÃO DO MODELO")
print(f"Modelo prevê aproximadamente: 68%")
print(f"Valor observado: {valor_observado:.2f}%")

# ==========================================
# 5. ANALISANDO FENÔMENOS PREVISÍVEIS
# ==========================================

fenomenos = {
    "Estatura média da população": "Fácil",
    "Tempo de deslocamento habitual": "Moderado",
    "Preço do dólar amanhã": "Difícil",
    "Música mais viral da internet": "Muito difícil"
}

print("\nANÁLISE DE PREVISIBILIDADE")

for fenomeno, dificuldade in fenomenos.items():
    print(f"{fenomeno}: {dificuldade}")

# ==========================================
# 6. VISUALIZANDO A DISTRIBUIÇÃO
# ==========================================

plt.hist(
    distribuicao,
    bins=50,
    density=True,
    color="steelblue",
    edgecolor="black",
    alpha=0.65,
    label="População simulada"
)

plt.axvline(
    media,
    color="red",
    linestyle="-",
    label="Média"
)

plt.axvspan(
    limite_68_min,
    limite_68_max,
    color="green",
    alpha=0.15,
    label="Intervalo de 68%"
)

plt.axvspan(
    limite_95_min,
    limite_95_max,
    color="orange",
    alpha=0.10,
    label="Intervalo de 95%"
)

plt.xlabel("Horas de sono")
plt.ylabel("Densidade")
plt.title("Modelo matemático do tempo de sono")
plt.legend()
plt.show()

# ==========================================
# 7. CONCLUSÃO
# ==========================================

print("\nCONCLUSÃO DO PROJETO")
print("O modelo matemático é uma aproximação da realidade.")
print("Fenômenos estáveis são geralmente mais previsíveis.")
print("Fenômenos voláteis são mais difíceis de prever.")
print("A validação com novos dados é fundamental.")
