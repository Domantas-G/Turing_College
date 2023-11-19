-- Extreme temperature identification by hour/day/week.
-- Use ranking for temperature extraction by creating a central view for the ranked temperatures.
-- Other views are based on the central view. Centralized view for ranking temperatures simplifies maintenance and saves computation requirements
CREATE OR REPLACE VIEW ranked_temps AS
SELECT
    city_name,
    temperature,
    DATE_FORMAT(timestamp, '%Y-%m-%d %H') AS t_hour,
    DATE(timestamp) AS t_day,
    YEARWEEK(timestamp, 1) AS t_week,
    RANK() OVER (PARTITION BY DATE_FORMAT(timestamp, '%Y-%m-%d %H') ORDER BY temperature DESC) AS rank_hotness_hour,
    RANK() OVER (PARTITION BY DATE_FORMAT(timestamp, '%Y-%m-%d %H') ORDER BY temperature) AS rank_coldness_hour,
    RANK() OVER (PARTITION BY DATE(timestamp) ORDER BY temperature DESC) AS rank_hotness_day,
    RANK() OVER (PARTITION BY DATE(timestamp) ORDER BY temperature) AS rank_coldness_day,
    RANK() OVER (PARTITION BY YEARWEEK(timestamp, 1) ORDER BY temperature DESC) AS rank_hotness_week,
    RANK() OVER (PARTITION BY YEARWEEK(timestamp, 1) ORDER BY temperature) AS rank_coldness_week
FROM weather_data;

CREATE OR REPLACE VIEW min_max_temp_hourly AS
SELECT
    t_hour,
    MAX(CASE WHEN rank_hotness_hour = 1 THEN city_name END) AS city_hottest,
    ROUND(MAX(CASE WHEN rank_hotness_hour = 1 THEN temperature END), 2) AS highest_temp,
    MAX(CASE WHEN rank_coldness_hour = 1 THEN city_name END) AS city_coldest,
    ROUND(MAX(CASE WHEN rank_coldness_hour = 1 THEN temperature END), 2) AS lowest_temp
FROM ranked_temps
GROUP BY t_hour;

CREATE OR REPLACE VIEW min_max_temp_daily AS
SELECT
    t_day,
    MAX(CASE WHEN rank_hotness_day = 1 THEN city_name END) AS city_hottest,
    ROUND(MAX(CASE WHEN rank_hotness_day = 1 THEN temperature END), 2) AS highest_temp,
    MAX(CASE WHEN rank_coldness_day = 1 THEN city_name END) AS city_coldest,
    ROUND(MAX(CASE WHEN rank_coldness_day = 1 THEN temperature END), 2) AS lowest_temp
FROM ranked_temps
GROUP BY t_day;

CREATE OR REPLACE VIEW min_max_temp_weekly AS
SELECT
    t_week,
    MAX(CASE WHEN rank_hotness_week = 1 THEN city_name END) AS city_hottest,
    ROUND(MAX(CASE WHEN rank_hotness_week = 1 THEN temperature END), 2) AS highest_temp,
    MAX(CASE WHEN rank_coldness_week = 1 THEN city_name END) AS city_coldest,
    ROUND(MAX(CASE WHEN rank_coldness_week = 1 THEN temperature END), 2) AS lowest_temp
FROM ranked_temps
GROUP BY t_week;