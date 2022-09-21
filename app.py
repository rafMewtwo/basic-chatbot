import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} a LOLDesign faz orcamentos para varios tipos de projetos, para diversos tipos de segmentos e empresas.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} a LOLDesign trabalha com diversas stacks e linguagems, entre elas frontend, backend e mobile.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} a LOLDesign trabalha com todo tipo de projetos{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} se o seu projeto for um legado, podemos fazer uma analise para entender seu contexto{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')

def start():
    #   Apresentar o chat bot
    print('Olá Bem-vindo a LolDesign')
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    while True:
        #   Oferecer o menu de opcoes
        resposta = input(f'O que gostaria de saber hoje?{os.linesep}[1] - A LOLDesign faz orcamentos de projetos?{os.linesep}[2] - Quais as stacks a LOLDesign trabalha?{os.linesep}[3] - A LOLDesign pode dar suporte para meus projetos?{os.linesep}[4] - A LOLDesign trabalha com projetos legados?')
        if resposta == 'parar':
            break
        #   Processar a resposta enviada
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()
    