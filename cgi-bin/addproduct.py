import cgi
import model

form = cgi.FieldStorage()

data_1 = model.fetchAllProduct()




print("""
    <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

    <title>Add Product</title>
  </head>
  <body>
""")


print("""   
        <div id="container">
            <section id="product">
                <h2 class="text-center">Add Product </h2>
                <hr>
                    <div class="row justify-content-center">
                        <div class="col-md-6">
                            <form action="confirmAddproduct.py" method="POST" class="container-fluid" enctype="multipart/form-data">
                                <div class="form-group " class="text-center">
                                    <label for="email">Pid</label>
                                    <input type="text" id="email" class="form-control" placeholder="Product Id"  autocomplete="off" name="p_id">
                                </div>
                                <div class="form-group " class="text-center">
                                    <label for="name">Product Categoery</label>
                                    <input type="text" id="Email" class="form-control" placeholder="Product Categoery"  autocomplete="off" name="p_category">
                                </div>
                                <div class="form-group " class="text-center">
                                    <label for="address">Product Name</label>
                                    <input type="text" id="product" class="form-control" placeholder="Product Name"  autocomplete="off" name="p_name">
                                </div>
                                <div class="form-group " class="text-center">
                                    <label for="contact">Product Brand</label>
                                    <input type="text" id="name" class="form-control" placeholder="Product Brand"  autocomplete="off" name="p_brand">
                                </div>
                                <div class="form-group " class="text-center">
                                    <label for="Payemnt">Product Price</label>
                                    <input type="text" class="form-control" placeholder="Product Price" required name="p_price">
                                     </div>
                                <div class="form-group " class="text-center">
                                    <label for="Image">Product Image</label>
                                       <input type="file" name="p_image" required id="Image">
                                     </div>
                            <button value="Submit" class="btn btn-danger" class="text-center" > Submit</button>

                            </form>
                        </div>

                    </div>
            </section>
        </div>
    """)

print("""
    <hr>
     <h2 class="text-center">All Product Available Here </h2>
     <table width='100%' border=2 cellpadding=10>
         <tr>
             <th>Product id</th>
             <th>Product Category</th>
             <th>Product Name</th>
             <th>Product Brand</th>
             <th>Product Price</th>
             <th>Product Image</th>
             <th>Delete Product</th>
     """)

for i in range(len(data_1)):
    print("""
             <tr>
                 <td> {} </td>
                 <td> {} </td>
                 <td> {} </td>
                 <td> {} </td>
                 <td> {} </td>
                 <td> {} </td>
                 <td> <a href='deleteproduct.py?' class="btn btn-danger">Delete Product</a> </td>
         """.format(data_1[i][0], data_1[i][1], data_1[i][2], data_1[i][3], data_1[i][4], data_1[i][-1]))

print("</table>")



print("""
      <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </body>
</html>
""")
