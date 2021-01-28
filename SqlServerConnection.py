import pypyodbc
import pandas as pd

con = pypyodbc.connect("Driver={SQL Server};"
                        "Server=127.0.0.1,1433;"
                        "Database=master;"
                        "uid=sa;pwd=P4ssw0rd")
                        #"Trusted_Connection=yes;")#

cursor = con.cursor()

# cursor.execute("INSERT INTO pessoa VALUES (40, 'Pessoa 40', 2345.78)")
# cursor.execute("UPDATE pessoa SET salario = 3456.89 WHERE id = 40")
# cursor.execute("DELETE pessoa WHERE id = 40")
# con.commit()

df = pd.read_sql_query('select * from pessoa', con)
print(df)
