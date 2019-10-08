#!/user/bin/python
import requests
import bs4
import xlsxwriter
from helpers import excel
from constants import constants
from os.path import abspath
import yaml

pages = yaml.safe_load(open(abspath('../../config/'+'config.yaml')))
locators = yaml.safe_load(open(abspath('../../scripts/vocabulary.com/locators.yaml')))
fileName = abspath('../../resources/' + constants.EXCELNAME)

res = requests.get(pages['URL1'])
list = bs4.BeautifulSoup(res.text, "html.parser")
words = list.select(locators['WORDS'])
meanings = list.select(locators['MEANINGS'])
examples = list.select(locators['DEFINITIONS'])

workbook = xlsxwriter.Workbook(fileName)
worksheet = excel.formatWorkSheet(workbook, constants.SHEETNAME)
meaning_format = workbook.add_format()
meaning_format.set_font_color('blue')
words_format = workbook.add_format()
words_format.set_font_color('green')

for i in range(len(words)):
    worksheet.write(i + 1, 0, words[i].getText(), words_format)

for j in range(len(meanings)):
    worksheet.write(j + 1, 1, meanings[j].getText(), meaning_format)

for k in range(len(examples)):
    worksheet.write(k + 1, 2, examples[k].getText())

workbook.close()
print('Word list created')