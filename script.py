import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--test', action='store_true')
"""
A seguinte sequência iterativa é definida pelo conjunto de inteiros
positivos onde:
n -> n/2 (se n é par)
n -> 3n + 1 (se n é impar)
Por exemplo, usando as regras acima e começando pelo número 13,
nós geraríamos a seguinte sequência:
13 40 20 10 5 16 8 4 2 1
O que pode ser observado dessa sequência
(começando no 13 e terminando no 1) é que ela contém 10 items.
Embora ainda não esteja matematicamente provado, é esperando que,
dado um numero inteiro positivo qualquer,
a sequencia sempre chegará em 1.
"""


def is_odd(num): return num % 2 != 0


def create_collatz(first_num):
    """
    Cria Lista seguindo as regras do algoritimo
    """
    collatz = [first_num]
    next_number = first_num

    while next_number > 1:
        if is_odd(next_number):
            next_number = next_number * 3 + 1
        else:
            next_number = next_number/2
        collatz.append(int(next_number))

    return collatz


def find_list_more_lenght(lenght):
    """
    Busca uma lista com um comprimento maior que o valor 
    que foi passado por parametro
    """
    num = 1
    while len(create_collatz(num)) < lenght:
        num += 1

    return num


if __name__ == "__main__":

    args = parser.parse_args()

    if args.test:
        assert 10 == len(create_collatz(13))
        assert 1 == len(create_collatz(1))
        assert 2 == len(create_collatz(2))

        assert [1] == create_collatz(1)
        assert [2, 1] == create_collatz(2)
        assert [13, 40, 20, 10, 5, 16, 8, 4, 2, 1] == create_collatz(13)

    print(f"Numero que retornaria uma lista com tamanho maior que 10: {find_list_of_lenght(10)}")
