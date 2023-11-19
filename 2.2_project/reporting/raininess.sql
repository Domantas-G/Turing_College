-- Raininess statistics.
-- Counting distinct timestamps in case the data upload script runs 2 times in same hours.
CREATE OR REPLACE VIEW city_rain_stats AS
WITH 
rain_1d AS (
    SELECT
        city_name,
        COUNT(DISTINCT DATE_FORMAT(timestamp, '%Y-%m-%d %H')) AS rain_hours_1d
    FROM weather_data
    WHERE `condition` = 'Rain'
      AND DATE(timestamp) = CURDATE()
    GROUP BY city_name
),
rain_7d AS (
    SELECT
        city_name,
        COUNT(DISTINCT DATE_FORMAT(timestamp, '%Y-%m-%d %H')) AS rain_hours_7d,
        RANK() OVER (ORDER BY COUNT(DISTINCT DATE_FORMAT(timestamp, '%Y-%m-%d %H')) DESC) AS raininess_rank_7d
    FROM weather_data
    WHERE `condition` = 'Rain'
      AND DATE(timestamp) >= CURDATE() - INTERVAL 7 DAY
    GROUP BY city_name
)
SELECT 
    c.city_name,
    COALESCE(ld.rain_hours_1d, 0) AS rain_hours_1d,
    COALESCE(lw.rain_hours_7d, 0) AS rain_hours_7d,
    lw.raininess_rank_7d
FROM cities c
LEFT JOIN rain_1d ld ON c.city_name = ld.city_name
LEFT JOIN rain_7d lw ON c.city_name = lw.city_name
-- Functions like `raininess_rank_7d ASC NULLS LAST`, 
-- essentially the inverse of raininess_rank_7d DESC placing the NULL values last but otherwise the same as raininess_rank_7d ASC    
ORDER BY -raininess_rank_7d DESC;