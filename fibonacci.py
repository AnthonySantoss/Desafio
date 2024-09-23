def fibonacci(n):
    # Inicializando os dois primeiros números da sequência de Fibonacci
    fib_sequence = [0, 1]
    
    # Gerar a sequência até que o último número seja maior ou igual ao número informado
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

def is_fibonacci_number(num):
    # Gerar a sequência de Fibonacci até o valor informado ou maior
    fib_sequence = fibonacci(num)
    
    # Verificar se o número está na sequência
    if num in fib_sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

# Solicitar entrada do usuário
numero = int(input("Informe um número: "))

# Verificar e exibir o resultado
print(is_fibonacci_number(numero))