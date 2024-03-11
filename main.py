import os
import shutil
import tkinter as tk
import zipfile


window = tk.Tk()
window.geometry('400x1000')                    #Задаем размер окна программы
window.title("Лаба №2")
window.resizable(width=False, height=False)    #Выключаем возможность менять размер окна


def create_folder():                                                #Функция для создания папки
    btn1_res = txtbtn1.get()                                        #Берем данные из окошки для ввода текста
    if len(btn1_res) > 0:                                           #Если длина данных из ячейки для ввода информации больше нуля
        res = " Создана папка с названием {}".format(txtbtn1.get()) #Текст который мы будем писать вместо "Доступные операции"
        lbl2.configure(text=res)                                    #Изменяем текст "Доступные перации"
    else:                                                           #Если данные из файла меньше или равны нулю (то есть если ячейка не заполнена), то пишем пользователю об этом
        print("Поле не заполнено")                                  #Вывод в консоль
        lbl2.configure(text="Поле не заполнено")                    #Изменяем текст "Доступные перации"
    try:                                                            #Попытка сделать определенную операцию
        if len(btn1_res) > 0:                                       #Если длина данных из ячейки для ввода информации больше нуля
            os.mkdir(btn1_res)                                      #Создаем папку с названием которое написано в ячейке
            print(f"Папка '{btn1_res}' успешно создана")            #Вывод в консоль
        else:                                                       #Если данные из из ячейки для ввода информации меньше или равны нулю (то есть если ячейка не заполнена), то пишем пользователю об этом
            lbl2.configure(text="Поле не заполнено")                #Изменяем текст "Доступные перации"
    except FileExistsError:                                         #Если программа при попытке видит, что такая папка существует, сообщаем информацию пользователю
        print(f"Папка '{btn1_res}' уже существует")                 #Вывод в консоль
def delete_folder():                                     #Функция для удаления папки
    btn2_res = txtbtn2.get()                             #Берем данные из окошки для ввода текста
    try:                                                 #Попытка сделать определенную операцию
        shutil.rmtree(btn2_res)                          #Удаляем папку с названием которое написано в ячейке
        print(f"Папка '{btn2_res}' успешно удалена")     #Вывод в консоль
    except FileNotFoundError:                            #Если программа при попытке видит, что такая папка существует, сообщаем информацию пользователю
        print(f"Ошибка: папка '{btn2_res}' не найдена")  #Вывод в консоль
def create_file():                                       #Функция для создания файла
    btn3_res = txtbtn3.get()                             #Берем данные из окошки для ввода текста
    try:                                                 #Попытка сделать определенную операцию
        if len(btn3_res) > 0:                            #Если длина данных из ячейки для ввода информации больше нуля
            open(btn3_res, 'w').close()                  #Создаем файл с названием из ячейки для ввода информации
            print(f"Файл '{btn3_res}' успешно создан")   #Вывод в консоль
        else:                                            #Если данные из из ячейки для ввода информации меньше или равны нулю (то есть если ячейка не заполнена), то пишем пользователю об этом
            lbl2.configure(text="Поле не заполнено")     #Изменяем текст "Доступные перации"
    except FileExistsError:                              #Если программа при попытке видит, что такая папка существует, сообщаем информацию пользователю
        print(f"Файл '{btn3_res}' уже существует")       #Вывод в консоль

def write_to_file():                                       #Функция для того чтобы мы могли вписать в файл информацию
    btn4_res = txtbtn4.get()                               #Вводим название файла в который будем вписывать информацию
    btn4_content = txtbtn4content.get()                    #Вводим текст который будем вписан в файл
    try:                                                   #Попытка сделать определенную операцию
        with open(btn4_res, 'w') as file:                  #Открываем файл в который будем вписывать информацию
            file.write(btn4_content)                       #Вписываем в файл информацию которое было введено в окошко для ввода
        print(f"Текст успешно записан в файл '{btn4_res}'")#Вывод в консоль
    except FileNotFoundError:                              #Если программа при попытке видит, что такая папка существует, сообщаем информацию пользователю
        print(f"Ошибка: файл '{btn4_res}' не найден")      #Вывод в консоль

def read_file():                                                  #Функция для чтения информации из файла
    btn5_res = txtbtn5.get()                                      #Вводим название файла для чтения из нее информации
    try:                                                          #Попытка сделать определенную операцию
        with open(btn5_res, 'r') as file:                         #Открываем файл из которого будем читать информацию
            btn5_content = file.read()                            #Читаем информацию из файла
        print(f"Содержимое файла '{btn5_res}':")                  #Вывод в консоль
        print(btn5_content)                                       #Вывод в консоль
        lb6content.configure(text="СОДЕРЖИМОЕ: " + btn5_content)  #Вывод содержимого файла
    except FileNotFoundError:                                     #Если программа при попытке видит, что такая папка существует, сообщаем информацию пользователю
        print(f"Ошибка: файл '{btn5_res}' не найден")             #Вывод в консоль

