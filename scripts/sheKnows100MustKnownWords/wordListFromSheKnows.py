#!/user/bin/python
import requests
import bs4
import re
import xlsxwriter
from helpers import excel
from constants import constants
from os.path import abspath
import yaml

pages = yaml.safe_load(open(abspath('../../config/' + 'config.yaml')))
locators = yaml.safe_load(open(abspath('../../scripts/sheKnows100MustKnownWords/locators.yaml')))
fileName = abspath('../../resources/' + constants.SHEKNOWSEXCLNAME)
new = []
new1 = []
new2 = []
words = []
meanings = []
examples = []

workbook = xlsxwriter.Workbook(fileName)
worksheet = excel.formatWorkSheet(workbook, constants.SHEETNAME)
meaning_format = workbook.add_format()
meaning_format.set_font_color('blue')
words_format = workbook.add_format()
words_format.set_font_color('green')

for page_num in range(1, 10):
    res = requests.get(pages['sheknows'] + str(page_num) + '/')
    list = bs4.BeautifulSoup(res.text, "html.parser")
    wordlist = list.select(locators['WORDS'])
    meaningList = list.find_all(string=re.compile("Definition"))
    exampleList = list.find_all(string=re.compile("Example"))
    for i in range(len(wordlist)):
        new = wordlist[i].getText()
        words.append(new)

    for j in range(len(meaningList)):
        new1 = meaningList[j]
        meanings.append(new1)

    for k in range(len(exampleList)):
        new2 = exampleList[k]
        examples.append(new2)

for m in range(len(words)):
    worksheet.write(m + 1, 0, words[m], words_format)

for l in range(len(meanings)):
    worksheet.write(l + 1, 1, meanings[l].replace('Definition:', ''), meaning_format)

for n in range(len(examples)):
    worksheet.write(n + 1, 2, examples[n].replace('Example:', ''))

workbook.close()
print('Word list created')
