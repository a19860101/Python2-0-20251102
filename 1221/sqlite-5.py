import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 更新資料
# UPDATE 資料表 SET 欄位=值,欄位=值,... WHERE id=值
sql_update = 'UPDATE users SET name=?,phone=?,email=? WHERE id=?'
cursor.execute(sql_update,['Mary','0922654321','mary@gmail.com',2])

conn.commit()
conn.close()