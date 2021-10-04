import cgi
import  model
import footer
import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',
                             database='onlineshopping',autocommit=True)

cursor = connection.cursor()

query = "select * from product"
cursor.execute(query)
data = cursor.fetchall()

query = "select * from cart_table"
cursor.execute(query)
cart_length = cursor.rowcount
data1 = cursor.fetchall()

form = cgi.FieldStorage()
Email = form.getvalue('Email')
Password = form.getvalue('Password')
cust  =  model.login(Email,Password)

name = cust[0][1]
Uid = cust[0][0]




print("""
    <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

    <title>Hello, world!</title>
    <style>
        #footer {
    background-color: #222;
    color: #888;
    margin: 76px 0px;
    padding: 55px 0px;
}
#footer .copy {
    text-align: center;
    margin: 30px 0px;
}
#footer .links {
    font-size: 32px;
    display: block;
}
    </style>
  </head>
  <body>
""")


def log():
    print("""
           <nav class="navbar navbar-expand-lg navbar-light bg-danger">
         <a class="navbar-brand" href="#">ShopingVilla</a>
         <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
           <span class="navbar-toggler-icon"></span>
         </button>
         
         <form class="form-inline my-2 my-lg-0" action="serach.py">
             <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
             <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
           </form>
           
         <h4>Welcome {} To Our Villa</h4>

         <div class="collapse navbar-collapse" id="navbarSupportedContent">
           <ul class="navbar-nav mr-auto">
             <li class="nav-item active">
               <a class="nav-link" href="#"><span class="sr-only">(current)</span></a> 
           </ul>
           <a href="viewOrder.py?Uid={}" class="btn btn-info">View Order</a>
           
         </div>
           <!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
  Your Cart {}
</button>
&nbsp;&nbsp;&nbsp;&nbsp;
<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Your Cart</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
       
      <div class="modal-body">
      
       </nav>   
     <a href="index.py" class="btn btn-dark">Logout</a>                                                                                        
       """.format(name,Uid,cart_length))





    print("""
       <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
         <ol class="carousel-indicators">
           <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
           <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
           <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
         </ol>
         <div class="carousel-inner">
           <div class="carousel-item active">
             <img src="https://www.carloisles.com/project-cms/wp-content/uploads/2014/09/Shop-Online-Made-Easy-in-the-Philippines.gif" class="d-block w-100" alt="...">
           </div>
           <div class="carousel-item">
             <img src="http://blog.cubber.in/wp-content/uploads/2017/10/Amazon-Great-Indian-Diwali-Festival-Sale-for-Online-Shopping-Through-Cubber.jpg" class="d-block w-100" alt="...">
           </div>
           <div class="carousel-item">
             <img src="https://media.gettyimages.com/vectors/sale-banner-and-vector-of-online-shop-vector-id622202466" class="d-block w-100" alt="...">
           </div>
         </div>
         <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
           <span class="carousel-control-prev-icon" aria-hidden="true"></span>
           <span class="sr-only">Previous</span>
         </a>
         <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
           <span class="carousel-control-next-icon" aria-hidden="true"></span>
           <span class="sr-only">Next</span>
         </a>
       </div>
       """)

    print("""
       <div class="container">
           <div class='row' style='align-items:stretch;'>
       """)

    for i in range(len(data)):
        print("""
               <div class='col-md-3 product'>
                   <div class="card">
                   <img src='../ProductImages/{}' class="card-img-top w-100" alt="..." style='min-height:200px;max-height:500px '>
                   <div class="card-body w-100">
                       <h5 class="card-title">{}</h5>
                       <p class="card-text">Price : {} </p>
                       <a href="product_detail.py?p_id={}&Uid={}" class="btn btn-primary">Details</a>

                 </div>
               </div>
               </div>
               """.format(data[i][-1], data[i][2], data[i][4], data[i][0], Uid))
log()
print("</div>")
print("</div>")
footer.footer()


print("""
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </body>
</html>
""")