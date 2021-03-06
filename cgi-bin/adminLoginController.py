import cgi
import model


form = cgi.FieldStorage()


adminId = form.getvalue('adminId')
Password = form.getvalue('Password')

data = model.admin(adminId,Password)
name = data[0][0]


print("""
    <!doctype html>
<html lang="en">
  <head> 
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <title>admin||Home Page</title>
  </head>
  <body>
""")


def homepage():
    print("""
         <section id="tabs">
        <div class="container">
          <h3 class="text-center">Welcome {}</h3>
          <hr>
          <a href="addproduct.py" class="btn btn-primary">Add Product</a>
          
          <a href="viewPayment.py" class="btn btn-info">View Payment</a>
          <a href="viewFeedback.py" class="btn btn-success">View Feedback</a>
          <a href="viewUser.py" class="btn btn-danger">View Customer</a>
         </div>
    </section>
      <hr>    
    """.format(name))

if isinstance(data,str):
    print("<h2>Login failed</h2>")
else:
    homepage()

print("""
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </body>
</html>    
""")