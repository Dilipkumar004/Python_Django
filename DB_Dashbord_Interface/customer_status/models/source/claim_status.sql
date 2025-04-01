{{ config(
    materialized='view',
    database_name='postgres',
    schema='public') 
}}

with source as (
    select transaction_id
        , payment_status
        , created_date
    from claim_status
)

select *
from source