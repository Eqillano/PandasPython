import pandas as pd


df = pd.read_json('json/small_data_contracts.json')

''' Задание 2.4 '''


# меняем тип данных что-бы можно было проводить с ними вычисления
df['From'] = pd.to_datetime(df['From'])
df['To'] = pd.to_datetime(df['To'])


#cоздаём столбец что-бы просчитать разницу во времени, затем фильтруем по длительности от 5 минут
df['duration'] = df['To'] - df['From']
df1 = df[df['duration'] >= '00:05:00']


#группируем по member_id и считаем кол-во контактов,сортируем в убывающем порядке

df1 = df1.groupby(['Member1_ID']).size().to_frame('count').reset_index().sort_values(['count'], ascending=[False])




'''   ЗАДАНИЕ 2.5

Вывести список людей, отсортированный в обратном порядке по общей длительности
контакта с другими людьми. '''

# группируем по Member1_ID и суммируем длительность котнтактов , сортируем по длительности и выводим в обратном порядке
df2 = df.groupby(['Member1_ID'])['duration'].sum().to_frame('sum_duration').reset_index()\
.sort_values(['sum_duration'],ascending=[False])
