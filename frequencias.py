from dados import *

# Frequência Simples de Gênero
frequencia_genero = df['Genero'].value_counts().sort_index()
print("Frequência Simples de Gênero:")
print(pd.DataFrame({'Frequência': frequencia_genero}))
print()

# Frequência Relativa de Gênero
frequencia_relativa_genero = df['Genero'].value_counts(normalize=True).sort_index() * 100
print("Frequência Relativa (%) de Gênero:")
print(pd.DataFrame({'Frequência Relativa (%)': frequencia_relativa_genero}))
print()

# Frequência Simples de Grau de Instrução
frequencia_instrucao = df['Grau_de_Instrucao'].value_counts().sort_index()
print("Frequência Simples de Grau de Instrução:")
print(pd.DataFrame({'Frequência': frequencia_instrucao}))
print()

# Frequência Relativa de Grau de Instrução
frequencia_relativa_instrucao = df['Grau_de_Instrucao'].value_counts(normalize=True).sort_index() * 100
print("Frequência Relativa (%) de Grau de Instrução:")
print(pd.DataFrame({'Frequência Relativa (%)': frequencia_relativa_instrucao}))
print()


# Função para calcular frequências simples e relativas
def calcular_frequencias(coluna):
    frequencia_simples = coluna.value_counts().sort_index()
    frequencia_relativa = coluna.value_counts(normalize=True).sort_index() * 100
    return frequencia_simples, frequencia_relativa


# Calcular frequências para N_Filhos
frequencia_simples_filhos, frequencia_relativa_filhos = calcular_frequencias(df['N_Filhos'])
print("Frequência Simples de Número de Filhos:")
print(pd.DataFrame({'Frequência': frequencia_simples_filhos}))
print("\nFrequência Relativa (%) de Número de Filhos:")
print(pd.DataFrame({'Frequência Relativa (%)': frequencia_relativa_filhos}))
print()

# Calcular frequências para Idade
frequencia_simples_idade, frequencia_relativa_idade = calcular_frequencias(df['Idade'])
print("Frequência Simples de Idade:")
print(pd.DataFrame({'Frequência': frequencia_simples_idade}))
print("\nFrequência Relativa (%) de Idade:")
print(pd.DataFrame({'Frequência Relativa (%)': frequencia_relativa_idade}))
print()

# Calcular frequências para Altura
frequencia_simples_altura, frequencia_relativa_altura = calcular_frequencias(df['Altura'])
print("Frequência Simples de Altura:")
print(pd.DataFrame({'Frequência': frequencia_simples_altura}))
print("\nFrequência Relativa (%) de Altura:")
print(pd.DataFrame({'Frequência Relativa (%)': frequencia_relativa_altura}))
print()

# Calcular frequências para Salário
frequencia_simples_salario, frequencia_relativa_salario = calcular_frequencias(df['Salario'])
print("Frequência Simples de Salário:")
print(pd.DataFrame({'Frequência': frequencia_simples_salario}))
print("\nFrequência Relativa (%) de Salário:")
print(pd.DataFrame({'Frequência Relativa (%)': frequencia_relativa_salario}))
