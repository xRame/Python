import re
import os
import time
import shutil
file_path = '/ftpshare/inbox'  # путь к корню где искать
file_name = 'file.txt'  # имя файла который ищем
backup1 = '/ftpshare/copy'  # путь к корню куда сохраняем
backup2 = '/ftpshare/start'  # путь к корню куда сохраняем
pause = 1  # секууды паузы
 
def replace(fpath):
    npath = re.sub(file_path, "", fpath)
    npath = re.sub(file_name, "", npath)
    npath1 = backup1+npath
    npath2 = backup2+npath
    print(npath)
    try:
        os.makedirs(npath1)
        os.makedirs(npath2)
    except FileExistsError:
        pass
    shutil.copy2(fpath, npath1)
    shutil.copy2(fpath, npath2)    
    os.remove(fpath)
 
def func(fpath):  # запуск функции которая что-то делает с файло, fpath - путь файлу
    # тут что-то делать
 

 
    #раскоментировать первое для просто удаление, второе - для сохранения, а зетем удаления
    #os.remove(fpath) # удаление файл
    replace(fpath)  # перемещение и удаление
 
def find():
    for dirpath, dirnames, filenames in os.walk(file_path):
        for filename in filenames:
            if(filename == file_name):
                fpath = os.path.join(dirpath, filename)
                print("File:", fpath)
                return True, fpath
    return False, ''
 
while True:
    flag, fpath = find()
    if flag:
        func(fpath) # тут отправляется в функцию путь к файлу
 
    else:
        print('file dont found')
        time.sleep(pause)