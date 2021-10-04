import model
import cgi
form = cgi.FieldStorage()

p_id = form.getvalue('p_id')
p_category = form.getvalue('p_category')
p_name = form.getvalue('p_name')
p_brand = form.getvalue('p_brand')
p_price = form.getvalue('p_price')
p_image = form['p_image']
model.adminInsertProduct(p_id,p_category,p_name,p_brand, p_price,p_image)
data = model.getProductId(p_id)

print("""
    <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

    <title>Add Product Details</title>
  </head>
  <body>
""")


print("""
        <div id="container">
            <section id="product">
                <h2 class="text-center">Add Product Details </h2>
                <hr>
                    <div class="row justify-content-center">
                        <div class="col-md-6">
                            <form action="addDetails.py" method="POST">
                            <table cellpadding=10>
            <tr>
                <td>Select Your Product Id</td>
                <td>
                    <select name='p_id'>
                    """)
for i in range(len(data)):
    print("""
    <option value = {}>{}</option>
    """.format(data[i][0], data[i][0]))

print("""
        </select>
        </td>
        </tr>
        </table>
         <label for="email">Enter Your Product Description</label>
                                    <input type="text" id="email" class="form-control" placeholder="Enter Your Product Description"  autocomplete="off" name="p_desc">
                                </div>
                                <div class="form-group " class="text-center">
                                    <label for="name">Enter Your Product Ratings</label>
                                    <input type="text" id="Email" class="form-control" placeholder="Enter Rating"  autocomplete="off" name="p_rating">
                                </div>
                                <div class="form-group " class="text-center">
                                    <label for="address">Offers</label>
                                    <input type="text" id="product" class="form-control" placeholder="Offers"  autocomplete="off" name="p_offers">
                                </div>
                                <div class="form-group " class="text-center">
                                    <label for="contact">Product Highlights</label>
                                    <input type="text" id="name" class="form-control" placeholder="Product Highlights"  autocomplete="off" name="p_highlights">
                                </div>
                                <div class="form-group " class="text-center">
                                    <label for="Payemnt">Product Colour</label>
                                    <input type="text" class="form-control" placeholder="Product Color" required name="p_color">
                                     </div> 
                            <button value="Submit" class="btn btn-danger" class="text-center" > Submit</button>

                            </form>
                        </div>

                    </div>
            </section>
        </div>       
                                   
    """)



print("""
      <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </body>
</html>
""")