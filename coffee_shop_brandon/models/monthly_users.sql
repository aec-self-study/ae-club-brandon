-- models/monthly_users.sql
 select
  date_trunc(first_order_at, month)
  count(*)
 
from {{ ref('customers') }}
 
group by 1
