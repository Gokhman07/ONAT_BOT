import mysql.connector



from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton

SMILE = ['😊', '😀', '😇', '🤠', '😎', '🤓', '👶', '🧑‍🚀', '👮', '🦸', '🧟']

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="printer10",
  database='onat_schedule'

)
cursor = mydb.cursor()


# функция создает клавиатуру и ее разметку
def get_keyboard():

    cursor.execute("SELECT Name FROM  TEACHERS")
    data= (cursor.fetchall())
    print(data)
    ls=[]
    for teacher in data:
      ls.append(list(teacher))


    
  

    my_keyboard = ReplyKeyboardMarkup(ls,resize_keyboard=True)  # добавляем кнопки
    return my_keyboard

def get_url(name):
    cursor.execute(f"SELECT URL, conf_id, password  FROM  TEACHERS WHERE Name ='{name}'")
    data= list(cursor.fetchall())
   
    
    conf=[]
    for col in data[0]:
      if col != None:
        conf.append(col)

    print(conf)
    return conf


    
