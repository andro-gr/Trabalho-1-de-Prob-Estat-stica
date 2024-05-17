import matplotlib.pyplot as plt
import seaborn as sns
from frequencias import *

# Gráfico de barras para Gênero
plt.figure(figsize=(8, 6))
sns.countplot(x='Genero', data=df)
plt.title('Distribuição por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.show()

# Gráfico de barras para Grau de Instrução
plt.figure(figsize=(10, 6))
sns.countplot(x='Grau_de_Instrucao', data=df)
plt.title('Distribuição por Grau de Instrução')
plt.xlabel('Grau de Instrução')
plt.ylabel('Contagem')
plt.xticks(rotation=45)
plt.show()

# Histograma para Número de Filhos
plt.figure(figsize=(8, 6))
sns.histplot(df['N_Filhos'], bins=10, kde=True)
plt.title('Distribuição de Número de Filhos')
plt.xlabel('Número de Filhos')
plt.ylabel('Frequência')
plt.show()

# Histograma para Idade
plt.figure(figsize=(8, 6))
sns.histplot(df['Idade'], bins=10, kde=True)
plt.title('Distribuição de Idade')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()

# Histograma para Altura
plt.figure(figsize=(8, 6))
sns.histplot(df['Altura'], bins=10, kde=True)
plt.title('Distribuição de Altura')
plt.xlabel('Altura')
plt.ylabel('Frequência')
plt.show()

# Histograma para Salário
plt.figure(figsize=(8, 6))
sns.histplot(df['Salario'], bins=10, kde=True)
plt.title('Distribuição de Salário')
plt.xlabel('Salário')
plt.ylabel('Frequência')
plt.show()
