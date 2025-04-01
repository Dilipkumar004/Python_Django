{{ config(
    materialized='view',
    database_name='postgres',
    schema='public') 
}}

with source as (
    select user_id
        , address
        , location
        , contact_number
    from claim_address
)

select * 
from source