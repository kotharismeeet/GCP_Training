#https://blog.panoply.io/how-to-load-pandas-dataframes-into-sql
from io import StringIO
def uploadDftoDB(df,pool):
    df.head(0).to_sql('STOCKS',con=pool,index=False)
    raw_conn = pool.raw_connection()
    raw_cur = raw_conn.cursor()
    out = StringIO()

    # write just the body of your dataframe to a csv-like file object
    df.to_csv(out, sep='\t', header=False, index=False) 

    out.seek(0) # sets the pointer on the file object to the first line
    contents = out.getvalue()
    print(contents)
    # copies the contents of the file object into the SQL cursor and sets null values to empty strings
    raw_cur.copy_from(contents, 'STOCKS', null="") 
    raw_conn.commit()