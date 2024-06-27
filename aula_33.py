numero_1 = input("Digite um número: ")
numero_2 = input("Digite outro número: ")

int_numero_1 = int (numero_1)   #evitar que o programa quebre caso o usuário digite uma letra
int_numero_2 = int (numero_2)

print(f"A soma desses dois números inteiros é de: {int_numero_1 + int_numero_2}.")