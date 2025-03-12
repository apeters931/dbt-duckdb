# call API and create seeds
python3 01_extract/extract.py                                 
# cuild dbt project
cd 02_transform && dbt run && cd && cd dbt-duckdb
# load dbt models to JSON
python3 03_load/load.py
# open data visualizations localy
python3 -m http.server & open http://localhost:8000/04_dashboard/index.html