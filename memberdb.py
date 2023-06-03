import sqlite3

conn = sqlite3.connect('memberdb.sqlite3')  #create data base
c = conn.cursor()

# create table for data storage
c.execute("""CREATE TABLE IF NOT EXISTS member (
                ID  INTEGER PRIMARY KEY AUTOINCREMENT,
                membercode TEXT,
                fullname TEXT,
                tel TEXT,
                usertype TEXT,
                points INTERGER )""")

def Insert_member(membercode,fullname,tel,usertype,points):
    with conn:
        command = 'INSERT INTO member VALUES (?,?,?,?,?,?)' #sql command  NUMBER OF ? IS NUMBER OF DATA ,INCLUDING ID
        c.execute(command,(None,membercode,fullname,tel,usertype,points))
    conn.commit()  #save data base, if it does't commit , database will be locked.
    print('saved')

def View_member():
    # READ
    with conn:
        command = 'SELECT * FROM  member'
        c.execute(command)
        result = c.fetchall() # fet(all) get all, fet(one) get a data , fet(many) get a handful
    print(result)
    return result  

# res = View_member()
# print(res[1])

def Update_member(ID,field,newvalue):
    #UPDATE
    with conn:
        command = f'UPDATE member SET {field} = (?) WHERE ID =(?)'
        c.execute(command,([newvalue,ID]))
    conn.commit()
    print('updated')


def Delete_member(ID):
    with conn:
        command = 'DELETE FROM  member WHERE ID=(?)'
        c.execute(command,([ID]))
    conn.commit()
    print('deleted')

#Update_member(2,'fullname','somsak chareanrungruang')
#Delete_member(1)
#View_member()
if __name__ == '__main__':
     Insert_member('MB-1001','somchai kengmark','08318555','general',100)

