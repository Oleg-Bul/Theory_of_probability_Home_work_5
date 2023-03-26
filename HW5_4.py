import scipy.stats as stats

# Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169
# Рост взрослых дочерей:173, 175, 162, 174, 175, 168, 155, 170, 160

# Задачу решать с помощью функции.
# Есть ли статистически значимые различия в росте дочерей и матерей?

mothers = [172, 177, 158, 170, 178, 175, 164, 160, 169, 165]
daughters = [173, 175, 162, 174, 175, 168, 155, 170, 160, 163]

print(stats.ttest_rel(mothers, daughters))

print('Так как p_value > alpha(0.05) \
H0 - не отвергаем \
Статистически заничмых различий нет.')
