import cgi
import model

form = cgi.FieldStorage()
p_id = form.getvalue('p_id')
p_desc = form.getvalue('p_desc')
p_rating = form.getvalue('p_rating')
p_offers = form.getvalue('p_offers')
p_highlights = form.getvalue('p_highlights')
p_color = form.getvalue('p_color')
model.storeProductDetails(p_id,p_desc,p_rating,p_offers,p_highlights,p_color)

print("""
<!doctype html>
<html lang="en">
  <head>
   
  </head>
  <body>
  <h1> Inser Successfully</h1>
   <script>
        window.location.assign("http://localhost:8000/cgi-bin/addproduct.py")
    </script>
  </body>
</html>
""")



