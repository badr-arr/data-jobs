-------------------------------------------------
-- Demateralization rate for each liberal doctors
-------------------------------------------------
with papered_doctors as (
select sender_name, count(*) as number_papered_com
from lifen.communication
where telecom='paper' and sender_category='liberal'
group by sender_name
),

total_communications as (
select sender_name, count(*) as total_com
from lifen.communication
where sender_category='liberal'
group by sender_name
)

Select sender_name, number_papered_com, total_com, number_papered_com/total_com as rate
from papered_doctors
join total_communications using(sender_name)

--------------------------------------------------------------------------------------------------------------
-- Doctors list that have sent at least 5 communications during the 7 days following their first communication
--------------------------------------------------------------------------------------------------------------
with doctors_min_date as (
select sender_name, min(created_at) as min_date from lifen.communication group by sender_name
),

doctors_min_and_max_date as (
select sender_name, min_date, date_add(min_date, interval 7 day) as max_date from doctors_min_date
)

Select sender_name from lifen.communication
join doctors_min_and_max_date using(sender_name) where created_at > min_date and created_at < max_date
group by sender_name having count(*) > 5