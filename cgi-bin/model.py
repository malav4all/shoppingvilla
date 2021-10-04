import pymysql
import os

connection = pymysql.connect(host='localhost',port=3306,user='root',
                             database='onlineshopping',autocommit=True)

cursor = connection.cursor()

class Product():

    def __init__(self,p_id,p_name,p_image,p_price):
        self.p_id = p_id
        self.p_name = p_name
        self.p_image = p_image
        self.p_price = p_price


class User:
    def __init__(self,Uid,Name,Email,Password,Gender,Contact,Address):
        self.Uid = Uid
        self.Name = Name
        self.Email = Email
        self.Password = Password
        self.Gender = Gender
        self.Contact = Contact
        self.Address = Address


class Feedback:
    #constructor
    def __init__(self,Uid,message):
        self.Uid = Uid
        self.message = message

class insertProduct:
    def __init__(self,p_id,p_category,p_name,p_brand,p_price,p_image):
        self.p_id = p_id
        self.p_category = p_category
        self.p_name = p_name
        self.p_brand = p_brand
        self.p_price = p_price
        self.p_image = p_image


#Customer Registration Function
def customer(Uid,Name,Email,Password,Gender,Contact,Address):
    cust = User(Uid,Name,Email,Password,Gender,Contact,Address)
    query = "insert into user values (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(cust.Uid,cust.Name,cust.Email,cust.Password,cust.Gender,cust.Contact,cust.Address))
# ------------------------------------------------------------------------------------------------------------------
#customer login Function
def login(Email,Password):
    query = "select * from user where Email=%s and Password=%s"
    cursor.execute(query,(Email,Password))
    cust = cursor.fetchall()
    # return user
    if len(cust) < 1:
        return "Invalid Customer"
    else:
        return cust
# ----------------------------------------------------------------------------------------------------------------------

#Add To cart System
def addToCart(p_id,p_name,p_image,p_price):
    prod = Product(p_id,p_name,p_image,p_price)
    query = "insert into cart_table values(%s,%s,%s,%s)"
    cursor.execute(query, (prod.p_id,prod.p_name,prod.p_image,prod.p_price))
# ----------------------------------------------------------------------------------------------------------------------


#FeedBack Function
def feedback(Uid,Email,message):
    query="insert into feedback values (%s,%s,%s)"
    cursor.execute(query,(Uid,Email,message))



#admin login
def admin(adminId,Password):
    query = "select * from admin where adminId = %s and Password = %s"
    cursor.execute(query,(adminId,Password))
    data = cursor.fetchall()
    if len(data) < 1:
        return "Invalid Admin"
    else:
        return data


def fetchAllUser():
    query = "select * from user "
    cursor.execute(query)
    data = cursor.fetchall()
    return data


def place(p_id,p_name,Uid,Name,Email,Address,Contactno,quantity,paymentmode,price):
    query = "insert into payment(p_id,p_name,Uid,Name,Email,Address,Contactno,quantity,paymentmode,price) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(p_id,p_name,Uid,Name,Email,Address,Contactno,quantity,paymentmode,price))


def fetchAllPayment():
    query = "select * from payment"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def adminInsertProduct(p_id,p_category,p_name,p_brand,p_price,p_image):
    if p_image.filename:
        fn = os.path.basename(p_image.filename)
        img = p_image.file.read()
        file = open("ProductImages/" + fn, 'wb')
        file.write(img)
        file.close()
    else:
        fn = "defaultpic.jpg"
    product = insertProduct(p_id,p_category,p_name,p_brand,p_price,fn)
    query = "insert into product(p_id,p_category,p_name,p_brand,p_price,p_image) values (%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(product.p_id,product.p_category,product.p_name,product.p_brand,product.p_price,product.p_image))

def getProductId(p_id):
    query = "select * from product where p_id = %s"
    cursor.execute(query,p_id)
    data = cursor.fetchall()
    return data


def storeProductDetails(p_id,p_desc,p_rating,p_offers,p_highlights,p_color):
    query = "insert into product_detail(p_id,p_desc,p_rating,p_offers,p_highlights,p_color) values (%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(p_id,p_desc,p_rating,p_offers,p_highlights,p_color))


def ViewOrder(Email):
    query = "select * from payment where Uid=%s"
    cursor.execute(query,Email)
    data = cursor.fetchall()
    return data


def CancelOrder(Email):
    query = "delete from payment where Uid = %s"
    cursor.execute(query,Email)


def fetchAllProduct():
    query = "select *  from product"
    cursor.execute(query)
    data_1 = cursor.fetchall()
    return data_1

def FetchAllfeedback():
    query = "select * from feedback"
    cursor.execute(query)
    data = cursor.fetchall()
    return data




