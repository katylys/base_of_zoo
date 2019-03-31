# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 01:42:31 2018

@author: katyl
"""

#import sys
#sys.path.insert(0,'./library')
#import gui

import pickle as pic
from tkinter import *


def vid():
    
    if gui.inputv.winfo_viewable():
        gui.wwodv.set('')
        gui.inputv.grid_remove()
        gui.labelv.grid_remove()
        if gui.labelk.winfo_viewable()!=False or gui.labelp.winfo_viewable()!=False or gui.inputc.winfo_viewable()!=False or gui.inputn.winfo_viewable()!=False or gui.labelf.winfo_viewable()!=False:
            gui.root.geometry('701x401')
        else:
            gui.root.geometry('701x330')
    else:
        gui.labelv.grid(row=5, column=1, columnspan=1)
        gui.inputv.grid(row=6,column=1)
        gui.root.geometry('701x401')
        
        
def klass():
    
    if gui.labelk.winfo_viewable():
        gui.comboboxk.set(u"-")
        gui.comboboxk.grid_remove()
        gui.labelk.grid_remove()
        if gui.inputv.winfo_viewable()!=False or gui.labelp.winfo_viewable()!=False or gui.inputc.winfo_viewable()!=False or gui.inputn.winfo_viewable()!=False or gui.labelf.winfo_viewable()!=False:
            gui.root.geometry('701x401')
        else:
            gui.root.geometry('701x330')
    else:
        gui.labelk.grid(row=5, column=2, columnspan=1)
        gui.comboboxk.grid(row=6, column=2,columnspan=1)
        gui.root.geometry('701x401')
        
def life():
    if gui.labelp.winfo_viewable():
        gui.wwoda.set('-')
        gui.do['state']='disabled'
        gui.ot['state']='disabled'
        gui.since.set('')
        gui.until.set('')
        gui.labelp.grid_remove()
        gui.lifel.grid_remove()
        if gui.labelk.winfo_viewable()!=False or gui.inputv.winfo_viewable()!=False or gui.inputc.winfo_viewable()!=False or gui.inputn.winfo_viewable()!=False or gui.labelf.winfo_viewable()!=False:
            gui.root.geometry('701x401')
        else:
            gui.root.geometry('701x330')
    else:
        gui.ot.place(x=57,y=0)
        gui.do.place(x=88,y=0)
        gui.comboboxl.place(x=0,y=0)
        gui.labelp.grid(row=5, column=3, columnspan=1)
        gui.lifel.grid(row=6,column=3)
        gui.root.geometry('701x401')
        
def country():
    
    if gui.inputc.winfo_viewable():
        gui.wwodc.set('')
        gui.inputc.grid_remove()
        gui.labelc.grid_remove()
        if gui.labelk.winfo_viewable()!=False or gui.labelp.winfo_viewable()!=False or gui.inputv.winfo_viewable()!=False or gui.inputn.winfo_viewable()!=False or gui.labelf.winfo_viewable()!=False:
            gui.root.geometry('701x401')
        else:
            gui.root.geometry('701x330')
    else:
        gui.labelc.grid(row=5, column=6, columnspan=1)
        gui.inputc.grid(row=6,column=6)
        gui.root.geometry('701x401')
        

         
def chose():
    if gui.inputn.winfo_viewable():
        gui.wwodn.set('-')
        gui.inputn.grid_remove()
        gui.labeln.grid_remove()
        if gui.labelk.winfo_viewable()!=False or gui.labelp.winfo_viewable()!=False or gui.inputc.winfo_viewable()!=False or gui.inputv.winfo_viewable()!=False or gui.labelf.winfo_viewable()!=False:
            gui.root.geometry('701x401')
        else:
            gui.root.geometry('701x330')
    else:
        gui.inputn.grid(row=6,column=5)
        gui.labeln.grid(row=5,column=5)
        gui.root.geometry('701x401')
    
    
def food():
    if gui.labelf.winfo_viewable():
        gui.comboboxf.set(u"-")
        gui.comboboxf.grid_remove()
        gui.labelf.grid_remove()
        if gui.labelk.winfo_viewable()!=False or gui.labelp.winfo_viewable()!=False or gui.inputc.winfo_viewable()!=False or gui.inputn.winfo_viewable()!=False or gui.inputv.winfo_viewable()!=False:
            gui.root.geometry('701x401')
        else:
            gui.root.geometry('701x330')
        
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
        fl1 = open ("../output/txt.txt", "wb")
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
            fl1 = open ("../output/txt.txt", "wb")
            pic.dump(d,fl1)
            fl1.close()
            voz.grid_remove()
            alldelete(event)
            create()
            mb.showinfo("Вау", "Произошло удаение")
        else:
             mb.showwarning("Предупреждение", "Такого вида нет")
    
    
def rucov():
    mb.showinfo("Обрати внимание", "ЛКМ - левой кнопкой мыши, ПКМ - правой кнопкой мыши\n\nПоиск: Найти ЛКМ -> заполните одно, несколько или все поля -> Найти ЛКМ. Во всплывающем окне: Расчеты показывает рассчитанные данные и записывает их в файл в папке output; Продолжить поиск сохраняет заполненные ранее поля; Новый поиск очищает поля\n\n Редактирование: Редактировать ЛКМ -> введите вид животного -> Найти ПКМ -> отредактируйте поля -> Редактировать ПКМ\n\n Добавление: Добавить ЛКМ -> заполните все поля -> Добавить ПКМ\n\n Удаление: Удалить ЛКМ -> введите вид животного -> Найти ПКМ -> Удалить ПКМ")
        
    
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
                    if wwodv.get() == '' and wwodk.get() == '-'  and wwodf.get()=='-' and wwodn.get() == '-' and wwodc.get()=='' and since.get()=='' and until.get()=='':
                        mb.showwarning("Предупреждение", "Введите данные для поиска")
                        z=1
                        break
                    else: 
                        if i[1]["Вид"] == wwodv.get() or wwodv.get() == '' :
                            if i[1]["Класс"] == wwodk.get() or wwodk.get() == '-' :
                                if (p==1 or (p==2 and  int(i[1]["Продолжительность жизни"])>= int(since.get())) or (p==3 and int(i[1]["Продолжительность жизни"])<=int(until.get())) or (p==4 and (int(i[1]["Продолжительность жизни"])<=int(until.get()) and int(i[1]["Продолжительность жизни"])>=int(since.get())))) or (since.get()=='' and until.get()==''):
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