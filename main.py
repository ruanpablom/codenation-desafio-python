import csv
from decimal import Decimal

class Data:
    def __init__(self):
        self.datas = []

    def load_data(self):
        with open('data.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.datas.append(row)
    
    def get_datas(self):
        return self.datas

data = Data()
data.load_data()
    

# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.



# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
#
def q_1():
    nationalitys={}
    for row in data.get_datas():
        nationality = row['nationality']
        nationalitys[nationality] = 0
    return len(nationalitys)

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    clubs={}
    for row in data.get_datas():
        club = row['club']
        clubs[club] = 0
    return len(clubs)

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    players = [];
    count = 0;
    for item in data.get_datas():
        players.append(item['full_name'])
        count+=1
        if count == 20:
            break

    return players;

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?


def q_4():
    best_wages = [0,0,0,0,0,0,0,0,0,0]
    players = ["","","","","","","","","",""]

    for item in data.get_datas():
        if Decimal(item['eur_wage']) > best_wages[9]:
            for index,wage in enumerate(best_wages):
                if Decimal(item['eur_wage']) > wage:
                    best_wages.insert(index,Decimal(item['eur_wage']))
                    del best_wages[-1]
                    players.insert(index,item['full_name'])
                    del players[-1]
                    break
    return players

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    olders = [0,0,0,0,0,0,0,0,0,0]
    players = ["","","","","","","","","",""]

    for item in data.get_datas():
        if Decimal(item['age']) > olders[9]:
            for index,age in enumerate(olders):
                if Decimal(item['age']) > age:
                    olders.insert(index,Decimal(item['age']))
                    del olders[-1]
                    players.insert(index,item['full_name'])
                    del players[-1]
                    break
    return players

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    ages = {}
    for item in data.get_datas():
        if int(item['age']) in ages:
            ages[int(item['age'])] += 1
        else:
            ages[int(item['age'])] = 1
    return ages