def copy_file():                                                             #Функция для копирования файла
    btn6path = txtbtn6path.get()                                             #Берем рассположение файла которое будет скопировано
    btn6distanation = txtbtn6distanation.get()                               #Берем рассположение куда будет скопирован файл
    try:                                                                     #Попытка сделать определенную операцию
        shutil.copy(btn6path, btn6distanation)                               #Копируем файл
        print(f"Файл '{btn6path}' успешно скопирован в '{btn6distanation}'") #Вывод в консоль
    except FileNotFoundError:                                                #Если программа при попытке видит, что такая папка существует, сообщаем информацию пользователю
        print(f"Ошибка: файл '{btn6path}' не найден")                        #Вывод в консоль
    except FileExistsError:                                                  #Если программа при попытке видит, что такая папка существует, сообщаем информацию пользователю
        print(f"Ошибка: файл '{btn6distanation}' уже существует")            #Вывод в консоль

def rename_file():                                                           #Функция для переименования файла
    btn7_path = txtbtn7path.get()                                            #Вводим имя файла которое хотим переименовать
    btn7_newname = txtbtn7newname.get()                                      #Вводим новое имя файла которое написали в ячейке для переименования
    try:                                                                     #Попытка сделать определенную операцию
        os.rename(btn7_path, btn7_newname)                                   #Переименововываем файл
        print(f"Файл '{btn7_path}' успешно переименован в '{btn7_newname}'") #Вывод в консоль
    except FileNotFoundError:                                                #Если программа при попытке видит, что такая папка существует, сообщаем информацию пользователю
        print(f"Ошибка: файл '{btn7_path}' не найден")                       #Вывод в консоль

def create_user():                                                           #Функция для создания юзера для опеределенной папки
    btn8_LOGIN = txtbtn7LOGIN.get()                                          #Берем Имя юзера

    if os.path.exists(btn8_LOGIN):                                           #Если пользователь уже существует, выводим сообщение об ошибке
        print("Пользователь с таким именем уже существует")                  #Вывод в консоль
        return False                                                         #Возврашаем ложь

    if len(btn8_LOGIN) > 0:                                                  #Если ячейка для ввода имени юзера больше нулю(заполнена)
        res = " Создана папка с названием {}".format(txtbtn1.get())          #Создаем пользователя с таким названием
        lbl2.configure(text=res)                                             #Изменяем текст "Доступные перации"
    else:                                                                    #Иначе
        print("Поле не заполнено")                                           #Вывод в консоль
        lbl2.configure(text="Поле не заполнено")                             #Изменяем текст "Доступные перации"
    try:                                                                     #Попытка сделать определенную операцию
        if len(btn8_LOGIN) > 0:                                              #Если ячейка для ввода имени юзера больше нулю(заполнена)
            os.mkdir(btn8_LOGIN)                                             #Создаем папку с именем пользователя
            print(f"Папка '{btn8_LOGIN}' успешно создана")                   #Вывод в консоль
        else:                                                                #Иначе
            lbl2.configure(text="Поле не заполнено")                         #Изменяем текст "Доступные перации"
    except FileExistsError:                                                  #Если программа при попытке видит, что такая папка существует, сообщаем информацию пользователю
        print(f"Папка '{btn8_LOGIN}' уже существует")                        #Вывод в консоль


def zip_file():                                                              #Функция для арзивации файла
    zip_filename = txtbtn7zip.get()                                          #Берем рассположение файла которое хотим архивировать
    zip_path = "C:/Users/228930/PycharmProjects/pythonProject/"              #Задаем путь где будет архивирован файл
    with zipfile.ZipFile(zip_path, 'w') as zip_file:                         #Архивируем файл
        zip_file.write(zip_filename, arcname=os.path.basename(zip_filename)) #Архивируем файл


#Текст Оглавления
Title_str = tk.Label(window, text="ГРАФИЧЕСКИЙ ИНТЕРФЕЙС",
                      font=("Futura",20,"bold"), bg = '#008080', width=90, pady=15)
Title_str.pack()

lbl2 = tk.Label(window, text="ДОСТУПНЫЕ ОПЕРАЦИИ:",
                font=("Futura",15,"bold"), bg = '#008B8B', width=90)
lbl2.pack()


#Интерфейс
line1 = tk.Label(window, text="")
line1.pack()
lb5content = tk.Label(window, text="НАПИШИТЕ ИМЯ ПАПКИ, КОТОРОЕ НУЖНО СОЗДАТЬ",
                      font=("Futura",6,"bold"), bg = '#008B8B', width=63)
lb5content.pack()
txtbtn1 = tk.Entry(window , width=53)
txtbtn1.pack()
btn_createFolder = tk.Button(window, text="Создать папку", command=create_folder)
btn_createFolder.pack()
line2 = tk.Label(window, text="")
line2.pack()


delite_folder_txt = tk.Label(window, text="НАПИШИТЕ ИМЯ ФАЙЛА, КОТОРОЕ НУЖНО УДАЛИТЬ",
                             font=("Futura",6,"bold"), bg = '#008B8B', width=63)
delite_folder_txt.pack()
txtbtn2 = tk.Entry(window, width=53)
txtbtn2.pack()
btn_deliteFolder = tk.Button(window, text="Удалить папку", command=delete_folder)
btn_deliteFolder.pack()
line3 = tk.Label(window, text="")
line3.pack()

