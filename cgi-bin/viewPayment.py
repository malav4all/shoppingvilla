import model

data = model.fetchAllPayment()

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
     <section id="section_3">
        <div class="container">
        <hr>
            <h2 class="text-center">Payment Details Availabe Here</h2>
            <hr>
            <table class="table table-hover w-100">
                <thead>
                    <tr>
                        <th scope="col">OrderId</th>
                        <th scope="col">P_id</th>
                        <th scope="col">ProductName</th>
                        <th scope="col">CustomerId</th>
                        <th scope="col">CustomerName</th>
                        <th scope="col">Email</th>
                        <th scope="col">Address</th>
                        <th scope="col">Contact No</th>
                        <th scope="col">Quantity</th>
                        <th scope="col">PaymentMode</th>
                        <th scope="col">Price</th>
                    </tr>
                     </thead>

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
             <td> {} </td>
             <td> {} </td>
             <td> {} </td>
             <td> {} </td>
     """.format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],data[i][5],data[i][6],data[i][7],data[i][8],data[i][9],data[i][-1]))

print("""        
        </tr>    
            </table>
        </div>
      </section>
""")

print("""
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </body>
</html>
""")