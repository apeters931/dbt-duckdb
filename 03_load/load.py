import duckdb
import json

# get data
conn1 = duckdb.connect('./transform/dev.duckdb')
query1 = "select * from rick_and_morty_characters"
result1 = conn1.execute(query1)
df1 = result1.df()
df1.to_json('load/characters_transformed.json')
print("characters_transformed.json created in load directory")
conn1.close()
