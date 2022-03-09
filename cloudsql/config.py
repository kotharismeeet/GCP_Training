from google.cloud.sql.connector import connector
import sqlalchemy

def getCloudSQLConnection(region,user,password,dbname):
    conn: pymysql.connections.Connection =  connector.connect(region,'pg8000',user,password,db=dbname)
    return conn

def getPool(region,user,password,dbname):
    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getCloudSQLConnection(region,user,password,dbname),
    )
    return pool