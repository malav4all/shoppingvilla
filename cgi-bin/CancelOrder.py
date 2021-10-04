import cgi
import model


form = cgi.FieldStorage()
Uid = form.getvalue('Uid')

model.CancelOrder(Uid)

print("""
<!doctype html>
<html lang="en">
  <head> 
  </head>
  <body>
  <h1>Your Order Cancel Succefully</h1>
  </body>
</html>
""")