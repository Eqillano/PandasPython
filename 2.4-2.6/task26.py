import pandas as pd


df = pd.read_json('json/small_data_contracts.json')
df2 = pd.read_json('json/small_data_persons.json')

#print(df.head())
#print(df2.head())


'''
Задание 2.6

Найти возрастную группу людей, которая имеет наиболее частый контакт с другими
людьми. Так же, как и в задании 2.1 контактом считается контакт длительностью 5 и более'''

# соединяем две талблицы используя inner join
dfx = pd.merge(df,df2,left_on='Member1_ID',right_on='ID',how='inner')

#меняем тип данных что-бы можно было проводить с ними вычисления
dfx['From'] = pd.to_datetime(df['From'])
dfx['To'] = pd.to_datetime(df['To'])

#создаём колонку длительность контакта
dfx['duration'] = dfx['To'] - dfx['From']

# условеия что-бы контакт был больше двух минут
dfx = dfx[dfx['duration'] >= '00:05:00']

# убираем колонку
dfx.drop(['Member2_ID'],axis=1,inplace=True)

# создаём группы людей
dfx.loc[(dfx.Age > 18) ,  'Возрастная Группа'] = '18-30'
dfx.loc[(dfx.Age > 30),  'Возрастная Группа'] = '30-50'
dfx.loc[(dfx.Age > 50),  'Возрастная Группа'] = '50-70'
dfx.loc[(dfx.Age > 70),  'Возрастная Группа'] = '> 70'


# группируем по возрстной группе и считаем общее кол-во людей в общей группе,сортируем в убывающем порядке
dfxx = dfx.groupby(['Возрастная Группа'])['Member1_ID'].count().to_frame('кол-во').reset_index().sort_values(['кол-во'],ascending=[False])
#Наиболее частый контакт имеет группа 18-30 лет
