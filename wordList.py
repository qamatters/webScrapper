#!/user/bin/python
import requests
import bs4
import xlsxwriter
import pandas as pd


# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('MyWorldList.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some data headers.
worksheet.write('A1', 'Words', bold)
worksheet.write('B1', 'Meanings', bold)

res = requests.get('put your URL')
list = bs4.BeautifulSoup(res.text, "html.parser")
words = list.select('a.word.dynamictext')
# print(words)
print('Total words count :' + str(len(words)))

# Print duplicate words
duplicateWords = pd.Series(words)[pd.Series(words).duplicated()].values
print('Total Number of Duplicate words ' + str(len(duplicateWords)))
print(duplicateWords)

meanings = list.select('.definition')
# print(meanings)
print('Total Meanings :' + str(len(meanings)))

# Print duplicate meanings
duplicateMeanings = pd.Series(meanings)[pd.Series(meanings).duplicated()].values
print('Total Number of Duplicate Meanings ' + str(len(duplicateMeanings)))
print(duplicateMeanings)

for i in range(len(words)):
    # print(words[i].getText())
    worksheet.write(i+1, 0, words[i].getText())

for j in range(len(meanings)):
    # print(meanings[j].getText())
    worksheet.write(j+1, 1, meanings[j].getText())

workbook.close()
print('Word list created')


