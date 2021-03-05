per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input("Введите сумму вклада\n"))
deposite = list(map(lambda x: x * money / 100, per_cent.values()))

print("Максимальная сумма, которую вы можете заработать — " + str(max(deposite)))
