-- how many unique user
select count(distinct user_id) from users;

-- how many cookie id for each user on avg
select count(cookie_id),user_id from clique_bait.users group by user_id;

-- what is unique number of visits by all users per month
select date_format(e.event_time,'%y-%m') as month ,count(distinct visit_id) as unique_visit
from events as e
group by date_format(e.event_time,'%y-%m') ;

-- what is the number of events for each event type
select count(*),event_type from events group by event_type;

-- what is the number of events for each event time
select count(event_type),event_time from events group by event_time;

-- what is the percentage of visits which have a purchase event

SELECT
sum(CASE WHEN event_type = 3 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) 
FROM events;


-- what is the percentage of visits which view the checkout page but do not have a purchase event 

select sum(case when page_name="Checkout" and event_type!=3 then 1 else 0 end )*100/count(*)
from events as e
join  page_hierarchy as ph
on e.page_id=ph.page_id ;  


-- what are the top 3 pages by number of views


select page_name,sum(case when event_type=1 then 1 else 0 end ) as x
from events as e
join  page_hierarchy as ph
on e.page_id=ph.page_id 
group by page_name
order by x desc
limit 3;

SELECT 
  ph.page_name,
  COUNT(*) AS views
FROM events as e
JOIN page_hierarchy as ph
  ON e.page_id = ph.page_id
WHERE e.event_type = 1
GROUP BY ph.page_name
ORDER BY views DESC
LIMIT 3;



-- what is number of views and cart adds for each product category 


select product_category,
 sum(case when event_type=1 then 1 else 0 end )as page_views,
sum(case when event_type=2 then 1 else 0 end ) as add_cart
from events as e
join  page_hierarchy as ph
on e.page_id=ph.page_id 
group by product_category;


-- what are the top 3 products by purchases?

select page_name as product_name, product_id,
 sum(case when event_type=3 then 1 else 0 end )as purchase
from events as e
join  page_hierarchy as ph
on e.page_id=ph.page_id 
group by product_name,product_id
order by purchase desc 
limit 3;

