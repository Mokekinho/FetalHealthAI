import pandas as pd

df = pd.read_csv("fetal_health.csv")

print(df.info())

print("-----"*20)


print(f"Total de amostras: {len(df)}")

# Contagem de classes
print("\nAmostras por classe:")
print(df['fetal_health'].value_counts())

print("\nDistribuição percentual das classes:")
print(df['fetal_health'].value_counts(normalize=True) * 100)

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

# Seu código para gerar o gráfico:
df['fetal_health'].value_counts().sort_index().plot(
    kind='bar', 
    title='Distribuição das Classes de Saúde Fetal',
    xlabel='Classe (1=Normal, 2=Suspeito, 3=Patológico)',
    ylabel='Número de amostras'
)

# ➡️ NOVA LINHA: Use plt.savefig() no lugar de plt.show()
plt.savefig('distribuicao_saude_fetal.png')

print("\nValores nulos por coluna:")
print(df.isnull().sum())