import mysql.connector
import datetime
# def get_coupon_homepage():
#     url = "https://www.4freeapp.com/"
#     respond = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
#     html = BeautifulSoup(respond.text)
#     main = html.find_all("div", class_="caption")

mydb = mysql.connector.connect(
    user='root',
    passwd='April29love',
    host='localhost',
    database='mysql ',
)

mycursor = mydb.cursor()
mycursor.execute('use mangerdb')

def prevent_duplicate(id,title,MyClass,content):
    # test_id = (id,)
    test_title = (title,)
    sql = "select * from mangerdb_item where title = %s"
    mycursor.execute(sql,test_title)
    myresult = mycursor.fetchall()
    if myresult:
        print('重複的資料','id',id,'標題',test_title[0])
    else:
        insert_sql = "insert ignore into mangerdb_item (id , title ,Myclass , content) values (%s,%s,%s,%s)"
        insert_data = (id,title,MyClass,content)
        mycursor.execute(insert_sql,insert_data)
        mydb.commit()
        if mycursor.rowcount:
            print("資料成功輸入")
        else:
            time_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            insert_data = (time_id,title,MyClass,content)
            mycursor.execute(insert_sql,insert_data)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.","id改為時間參數")
