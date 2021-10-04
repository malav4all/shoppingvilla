import pymysql
import base
import cgi

connection = pymysql.connect(host='localhost',user='root',database='onlineshopping',
                             port = 3306, autocommit = True)
cursor = connection.cursor()

form = cgi.FieldStorage()
p_id = form.getvalue('p_id')
query_1 = "select * from product_detail where p_id = %s"
cursor.execute(query_1, (p_id))
product_detail = cursor.fetchall()

query_2 = "select * from product where p_id = %s"
cursor.execute(query_2, (p_id))
data = cursor.fetchall()
price = data[0][4]
p_name = data[0][2]

Uid = form.getvalue('Uid')

print("""
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="../styles.css">
    <title>Hello, world!</title>
  </head>
  <body>
  """)

base.header()



print("""
<div class="container">
<h2 class='text-center'> Product Detail </h2>
<hr>
        <div class="row">
            <div class="col-md-4">
                <img src="../ProductImages/{}" class='w-100'>
            </div>
            <div class="col-md-8">
                <h3>Title</h3>
                <p>{}</p>
                <h4>Price</h4>
                <p>{}</p>
                <h4>Rating : {}</h4>
                <h4>Description</h4>
                <p>{}</p>
                <p>Offers : {}</p>
                <h4>Highlights</h4>
                <p>{}</p>
                
                <form action='cartController.py'>
        <input type='hidden' name='p_id' value={}>
            <button type='submit' class='btn btn-danger'>Add to Cart </button>  
            <a href="placeorder.py?p_id={}&price={}&p_name={}&Uid={}" class="btn btn-secondary">PlaceOrder</a>   
        </form>
        
            </div>
            
        </div>
    </div>
""".format(data[0][-1], data[0][3], data[0][4],
product_detail[0][2],product_detail[0][1],product_detail[0][3],
product_detail[0][4],data[0][0],p_id,price,p_name,Uid))

print("""
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
""")