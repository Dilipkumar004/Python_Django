{{ config(
    materialized='view',
    database_name='postgres',
    schema='public') }}

with source_data as (
    select name
        , user_id
        , age
        , gender
    from claim_user  
)

select * 
from source_data

--dbt run --target dev2 --model models\source