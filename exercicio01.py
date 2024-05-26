from random import randint


class Questao01:
    """
    classe que calcula o imposto de peixes pescados
    """
    fish_max_weight = 50
    tax = 4
    tax_total = 0

    def __init__(self, fish_weight):
        self.fish_weight = fish_weight

    def gets_total_tax(self):
        if self.fish_weight > self.fish_max_weight:
            self.tax_total = self.tax * (self.fish_weight - self.fish_max_weight)
        return self.tax_total

class Questao02:
    """
    classe que calcula o salário total de um funcionário
    """
    def __init__(self, per_hour, per_month_worked):
        self.per_hour = per_hour
        self.per_month_worked = per_month_worked
        self.total_salary = self.per_hour * self.per_month_worked
        return print(f'O salário total é de R${self.total_salary:.2f}')

class Questao03:
    """
    ao ser chamada, gera uma lista de 30 números aleatórios de 1 a 100
    """
    def __init__(self):
        self.bingo_list = [randint(1, 100) for i in range(1, 31)]
        return print(f'Os números sorteados foram: {self.bingo_list}')

class Questao04:
    ticket = 20
    age = range(1, 101)

    def __init__(self, age):
        if age <= 18:
            self.ticket = self.ticket * 0.5
            return print(f'O valor do ingresso é de R${self.ticket:.2f}')
        elif age >= 60:
            self.ticket = self.ticket * 0.5
            return print(f'O valor do ingresso é de R${self.ticket:.2f}')
        return print(f'O valor do ingresso é de R${self.ticket:.2f}')



class Questao05:
    """
    classe que gera o total de um salário após aumento de 1.5% em um numero de anos
    """
    def __init__(self, wage, raise_percent):
        self.wage = wage
        self.raise_percent = raise_percent
        self.total_wage = self.wage * (1 + self.raise_percent / 100) * 12
        return print(f'O salário total é de R${self.total_wage:.2f}')

Questao05(1000, 10)
