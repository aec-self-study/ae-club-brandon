{% macro get_product_categories() %}

{{ return(get_column_values('category', ref('sales'))) }}

{% endmacro %}