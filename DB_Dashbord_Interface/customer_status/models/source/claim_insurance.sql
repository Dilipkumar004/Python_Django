{{ config(
    materialized='view',
    database_name='postgres',
    schema='public') 
}}

with source as (
    select claim_id
        , user_id
        , claim_details
        , created_date
    from claim_insurance
)

select *
from source