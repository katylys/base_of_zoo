# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 02:25:42 2018

@author: katyl
"""

import pickle as pic
from tkinter import messagebox as mb
import tkinter as tk
import tkinter.ttk as ttk
import os

from os.path import dirname, abspath
import sys

scripts_folder = dirname(abspath(__file__))

workspace = dirname(scripts_folder)

sys.path.insert(0, workspace)
from library import universal

fl1=open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../data/txt.txt'), 'rb')
d=pic.load(fl1)
fl1.close()

root=tk.Tk()

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



v='../output/'+'report_'
  

def vid():
    
    if inputv.winfo_viewable():
        wwodv.set('')
        inputv.grid_remove()
        labelv.grid_remove()
        if labelk.winfo_viewable()!=False or labelp.winfo_viewable()!=False or inputc.winfo_viewable()!=False or inputn.winfo_viewable()!=False or labelf.winfo_viewable()!=False:
            root.geometry('701x401')
        else:
            root.geometry('701x330')
    else:
        labelv.grid(row=5, column=1, columnspan=1)
        inputv.grid(row=6,column=1)
        root.geometry('701x401')
        
        
def klass():
    
    if labelk.winfo_viewable():
        comboboxk.set(u"-")
        comboboxk.grid_remove()
        labelk.grid_remove()
        if inputv.winfo_viewable()!=False or labelp.winfo_viewable()!=False or inputc.winfo_viewable()!=False or inputn.winfo_viewable()!=False or labelf.winfo_viewable()!=False:
            root.geometry('701x401')
        else:
            root.geometry('701x330')
    else:
        labelk.grid(row=5, column=2, columnspan=1)
        comboboxk.grid(row=6, column=2,columnspan=1)
        root.geometry('701x401')
        
def life():
    if labelp.winfo_viewable():
        wwoda.set('-')
        do['state']='disabled'
        ot['state']='disabled'
        since.set('')
        until.set('')
        labelp.grid_remove()
        lifel.grid_remove()
        if labelk.winfo_viewable()!=False or inputv.winfo_viewable()!=False or inputc.winfo_viewable()!=False or inputn.winfo_viewable()!=False or labelf.winfo_viewable()!=False:
            root.geometry('701x401')
        else:
            root.geometry('701x330')
    else:
        ot.place(x=57,y=0)
        do.place(x=88,y=0)
        comboboxl.place(x=0,y=0)
        labelp.grid(row=5, column=3, columnspan=1)
        lifel.grid(row=6,column=3)
        root.geometry('701x401')
        
def country():
    
    if inputc.winfo_viewable():
        wwodc.set('')
        inputc.grid_remove()
        labelc.grid_remove()
        if labelk.winfo_viewable()!=False or labelp.winfo_viewable()!=False or inputv.winfo_viewable()!=False or inputn.winfo_viewable()!=False or labelf.winfo_viewable()!=False:
            root.geometry('701x401')
        else:
            root.geometry('701x330')
    else:
        labelc.grid(row=5, column=6, columnspan=1)
        inputc.grid(row=6,column=6)
        root.geometry('701x401')
        

         
def chose():
    if inputn.winfo_viewable():
        wwodn.set('-')
        inputn.grid_remove()
        labeln.grid_remove()
        if labelk.winfo_viewable()!=False or labelp.winfo_viewable()!=False or inputc.winfo_viewable()!=False or inputv.winfo_viewable()!=False or labelf.winfo_viewable()!=False:
            root.geometry('701x401')
        else:
            root.geometry('701x330')
    else:
        inputn.grid(row=6,column=5)
        labeln.grid(row=5,column=5)
        root.geometry('701x401')
    
    
def food():
    if labelf.winfo_viewable():
        comboboxf.set(u"-")
        comboboxf.grid_remove()
        labelf.grid_remove()
        if labelk.winfo_viewable()!=False or labelp.winfo_viewable()!=False or inputc.winfo_viewable()!=False or inputn.winfo_viewable()!=False or inputv.winfo_viewable()!=False:
            root.geometry('701x401')
        else:
            root.geometry('701x330')
        
    else:
        comboboxf.grid(row=6, column=4,columnspan=1)
        labelf.grid(row=5, column=4, columnspan=1)
        root.geometry('701x401')
        

def age():
    k=0
    if wwoda.get()=='-':
        do['state']='disabled'
        ot['state']='disabled'
        k=1
    if wwoda.get()=='От':
        ot['state']='normal'
        do['state']='disabled'
        k=2
    if wwoda.get()=='До':
        ot['state']='disabled'
        do['state']='normal'
        k=3
    if wwoda.get()=='Между':
        do['state']='normal'
        ot['state']='normal'
        k=4
    return(k)
  

    
    
def delete(): #очистка всех полей
    wwodv.set('')
    comboboxk.set(u"-")
    wwoda.set('-')
    do['state']='disabled'
    ot['state']='disabled'
    since.set('')
    until.set('')
    wwodc.set('')
    comboboxf.set(u"-")
    wwodn.set('-')
    wwodp.set('')
    
    
def edit1(): #
    comboboxf.grid_remove()
    comboboxk.grid_remove()
    voz.grid_remove()
    delete()
    root.geometry('701x401')
    if labelk.winfo_viewable():
        comboboxk.grid_remove()
        labelk.grid_remove()
    if labelp.winfo_viewable():
        lifel.grid_remove()
        labelp.grid_remove()
    if inputc.winfo_viewable():
        inputc.grid_remove()
        labelc.grid_remove()
    if inputn.winfo_viewable():
        inputn.grid_remove()
        labeln.grid_remove()
    if labelf.winfo_viewable():
        comboboxf.grid_remove()
        labelf.grid_remove()
    if inputv.winfo_viewable()==False:
        labelv.grid(row=5, column=1, columnspan=1)
        inputv.grid(row=6,column=1)
        
        
        
        
def create():
    
    lowFrame = tk.Frame(root,height=178,width=680)
    lowFrame.grid(row=3, column=1, sticky='nsew', columnspan=7)
    canvas = tk.Canvas(lowFrame,height=178,width=680)
    frame = tk.Frame(canvas,height=178,width=680)
    myscrollbar = tk.Scrollbar(lowFrame, orient = 'vertical', command = canvas.yview)
    canvas.configure(yscrollcommand = myscrollbar.set)
    myscrollbar.grid(row=3, column=10, sticky='ns')
    canvas.grid(row=3, column=1, sticky='nsew', columnspan=7)
    canvas.create_window((0, 0), window = frame, anchor = 'nw')
    def conf(event):
        canvas.configure(scrollregion = canvas.bbox('all'))
    frame.bind('<Configure>', conf)
    z=0
    for i in d.items(): 
    
        if z!=0:
            n0_.grid(row=2+2*z,column=4,columnspan=5)
        n0_=tk.Label(frame,text='   ')
        n1_=tk.Label(frame,text=i[1]["Вид"].replace(" ","\n"),width=16)
        n1_.grid(row=3+z*2,column=1,columnspan=1)
        n2_=tk.Label(frame,text=i[1]["Класс"].replace(" ","\n"),width=15)
        n2_.grid(row=3+z*2,column=2,columnspan=1)
        n3_=tk.Label(frame,text=i[1]["Продолжительность жизни"].replace(" ","\n"),width=18)
        n3_.grid(row=3+z*2,column=3,columnspan=1)
        n4_=tk.Label(frame,text=i[1]["Питание"].replace(" ","\n"),width=15)
        n4_.grid(row=3+z*2,column=4,columnspan=1)
        n5_=tk.Label(frame,text=i[1]["Есть ли в красной книге"].replace(" ","\n"),width=17)
        n5_.grid(row=3+z*2,column=5,columnspan=1)
        n6_=tk.Label(frame,text=i[1]["Место обитания"].replace(" ","\n"),width=15)
        n6_.grid(row=3+z*2,column=6,columnspan=1)
        z=z+1
            
        

    
        
def cout(event):
    voz.grid_remove()
    h=0
    if wwodv.get=='':
        mb.showerror("Ошибка", "Такого вида нет.\nВведите корректный вид.")
        
    else:
        for i in d.items(): 
            if i[1]["Вид"] == wwodv.get():
                key.set(i[0])
                if labelk.winfo_viewable()==False:
                    comboboxk.grid(row=6, column=2,columnspan=1)
                    wwodk.set(i[1]["Класс"])
                    voz.grid(row=6,column=3,columnspan=1)
                    wwodp.set(i[1]["Продолжительность жизни"])
                    comboboxf.set(i[1]["Питание"])
                    comboboxf.grid(row=6, column=4,columnspan=1)
                    wwodn.set(i[1]["Есть ли в красной книге"])
                    inputn.grid(row=6,column=5)
                    wwodc.set(i[1]["Место обитания"])
                    inputc.grid(row=6,column=6)
                    h=1
                    
        if h==0:
            mb.showerror("Ошибка", "Такого вида нет в базе")  
         
          

def edit2(event):
    if wwodv.get() == '' or wwodk.get() == '-' or wwodp.get()=='' or wwodf.get()=='-' or wwodn.get() == '-' or wwodc.get()=='' :
        mb.showwarning("Предупреждение", "Введите данные для редактирования")
    else:
        e=[wwodv.get(), wwodk.get(), wwodp.get(), comboboxf.get(),wwodn.get(), wwodc.get()]
        #print(e)
        fields = [ "Вид", "Класс", "Продолжительность жизни", "Питание", "Есть ли в красной книге", "Место обитания"] 
        w1 = dict(zip(fields,e) )
        d[key.get()] = w1
        fl1 = open ("../data/txt.txt", "wb")
        pic.dump(d, fl1)
        fl1.close()
        edit1()
        inputv.grid_remove()
        labelv.grid_remove()
        comboboxk.grid_remove()
        lifel.grid_remove()
        inputc.grid_remove()
        inputn.grid_remove()
        comboboxf.grid_remove()
        voz.grid_remove()
        create()
        root.geometry('701x330')
        delete()
        mb.showinfo("Вау", "Произошло редактирование")
    '''else:
        mb.showwarning("Предупреждение", "Введите вид для редактирования")'''
    
def add():
    
    voz.grid_remove()
    labelv.grid(row=5, column=1, columnspan=1)
    inputv.grid(row=6,column=1)
    labelk.grid(row=5, column=2, columnspan=1)
    comboboxk.grid(row=6, column=2,columnspan=1)
    ot.place(x=57,y=0)
    do.place(x=88,y=0)
    comboboxl.place(x=0,y=0)
    labelp.grid(row=5, column=3, columnspan=1)
    voz.grid(row=6,column=3,columnspan=1)
    labelc.grid(row=5, column=6, columnspan=1)
    inputc.grid(row=6,column=6)
    inputn.grid(row=6,column=5)
    labeln.grid(row=5,column=5)
    comboboxf.grid(row=6, column=4,columnspan=1)
    labelf.grid(row=5, column=4, columnspan=1)
    delete()
    root.geometry('701x401')


def alladd(event):
    if wwodv.get() == '' or wwodk.get() == '-' or wwodp.get()=='' or wwodf.get()=='-' or wwodn.get() == '-' or wwodc.get()=='':
        mb.showwarning("Предупреждение", "Введите данные для добавления")
    else:
        e=[wwodv.get(), wwodk.get(), wwodp.get(), comboboxf.get(),wwodn.get(), wwodc.get()]
        fields = [ "Вид", "Класс", "Продолжительность жизни", "Питание", "Есть ли в красной книге", "Место обитания"] 
        w1 = dict(zip(fields,e) )
        d[e[0]] = w1
        fl1 = open ("../data/txt.txt", "wb")
        pic.dump(d, fl1) 
        fl1.close()
        voz.grid_remove()
        edit1()
        alldelete(event)
        create()
        
        mb.showinfo("Вау", "Произошло добавление")
   
    
def strikeoff(event):
    if wwodv.get!='':
        edit1()
        if key.get() in d:
            del d[key.get()]
            fl1 = open ("../data/txt.txt", "wb")
            pic.dump(d,fl1)
            fl1.close()
            voz.grid_remove()
            alldelete(event)
            create()
            mb.showinfo("Вау", "Произошло удаение")
        else:
             mb.showwarning("Предупреждение", "Такого вида нет")
    
    

        
    
def alldelete(event):
    voz.grid_remove()
    comboboxk.grid_remove()
    labelk.grid_remove()
    inputv.grid_remove()
    labelv.grid_remove()
    labelp.grid_remove()
    lifel.grid_remove()
    inputc.grid_remove()
    labelc.grid_remove()
    inputn.grid_remove()
    labeln.grid_remove()
    comboboxf.grid_remove()
    labelf.grid_remove()
    root.geometry('701x330')




def search():
        summ=0
        summ_2=0
        n=0
        def destroy(event):
            buttonnd['state']='normal'
            buttonn['state']='normal'
            buttonnd['state']='normal'
            buttoned['state']='normal'
            buttonnd['state']='normal'
            buttonadd['state']='normal'
            buttondel['state']='normal'
            buttonextra['state']='normal'

        def continuesearch():
            new.destroy()
            buttonnd['state']='normal'
            buttonn['state']='normal'
            buttonnd['state']='normal'
            buttoned['state']='normal'
            buttonnd['state']='normal'
            buttonadd['state']='normal'
            buttondel['state']='normal'
            buttonextra['state']='normal'
    
        def newsearch():
            continuesearch()
            delete()
            
        def example():
            r=np.random.sample()
            sr=round(summ/n, 1)            
            srs=str(sr)       #среднее значение     
            dis=round(summ_2/n-(sr)**2, 2) #sum_2 сумма квадратов элементов
            diss=str(dis)
            txt="Средний возраст искомых животных - " + srs + "\nВыборочная дисперсися - "+diss
            label3=tk.Label(new, text=txt, height=2, width=50 )
            label3.place(x=348,y=213)
            p=str(r)
            f = open(v + p + ".txt", "w")
            f.write("\nСтатистика по поиску \nСредний возраст: " + srs + "\nВыборочная дисперсия = " + diss)
            f.close() 
   
        p=age()
        k=0
        j=0
        z=0

        for i in d.items(): 
                    if wwodv.get() == '' and wwodk.get() == '-'  and wwodf.get()=='-' and wwodn.get() == '-' and wwodc.get()=='' and since.get()=='' and until.get()=='' and ((since.get()).isdigit()==False or (until.get()).isdigit()==False):
                        mb.showwarning("Предупреждение", "Введите данные для поиска")
                        z=1
                        break
                    else: 
                        if i[1]["Вид"] == wwodv.get() or wwodv.get() == '' :
                            if i[1]["Класс"] == wwodk.get() or wwodk.get() == '-' :
                                if (p==1 or (p==2 and  int(i[1]["Продолжительность жизни"])>= int(since.get())) or (p==3 and int(i[1]["Продолжительность жизни"])<=int(until.get())) or (p==4 and (int(i[1]["Продолжительность жизни"])<=int(until.get()) and int(i[1]["Продолжительность жизни"])>=int(since.get())))):
                                    #i[1]["Продолжительность жизни"] == wwodl.get() or wwodl.get()=='':
                                    if i[1]["Питание"] ==wwodf.get() or wwodf.get()=='-':
                                        if i[1]["Есть ли в красной книге"] == wwodn.get() or wwodn.get() == '-':
                                            if i[1]["Место обитания"] == wwodc.get() or wwodc.get()=='':
                                                n+=1
                                                summ=summ+int(i[1]["Продолжительность жизни"])
                                                summ_2=summ_2+int(i[1]["Продолжительность жизни"])**2
                                                if j==0:
                                                    
                                                    new=tk.Tk()
                                                    new.bind('<Destroy>', destroy)
                                                    new.geometry('740x268')
                                                    new.resizable(width=False, height=False)
                                                    new.title("Результат поиска")
                                                    lowFramen = tk.Frame(new,height=178,width=715)
                                                    lowFramen.grid(row=3, column=1, sticky='nsew', columnspan=9)
                                                    calling = tk.Label(new,height=2, width=15,text=u'Результаты поиска')
                                                    canvasn = tk.Canvas(lowFramen,height=178,width=715)
                                                    framen = tk.Frame(canvasn,height=178,width=715)
                                                    myscrollbarn = tk.Scrollbar(lowFramen, orient = 'vertical', command = canvasn.yview)
                                                    canvasn.configure(yscrollcommand = myscrollbarn.set)
                                                    newbutton1=tk.Button(new, text='Новый поиск', fg='red', width=15, height=3,command=newsearch)
                                                    
                                                    newbutton2=tk.Button(new, text='Продолжить поиск', fg='red', width=15, height=3, command=continuesearch)
                                                    calling.grid(row=1,column=5,columnspan=2)
                                                    
                                                    newbutton3=tk.Button(new, text='Расчеты',fg='red', width=15, height=3, command = example)
                                                    
                                                    
                                                    canvasn.grid(row=3, column=1, sticky='nsew', columnspan=9)
                                                    newbutton1.place(x=0,y=213)  
                                                    newbutton2.place(x=116,y=213)
                                                    newbutton3.place(x=232,y=213)
                                                    
                                                    canvasn.create_window((0, 0), window = framen, anchor = 'nw')
                                                    myscrollbarn.grid(row=3, column=10, sticky='ns')
                                                    def confn(event):
                                                        canvasn.configure(scrollregion = canvasn.bbox('all'))
                                                    framen.bind('<Configure>', confn) 
                                            
                                                    n11=tk.Label(framen,text='Вид',width=15)
                                                    n22=tk.Label(framen,text='Класс')
                                                    n33=tk.Label(framen,text='Продолжительность \nжизни(лет)')
                                                    n44=tk.Label(framen,text='Питание')
                                                    n55=tk.Label(framen,text='Есть ли в красной книге')
                                                    n66=tk.Label(framen,text='Место обитания')
                                                    
                                                
                                                if j!=0:
                                                    n0.grid(row=3+2*j,column=4,columnspan=5)
                                                else:
                            
                                                    n11.grid(row=3,column=1,columnspan=1)
                                                    n22.grid(row=3,column=2,columnspan=1)
                                                    n33.grid(row=3,column=3,columnspan=1)
                                                    n44.grid(row=3,column=4,columnspan=1)
                                                    n55.grid(row=3,column=5,columnspan=1)
                                                    n66.grid(row=3,column=6,columnspan=1)
                            
                                                n0=tk.Label(framen,text='   ')
                                                n1=tk.Label(framen,text=i[1]["Вид"].replace(" ","\n"),width=16)
                                                n1.grid(row=4+j*2,column=1,columnspan=1)
                                                n2=tk.Label(framen,text=i[1]["Класс"].replace(" ","\n"),width=15)
                                                n2.grid(row=4+j*2,column=2,columnspan=1)
                                                n3=tk.Label(framen,text=i[1]["Продолжительность жизни"].replace(" ","\n"),width=18)
                                                n3.grid(row=4+j*2,column=3,columnspan=1)
                                                n4=tk.Label(framen,text=i[1]["Питание"].replace(" ","\n"),width=15)
                                                n4.grid(row=4+j*2,column=4,columnspan=1)
                                                n5=tk.Label(framen,text=i[1]["Есть ли в красной книге"].replace(" ","\n"),width=17)
                                                n5.grid(row=4+j*2,column=5,columnspan=1)
                                                n6=tk.Label(framen,text=i[1]["Место обитания"].replace(" ","\n"),width=15)
                                                n6.grid(row=4+j*2,column=6,columnspan=1)
                                                j=j+1
                                                k=1
                                                buttonn['state']='disabled'
                                                buttonnd['state']='disabled'
                                                buttoned['state']='disabled'
                                                buttonnd['state']='disabled'
                                                buttonadd['state']='disabled'
                                                buttondel['state']='disabled'
                                                buttonextra['state']='disabled'
        if k==0:
            if z==0:
                mb.showerror("Ошибка", "Подходящих вариантов нет")
        else:    
            new.mainloop()
                
                

root.geometry('701x330')
root.resizable(width=False, height=False)
root.title("База данных местного зоопарка");

main_label=tk.Label(root,text=u'Зоопарк', fg='white', bg='#6495ED', height=1, font='Courier 20')
main_label.grid(row=1,column=1, columnspan=10,sticky='we')


button1=tk.Button(root,command=vid, text=u'Вид', fg='red', width=15, height=3)
button1.grid(row=2,column=1)

inputv = tk.Entry (root,width=18,font='Arial 8', textvariable=wwodv)
labelv = tk.Label(text = u'Введите вид', width = 15, height = 3, bg = 'LightSalmon')

button2=tk.Button(root,command=klass,text=u'Класс', fg='red', width=16, height=3)
button2.grid(row=2,column=2)

comboboxk = ttk.Combobox(root,values = [u"-",u"Млекопитающие",u"Птицы",u"Рептилии"],width=16,height=2, textvariable=wwodk)
comboboxk.set(u"-")#с помощью этой строчки мы установим Combobox в значение ОДИН изначально

labelk = tk.Label(text = u'Введите класс', width = 16, height = 3, bg = 'LightSalmon')

button5=tk.Button(root,command=life,text=u'Продолжительность \n жизни', fg='red', width=16, height=3)
button5.grid(row=2,column=3)

lifel=tk.Frame(root,width=120,height=25)
comboboxl=tk.Spinbox(lifel,values = [u"-",u"До",u"От",u"Между"],width=6,textvariable=wwoda,command=age,font='Arial 10')

ot=tk.Entry(lifel,width=3,font='Arial 11', textvariable=since,state='disabled')
do=tk.Entry(lifel,width=3,font='Arial 11', textvariable=until,state='disabled')
voz=tk.Entry(root,width=16,textvariable=wwodp,font='Arial 8')
labelp = tk.Label(text = u'Введите\nпродолжительность\nжизни', width = 16, height = 3, bg = 'LightSalmon')

button6=tk.Button(root,command = food, text=u'Питание', fg='red', width=15, height=3)
button6.grid(row=2,column=4)


labelf = tk.Label(text = u'Чем питается?', width = 15, height = 3, bg = 'LightSalmon')
comboboxf = ttk.Combobox(root,values = [u"-",u"Хищник",u"Травоядное",u"Всеядное"],width=15,height=3,textvariable=wwodf)
comboboxf.set(u"-")#с помощью этой строчки мы установим Combobox в значение ОДИН изначально


button7=tk.Button(root,command=chose,text=u'Наличие \nв Красной книге', fg='red', width=15, height=3)
button7.grid(row=2,column=5)

inputn=tk.Spinbox(root, values=("-","Да", "Нет"), width = 16,textvariable=wwodn)
labeln=tk.Label(text = u'Есть ли в\nкрасной книге', width = 15, height = 3, bg = 'LightSalmon')

button8=tk.Button(root,command=country,text=u'Материк обитания', fg='red', width=15, height=3)
button8.grid(row=2,column=6)

inputc = tk.Entry(root,width=18,font='Arial 8', textvariable=wwodc)
labelc = tk.Label(text = u'Введите\nматерик \nобитания', width = 15, height = 3, bg = 'LightSalmon')

buttonn=tk.Button(root,text=u'Найти', fg='red', width=15, height=3,command=search)
buttonn.grid(row=7,column=1,columnspan=1)

buttonnd=tk.Button(root,text=u'Очистить', fg='red', width=16, height=3,command=delete)
buttonnd.grid(row=7,column=2,columnspan=1)
buttonnd.bind('<3>',alldelete)

buttoned=tk.Button(root,text=u'Редактировать', fg='red', width=16, height=3, command=edit1)
buttoned.grid(row=7,column=3,columnspan=1)
buttoned.bind('<3>',edit2)
buttonn.bind('<3>',cout)

buttonadd=tk.Button(root,text=u'Добавить', fg='red', width=15, height=3, command=add)
buttonadd.grid(row=7,column=4,columnspan=1)
buttonadd.bind('<3>',alladd)

buttondel=tk.Button(root,text=u'Удалить', fg='red', width=15, height=3,command=edit1)
buttondel.grid(row=7,column=5,columnspan=1)
buttondel.bind('<3>', strikeoff)

buttonextra=tk.Button(root,text=u'Руководство\nпользователя', fg='red', width=15, height=3, command=universal.rucov)
buttonextra.grid(row=7,column=6,columnspan=1)

create()
    
root.mainloop()
