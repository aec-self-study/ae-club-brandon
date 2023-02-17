-- models/monthly_users.sql
{{ config(
    materialized="table"
)}}

select
	date_trunc(first_order_at, month) AS month_start,
  	count(*) AS number_new_customers
 
from 
	{{ref('customers')}}
 
group by
	month_start
