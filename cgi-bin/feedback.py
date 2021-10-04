import cgi
import model


form = cgi.FieldStorage()
Uid = form.getvalue("Uid")
Email = form.getvalue('Email')
print("""
    <!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Feedback</title>
  </head>
  <body>
""")
def feedBack():
    print("""
<form action="feedback.py" method="post">
<input type="hidden" value={} name="Uid">
<input type="hidden" value={} name="Email"> 
  <div class="form-group">
    <label for="Select Your FeedBack">Enter your FeedBack</label>
    <select class="form-control" name="message">
      <option>Worst</option>
      <option>Poor</option>
      <option>Average</option>
      <option>Good</option>
      <option>Exellent</option>
    </select>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
    """.format(Uid,Email))


feedBack()

# Uid = form.getvalue('Uid')
message = form.getvalue('message')


data = model.feedback(Uid,message)


print("""
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>
""")