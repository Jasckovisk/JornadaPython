import os
import sys

def processoresposta(resposta, nome):
    if resposta == '0':
        print('Até logo!')
        sys.exit()
    elif resposta == '1': 
        print(f'{os.linesep}{nome} o cultivo é feito através de um meio de cultura, onde um grão rico em amido é preparado, hidratado e esterilizado em uma panela de pressão e em seguida, é "semeado" utilizando um inóculo contendo a matriz de origem do fungo, para criar a colônia. A colônia quando completa seu desenvolvimento, pode ser frutificada para obter-se os cogumelos em uma terrário(câmara úmida).')
    elif resposta == '2':
        print(f'{os.linesep}{nome} o investimento varia de acordo com a quantidade de cogumelos a ser produzido, pois quanto maior a produção, maior a necessidade de equipamentos e substratos para o desenvolvimento. Uma produção pequena (doméstica) pode ser iniciada com pouco investimento, tendo em vista que a maioria dos materiais utilizados são de uso comum. Em nossa loja existem kits a partir de 50 Reais para criar sua colônia, e kits com colônias prontas disponíveis a partir de 100 Reais.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} a média de produção de uma colônia em boas condições é de 3 vezes. Em alguns casos elas produzem até 6 vezes, diminuindo sua produtividade a cada colheita.{os.linesep}')
    elif resposta == '4':
        print(
            f'{os.linesep}{nome} é a solução ou substrato utilizado para proliferar a colônia. O meio de cultura pode ser um substrato ou uma cultura a ser colonizada.{os.linesep}')
    elif resposta == '5':
        print(
            f'{os.linesep}{nome} terrário é o termo utilizado para descrever o local onde se cultiva o cogumelo, seguindo o princípio de câmara úmida. Geralmente uma caixa organizadora entre 35 e 50L.{os.linesep}')
    elif resposta == '6':
        print(
            f'{os.linesep}{nome} é a matriz de origem do fungo que será cultivado. Pode ser uma cultura líquida, solução de esporos ou um bolo/spawn colonizado.{os.linesep}')
    elif resposta == '7':
        print(
            f'{os.linesep}{nome} consiste de uma massa de ramificação formada por um conjunto de hifas do fungo emaranhadas.{os.linesep}')
    elif resposta == '8':
        print(
            f'{os.linesep}{nome} bolo é o termo utilizado para os copos onde posteriormente serão desenvolvidas as colônias do fungo. Geralmente são feitos com a receita clássica PFTEK (arroz integral + vermiculita). O bolo é um meio de cultura.{os.linesep}')
    elif resposta == '9':
        print(
            f'{os.linesep}{nome} os casings são colônias preparadas prontas para frutificação. Geralmente são confeccionados a partir de grãos colonizados e vermiculita estéril.{os.linesep}')
    elif resposta == '10':
        print(
            f'{os.linesep}{nome} cultura líquida é o exemplo de micélio vivo desenvolvido em uma solução nutritiva (água destilada + dextrose). Elas são amplamente utilizadas para acelerar o processo de colonização do fungo no substrato, uma vez que o micélio do fungo já está desenvolvido, o tempo de colonização do substrato é menor.{os.linesep}')
    elif resposta == '11':
        print(
            f'{os.linesep}{nome} carimbo é o termo utilizado para se referir aos esporos do fungo que são depositados no papel laminado. São utilizados para iniciar o cultivo de cogumelo.{os.linesep}')
    elif resposta == '12':
        print(
            f'{os.linesep}{nome} spawn é o termo utilizado para descrever os cereais(em grãos) devidamente preparados para crescimento de fungos. São utilizados para propagação de diversas espécies de cogumelos. Geralmente é utilizado: trigo, sorgo, centeio, cevada, malte, painço, arroz, etc..{os.linesep}')
    elif resposta == '13':
        print(
            f'{os.linesep}{nome} a solução de esporos é confeccionada a partir de um carimbo de esporos + água destilada. São utilizadas para iniciar o desenvolvimento do fungo no substrato ao qual deseja iniciar o cultivo.{os.linesep}')
    elif resposta == '14':
        print(
            f'{os.linesep}{nome} contaminação é o termo utilizado para descrever a presença de outros microrganismos competidores ao substrato onde se cultiva o fungo.{os.linesep}')
    elif resposta == '15':
        print(
            f'{os.linesep}{nome} quando o objeto ou superfície no qual microrganismos são ausentes ou incapazes de se reproduzir. É considerado um artigo estéril quando a probabilidade de sobrevivência dos microrganismos é menor do que 1:1.000.000.{os.linesep}')
    elif resposta == '16':
        print(
            f'{os.linesep}{nome} processo pelo qual os microrganismos são mortos ao ponto que não sejam mais detectáveis. Existem diversas técnicas de esterilização de materiais, como autoclave, chama, forno, produtos químicos bactericidas ou bacteriostáticos, radiação UV, ultrafiltração, etc. No cultivo de cogumelos, a esterilização é feita através do vapor úmido(TEMPERATURA+VAPOR=PRESSÃO).{os.linesep}')
    elif resposta == '17':
        print(
            f'{os.linesep}{nome} é o processo do desenvolvimento do fungo no substrato. Desenvolvimento da colônia.{os.linesep}')
    elif resposta == '18':
        print(
            f'{os.linesep}{nome} é o termo utilizado para descrever as levas de cogumelos que nascem na colônia. Exemplo: O casing está no segundo flush (Segunda leva de produção).{os.linesep}')
    elif resposta == '19':
        print(
            f'{os.linesep}{nome} dunk ou hidratação é a técnica utilizada para hidratar as colônias após frutificação.{os.linesep}')
    elif resposta == '20':
        print(
            f'{os.linesep}{nome} todas as variedades de Psilocybe cubensis têm a potência muito próxima ou semelhante. Também é observado que os parâmetros de cultivo determinam a potência do fruto.{os.linesep}')
    else:
        print('Digite de 1 à 20')
        return False

