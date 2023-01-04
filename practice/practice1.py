import requests #импортируем модуль
f=open(r'D:\projects',"wb") #открываем файл для записи, в режиме wb
ufr = requests.get("https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE") #делаем запрос
f.write(ufr.content) #записываем содержимое в файл; как видите - content запроса
f.close()