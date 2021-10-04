import model
import cgi
form = cgi.FieldStorage()
Uid = form.getvalue('Uid')
data = model.ViewOrder(Uid)

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
  </head>
  <body>

""")

print("""
     <h2 class="text-center">Your Order Is Avaiable Here </h2>
     <table width='100%' border=2 cellpadding=10>
         <tr>
             <th>Order Id</th>
             <th>Product Id</th>
             <th>Product Name</th>
             <th>Payment Mode</th>
             <th>Price</th>
             <th>Contact No</th>
             <th>Quantity</th>
             <th>Cancel Order</th>
     """)

for i in range(len(data)):
    print("""
             <tr>
                 <td> {} </td>
                 <td> {} </td>
                 <td> {} </td>
                 <td> {} </td>
                 <td> {} </td>
                 <td> {} </td>
                 <td> {} </td>
                 <td> <a href='cancelOrder.py?Uid={}' class="btn btn-danger">Cancel Order</a> </td>
         """.format(data[i][0], data[i][1], data[i][2], data[i][9], data[i][-1], data[i][7], data[i][8], Uid))

print("</table>")


print("""
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </body>
</html>
""")


