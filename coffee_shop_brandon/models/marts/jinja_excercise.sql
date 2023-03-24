{%- set categories = get_product_categories() -%}

select
  date_trunc(created_at, month) as date_month,
  {%- for category in categories %}
  sum(case when category = '{{category}}' then total end) as {{category | replace(" ", "_")}}_amount
  {%- if not loop.last %},{% endif -%}
  {% endfor -%}
-- you may have to `ref` a different model here, depending on what you've built previously
from {{ ref('sales') }}
group by 1

