from dados import *

# Medidas de posição e variabilidade para Número de Filhos
print("Medidas de Posição e Variabilidade para Número de Filhos:")
print("Média:", round(df['N_Filhos'].mean(), 2))
print("Mediana:", round(df['N_Filhos'].median(), 2))
print("Moda:", round(df['N_Filhos'].mode()[0], 2))
print("Desvio Padrão:", round(df['N_Filhos'].std(), 2))
print("Amplitude:", round(df['N_Filhos'].max() - df['N_Filhos'].min(), 2))
print("\n")
# Medidas de posição e variabilidade para Idade
print("Medidas de Posição e Variabilidade para Idade:")
print("Média:", round(df['Idade'].mean(), 2))
print("Mediana:", round(df['Idade'].median(), 2))
print("Moda:", round(df['Idade'].mode()[0], 2))  # Se houver múltiplas modas, mode() retorna uma série, pegamos o
# primeiro valor
print("Desvio Padrão:", round(df['Idade'].std(), 2))
print("Amplitude:", round(df['Idade'].max() - df['Idade'].min(), 2))
print()

# Medidas de posição e variabilidade para Altura
print("Medidas de Posição e Variabilidade para Altura:")
print("Média:", round(df['Altura'].mean(), 2))
print("Mediana:", round(df['Altura'].median(), 2))
print("Moda:", round(df['Altura'].mode()[0], 2))
print("Desvio Padrão:", round(df['Altura'].std(), 2))
print("Amplitude:", round(df['Altura'].max() - df['Altura'].min(), 2))
print()

# Medidas de posição e variabilidade para Salário
print("Medidas de Posição e Variabilidade para Salário:")
print("Média:", round(df['Salario'].mean(), 2))
print("Mediana:", round(df['Salario'].median(), 2))
print("Moda:", round(df['Salario'].mode()[0], 2))
print("Desvio Padrão:", round(df['Salario'].std(), 2))
print("Amplitude:", round(df['Salario'].max() - df['Salario'].min(), 2))
