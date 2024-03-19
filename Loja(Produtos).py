# Aprendi uzar o metodo 'with open', peguei um exemplo deste site (tem bons exemplos e esta bem explicado):
# https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/


# Definindo a função para escrever no arquivo
def EscrNoArquivo(produto, preco):
    with open('produtos.txt', 'a') as file:
        file.write(f'{produto}: {preco} €\n')

# Iniciando o loop para adicionar produtos e preços
continuar = 'SIM'
while continuar.upper() == 'SIM':
    produto = input("Escreva o nome do produto: ")
    preco = input("Escreva o preço do produto: ")
    EscrNoArquivo(produto, preco)
    continuar = input("Quer adicionar mais um produto e preço? (SIM/NÃO): ")

# Mostrando os produtos do arquivo
print("\nProdutos no arquivo:")
with open('produtos.txt', 'r') as file:
    print(file.read())
