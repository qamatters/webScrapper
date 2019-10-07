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
meaning_format = workbook.add_format()
meaning_format.set_font_color('blue')

words_format = workbook.add_format()
words_format.set_font_color('green')

# example_format = workbook.add_format()
# example_format.set_text_wrap()


# Write some data headers.
worksheet.write('A1', 'Words', bold)
worksheet.write('B1', 'Meanings', bold)
worksheet.write('C1', 'Example', bold)

res = requests.get('https://www.vocabulary.com/lists/1527292')
list = bs4.BeautifulSoup(res.text, "html.parser")
words = list.select('a.word.dynamictext')
# print(words)
# print('Total words count :' + str(len(words)))

# Print duplicate words
# duplicateWords = pd.Series(words)[pd.Series(words).duplicated()].values
# print('Total Number of Duplicate words ' + str(len(duplicateWords)))
# print(duplicateWords)

meanings = list.select('.definition')
# print(meanings)
# print('Total Meanings :' + str(len(meanings)))

# Print duplicate meanings
# duplicateMeanings = pd.Series(meanings)[pd.Series(meanings).duplicated()].values
# print('Total Number of Duplicate Meanings ' + str(len(duplicateMeanings)))
# print(duplicateMeanings)

examples = list.select('.example')

for i in range(len(words)):
    # print(words[i].getText())
    worksheet.write(i + 1, 0, words[i].getText(), words_format)

for j in range(len(meanings)):
    # print(meanings[j].getText())
    worksheet.write(j + 1, 1, meanings[j].getText(), meaning_format)

for k in range(len(examples)):
    # print(examples[k].getText())
    worksheet.write(k + 1, 2, examples[k].getText())


workbook.close()
print('Word list created')
