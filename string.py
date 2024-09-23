def contar_a(texto):
    # Contar a ocorrência de 'a' ou 'A'
    contador = texto.lower().count('a')
    
    # Verificar se a letra 'a' está presente e exibir o resultado
    if contador > 0:
        return f"A letra 'a' ocorre {contador} vez(es) na string."
    else:
        return "A letra 'a' não foi encontrada na string."

# Solicitar a string do usuário
entrada = input("Digite uma string: ")

# Exibir o resultado
print(contar_a(entrada))