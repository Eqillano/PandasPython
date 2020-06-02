import pandas as pd


df = pd.read_json('TestJson/small_data_contracts.json')
#print(df.head())
''' Задание 2.4 '''

''' трансформируем два столбца что-бы можно было с ними проводить вычисление'''

df['From'] = pd.to_datetime(df['From'])
df['To'] = pd.to_datetime(df['To'])


''' cоздаём столбец что-бы просчитать время '''

df['duration'] = df['To'] - df['From']
df1 = df[df['duration'] >= '00:05:00']


''' группируем по member_id и считаем кол-во контактов в убывающем порядке '''

df1 = df1.groupby(['Member1_ID']).size().to_frame('count').reset_index().sort_values(['count'], ascending=[True])


'''   ЗАДАНИЕ 2.5

Вывести список людей, отсортированный в обратном порядке по общей длительности
контакта с другими людьми. '''


df2 = df.groupby(['Member1_ID'])['duration'].sum().to_frame('sum_duration').reset_index().sort_values(['sum_duration'],ascending=[False])
print(df2)
