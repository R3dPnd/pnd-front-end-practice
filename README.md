# Front-end Practice

```sql
/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/

/*
* customer name
* product name
* quantity
*/

SELECT customer_name, product_name, quantity  FROM (SELECT 
    COALESCE(c.customer_name, 'N/A') as customer_name,
    COALESCE(ii.quantity, 0) as quantity,
    COALESCE(p.product_name, 'N/A') as product_name,
    COALESCE(c.id, 0) as customer_id,
    COALESCE(p.id, 0) as product_id,
    COALESCE(ii.id, 0) as invoice_item_id

FROM customer c
LEFT JOIN invoice i ON c.id = i.customer_id
LEFT JOIN invoice_item ii ON i.id = ii.invoice_id
LEFT JOIN product p ON ii.product_id = p.id

UNION

SELECT 
    COALESCE(c.customer_name, 'N/A') as customer_name,
    COALESCE(ii.quantity, 0) as quantity,
    COALESCE(p.product_name, 'N/A') as product_name,
    COALESCE(c.id, 0) as customer_id,
    COALESCE(p.id, 0) as product_id,
    COALESCE(ii.id, 0) as invoice_item_id
FROM product p
LEFT JOIN invoice_item ii ON p.id = ii.product_id
LEFT JOIN invoice i ON ii.invoice_id = i.id
LEFT JOIN customer c ON i.customer_id = c.id

ORDER BY
    CASE WHEN customer_name = 'N/A' THEN 1 else 0 END,
    customer_id,
    product_id, 
    invoice_item_id) sol
```
