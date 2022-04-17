
import sqlite3
import pandas as pd

con = sqlite3.connect("my_contacts.sqlite") # 
cur=con.cursor()

cur.execute("DROP TABLE IF EXISTS my_contacts") # sql 명령어
cur.execute("CREATE TABLE my_contacts (Name, Phone, Email, Birthday)")
cur.execute("INSERT INTO my_contacts VALUES('토비', '080-8686', 'tb@tb.com', '19888-3-3')")
cur.execute("INSERT INTO my_contacts VALUES('아이언맨', '1234-5678', 'tony@avengers.com','1970-5-29')")

con.commit() # 실제로 DB에 적용 

for row in cur.execute('SELECT * FROM my_contacts'):
    print(row)
    
con.close()


# df = pd.DataFrame(
#     {
#         "Name": ["성기훈", "아이언맨", "Robin"],
#         "Phone": ["8734-2398", "1234-5678", "2754-8384"],
#         "Email": ["gh@squid.kr", "tony@avengers.com", "red@dc.net"],
#         "Birthday": ["1974-10-31", "1970-5-29", "1996-3-15"],
#     }
# )

