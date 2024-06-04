import os
# função menu

def exibir_menu():
    print('1 - Área do círculo.')
    print('2 - Área do triângulo.')
    print('3 - Área do trapézio.')
    print('4 - Sair do programa.')

# função da área do círculo
def calcular_circulo(r):
    a = 3.14*r**2
    return a

def calcular_triangulo(b, h):
    h = (b*h)/2
    return h

def calcular_trapezio(base_menor, base_maior, h):
    a = ((base_menor + base_maior)*h)/2
    return a     
    
while True:
    exibir_menu()
    opcao = input('Opção desejada: ')
    os.system('cls')

    match opcao:
        case '1':
            print('Área do círculo: a = π*r²')
            r = int(input('Informe o valor do ráio: '))
            print(f'Área do círculo: {calcular_circulo(r)}. ')
            continue
        case '2':
            print('Área do triângulo: a = (b*a/2)')
            b = int(input('Informe o valor da base: '))
            h = int(input('Informe o valor da altura: '))
            print(f'Área do triângulo: {calcular_triangulo(b, h)}. ')
            continue
        case '3':
            print('Área do trapézio: a = ((b+B)*h)/2' )
            base_menor = int(input(f'Informe o valor da base menor: '))
            base_maior = int(input(f'Informe o valor da base maior: '))
            h = int(input(f'Informe o valor da altura do trapézio: '))
            print(f'Área do trapézio: {calcular_trapezio(base_menor, base_maior, h)}. ')
            continue
        case '4':
            break
        case _:
            print('Opção inválida. ')

