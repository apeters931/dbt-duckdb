import duckdb
import json

# get data
conn1 = duckdb.connect('./dev.duckdb')
conn2 = duckdb.connect('./dev.duckdb')
query1 = "select * from rick_and_morty_characters"
query2 = "select name from rick_and_morty_characters"
result1 = conn1.execute(query1)
result2 = conn2.execute(query2)
df1 = result1.df()
df2 = result2.df()
df1.to_json('exports/characters_transformed.json')
df2.to_json('exports/names.json')
conn1.close()
conn2.close()
