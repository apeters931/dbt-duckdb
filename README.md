local ETL data pipepline using dbt and duckdb.

1. API call to [Rick and Morty API](https://rickandmortyapi.com/about); Data is loaded as a seed (csv) in the dbt project
2. dbt transforms the seed files and materilzes the tables to duckdb
3. Python script converts the transformed data to JSON
4. Data visualizations are created with Chart JS using the JSON data