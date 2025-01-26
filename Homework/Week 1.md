Question 3:

```
SELECT 
    COUNT(CASE WHEN trip_distance <= 1 THEN 1 END) as "up_to_1_mile",
    COUNT(CASE WHEN trip_distance > 1 AND trip_distance <= 3 THEN 1 END) as "1_to_3_miles",
    COUNT(CASE WHEN trip_distance > 3 AND trip_distance <= 7 THEN 1 END) as "3_to_7_miles",
    COUNT(CASE WHEN trip_distance > 7 AND trip_distance <= 10 THEN 1 END) as "7_to_10_miles",
    COUNT(CASE WHEN trip_distance > 10 THEN 1 END) as "over_10_miles"
FROM green_taxi_silver
WHERE lpep_pickup_datetime >= '2019-10-01' 
AND lpep_pickup_datetime < '2019-11-01';
```
Question 4:

```
SELECT 
   DATE(lpep_pickup_datetime) as pickup_date,
   MAX(trip_distance) as max_distance
FROM green_taxi_silver
GROUP BY DATE(lpep_pickup_datetime)
ORDER BY max_distance DESC
LIMIT 1;
```

Question 5:
```
SELECT 
   DATE(lpep_pickup_datetime) as pickup_date,
   trip_distance
FROM green_taxi_silver
ORDER BY trip_distance DESC
LIMIT 1;
```

Question 6:
```
SELECT 
    tz."Zone" as dropoff_zone,
    MAX(g."tip_amount") as highest_tip
FROM green_taxi_silver g
LEFT JOIN taxi_zones tz 
ON g."DOLocationID" = tz."LocationID"
WHERE 
    DATE_TRUNC('month', g."lpep_pickup_datetime") = '2019-10-01'
    AND g."Zone" = 'East Harlem North'
GROUP BY tz."Zone"
ORDER BY highest_tip DESC
LIMIT 1;
```

