SELECT f.title,
  group_concat(a.last_name order by a.last_name 
    separator ', ') actors
FROM actor a
  INNER JOIN film_actor fa
  ON a.actor_id = fa.actor_id
  INNER JOIN film f
  ON fa.film_id = f.film_id
GROUP BY f.title
HAVING count(*) = 3;