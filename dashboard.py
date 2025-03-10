import duckdb
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

conn = duckdb.connect('dev.duckdb')

query = "select * from rick_and_morty_characters"

result = conn.execute(query)

df = result.df()

sns.barplot(x = 'name',
            y = 'no_ep',
            data = df.head())

#plt.show()
plt.savefig('my_plot.png')

conn.close()