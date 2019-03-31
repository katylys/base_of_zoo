# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 01:36:47 2018

@author: katyl
"""



from tkinter import messagebox as mb
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog as fd
import numpy as np


wwodv=tk.StringVar()
wwodv.set('')

wwodk = tk.StringVar()

wwodl=tk.StringVar()
wwodl.set('')

wwodf=tk.StringVar()

wwodn=tk.StringVar()

wwodc = tk.StringVar()
wwodc.set('')

wwoda=tk.StringVar()

since=tk.StringVar()
since.set('')
until=tk.StringVar()
until.set('')
wwodp=tk.StringVar()
wwodp.set('')

key=tk.StringVar()

srs=tk.StringVar()
diss=tk.StringVar()


root=tk.Tk()

main_label=tk.Label(root,text=u'Зоопарк', fg='white', bg='#6495ED', height=1, font='Courier 20')
main_label.grid(row=1,column=1, columnspan=10,sticky=W+E)


button1=tk.Button(root,command=fun.vid, text=u'Вид', fg='red', width=15, height=3)
button1.grid(row=2,column=1)

inputv = tk.Entry (root,width=18,font='Arial 8', textvariable=wwodv)
labelv = tk.Label(text = u'Введите вид', width = 15, height = 3, bg = 'LightSalmon')

button2=tk.Button(root,command=fun.klass,text=u'Класс', fg='red', width=16, height=3)
button2.grid(row=2,column=2)

comboboxk = ttk.Combobox(root,values = [u"-",u"Млекопитающие",u"Птицы",u"Рептилии"],width=16,height=2, textvariable=wwodk)
comboboxk.set(u"-")#с помощью этой строчки мы установим Combobox в значение ОДИН изначально

labelk = tk.Label(text = u'Введите класс', width = 16, height = 3, bg = 'LightSalmon')

button5=tk.Button(root,command=fun.life,text=u'Продолжительность \n жизни', fg='red', width=16, height=3)
button5.grid(row=2,column=3)

lifel=tk.Frame(root,width=120,height=25)
comboboxl=tk.Spinbox(lifel,values = [u"-",u"До",u"От",u"Между"],width=6,textvariable=wwoda,command=fun.age,font='Arial 10')

ot=tk.Entry(lifel,width=3,font='Arial 11', textvariable=since,state='disabled')
do=tk.Entry(lifel,width=3,font='Arial 11', textvariable=until,state='disabled')
voz=tk.Entry(root,width=16,textvariable=wwodp,font='Arial 8')
labelp = tk.Label(text = u'Введите\nпродолжительность\nжизни', width = 16, height = 3, bg = 'LightSalmon')

button6=tk.Button(root,command = fun.food, text=u'Питание', fg='red', width=15, height=3)
button6.grid(row=2,column=4)


labelf = tk.Label(text = u'Чем питается?', width = 15, height = 3, bg = 'LightSalmon')
comboboxf = ttk.Combobox(root,values = [u"-",u"Хищник",u"Травоядное",u"Всеядное"],width=15,height=3,textvariable=wwodf)
comboboxf.set(u"-")#с помощью этой строчки мы установим Combobox в значение ОДИН изначально


button7=tk.Button(root,command=fun.chose,text=u'Наличие \nв Красной книге', fg='red', width=15, height=3)
button7.grid(row=2,column=5)

inputn=tk.Spinbox(root, values=("-","Да", "Нет"), width = 16,textvariable=wwodn)
labeln=tk.Label(text = u'Есть ли в\nкрасной книге', width = 15, height = 3, bg = 'LightSalmon')

button8=tk.Button(root,command=fun.country,text=u'Материк обитания', fg='red', width=15, height=3)
button8.grid(row=2,column=6)

inputc = tk.Entry(root,width=18,font='Arial 8', textvariable=wwodc)
labelc = tk.Label(text = u'Введите\nматерик \nобитания', width = 15, height = 3, bg = 'LightSalmon')

buttonn=tk.Button(root,text=u'Найти', fg='red', width=15, height=3,command=fun.search)
buttonn.grid(row=7,column=1,columnspan=1)

buttonnd=tk.Button(root,text=u'Очистить', fg='red', width=16, height=3,command=fun.delete)
buttonnd.grid(row=7,column=2,columnspan=1)
buttonnd.bind('<3>',fun.alldelete)

buttoned=tk.Button(root,text=u'Редактировать', fg='red', width=16, height=3, command=fun.edit1)
buttoned.grid(row=7,column=3,columnspan=1)
buttoned.bind('<3>',fun.edit2)
buttonn.bind('<3>',fun.cout)

buttonadd=tk.Button(root,text=u'Добавить', fg='red', width=15, height=3, command=fun.add)
buttonadd.grid(row=7,column=4,columnspan=1)
buttonadd.bind('<3>',fun.alladd)

buttondel=tk.Button(root,text=u'Удалить', fg='red', width=15, height=3,command=fun.edit1)
buttondel.grid(row=7,column=5,columnspan=1)
buttondel.bind('<3>', fun.strikeoff)

buttonextra=tk.Button(root,text=u'Руководство\nпользователя', fg='red', width=15, height=3, command=fun.rucov)
buttonextra.grid(row=7,column=6,columnspan=1)
