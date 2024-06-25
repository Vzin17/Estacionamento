'''
Autor: Vitor Josué Antonello Stolfo;
Data: 17/06/2024
'''
#Aqui eu fiz o dicionário para as especificações do carro
carros = {
        '':{
        'placa': 'CODE-0871',
        'marca': 'Audi',
        'cor': 'Preto',
        'proprietario': 'Vitor Antonello',
        'modelo': 'Audi-TT RS'
        }
}

#Aqui eu fiz o menu para escolher as opções, do que quer fazer!
def menu():
    print("1- Estacionar!")
    print("2- Retirar o carro!")
    print("3- Listar carros!")
    print("4- Verificar se está estacionado!")
    print("0- Sair")
    try:
        opt = int(input("Selecione uma opção: "))#Aqui é para digitar a opção que você quer fazer e retornar para o menu depois de fazer o que tem que ser feito
        return opt
    except Exception as e:
       print("numero digitado errado, burro!")#Aqui é para caso o usuário digite uma opção que não esxiste no menu para ele retornar e digitar o número certo

#Este 'def' é para adicionar os carros que vão ser estacionados
def estacionar():
    try:
        placa = input("digite a placa do carro: ")
        marca = input("informe a marca: ")
        cor = input("informe a cor: ")
        proprietario = input("informe o proprietario: ")
        modelo = input("informe o modelo: ")

        dados = {"placa": placa, "marca": marca,"cor": cor, "proprietario": proprietario, "modelo": modelo}
        carros[placa] = dados
    except Exception as e:
        print("algo foi digitado errado {e}")

#Aqui é para retirar, usei da placa como chave para aparecer e retirar o carro
def retirar():
    placa = input("digite a placa do carro ")
    if placa in carros:
        carro = carros.pop(placa)
        print(f"o carro:{carro['placa']} foi removido")
    else:
        print("o carro não foi estacionado, ou ouve erro de digitacao")
    input("fecha os olhos e clica em qualquer lugar, para continuar ")   

#Aqui é a lista onde eu peguei dos dados dos carros para dizer as especificações dos carros para enfim listar
def listar():
    for placa, dados in carros.items():
        print(f"placa: {placa} - marca: {dados['marca']} - cor: {dados['cor']} - proprietario: {dados['proprietario']} - modelo: {dados['modelo']}")
    input("fecha os olhos e clica em qualquer lugar, para continuar ")

#Verfica através da variável da placa para verificar se o carro está estacionado
def verificar():
    placa = input("digite a placa: ")
    if placa in carros:
        print("sim")
    else:
        print("nao")

#E aqui é o menu para digitar o que o usúario deseja fazer
if __name__ == '__main__':
    while True:
        match menu():
            case 1:
                estacionar()
            case 2:
                retirar()
            case 3:
                listar()
            case 4:
                verificar()
            case 0:
                break
