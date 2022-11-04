from . import bubble

def teste_vazio():
    try:
        arr = []
        bubble.bubble_sort(arr)

        print('\nteste_vazio: ')
        for i in range(len(arr)):
            print("% d" % arr[i], end=" ")

        for i in range(len(arr)-1):
            if i == len(arr):
                break
            if arr[i] > arr[i+1]:
                print('\nteste_vazio: falha em organizar')
            
    except Exception as ex:
        print('\nErro na validação de dados no teste_vazio ')
        print(ex)

def teste_negativo():

    try:
        arr = [64, 34, 25,-2, 12, 22, 11, 90]
        bubble.bubble_sort(arr)

        print('\nteste_negativo: ')
        for i in range(len(arr)):
            print("% d" % arr[i], end=" ")

        for i in range(len(arr)-1):
            if i == len(arr):
                break
            if arr[i] > arr[i+1]:
                print('\nteste_negativo: falha em organizar')
            
    except Exception as ex:
        print('\nErro na validação de dados no teste_negativo ')
        print(ex)


def teste_string():

    try:
        arr = [64, 34, 25, '12', 22, 11, 90]
        bubble.bubble_sort(arr)
        
        print('\nteste_string: ')
        for i in range(len(arr)):
            print("% d" % arr[i], end=" ")

        for i in range(len(arr)-1):
            if i == len(arr):
                break
            if arr[i] > arr[i+1]:
                print('\nteste_string: falha em organizar')
            
    except Exception as ex:
        print('\nErro na validação de dados no teste_string ')
        print(ex)


def teste_caminho_feliz():

    try:
        arr = [64, 34, 25, 12, 22, 11, 90]
        bubble.bubble_sort(arr)

        print('\nteste_caminho_feliz: ' )
        for i in range(len(arr)):
            print("% d" % arr[i], end=" ")

        for i in range(len(arr)-1):
            if i == len(arr):
                break
            if arr[i] > arr[i+1]:
                print('\nteste_caminho_feliz: falha em organizar')
            
    except Exception as ex:
        print('\nErro na validação de dados no teste_caminho_feliz ')
        print(ex)

def teste_ponto_flutuante():

    try:
        arr = [64, 34, 25, 12.5, 22, 11, 90]
        bubble.bubble_sort(arr)

        print('\nteste_ponto_flutuante: ')
        for i in range(len(arr)):
            print("% f" % arr[i], end=" ")

        for i in range(len(arr)-1):
            if i == len(arr):
                break
            if arr[i] > arr[i+1]:
                print('\nteste_ponto_flutuante: falha em organizar')
            
    except Exception as ex:
        print('\nErro na validação de dados no teste_ponto_flutuante ')
        print(ex)


if '__main__':
    teste_caminho_feliz()
    teste_negativo()
    teste_string()
    teste_ponto_flutuante()
    teste_vazio()