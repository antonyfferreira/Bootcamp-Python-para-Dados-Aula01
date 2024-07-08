CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite o seu salario: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o seu bonus: "))

# 4) Calcule o valor do bônus final

valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus
print(f"O usuario {nome_usuario} possui o bonus de {valor_do_bonus}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

# Validação da Entrada de Dados:

# O código assume que o usuário sempre digitará entradas válidas. 
# Se o usuário digitar algo que não possa ser convertido para float, ocorrerá uma exceção.
# Solução: Adicionar validação e tratamento de exceções para garantir que as entradas sejam válidas.
# Formatação de Saída:

# Para garantir que o valor do bônus seja exibido com duas casas decimais, adicionar:.2f na f-string.
# Exemplo: print(f"O usuário {nome_usuario} possui o bônus de {valor_do_bonus:.2f}")