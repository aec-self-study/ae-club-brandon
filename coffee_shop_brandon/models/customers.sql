-- models/customers.sql
 
{{ config(
    materialized='table'
 ) }}
 
SELECT
  customers.id AS customer_id,
  name,
  email,
  MIN(created_at) AS first_order_at,
  COUNT(orders.id) AS number_of_orders
FROM
  `analytics-engineers-club.coffee_shop.customers` AS customers
LEFT JOIN
  `analytics-engineers-club.coffee_shop.orders`AS orders
ON
  customers.id = orders.customer_id
GROUP BY
  customer_id,
  name,
  email
ORDER BY
  first_order_at
LIMIT
  5
