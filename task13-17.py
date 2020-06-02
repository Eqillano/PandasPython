import pandas as pd

dfbig = pd.read_json('TestJson/big_data_persons.json')
dfsmall = pd.read_json('TestJson/small_data_persons.json')


#print(dfsmall.head())

'''
Задание 1.3
Загружаем файлы в excel
'''

dfbig.to_excel('big_data_persons.xlsx')
dfsmall.to_excel('small_data_persons.xlsx')



'''
Задание 1.4
Делим колонку name на два столбца , убираем колонку name и сортируем по фамилии

'''

dfsmall[['Last','First']] = dfsmall.Name.str.split(expand=True)
dfsmall.drop(['Name'],axis=1,inplace=True)
dfsmall.sort_values('Last',inplace=True) #



'''
Второй датасет,делим колонку name на два столбца , убираем колонку name и сортируем по имени
'''

dfbig[['Last','First']] = dfbig.Name.str.split(expand=True)
dfbig.drop(['Name'],axis=1,inplace=True)
dfbig.sort_values('First',inplace=True)





'''
Задание 1.5

Находим людей в small_data которых нету в big_data и выводим их в excel

'''
new_df = pd.merge(dfsmall, dfbig, on=dfsmall.columns.to_list(), how='outer', indicator=True).query("_merge == 'left_only'").drop('_merge', 1)
new_df.to_excel('people_not_in_big.xlsx')




'''
Задание 1.6

 находим дубликаты по фамилии у которых разница в возрасте 10 лет и сохраняем в excel'''


dupes = dfsmall[dfsmall['Last'].duplicated(keep=False)]
dupes['diff'] = dupes['Age'] - dupes['Age'].shift()
dupesx = dupes[(dupes['diff'] == 10) | (dupes['diff'] == -10)]
dupesx.to_excel('lastname-age-diff.xlsx')



'''
Задание 1.7

находим слова где есть английские знаки и сохраняем их в excel '''

dfenglish = dfsmall[dfsmall['First'].str.contains('[A-Za-z]') | dfsmall['Last'].str.contains('[A-Za-z]')]
dfenglish.to_excel('contains_english_letters.xlsx')
