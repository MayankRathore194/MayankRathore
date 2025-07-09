
create database dannys_diner;
use dannys_diner;


CREATE TABLE sales (
  customer_id VARCHAR(1),
  order_date DATE,
  product_id INTEGER
);

INSERT INTO sales (customer_id, order_date, product_id) VALUES
  ('A', '2021-01-01', 1),
  ('A', '2021-01-01', 2),
  ('A', '2021-01-07', 2),
  ('A', '2021-01-10', 3),
  ('A', '2021-01-11', 3),
  ('A', '2021-01-11', 3),
  ('B', '2021-01-01', 2),
  ('B', '2021-01-02', 2),
  ('B', '2021-01-04', 1),
  ('B', '2021-01-11', 1),
  ('B', '2021-01-16', 3),
  ('B', '2021-02-01', 3),
  ('C', '2021-01-01', 3),
  ('C', '2021-01-01', 3),
  ('C', '2021-01-07', 3);

CREATE TABLE menu (
  product_id INTEGER,
  product_name VARCHAR(10),
  price INTEGER
);

INSERT INTO menu (product_id, product_name, price) VALUES
  (1, 'sushi', 10),
  (2, 'curry', 15),
  (3, 'ramen', 12);

CREATE TABLE members (
  customer_id VARCHAR(1),
  join_date DATE
);

INSERT INTO members (customer_id, join_date) VALUES
  ('A', '2021-01-07'),
  ('B', '2021-01-09');

select * from members; 

select * from menu;

select * from sales;


--1.
SELECT customer_id,sum(price)
FROM sales
LEFT JOIN menu
ON sales.product_id = menu.product_id
group by customer_id ;

--2.
select DISTINCT  customer_id,count(DISTINCT order_date)
from sales
group by customer_id;

--3
CREATE VIEW customer_A AS
SELECT customer_id,product_id,order_date
FROM sales
where customer_id='A';

CREATE VIEW customer_B AS
SELECT customer_id,product_id,order_date
FROM sales
where customer_id='B';

CREATE VIEW customer_C AS
SELECT customer_id,product_id,order_date
FROM sales
where customer_id='C';

SELECT product_id AS first_item_A
FROM customer_A
WHERE order_date = (
    SELECT MIN(order_date)
    FROM customer_A
);

SELECT product_id AS first_item_B
FROM customer_B
WHERE order_date = (
    SELECT MIN(order_date)
    FROM customer_B
);

SELECT product_id AS first_item_C
FROM customer_C
WHERE order_date = (
    SELECT MIN(order_date)
    FROM customer_C
);

--4
select product_id,y.freq  from (select product_id,count(product_id) as freq from sales group by product_id) as y where y.freq=(select MAX(x.freq) as max_order from (select product_id,count(product_id) as freq from sales group by product_id) as x); 

--5

SELECT product_id AS product_by_C, x.freq AS ordered_by_C
FROM (
    SELECT product_id, COUNT(product_id) AS freq
    FROM customer_C
    GROUP BY product_id
) AS x
WHERE x.freq = (
    SELECT MAX(x.freq) AS most_ordered
    FROM (
        SELECT product_id, COUNT(product_id) AS freq
        FROM customer_C
        GROUP BY product_id
    ) AS x
);



--6
SELECT * 
FROM ( 
    SELECT s.customer_id, s.order_date, s.product_id 
    FROM sales s 
    JOIN members m ON s.customer_id = m.customer_id 
    WHERE s.order_date < m.join_date 
) AS y 
WHERE order_date = ( 
    SELECT min(x.order_date) 
    FROM ( 
        SELECT s.order_date 
        FROM sales s 
        JOIN members m ON s.customer_id = m.customer_id 
        WHERE s.order_date < m.join_date 
    ) AS x 
); 

--7
SELECT * 
FROM ( 
    SELECT s.customer_id, s.order_date, s.product_id 
    FROM sales s 
    JOIN members m ON s.customer_id = m.customer_id 
    WHERE s.order_date < m.join_date 
) AS y 
WHERE order_date = ( 
    SELECT MAX(x.order_date) 
    FROM ( 
        SELECT s.order_date 
        FROM sales s 
        JOIN members m ON s.customer_id = m.customer_id 
WHERE s.order_date < m.join_date 
) AS x 
); 

--8
select x.customer_id,count(x.product_id),sum(price)
from 
(
SELECT s.customer_id, s.order_date, s.product_id
    FROM sales s
    JOIN members m ON s.customer_id = m.customer_id
    WHERE s.order_date < m.join_date
) as x
LEFT JOIN menu
ON x.product_id = menu.product_id
group by customer_id ;


--9
select p.customer_id,sum(p.points)
from 
(SELECT x.customer_id,
CASE 
           WHEN m.product_name = 'sushi' THEN m.price *20
           ELSE m.price * 10
       END AS points
FROM sales x
LEFT JOIN menu m ON x.product_id = m.product_id) as p
group by p.customer_id;


--10
select p.customer_id,sum(p.points)
from 
(SELECT x.customer_id,
CASE 
           WHEN m.product_name = 'sushi' THEN m.price *10
           ELSE m.price * 10
       END AS points
FROM (
    SELECT s.customer_id, s.order_date, s.product_id
    FROM sales s
    JOIN members m ON s.customer_id = m.customer_id
    WHERE s.order_date > m.join_date
      AND s.order_date < DATEADD(DAY, 7, m.join_date)
) AS x
LEFT JOIN menu m ON x.product_id = m.product_id) as p
group by p.customer_id;