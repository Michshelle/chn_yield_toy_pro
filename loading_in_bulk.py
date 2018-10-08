import pymysql
import pandas as pd
import sys
import os


def mysql_to_csv(sql,file_path,host,port,db,user,password):
    try:
        con = pymysql.connect(host=host,port=port,db=db,user=user,password=password)
        print("Connected to DB: {}".format(host))

        df = pd.read_sql(sql,con)
        df.to_csv(file_path,encoding='utf-8',header=True,doublequote=True,sep=',',index=False)
        print("File,{} has been created successfully".format(file_path))
        con.close()

    except Exception as e:
        print("Error:{}".format(str(e)))
        sys.exit(1)

def csv_to_mysql(load_sql,host,port,db,user,password):
    try:
        con = pymysql.connect(host=host,port=port,db=db,user=user,password=password,autocommit=True,local_infile=1)
        print("Connected to DB:{}".format(host))

        cursor=con.cursor()
        cursor.execute(load_sql)
        print("Successfully loaded the table from csv.")
        con.close()

    except Exception as e:
        print("Error:{}".format(str(e)))
        sys.exit(1)

if __name__ == "__main__":

    host = '127.0.0.1'
    port = 3306
    db = 'research_tool'
    user = 'root'
    password = os.environ['MYSQL_PD']
    

    

    ##loop files
    rootdir = './'
    listing = os.listdir(rootdir)
    for file_csv in listing:
        if file_csv.endswith('.csv'):

            load_sql = """LOAD DATA LOCAL INFILE '{}' INTO TABLE chn_yield_curve FIELDS TERMINATED by ',';;""".format(file_csv)
            csv_to_mysql(load_sql,host,port,db,user,password)






    
