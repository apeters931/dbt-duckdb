
  
  create view "dev"."main"."rick_and_morty_characters__dbt_tmp" as (
    select * 
from "dev"."main"."characters"
  );
