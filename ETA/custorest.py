# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import xlrd

from collections import defaultdict

book = xlrd.open_workbook('CUSTOREST.xls')
sh = book.sheet_by_name('DADOS')
data = defaultdict(list)

for rx in range(1, sh.nrows):
    row = sh.row(rx)
    local = row[0].value
    data[local].append(row[6].value)

fig = plt.figure()
for i, key in enumerate(data.keys()):
    sp = fig.add_subplot(121 + i)
    sp.set_title(key)
    sp.set_xlabel(u'Custo por refeição')
    sp.set_ylabel(u'Frequência')
    sp.hist(data[key], 7)

plt.show()
