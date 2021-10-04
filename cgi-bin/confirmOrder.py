import cgi
import model
form = cgi.FieldStorage()

p_id = form.getvalue('p_id')
p_name = form.getvalue('p_name')
Uid = form.getvalue('Uid')
price = form.getvalue('price')


Name = form.getvalue('name')
Email = form.getvalue('email')
Address = form.getvalue('address')
Contactno = form.getvalue('no')
quantity = form.getvalue('qty')
paymentmode = form.getvalue('mode')
model.place(p_id,p_name,Uid,Name,Email,Address,Contactno,quantity,paymentmode,price)

print("""
    <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <title>Place Order</title>
  </head>
  <body>
  """)


# print("<h2>Thank Your For Vist Our Shopping Villa</h2>")
print("""
    <h2 class="text-center">Thanks You For Visting Our Shopping Villa {}</h2>
     <a href="feedback.py?Uid={}&Email={}" class="btn btn-success">FeedBack</a>    
""".format(Name,Uid,Email))
print("""
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </body>
</html>
""")
