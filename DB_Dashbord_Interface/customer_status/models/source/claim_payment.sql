{{ config(
    materialized='view',
    database_name='postgres',
    schema='public') 
}}

with source as (
    select claim_id
        , total_amount
        , pending_amount
        , amount_paid
        , transaction_id
        , payment_date
    from claim_payment
)
select *
from source