import sqlite3

conn = sqlite3.connect('productdb.sqlite3')  #create data base
c = conn.cursor()

# create table for data storage
c.execute("""CREATE TABLE IF NOT EXISTS product(
                ID  INTEGER PRIMARY KEY AUTOINCREMENT,
                productid TEXT,
                title TEXT,
                price REAL,
                image TEXT)""")

def Insert_product(productid,title,price,image):
    with conn:
        command = 'INSERT INTO product VALUES (?,?,?,?,?)' #sql command  NUMBER OF ? IS NUMBER OF DATA ,INCLUDING ID
        c.execute(command,(None,productid,title,price,image))
    conn.commit()  #save data base, if it does't commit , database will be locked.
    print('saved')

def View_product():
    # READ
    with conn:
        command = 'SELECT * FROM  product'
        c.execute(command)
        result = c.fetchall() # fetch(all) get all, fetch(one) get a data , fetch(many) get a handful
    print(result)
    return result  

def View_product_single(productid):
    # READ
    with conn:
        command = 'SELECT * FROM  product WHERE productid=(?)'
        c.execute(command,([productid]))
        result = c.fetchone() # fetch(all) get all, fetch(one) get a data , fetch(many) get a handful
    print(result)
    return result 

if __name__ == '__main__':
    Insert_product('CF-002','expresso',45,r'C:\image\espresso.png')
    View_product()
        
