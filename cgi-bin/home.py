
import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',
                             database='onlineshopping',autocommit=True)

cursor = connection.cursor()

query = "select * from cart_table"
cursor.execute(query)
cart_length = cursor.rowcount
data = cursor.fetchall()

#
# def header():
#     print("""
#     <nav class="navbar navbar-expand-lg navbar-dark bg-danger">
#   <a class="navbar-brand" href="#">Online Shopping Villa</a>
#   <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
#     <span class="navbar-toggler-icon"></span>
#
#   </button>
#
#   <div class="collapse navbar-collapse" id="navbarSupportedContent">
#     <ul class="navbar-nav mr-auto">
#       <li class="nav-item active">
#         <a class="nav-link" href="#"> <span class="sr-only">(current)</span></a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="#"></a>
#       </li>
#
#       <li class="nav-item">
#       </li>
#     </ul>
#
#     <!-- Button trigger modal -->
# <button type="button" class="btn btn-danger" data-toggle="modal" data-target="#exampleModal">
#   Your Cart {}
# </button>
# &nbsp;&nbsp;&nbsp;&nbsp;
# <!-- Modal -->
# <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
#   <div class="modal-dialog" role="document">
#     <div class="modal-content">
#       <div class="modal-header">
#         <h5 class="modal-title" id="exampleModalLabel">Your Cart</h5>
#         <button type="button" class="close" data-dismiss="modal" aria-label="Close">
#           <span aria-hidden="true">&times;</span>
#         </button>
#       </div>
#       <div class="modal-body">""".format(cart_length))
#
#     for i in range(cart_length):
#         print("""
#                <div class='row align-items-center'>
#                    <div class='col-md-2'>
#                        <img src={} class='w-100'>
#                    </div>
#                    <div class='col-md-5'>
#                        <h5>{}</h5>
#                    </div>
#                    <div class='col-md-3'>
#                        <p> Price : {}</p>
#                    </div>
#                </div>
#                <hr>
#                """.format(data[i][2], data[i][1], data[i][-1]))
# print("""
#         </div>
#               <div class="modal-footer">
#                 <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
#                 <a href="#" class="btn btn-primary">Buy Now</a>
#               </div>
#             </div>
#           </div>
#         </div>
#             <form class="form-inline my-2 my-lg-0" action = 'serach.py'>
#             <center>
#               <input name = 'searchValue' class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
#               <button class="btn btn-warning my-2 my-sm-0" type="submit">Search</button>
#             </center>
#             </form>
#              <form class="form-inline my-1 my-lg-0" action = 'serach.py'>
#              &nbsp;&nbsp;&nbsp;&nbsp;
#             </form>
#             <form class="form-inline my-1 my-lg-0" action = 'serach.py'>
#              &nbsp;&nbsp;&nbsp;&nbsp;
#             </form>
#         """)
