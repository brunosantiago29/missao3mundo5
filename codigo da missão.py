import pandas as pd

df = pd.read_csv('Downloads/id.csv', sep=',', engine='python', encoding='utf-8')
print(df.head())

df = pd.read_csv('Downloads/id.csv') 
print(df.head())

df = pd.read_csv('Downloads/id.csv', sep=';') 


print(df.head())


dados = df

print(dados.describe())  

print(dados.info())


print(dados.head())

print(dados.tail())

# Cria uma cópia do DataFrame original
dados_copia = dados.copy()

# Verifica se a cópia foi criada com sucesso
print(dados_copia.head())
print(dados.columns)

print(dados.columns) 

# Substitui valores nulos na coluna 'Calories' por 0
dados['Calories'].fillna(0, inplace=True)  

# Substitui valores nulos na coluna 'Date' por '1900/01/01'
dados['Date'].fillna('1900/01/01', inplace=True)


# Transforma os dados da coluna 'Date' em datetime
dados_copia['Date'] = pd.to_datetime(dados_copia['Date'], errors='coerce')

print(dados_copia)

dados_copia['Date'] = dados_copia['Date'].replace('1900/01/01', pd.NaT)

# Transforma a coluna 'Date' para datetime
dados_copia['Date'] = pd.to_datetime(dados_copia['Date'])


print(dados_copia.head())


dados_copia['Date'] = dados_copia['Date'].replace('20201226', '2020/12/26')

# Transforma a coluna 'Date' para datetime
dados_copia['Date'] = pd.to_datetime(dados_copia['Date'])


print(dados_copia.head())


# Transforma a coluna 'Date' para datetime
dados_copia['Date'] = pd.to_datetime(dados_copia['Date'])


print(dados_copia.head())

# Remove registros com valores nulos na coluna 'Date'
dados_copia.dropna(subset=['Date'], inplace=True)


print(dados_copia.head())

# Imprime o DataFrame para verificar as transformações
print(dados_copia)
