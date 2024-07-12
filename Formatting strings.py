def competition(team1,team2,team1_num,team2_num,
                score_1,score_2,team1_time,team2_time ):
    # team1_score = dict(zip([team1],[score_1]))
    # team2_score = dict(zip([team2], [score_2]))
    tasks_total = score_1 + score_2
    time_avg = (team2_time + team1_time) / tasks_total
    print("В команде Мастера кода участников: %s ! " % team1_num)
    print("Итого сегодня в командах участников: %s и %s !" % (team1_num,team2_num))
    print("Команда Волшебники данных решила задач: {} !".format(score_2))
    print("Волшебники данных решили задачи за {} с !".format(team1_time))
    print(f"Команды решили {score_1} и {score_2} задач.")
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
        print(f'Результат битвы: {result}')
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
        print(f'Результат битвы: {result}')

    else:
        result = 'Ничья!'
        print(f'Результат битвы: {result}')

    # if team1_score.get(team1) > team2_score.get(team2):
    #     challenge_result = team1
    #     print(f"Результат битвы: победа команды {challenge_result}!")
    #
    # if team1_score.get(team1) < team2_score.get(team2):
    #     challenge_result = team2
    #     print(f"Результат битвы: победа команды {challenge_result}!")
    # else:
    #     print(f"Результат битвы: 'Ничья'!")


    print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")

competition('Мастера кода','Волшебники данных',
            6,6, 40,42,
            1552.512, 2153.31451)













#

