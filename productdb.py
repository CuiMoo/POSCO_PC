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

c.execute("""CREATE TABLE IF NOT EXISTS product_status(
                ID  INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                status TEXT)""")


def insert_product_status(pid,status):
    #pid = product id
    check = View_product_status(pid) #เช็คว่ามี ใน pid ไหม ถ้าไม่มีให้ insert
    if check == None:     
        with conn:
            command = 'INSERT INTO product_status VALUES(?,?,?)'
            c.execute(command,(None,pid,status))
        conn.commit()
        print('status saved')
    else:
        print('pid exist!')
        Update_product_status(pid,status)
    
def View_product_status(pid):
    # READ
    with conn:
        command = 'SELECT * FROM  product_status WHERE product_id=(?)'
        c.execute(command,([pid]))
        result = c.fetchone() # fetch(all) get all, fetch(one) get a data , fetch(many) get a handful
    return result 
    
def Update_product_status(pid,status):
    #UPDATE
    with conn:
        command = 'UPDATE product_status SET status = (?) WHERE product_id =(?)'
        c.execute(command,([status,pid]))
    conn.commit()
    print('updated:',(pid,status))


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

def View_product_table_icon(): #select partial of DB
    # READ
    with conn:
        command = 'SELECT ID, productid, title FROM  product'
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

'''
product = {'latte':{'name':'ลาเต้','price':30},
           'cappuccino':{'name':'คาปูชิโน','price':35},
           'espresso':{'name':'เอสเปรสโซ่','price':40},
           'greentea':{'name':'ชาเขียว','price':20},
           'icetea':{'name':'ชาเย็น','price':15},
           'hottea':{'name':'ชาร้อน','price':10},}
'''
def product_icon():
    with conn:
        command = 'SELECT * FROM  product'
        c.execute(command)
        product = c.fetchall()
    with conn:
        command = "SELECT * FROM product_status WHERE status ='show'"
        c.execute(command)
        status = c.fetchall()
    result = []

    for s in status:
        for p in product:
            if s[1] == p[0]:
                print(p,s[-1])
                result.append(p)
    
    print(result)


if __name__ == '__main__':
    product_icon()
    # insert_product_status('CF-1002','esspesso',45,r'C:\image\latte.png')
    # View_product()
    # View_product_table_icon()
    # insert_product_status(2,'')
    #print(View_product_status(2))