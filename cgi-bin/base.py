import model
import cgi



def header():
    print("""
    <nav class="navbar navbar-expand-lg navbar-dark bg-danger">
  <a class="navbar-brand" href="#">Online Shopping Villa</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    
  </button>
   
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#"> <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#"></a>
      </li>
      
      <li class="nav-item">
      </li>
    </ul>
            <form class="form-inline my-2 my-lg-0" action = 'serach.py'>
            <center>
              <input name = 'searchValue' class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-warning my-2 my-sm-0" type="submit">Search</button>
            </center>
            </form>
             <form class="form-inline my-1 my-lg-0" action = 'serach.py'>
             &nbsp;&nbsp;&nbsp;&nbsp;
            </form>
            <form class="form-inline my-1 my-lg-0" action = 'serach.py'>
             &nbsp;&nbsp;&nbsp;&nbsp;
            </form>
            
        <!-- Login For  -->
           <button type="button" class="btn btn-info btn-lg-block w3ls-btn px-4 text-capitalize mr-2" data-toggle="modal" data-target="#login">
                                      Login
                                  </button> 
            <div class="modal fade" id="login" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Login</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
                <form action="loginController.py" method="post">
                  <div class="form-group">
                      <label for="exampleInputEmail1">Email id</label>
                      <input type="text" name="Email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter id" required autocomplete="off">
                  </div>
                  <div class="form-group">
                      <label for="exampleInputPassword1">Password</label>
                      <input type="password" name="Password" class="form-control" id="exampleInputPassword1" placeholder="Password" required>
                  </div>
                  <button type="submit" class="btn btn-primary">LoginNow</button>
              </form>
                
              </div>
            </div>
          </div>
        </div>

       
       
        <!-- Registration Form For Students -->
         <button type="button" class="btn btn-primary btn-lg-block w3ls-btn px-4 text-capitalize " data-toggle="modal" data-target="#registration">
                                    Register
                                </button> 
                                
         <!-- Registration Form For Students -->
        <div class="modal fade " id="registration" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Registration For Customer</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
                <form action="regiseterController.py" method="post" enctype="multipart/form-data">
                  <div class="form-group">
                      <label for="name">Enter Your Customer Id</label>
                      <input type="text" name="Uid" class="form-control" id="name"  placeholder="Enter name">
                  </div>
                  <div class="form-group">
                      <label for="id">Enter  your Name</label>
                      <input type="text" name="Name" class="form-control" id="id"  placeholder="Enter id">
                      <span class='d-block' id="msg"></span>

                  </div>
                 <div class="form-group">
                    <label for="Email">Email</label>
                    <input type="email" name="Email" class="form-control" id="Pass" placeholder="Enter Your Email">
                 </div>
                    <div>
                    <label for="Password">Enter Your Password</label>
                    <input type="password" name="Password" class="form-control" placeholder="Enter Your Password">
                    </div>
                           <div class="form-group">
                            <label for="Course">Gender</label>
                               <select class="form-control" id="courses", name="Gender">
                                  <option></option>
                                  <option>Male</option>
                                  <option>Female</option>
                                  <option>Transgender</option>
                                </select>
                           </div>
                 <div class="form-group">
                     <label for="Contact No">Contact Number</label>
                    <input type="text" name="Contact" class="form-control" placeholder="Enter Your Contact No">
                 </div>
                  <div class="form-group">
                     <label for="Address">Address</label>
                     <input type="text" name="Address"  id="pro" placeholder="Enter Your Address" class="form-control">
                 </div>
                 <button type="submit" class="btn btn-primary" id="submit">Sign in</button>
                 <button type="reset" class="btn btn-primary">Reset</button>
             </form>
              </div>
            </div>
          </div>
        </div>
        <!-- Registration Form For Students -->
        
          </div>
        </nav>
            """)