def start():
    # Apresentação do chatbot
    print('Olá, bem-vindo ao Cultivo Mágico!')
    # Solicitar o nome
    nome = input('Digite seu nome: ')
    # Pedir o e-mail
    email = input('Digite seu email: ')
    while True:
        # Mostrar meu de opções
        resposta = input(
            f'{os.linesep}{nome}, o que gostaria de saber hoje sobre o Cultivo Mágico?{os.linesep}{os.linesep}[1] - Como se cultiva Psilocybe cubensis?{os.linesep}[2] - Quanto preciso investir para cultivar Psilocybe cubensis?{os.linesep}[3] - Quantas vezes uma colônia produz?{os.linesep}[4] - O que é um meio de cultura?{os.linesep}[5] - O que é terrário?{os.linesep}[6] - O que é inóculo?{os.linesep}[7] - O que é micélio?{os.linesep}[8] - O que é bolo?{os.linesep}[9] - O que é um casing?{os.linesep}[10] - O que é uma cultura líquida?{os.linesep}[11] - O que é um carimbo de esporos?{os.linesep}[12] - O que é spawn? {os.linesep}[13] - O que é uma solução de esporos?{os.linesep}[14] - O que é contaminação?{os.linesep}[15] - O que é estéril?{os.linesep}[16] - O que é esterilização?{os.linesep}[17] - O que é colonização?{os.linesep}[18] - O que é flush?{os.linesep}[19] - O que é dunk?{os.linesep}[20] - Qual variedade de Psilocybe cubensis é mais potente?{os.linesep}{os.linesep}Digite de 1 à 20{os.linesep}') 
        # Processar resposta enviada
        if processoresposta(resposta, nome):
            break

if __name__ == '__main__':
    start()
