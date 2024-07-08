CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite o seu nome: ")

try:
    # 2) Solicita ao usuário que digite o valor do seu salário
    salario_usuario = float(input("Digite o seu salário: "))
    
    # 3) Solicita ao usuário que digite o valor do bônus recebido
    bonus_usuario = float(input("Digite o seu bônus: "))
    
    # 4) Calcule o valor do bônus final
    valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario
    
    # 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bônus
    print(f"O usuário {nome_usuario} possui o bônus de {valor_do_bonus:.2f}")
except ValueError:
    print("Por favor, digite valores numéricos válidos para o salário e o bônus.")
