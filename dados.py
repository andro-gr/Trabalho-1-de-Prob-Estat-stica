import pandas as pd

# Criando o dicionário com os dados
dados = {
    "Genero": ["M", "F", "M", "M", "F", "F", "M", "M", "M", "M",
               "F", "F", "F", "F", "F", "M", "M", "M", "F", "M",
               "M", "F", "F", "F", "M", "F", "F", "M", "M", "F"],
    "Grau_de_Instrucao": ["Superior", "Superior", "Superior", "Ens Fundamental", "Ensino Médio",
                          "Superior", "Ens Fundamental", "Superior", "Superior", "Ensino Médio",
                          "Superior", "Ensino Médio", "Ensino Médio", "Ensino Médio", "Ensino Médio",
                          "Superior", "Superior", "Superior", "Ensino Médio", "Ensino Médio",
                          "Ens Fundamental", "Ens Fundamental", "Ensino Médio", "Superior", "Ensino Médio",
                          "Ens Fundamental", "Superior", "Ens Fundamental", "Superior", "Superior"],
    "N_Filhos": [1, 0, 0, 0, 0, 2, 0, 0, 1, 2,
                 0, 3, 0, 0, 1, 1, 0, 0, 2, 2,
                 2, 0, 0, 2, 4, 1, 1, 0, 0, 1],
    "Idade": [31, 25, 33, 20, 23, 37, 38, 37, 34, 40,
              41, 46, 26, 41, 43, 27, 26, 42, 43, 30,
              35, 33, 30, 32, 29, 40, 36, 32, 31, 35],
    "Altura": [160, 160, 157, 163, 163, 155, 165, 168, 163, 170,
               170, 157, 165, 160, 173, 175, 145, 165, 157, 163,
               168, 183, 175, 185, 173, 173, 191, 188, 193, 170],
    "Salario": [4.10, 2.65, 4.70, 1.45, 1.85, 2.20, 2.35, 2.70, 2.90, 1.60,
                3.00, 3.45, 1.00, 1.70, 1.85, 2.10, 3.20, 5.80, 4.30, 2.75,
                3.40, 2.05, 2.30, 3.30, 3.65, 3.65, 4.15, 1.90, 3.10, 4.00]
}

# Convertendo o dicionário para um DataFrame do pandas
df = pd.DataFrame(dados)
