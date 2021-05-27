import mysql.connector as conn
import csv
mydb = conn.connect(host="localhost", user="root", passwd="fsc", use_pure=True)
curr = mydb.cursor()
arr = []
with open('carbon_nanotubes.csv', 'r') as data:
    data_csv = csv.reader(data, delimiter="\n")
    column = ''
    for i in data_csv:
        k = 1
        column = i[0]
        if(k == 1):
            break
    x = 1
    for i in data_csv:
            a = ''
            b = False
            c=False
            for j in range(0, len(i[0])):
                if(i[0][j] != ';'):
                    if(c==True):
                        c=False
                        continue
                    if(b == False):
                        a += i[0][j]
                    else:
                        if(i[0][j]!='0'):
                            a += i[0][j]
                        else:
                            c=True             
                        b=False
                else:
                    a += ','
                    b = True
            arr.append(a)
        
queries = ["USE CARBONATOM","CREATE TABLE ATOMICITYYYY",
           "INSERT INTO ATOMICITYYYY VALUES"]
for query in range(0, len(queries)):
    if query == 1:
        b=queries[1]
        z=[]
        q=''
        for i in column:
            if(i==';'):
                z.append(q)
                q=''
            elif(i!="'"):
                if(i==' '):
                    q+='_'
                else:
                    q+=i
        z.append(q)
        b+="("
        f=""
        for i in range(0,len(z)):
             b+=(z[i]+" varchar(20),")
        fstr=b[0:len(b)-1]
        fstr+=")"
        curr=mydb.cursor()
        curr.execute(fstr)
    elif query == 2:
        for v in arr:
          curr = mydb.cursor() 
          if v[len(v)-1]==',':
              v+="765378"
          curr.execute(queries[2]+"({val})".format(val=((v))))
    else:
        curr = mydb.cursor()
        curr.execute(queries[query])

mydb.commit()
    