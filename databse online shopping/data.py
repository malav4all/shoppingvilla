import pymysql
connection = pymysql.connect(host="localhost",port=3306,user="root",database = "onlineshopping",autocommit = True)
cursor = connection.cursor()
p_id = 116
p_catergory = "laptop"
p_name = "Apple MacBook Air Core i5 5th Gen - (8 GB/128 GB SSD/Mac OS Sierra) MQD32HN/A A1466"
p_brand = "Apple"
p_price = "62,990"
p_image = "https://rukminim1.flixcart.com/image/352/352/jsnjbm80/computer/j/8/c/apple-na-thin-and-light-laptop-original-imafe6f78hur4jbh.jpeg?q=70"
query = "insert into product values (%s,%s,%s,%s,%s,%s)"
cursor.execute(query,(p_id,p_catergory,p_name,p_brand,p_price,p_image))
#data = cursor.fetchall()
print("Data inserted Sucessfully......")

