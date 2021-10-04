import model
import cgi

form  = cgi.FieldStorage()


p_id = form.getvalue('p_id')
p_name = form.getvalue('p_name')
Uid = form.getvalue('Uid')
price = form.getvalue('price')
# if form.getvalue('order'):




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

print("""
     <div id="container">
        <section id="order">
            <h2 class="text-center">Please Confirmed Your Detail </h2>
            <hr>
                <div class="row" >
                    <div class="col-md-6">
                        <form action="confirmOrder.py" method="POST" class="container-fluid">
                            <input type="hidden" value={} name="p_id">
                            <input type="hidden" value={} name="p_name">
                            <input type="hidden" value={} name="Uid">
                            <div class="form-group " class="text-center">
                                <label for="name">Enter Your Name</label>
                                <input type="text" id="name" class="form-control" placeholder="Enter Your Name"  autocomplete="off"  name="name" >
                            </div>
                            <div class="form-group " class="text-center">
                                <label for="email">Enter Your Email</label>
                                <input type="email" id="email" class="form-control" placeholder="Enter Your Email"  autocomplete="off" autofocus name="email" >
                            </div>
                            
                            <div class="form-group " class="text-center">
                                <label for="address">Enter Your Address</label>
                                <input type="text" id="address" class="form-control" placeholder="Enter Your Address"  autocomplete="off" autofocus name="address">
                            </div>
                            <div class="form-group " class="text-center">
                                <label for="contact">Enter Your Contact NO</label>
                                <input type="text" id="name" class="form-control" placeholder="Enter Your Contact no"  autocomplete="off" autofocus name="no">
                            </div>
                            <div class="form-group " class="text-center">
                                <label for="Payemnt">Enter  Product Quantity</label>
                                <input type="text" class="form-control" placeholder="Enter Your Product Quantity" required name="qty">
                            </div>
                            <div class="form-group " class="text-center">
                                <label for="Payemnt">Select Payment Mode</label>
                                    <select class="form-control" id="payment" required name="mode">
                                        <option></option>
                                        <option>Net Banking</option>
                                        <option>Debit/Credit card</option>
                                        <option>paytm</option>
                                        <option>Gpay</option>
                                        <option>Cash on delivery</option>
                                        <option>Phone Pay</option>
                                        <!-- <option></option> -->
                                    </select>
                                 </div>
                            <input type="hidden" value={} name="price">
                            <input type="submit" value="submit" class="btn btn-primary">
                        </form>
                        
                    </div>
                    

                </div>
        </section>
    </div>
    
""".format(p_id,p_name,Uid,price))



print("""
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </body>
</html>
""")
