-- Temperature statistics by city

-- Today's stats
CREATE OR REPLACE VIEW city_temperature_stats_today AS
SELECT
    city_name,
    MIN(temperature) AS min_temperature,
    MAX(temperature) AS max_temperature,
    ROUND(STDDEV(temperature), 2) AS stddev_temperature
FROM weather_data
WHERE DATE(timestamp) = CURDATE()
GROUP BY city_name;

-- Yesterday's stats
CREATE OR REPLACE VIEW city_temperature_stats_yesterday AS
SELECT
    city_name,
    MIN(temperature) AS min_temperature,
    MAX(temperature) AS max_temperature,
    ROUND(STDDEV(temperature), 2) AS stddev_temperature
FROM weather_data
WHERE DATE(timestamp) = CURDATE() - INTERVAL 1 DAY
GROUP BY city_name;

-- Current week stats
CREATE OR REPLACE VIEW city_temperature_stats_current_week AS
SELECT
    city_name,
    MIN(temperature) AS min_temperature,
    MAX(temperature) AS max_temperature,
    ROUND(STDDEV(temperature), 2) AS stddev_temperature
FROM weather_data
WHERE YEARWEEK(timestamp, 1) = YEARWEEK(CURDATE(), 1)
GROUP BY city_name;

-- The most recent 7 days
CREATE OR REPLACE VIEW city_temperature_stats_7days AS
SELECT
    city_name,
    MIN(temperature) AS min_temperature,
    MAX(temperature) AS max_temperature,
    ROUND(STDDEV(temperature), 2) AS stddev_temperature
FROM weather_data
WHERE DATE(timestamp) >= CURDATE() - INTERVAL 7 DAY
GROUP BY city_name;

-- Overview of temperature over the 7days, aggregating all views into one, to provide a comprehensive overview.
CREATE OR REPLACE VIEW city_temperature_overview AS
SELECT 
    t.city_name,
    t.min_temperature AS min_temp_today,
    t.max_temperature AS max_temp_today,
    t.stddev_temperature AS stddev_temp_today,
    y.min_temperature AS min_temp_yesterday,
    y.max_temperature AS max_temp_yesterday,
    y.stddev_temperature AS stddev_temp_yesterday,
    cw.min_temperature AS min_temp_current_week,
    cw.max_temperature AS max_temp_current_week,
    cw.stddev_temperature AS stddev_temp_current_week,
    ls.min_temperature AS min_temp_last_7days,
    ls.max_temperature AS max_temp_last_7days,
    ls.stddev_temperature AS stddev_temp_last_7days
FROM city_temperature_stats_today t
LEFT JOIN city_temperature_stats_yesterday y ON t.city_name = y.city_name
LEFT JOIN city_temperature_stats_current_week cw ON t.city_name = cw.city_name
LEFT JOIN city_temperature_stats_7days ls ON t.city_name = ls.city_name;