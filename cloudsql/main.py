from config import getPool
pool = getPool('region','user','password','dbname')

from data import getData
df = getData()
#print(df.columns)

from queries import uploadDftoDB
#uploadDftoDB(df,pool)