import cgi
import base
import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',
                             database='onlineshopping',autocommit=True)

cursor = connection.cursor()
form = cgi.FieldStorage()
product = form.getvalue('searchValue')
query = "select * from product where p_category LIKE '%{}%' or p_name = '{}' or p_brand = '{}'".format(product,product,product)
cursor.execute(query)
data = cursor.fetchall()


print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
""")

base.header()

print("""
<div class="container">
    <h1 class="text-center">Products</h1>
    <hr>
    <div class="row">
""")
for i in range(len(data)):
    searchValue = product.lower()
    if searchValue in data[i][1].lower() or searchValue == data[i][2].lower() or searchValue == data[i][3].lower():
        print("""
        <div class="col-md-3">
        <div class="card" style="width: 18rem;margin-bottom:20px; padding:10px;">
          <img src="{}" class="card-img-top" alt="img" height=400>
          <div class="card-body">
            <h5 class="card-title">{}</h5>
            <p class="card-text">Price : {}</p>
            <a href="cart.py" class="btn btn-primary">Add to Cart</a>
          </div>
        </div>
        </div>
        """.format(data[i][-1], data[i][2], data[i][3]))

print("""
</div>
</div>
""")
