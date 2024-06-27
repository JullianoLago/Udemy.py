# Operadores Lógicos
# and (e), or(ou), not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira
# será avaliada naquele valor.
# São considerados falsos ( 0, 0.0, False, " ")
# Também existem o None que é usado para representar um NÃO valor

Decisao = input("Voce deseja [E]ntrar ou [S]air? ")
Val_Senha = input("Digite a senha: ")
Senha = "123456"


if Decisao == "E" and Val_Senha == Senha:
    print("Você entrou")
elif Decisao == "S":
    print("Você saiu")

else:
    print("Comando errado.Tente Novamente")