import model
import cgi
import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',
                             database='onlineshopping',autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()

p_id = form.getvalue('p_id')

query = "select p_id,p_name,p_image,p_price from product where p_id = %s"
cursor.execute(query,p_id)
data = cursor.fetchall()

model.addToCart(data[0][0],data[0][1],data[0][2],data[0][3])

print("""
<!doctype html>
<html lang="en">
  <head>
    <script>
        window.location.assign("http://localhost:8088/cgi-bin/index.py")
    </script>
  </head>
  <body>
  </body>
</html>
""")