create_file_txt = tk.Label(window, text="НАПИШИТЕ ИМЯ ФАЙЛА, КОТОРОЕ НУЖНО СОЗДАТЬ",
                           font=("Futura",6,"bold"), bg = '#008B8B', width=63)
create_file_txt.pack()
txtbtn3 = tk.Entry(window, width=53)
txtbtn3.pack()
btn_createFile = tk.Button(window, text="Создать Файл", command=create_file)
btn_createFile.pack()
line4 = tk.Label(window, text="")
line4.pack()


txt5 = tk.Label(window, text="НАПИШИТЕ НАЗВАНИЕ ФАЙЛА, В КОТОРОЕ НУЖНО ЗАПИСАТЬ ТЕКСТ",
                font=("Futura",6,"bold"), bg = '#008B8B', width=63)
txt5.pack()
txtbtn4 = tk.Entry(window, width=53)
txtbtn4.pack()
txt55 = tk.Label(window, text="НАПИШИТЕ ТЕКСТ КОТОРЫЙ ХОТИТЕ ЗАПИСАТЬ В ФАЙЛ",
                 font=("Futura",6,"bold"), bg = '#008B8B', width=63)
txt55.pack()
txtbtn4content = tk.Entry(window, width=53)
txtbtn4content.pack()
btn_writeFile = tk.Button(window, text="Записать текст в файл", command=write_to_file)
btn_writeFile.pack()
line5 = tk.Label(window, text="")
line5.pack()

txt66 = tk.Label(window, text="НАПИШИТЕ ИМЯ ФАЙЛА, ИЗ КОТОРОГО ХОТИТЕ ПРОЧИТАТЬ ТЕКСТ",
                 font=("Futura",6,"bold"), bg = '#008B8B', width=63)
txt66.pack()
txtbtn5 = tk.Entry(window, width=53)
txtbtn5.pack()
lb6content = tk.Label(window, text="СОДЕРЖИМОЕ:" , anchor="nw", width=45)
lb6content.pack()
btn_readFile = tk.Button(window, text="Прочитать содержимое файла", command=read_file)
btn_readFile.pack()
line6 = tk.Label(window, text="")
line6.pack()

txt77 = tk.Label(window, text="НАПИШИТЕ РАСПОЛОЖЕНИЕ ФАЙЛА, КОТОРОЕ ХОТИТЕ СКОПИРОВАТЬ",
                 font=("Futura",6,"bold"), bg = '#008B8B', width=63)
txt77.pack()
txtbtn6path = tk.Entry(window, width=53)
txtbtn6path.pack()
txt88 = tk.Label(window, text="НАПИШИТЕ РАСПОЛОЖЕНИЕ, КУДА ХОТИТЕ СКОПИРОВАТЬ",
                 font=("Futura",6,"bold"), bg = '#008B8B', width=63)
txt88.pack()
txtbtn6distanation = tk.Entry(window, width=53)
txtbtn6distanation.pack()
btn_copyFile = tk.Button(window, text="Скопировать файл", command=copy_file)
btn_copyFile.pack()
line7 = tk.Label(window, text="")
line7.pack()

txt99 = tk.Label(window, text="НАПИШИТЕ ИМЯ ФАЙЛА, КОТОРОЕ ХОТИТЕ ПЕРЕИМЕНОВАТЬ",
                 font=("Futura",6,"bold"), bg = '#008B8B', width=63)
txt99.pack()
txtbtn7path = tk.Entry(window, width=53)
txtbtn7path.pack()
txt99 = tk.Label(window, text="НАПИШИТЕ НОВОЕ ИМЯ ФАЙЛА",
                 font=("Futura",6,"bold"), bg = '#008B8B', width=63)
txt99.pack()
txtbtn7newname = tk.Entry(window, width=53)
txtbtn7newname.pack()
btn_renameFile = tk.Button(window, text="Переименовать файл", command=rename_file)
btn_renameFile.pack()
line8 = tk.Label(window, text="")
line8.pack()

txt10 = tk.Label(window, text="НАПИШИТЕ ЛОГИН",
                 font=("Futura",6,"bold"), bg = '#008B8B', width=63)
txt10.pack()
txtbtn7LOGIN = tk.Entry(window, width=53)
txtbtn7LOGIN.pack()
btn_renameFile = tk.Button(window, text="СОЗДАТЬ ПОЛЬЗОВАТЕЛЯ", command=create_user)
btn_renameFile.pack()
line8 = tk.Label(window, text="")
line8.pack()

txt11 = tk.Label(window, text="НАПИШИТЕ ИМЯ ФАЙЛА, КОТОРОЕ НУЖНО АРХИВИРОВАТЬ",
                 font=("Futura",6,"bold"), bg = '#008B8B', width=63)
txt11.pack()
txtbtn7zip = tk.Entry(window, width=53)
txtbtn7zip.pack()
btn_zipFile = tk.Button(window, text="АРХИВИРОВАТЬ ФАЙЛ", command=zip_file)
btn_zipFile.pack()
line8 = tk.Label(window, text="")
line8.pack()


window.mainloop()
