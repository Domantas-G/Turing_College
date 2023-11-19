-- MySQL dump 10.13  Distrib 8.1.0, for macos13 (arm64)
--
-- Host: localhost    Database: weather_db
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cities` (
  `city_id` int NOT NULL AUTO_INCREMENT,
  `city_name` varchar(40) NOT NULL,
  PRIMARY KEY (`city_id`),
  UNIQUE KEY `city_name` (`city_name`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES (17,'Barcelona'),(16,'Belgrade'),(5,'Berlin'),(9,'Bucharest'),(15,'Budapest'),(14,'Hamburg'),(1,'Istanbul'),(19,'Kharkiv'),(7,'Kyiv'),(3,'London'),(6,'Madrid'),(20,'Milan'),(11,'Minsk'),(2,'Moscow'),(18,'Munich'),(10,'Paris'),(8,'Rome'),(4,'Saint Petersburg'),(12,'Vienna'),(21,'Vilnius'),(13,'Warsaw');
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `city_rain_stats`
--

DROP TABLE IF EXISTS `city_rain_stats`;
/*!50001 DROP VIEW IF EXISTS `city_rain_stats`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `city_rain_stats` AS SELECT 
 1 AS `city_name`,
 1 AS `rain_hours_1d`,
 1 AS `rain_hours_7d`,
 1 AS `raininess_rank_7d`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `city_temperature_overview`
--

DROP TABLE IF EXISTS `city_temperature_overview`;
/*!50001 DROP VIEW IF EXISTS `city_temperature_overview`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `city_temperature_overview` AS SELECT 
 1 AS `city_name`,
 1 AS `min_temp_today`,
 1 AS `max_temp_today`,
 1 AS `stddev_temp_today`,
 1 AS `min_temp_yesterday`,
 1 AS `max_temp_yesterday`,
 1 AS `stddev_temp_yesterday`,
 1 AS `min_temp_current_week`,
 1 AS `max_temp_current_week`,
 1 AS `stddev_temp_current_week`,
 1 AS `min_temp_last_7days`,
 1 AS `max_temp_last_7days`,
 1 AS `stddev_temp_last_7days`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `city_temperature_stats_7days`
--

DROP TABLE IF EXISTS `city_temperature_stats_7days`;
/*!50001 DROP VIEW IF EXISTS `city_temperature_stats_7days`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `city_temperature_stats_7days` AS SELECT 
 1 AS `city_name`,
 1 AS `min_temperature`,
 1 AS `max_temperature`,
 1 AS `stddev_temperature`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `city_temperature_stats_current_week`
--

DROP TABLE IF EXISTS `city_temperature_stats_current_week`;
/*!50001 DROP VIEW IF EXISTS `city_temperature_stats_current_week`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `city_temperature_stats_current_week` AS SELECT 
 1 AS `city_name`,
 1 AS `min_temperature`,
 1 AS `max_temperature`,
 1 AS `stddev_temperature`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `city_temperature_stats_today`
--

DROP TABLE IF EXISTS `city_temperature_stats_today`;
/*!50001 DROP VIEW IF EXISTS `city_temperature_stats_today`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `city_temperature_stats_today` AS SELECT 
 1 AS `city_name`,
 1 AS `min_temperature`,
 1 AS `max_temperature`,
 1 AS `stddev_temperature`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `city_temperature_stats_yesterday`
--

DROP TABLE IF EXISTS `city_temperature_stats_yesterday`;
/*!50001 DROP VIEW IF EXISTS `city_temperature_stats_yesterday`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `city_temperature_stats_yesterday` AS SELECT 
 1 AS `city_name`,
 1 AS `min_temperature`,
 1 AS `max_temperature`,
 1 AS `stddev_temperature`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `min_max_temp_daily`
--

DROP TABLE IF EXISTS `min_max_temp_daily`;
/*!50001 DROP VIEW IF EXISTS `min_max_temp_daily`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `min_max_temp_daily` AS SELECT 
 1 AS `t_day`,
 1 AS `city_hottest`,
 1 AS `highest_temp`,
 1 AS `city_coldest`,
 1 AS `lowest_temp`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `min_max_temp_hourly`
--

DROP TABLE IF EXISTS `min_max_temp_hourly`;
/*!50001 DROP VIEW IF EXISTS `min_max_temp_hourly`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `min_max_temp_hourly` AS SELECT 
 1 AS `t_hour`,
 1 AS `city_hottest`,
 1 AS `highest_temp`,
 1 AS `city_coldest`,
 1 AS `lowest_temp`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `min_max_temp_weekly`
--

DROP TABLE IF EXISTS `min_max_temp_weekly`;
/*!50001 DROP VIEW IF EXISTS `min_max_temp_weekly`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `min_max_temp_weekly` AS SELECT 
 1 AS `t_week`,
 1 AS `city_hottest`,
 1 AS `highest_temp`,
 1 AS `city_coldest`,
 1 AS `lowest_temp`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `ranked_temps`
--

DROP TABLE IF EXISTS `ranked_temps`;
/*!50001 DROP VIEW IF EXISTS `ranked_temps`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `ranked_temps` AS SELECT 
 1 AS `city_name`,
 1 AS `temperature`,
 1 AS `t_hour`,
 1 AS `t_day`,
 1 AS `t_week`,
 1 AS `rank_hotness_hour`,
 1 AS `rank_coldness_hour`,
 1 AS `rank_hotness_day`,
 1 AS `rank_coldness_day`,
 1 AS `rank_hotness_week`,
 1 AS `rank_coldness_week`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `weather_data`
--

DROP TABLE IF EXISTS `weather_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `weather_data` (
  `weather_id` int NOT NULL AUTO_INCREMENT,
  `city_name` varchar(40) NOT NULL,
  `temperature` float DEFAULT NULL,
  `unit` varchar(20) DEFAULT 'Celsius',
  `condition` varchar(50) DEFAULT NULL,
  `conditions_description` varchar(255) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`weather_id`),
  KEY `city_name` (`city_name`),
  CONSTRAINT `weather_data_ibfk_1` FOREIGN KEY (`city_name`) REFERENCES `cities` (`city_name`),
  CONSTRAINT `weather_data_chk_1` CHECK ((`unit` in (_utf8mb4'Fahrenheit',_utf8mb4'Celsius',_utf8mb4'Kelvin'))),
  CONSTRAINT `weather_data_chk_2` CHECK ((`temperature` between -(100) and 100))
) ENGINE=InnoDB AUTO_INCREMENT=478 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weather_data`
--

LOCK TABLES `weather_data` WRITE;
/*!40000 ALTER TABLE `weather_data` DISABLE KEYS */;
INSERT INTO `weather_data` VALUES (1,'London',11.67,'Celsius','Clouds','scattered clouds','2023-11-15 22:16:47'),(2,'Berlin',8.73,'Celsius','Clouds','broken clouds','2023-11-15 22:16:47'),(3,'London',11.67,'Celsius','Clouds','scattered clouds','2023-11-15 22:17:09'),(4,'Berlin',8.73,'Celsius','Clouds','broken clouds','2023-11-15 22:17:09'),(5,'London',11.67,'Celsius','Clouds','scattered clouds','2023-11-15 22:18:01'),(6,'Berlin',8.73,'Celsius','Clouds','broken clouds','2023-11-15 22:18:01'),(7,'London',11.58,'Celsius','Clouds','scattered clouds','2023-11-15 22:25:45'),(8,'Berlin',8.83,'Celsius','Clouds','broken clouds','2023-11-15 22:25:45'),(9,'Moscow',1.94,'Celsius','Clouds','overcast clouds','2023-11-15 22:37:35'),(10,'London',11.58,'Celsius','Clouds','scattered clouds','2023-11-15 22:37:35'),(11,'Istanbul',20.64,'Celsius','Clouds','few clouds','2023-11-15 22:37:35'),(12,'Berlin',8.7,'Celsius','Clouds','broken clouds','2023-11-15 22:37:36'),(13,'Kyiv',9.96,'Celsius','Clouds','overcast clouds','2023-11-15 22:37:36'),(14,'Saint Petersburg',1.12,'Celsius','Clouds','overcast clouds','2023-11-15 22:37:36'),(15,'Rome',14.53,'Celsius','Clouds','few clouds','2023-11-15 22:37:36'),(16,'Bucharest',14.98,'Celsius','Clouds','few clouds','2023-11-15 22:37:36'),(17,'Paris',13.22,'Celsius','Clouds','broken clouds','2023-11-15 22:37:36'),(18,'Vienna',12.77,'Celsius','Clear','clear sky','2023-11-15 22:37:37'),(19,'Minsk',1.86,'Celsius','Clouds','overcast clouds','2023-11-15 22:37:38'),(20,'Budapest',13.07,'Celsius','Clouds','broken clouds','2023-11-15 22:37:38'),(21,'Warsaw',6.89,'Celsius','Clouds','broken clouds','2023-11-15 22:37:38'),(22,'Hamburg',8.93,'Celsius','Clouds','broken clouds','2023-11-15 22:37:38'),(23,'Belgrade',12.62,'Celsius','Clouds','broken clouds','2023-11-15 22:37:38'),(24,'Barcelona',18.03,'Celsius','Clouds','broken clouds','2023-11-15 22:37:38'),(25,'Munich',9.34,'Celsius','Rain','moderate rain','2023-11-15 22:37:39'),(26,'Kharkiv',8.44,'Celsius','Clouds','broken clouds','2023-11-15 22:37:39'),(27,'Vilnius',2.09,'Celsius','Clouds','overcast clouds','2023-11-15 22:37:39'),(28,'Milan',17.55,'Celsius','Clear','clear sky','2023-11-15 22:37:39'),(29,'Istanbul',13.45,'Celsius','Clouds','broken clouds','2023-11-16 09:23:53'),(30,'London',5.09,'Celsius','Clouds','overcast clouds','2023-11-16 09:23:53'),(31,'Moscow',0.67,'Celsius','Clouds','overcast clouds','2023-11-16 09:23:53'),(32,'Berlin',7.04,'Celsius','Clear','clear sky','2023-11-16 09:23:53'),(33,'Madrid',10.58,'Celsius','Fog','fog','2023-11-16 09:23:53'),(34,'Saint Petersburg',-0.99,'Celsius','Clouds','overcast clouds','2023-11-16 09:23:54'),(35,'Kyiv',8.79,'Celsius','Rain','light rain','2023-11-16 09:23:54'),(36,'Rome',15.4,'Celsius','Clouds','overcast clouds','2023-11-16 09:23:54'),(37,'Paris',7.9,'Celsius','Clear','clear sky','2023-11-16 09:23:54'),(38,'Minsk',0.86,'Celsius','Clouds','overcast clouds','2023-11-16 09:23:54'),(39,'Bucharest',9.48,'Celsius','Clear','clear sky','2023-11-16 09:23:54'),(40,'Vienna',9.55,'Celsius','Clouds','broken clouds','2023-11-16 09:23:54'),(41,'Warsaw',3.44,'Celsius','Clouds','few clouds','2023-11-16 09:23:54'),(42,'Hamburg',8.93,'Celsius','Clouds','broken clouds','2023-11-16 09:23:54'),(43,'Budapest',9.49,'Celsius','Clouds','few clouds','2023-11-16 09:23:55'),(44,'Belgrade',7.58,'Celsius','Clear','clear sky','2023-11-16 09:23:55'),(45,'Barcelona',15.98,'Celsius','Clouds','few clouds','2023-11-16 09:23:55'),(46,'Munich',5.43,'Celsius','Clouds','scattered clouds','2023-11-16 09:23:55'),(47,'Milan',8.73,'Celsius','Clear','clear sky','2023-11-16 09:23:55'),(48,'Kharkiv',7.37,'Celsius','Clouds','overcast clouds','2023-11-16 09:23:55'),(49,'Vilnius',0.85,'Celsius','Clouds','overcast clouds','2023-11-16 09:23:55'),(50,'London',5.17,'Celsius','Clouds','overcast clouds','2023-11-16 09:56:16'),(51,'London',4.8,'Celsius','Clouds','overcast clouds','2023-11-16 10:09:25'),(52,'Berlin',7.13,'Celsius','Clouds','few clouds','2023-11-16 10:09:25'),(53,'London',4.8,'Celsius','Clouds','overcast clouds','2023-11-16 10:11:30'),(54,'Berlin',7.05,'Celsius','Clouds','broken clouds','2023-11-16 10:11:30'),(55,'Moscow',0.68,'Celsius','Clouds','overcast clouds','2023-11-16 11:08:55'),(56,'London',4.73,'Celsius','Clouds','overcast clouds','2023-11-16 11:08:55'),(57,'Istanbul',12.59,'Celsius','Rain','light intensity shower rain','2023-11-16 11:08:55'),(58,'Madrid',10.37,'Celsius','Fog','fog','2023-11-16 11:08:56'),(59,'Berlin',7.33,'Celsius','Rain','shower rain','2023-11-16 11:08:56'),(60,'Kyiv',8.24,'Celsius','Clouds','overcast clouds','2023-11-16 11:08:56'),(61,'Saint Petersburg',-1.78,'Celsius','Clouds','overcast clouds','2023-11-16 11:08:56'),(62,'Rome',14.1,'Celsius','Clouds','broken clouds','2023-11-16 11:08:56'),(63,'Paris',8.02,'Celsius','Clear','clear sky','2023-11-16 11:08:56'),(64,'Bucharest',8.55,'Celsius','Clear','clear sky','2023-11-16 11:08:56'),(65,'Minsk',0.86,'Celsius','Clouds','overcast clouds','2023-11-16 11:08:57'),(66,'Warsaw',2.28,'Celsius','Clouds','broken clouds','2023-11-16 11:08:57'),(67,'Vienna',8.85,'Celsius','Clouds','scattered clouds','2023-11-16 11:08:57'),(68,'Budapest',8.44,'Celsius','Clouds','scattered clouds','2023-11-16 11:08:57'),(69,'Hamburg',8.62,'Celsius','Clouds','overcast clouds','2023-11-16 11:08:57'),(70,'Belgrade',6.75,'Celsius','Clear','clear sky','2023-11-16 11:08:57'),(71,'Munich',4.86,'Celsius','Clouds','broken clouds','2023-11-16 11:08:57'),(72,'Barcelona',15.46,'Celsius','Clouds','few clouds','2023-11-16 11:08:57'),(73,'Milan',8.79,'Celsius','Clear','clear sky','2023-11-16 11:08:58'),(74,'Kharkiv',7.26,'Celsius','Clouds','overcast clouds','2023-11-16 11:08:58'),(75,'Vilnius',0.85,'Celsius','Snow','light snow','2023-11-16 11:08:58'),(76,'London',5.83,'Celsius','Rain','light rain','2023-11-16 16:13:05'),(77,'Istanbul',14.38,'Celsius','Clouds','broken clouds','2023-11-16 16:13:05'),(78,'Saint Petersburg',-1.88,'Celsius','Clouds','broken clouds','2023-11-16 16:13:05'),(79,'Madrid',10.59,'Celsius','Fog','fog','2023-11-16 16:13:06'),(80,'Berlin',7.81,'Celsius','Clouds','few clouds','2023-11-16 16:13:06'),(81,'Kyiv',6.6,'Celsius','Clouds','overcast clouds','2023-11-16 16:13:06'),(82,'Rome',11.29,'Celsius','Clouds','overcast clouds','2023-11-16 16:13:06'),(83,'Bucharest',10.52,'Celsius','Clear','clear sky','2023-11-16 16:13:06'),(84,'Paris',8.93,'Celsius','Rain','moderate rain','2023-11-16 16:13:06'),(85,'Minsk',-0.14,'Celsius','Clouds','overcast clouds','2023-11-16 16:13:06'),(86,'Vienna',10.87,'Celsius','Clear','clear sky','2023-11-16 16:13:06'),(87,'Warsaw',2.41,'Celsius','Fog','fog','2023-11-16 16:13:07'),(88,'Hamburg',4.91,'Celsius','Clouds','overcast clouds','2023-11-16 16:13:07'),(89,'Budapest',10.83,'Celsius','Clouds','few clouds','2023-11-16 16:13:07'),(90,'Barcelona',17.41,'Celsius','Clear','clear sky','2023-11-16 16:13:07'),(91,'Munich',5.4,'Celsius','Clouds','overcast clouds','2023-11-16 16:13:07'),(92,'Belgrade',10.67,'Celsius','Clear','clear sky','2023-11-16 16:13:07'),(93,'Kharkiv',7.54,'Celsius','Clouds','overcast clouds','2023-11-16 16:13:07'),(94,'Milan',9.79,'Celsius','Clear','clear sky','2023-11-16 16:13:07'),(95,'Vilnius',1.47,'Celsius','Clouds','overcast clouds','2023-11-16 16:13:08'),(96,'London',5.96,'Celsius','Rain','light rain','2023-11-16 16:24:19'),(97,'Berlin',7.8,'Celsius','Rain','light rain','2023-11-16 16:24:19'),(98,'Berlin',7.8,'Celsius','Rain','light rain','2023-11-16 16:30:03'),(99,'London',5.96,'Celsius','Rain','light rain','2023-11-16 16:30:03'),(100,'London',6.21,'Celsius','Rain','light rain','2023-11-16 16:56:38'),(101,'Istanbul',13.59,'Celsius','Clouds','broken clouds','2023-11-16 16:56:38'),(102,'Moscow',0.79,'Celsius','Clouds','overcast clouds','2023-11-16 16:56:38'),(103,'Berlin',7.93,'Celsius','Clouds','overcast clouds','2023-11-16 16:56:38'),(104,'Madrid',10.89,'Celsius','Fog','fog','2023-11-16 16:56:38'),(105,'Saint Petersburg',-1.88,'Celsius','Clouds','broken clouds','2023-11-16 16:56:38'),(106,'Rome',11.5,'Celsius','Clouds','overcast clouds','2023-11-16 16:56:38'),(107,'Bucharest',12.33,'Celsius','Clear','clear sky','2023-11-16 16:56:38'),(108,'Kyiv',6.05,'Celsius','Clouds','overcast clouds','2023-11-16 16:56:38'),(109,'Paris',9.06,'Celsius','Rain','light rain','2023-11-16 16:56:39'),(110,'Minsk',-0.14,'Celsius','Clouds','overcast clouds','2023-11-16 16:56:39'),(111,'Vienna',11.56,'Celsius','Clear','clear sky','2023-11-16 16:56:39'),(112,'Warsaw',3.21,'Celsius','Fog','fog','2023-11-16 16:56:39'),(113,'Hamburg',5.27,'Celsius','Clouds','broken clouds','2023-11-16 16:56:39'),(114,'Budapest',11.35,'Celsius','Clouds','few clouds','2023-11-16 16:56:39'),(115,'Barcelona',18.06,'Celsius','Clear','clear sky','2023-11-16 16:56:39'),(116,'Belgrade',11.36,'Celsius','Clear','clear sky','2023-11-16 16:56:40'),(117,'Munich',6.57,'Celsius','Clouds','overcast clouds','2023-11-16 16:56:40'),(118,'Milan',10.81,'Celsius','Clear','clear sky','2023-11-16 16:56:40'),(119,'Kharkiv',7.85,'Celsius','Clouds','overcast clouds','2023-11-16 16:56:40'),(120,'Vilnius',1.47,'Celsius','Clouds','overcast clouds','2023-11-16 16:56:40'),(121,'London',6.29,'Celsius','Rain','light rain','2023-11-16 17:13:05'),(122,'Istanbul',14.59,'Celsius','Clouds','broken clouds','2023-11-16 17:13:05'),(123,'Moscow',0.83,'Celsius','Clouds','overcast clouds','2023-11-16 17:13:05'),(124,'Saint Petersburg',-1.88,'Celsius','Clouds','broken clouds','2023-11-16 17:13:06'),(125,'Madrid',10.91,'Celsius','Fog','fog','2023-11-16 17:13:06'),(126,'Berlin',8.01,'Celsius','Clouds','broken clouds','2023-11-16 17:13:06'),(127,'Rome',11.47,'Celsius','Clouds','overcast clouds','2023-11-16 17:13:06'),(128,'Bucharest',12.64,'Celsius','Clear','clear sky','2023-11-16 17:13:06'),(129,'Kyiv',6.05,'Celsius','Clouds','overcast clouds','2023-11-16 17:13:06'),(130,'Minsk',-0.14,'Celsius','Clouds','overcast clouds','2023-11-16 17:13:07'),(131,'Vienna',11.82,'Celsius','Clouds','few clouds','2023-11-16 17:13:07'),(132,'Paris',9.06,'Celsius','Rain','light rain','2023-11-16 17:13:07'),(133,'Warsaw',3.27,'Celsius','Fog','fog','2023-11-16 17:13:07'),(134,'Budapest',11.91,'Celsius','Clouds','few clouds','2023-11-16 17:13:07'),(135,'Hamburg',5.09,'Celsius','Clouds','overcast clouds','2023-11-16 17:13:07'),(136,'Barcelona',18.52,'Celsius','Clear','clear sky','2023-11-16 17:13:07'),(137,'Munich',6.77,'Celsius','Clouds','overcast clouds','2023-11-16 17:13:07'),(138,'Belgrade',11.74,'Celsius','Clear','clear sky','2023-11-16 17:13:07'),(139,'Kharkiv',7.85,'Celsius','Rain','light rain','2023-11-16 17:13:08'),(140,'Milan',11.52,'Celsius','Clouds','few clouds','2023-11-16 17:13:08'),(141,'Vilnius',1.47,'Celsius','Clouds','broken clouds','2023-11-16 17:13:08'),(142,'Moscow',0.82,'Celsius','Clouds','overcast clouds','2023-11-16 17:24:07'),(143,'London',6.29,'Celsius','Rain','light rain','2023-11-16 17:24:07'),(144,'Istanbul',14.59,'Celsius','Clouds','broken clouds','2023-11-16 17:24:07'),(145,'Madrid',11,'Celsius','Fog','fog','2023-11-16 17:24:07'),(146,'Saint Petersburg',-1.88,'Celsius','Clouds','broken clouds','2023-11-16 17:24:07'),(147,'Berlin',8.11,'Celsius','Clouds','broken clouds','2023-11-16 17:24:07'),(148,'Rome',11.59,'Celsius','Clouds','overcast clouds','2023-11-16 17:24:08'),(149,'Kyiv',6.05,'Celsius','Clouds','overcast clouds','2023-11-16 17:24:08'),(150,'Bucharest',13.19,'Celsius','Clear','clear sky','2023-11-16 17:24:08'),(151,'Paris',9.08,'Celsius','Rain','light rain','2023-11-16 17:24:08'),(152,'Vienna',11.95,'Celsius','Clouds','few clouds','2023-11-16 17:24:08'),(153,'Minsk',-0.14,'Celsius','Clouds','overcast clouds','2023-11-16 17:24:08'),(154,'Warsaw',3.22,'Celsius','Fog','fog','2023-11-16 17:24:09'),(155,'Budapest',11.91,'Celsius','Clouds','few clouds','2023-11-16 17:24:09'),(156,'Hamburg',5.26,'Celsius','Clouds','overcast clouds','2023-11-16 17:24:09'),(157,'Belgrade',11.76,'Celsius','Clear','clear sky','2023-11-16 17:24:09'),(158,'Munich',7.04,'Celsius','Clouds','overcast clouds','2023-11-16 17:24:09'),(159,'Barcelona',18.88,'Celsius','Clear','clear sky','2023-11-16 17:24:09'),(160,'Kharkiv',7.85,'Celsius','Clouds','overcast clouds','2023-11-16 17:24:10'),(161,'Milan',11.68,'Celsius','Clouds','few clouds','2023-11-16 17:24:10'),(162,'Vilnius',1.95,'Celsius','Clouds','broken clouds','2023-11-16 17:24:10'),(163,'Istanbul',14.59,'Celsius','Clouds','broken clouds','2023-11-16 17:42:08'),(164,'London',6.43,'Celsius','Rain','light rain','2023-11-16 17:42:08'),(165,'Moscow',0.78,'Celsius','Clouds','overcast clouds','2023-11-16 17:42:08'),(166,'Berlin',8.08,'Celsius','Clouds','broken clouds','2023-11-16 17:42:09'),(167,'Madrid',11.1,'Celsius','Fog','fog','2023-11-16 17:42:09'),(168,'Saint Petersburg',-1.88,'Celsius','Clouds','broken clouds','2023-11-16 17:42:09'),(169,'Rome',11.67,'Celsius','Clouds','overcast clouds','2023-11-16 17:42:09'),(170,'Kyiv',5.52,'Celsius','Clouds','overcast clouds','2023-11-16 17:42:09'),(171,'Bucharest',13.79,'Celsius','Clear','clear sky','2023-11-16 17:42:09'),(172,'Minsk',-0.14,'Celsius','Clouds','overcast clouds','2023-11-16 17:42:10'),(173,'Paris',9.03,'Celsius','Mist','mist','2023-11-16 17:42:10'),(174,'Vienna',12.11,'Celsius','Clouds','few clouds','2023-11-16 17:42:10'),(175,'Hamburg',5.32,'Celsius','Clouds','broken clouds','2023-11-16 17:42:10'),(176,'Warsaw',3.64,'Celsius','Fog','fog','2023-11-16 17:42:10'),(177,'Budapest',12.23,'Celsius','Clouds','few clouds','2023-11-16 17:42:10'),(178,'Barcelona',19.4,'Celsius','Clear','clear sky','2023-11-16 17:42:10'),(179,'Munich',7.62,'Celsius','Clouds','overcast clouds','2023-11-16 17:42:10'),(180,'Belgrade',12.28,'Celsius','Clear','clear sky','2023-11-16 17:42:11'),(181,'Kharkiv',8.8,'Celsius','Clouds','overcast clouds','2023-11-16 17:42:11'),(182,'Milan',12.02,'Celsius','Clear','clear sky','2023-11-16 17:42:11'),(183,'Vilnius',1.47,'Celsius','Clouds','broken clouds','2023-11-16 17:42:11'),(184,'London',7.39,'Celsius','Rain','light rain','2023-11-16 19:56:38'),(185,'Istanbul',16.45,'Celsius','Clouds','scattered clouds','2023-11-16 19:56:38'),(186,'Moscow',0.36,'Celsius','Clouds','overcast clouds','2023-11-16 19:56:38'),(187,'Saint Petersburg',-1.85,'Celsius','Clouds','overcast clouds','2023-11-16 19:56:39'),(188,'Berlin',8.89,'Celsius','Clouds','broken clouds','2023-11-16 19:56:39'),(189,'Madrid',11.77,'Celsius','Mist','mist','2023-11-16 19:56:39'),(190,'Rome',11.47,'Celsius','Clouds','overcast clouds','2023-11-16 19:56:39'),(191,'Paris',9.35,'Celsius','Rain','moderate rain','2023-11-16 19:56:40'),(192,'Minsk',0.86,'Celsius','Clouds','overcast clouds','2023-11-16 19:56:40'),(193,'Bucharest',15.33,'Celsius','Clear','clear sky','2023-11-16 19:56:41'),(194,'Kyiv',4.41,'Celsius','Clouds','overcast clouds','2023-11-16 19:56:41'),(195,'Vienna',14.03,'Celsius','Clouds','few clouds','2023-11-16 19:56:41'),(196,'Warsaw',4.45,'Celsius','Fog','fog','2023-11-16 19:56:41'),(197,'Hamburg',5.67,'Celsius','Clouds','overcast clouds','2023-11-16 19:56:41'),(198,'Barcelona',21,'Celsius','Clear','clear sky','2023-11-16 19:56:41'),(199,'Belgrade',14.2,'Celsius','Clear','clear sky','2023-11-16 19:56:41'),(200,'Budapest',13.89,'Celsius','Clouds','scattered clouds','2023-11-16 19:56:41'),(201,'Munich',8.96,'Celsius','Clouds','overcast clouds','2023-11-16 19:56:42'),(202,'Kharkiv',9.23,'Celsius','Clouds','overcast clouds','2023-11-16 19:56:42'),(203,'Milan',13.39,'Celsius','Clouds','scattered clouds','2023-11-16 19:56:42'),(204,'Vilnius',1.95,'Celsius','Clouds','overcast clouds','2023-11-16 19:56:42'),(205,'Istanbul',14.73,'Celsius','Clouds','scattered clouds','2023-11-16 20:24:08'),(206,'London',7.58,'Celsius','Rain','light rain','2023-11-16 20:24:08'),(207,'Moscow',0.66,'Celsius','Clouds','overcast clouds','2023-11-16 20:24:08'),(208,'Madrid',12.1,'Celsius','Mist','mist','2023-11-16 20:24:08'),(209,'Saint Petersburg',-1.12,'Celsius','Clouds','overcast clouds','2023-11-16 20:24:08'),(210,'Berlin',8.76,'Celsius','Clouds','broken clouds','2023-11-16 20:24:08'),(211,'Rome',11.42,'Celsius','Clouds','overcast clouds','2023-11-16 20:24:09'),(212,'Kyiv',4.41,'Celsius','Clouds','overcast clouds','2023-11-16 20:24:09'),(213,'Bucharest',15.34,'Celsius','Clear','clear sky','2023-11-16 20:24:09'),(214,'Paris',9.52,'Celsius','Rain','heavy intensity rain','2023-11-16 20:24:09'),(215,'Minsk',0.86,'Celsius','Clouds','overcast clouds','2023-11-16 20:24:09'),(216,'Vienna',14.35,'Celsius','Clear','clear sky','2023-11-16 20:24:09'),(217,'Warsaw',4.42,'Celsius','Mist','mist','2023-11-16 20:24:09'),(218,'Budapest',13.88,'Celsius','Clouds','scattered clouds','2023-11-16 20:24:10'),(219,'Hamburg',6.05,'Celsius','Clouds','overcast clouds','2023-11-16 20:24:10'),(220,'Belgrade',14.31,'Celsius','Clear','clear sky','2023-11-16 20:24:10'),(221,'Munich',8.74,'Celsius','Clouds','overcast clouds','2023-11-16 20:24:10'),(222,'Kharkiv',9.23,'Celsius','Clouds','overcast clouds','2023-11-16 20:24:11'),(223,'Barcelona',21.42,'Celsius','Clear','clear sky','2023-11-16 20:24:11'),(224,'Milan',13.11,'Celsius','Clouds','scattered clouds','2023-11-16 20:24:11'),(225,'Vilnius',1.95,'Celsius','Clouds','broken clouds','2023-11-16 20:24:12'),(226,'Moscow',0.26,'Celsius','Clouds','overcast clouds','2023-11-16 21:24:09'),(227,'London',7.73,'Celsius','Rain','light rain','2023-11-16 21:24:09'),(228,'Istanbul',15.59,'Celsius','Clouds','scattered clouds','2023-11-16 21:24:09'),(229,'Saint Petersburg',-1.18,'Celsius','Clouds','broken clouds','2023-11-16 21:24:09'),(230,'Berlin',8.68,'Celsius','Clouds','scattered clouds','2023-11-16 21:24:09'),(231,'Madrid',13.13,'Celsius','Mist','mist','2023-11-16 21:24:09'),(232,'Kyiv',4.41,'Celsius','Clouds','overcast clouds','2023-11-16 21:24:10'),(233,'Rome',11.38,'Celsius','Clouds','few clouds','2023-11-16 21:24:10'),(234,'Paris',9.63,'Celsius','Mist','mist','2023-11-16 21:24:10'),(235,'Minsk',0.86,'Celsius','Clouds','overcast clouds','2023-11-16 21:24:11'),(236,'Vienna',13.39,'Celsius','Clear','clear sky','2023-11-16 21:24:12'),(237,'Hamburg',6,'Celsius','Clouds','broken clouds','2023-11-16 21:24:13'),(238,'Warsaw',4.14,'Celsius','Clouds','broken clouds','2023-11-16 21:24:18'),(239,'Belgrade',14.38,'Celsius','Clear','clear sky','2023-11-16 21:24:18'),(240,'Barcelona',21.73,'Celsius','Clear','clear sky','2023-11-16 21:24:19'),(241,'Munich',8.82,'Celsius','Clouds','overcast clouds','2023-11-16 21:24:20'),(242,'Bucharest',16.29,'Celsius','Clear','clear sky','2023-11-16 21:24:20'),(243,'Budapest',13.19,'Celsius','Clouds','scattered clouds','2023-11-16 21:24:20'),(244,'Kharkiv',8.66,'Celsius','Clouds','overcast clouds','2023-11-16 21:24:20'),(245,'Milan',12.73,'Celsius','Clouds','scattered clouds','2023-11-16 21:24:20'),(246,'Vilnius',1.95,'Celsius','Clouds','overcast clouds','2023-11-16 21:24:26'),(247,'London',9.77,'Celsius','Clouds','overcast clouds','2023-11-17 23:31:54'),(248,'Istanbul',15.45,'Celsius','Clouds','broken clouds','2023-11-17 23:31:54'),(249,'Moscow',-3.49,'Celsius','Clouds','few clouds','2023-11-17 23:31:54'),(250,'Berlin',5.5,'Celsius','Clouds','overcast clouds','2023-11-17 23:31:55'),(251,'Madrid',16.88,'Celsius','Clear','clear sky','2023-11-17 23:31:55'),(252,'Saint Petersburg',-4.44,'Celsius','Clouds','broken clouds','2023-11-17 23:31:55'),(253,'Rome',17.48,'Celsius','Clouds','scattered clouds','2023-11-17 23:31:55'),(254,'Kyiv',3.24,'Celsius','Clouds','overcast clouds','2023-11-17 23:31:55'),(255,'Bucharest',9.29,'Celsius','Clear','clear sky','2023-11-17 23:31:55'),(256,'Minsk',-3.14,'Celsius','Clouds','overcast clouds','2023-11-17 23:31:55'),(257,'Paris',11.14,'Celsius','Clouds','few clouds','2023-11-17 23:31:55'),(258,'Vienna',6.2,'Celsius','Clouds','broken clouds','2023-11-17 23:31:56'),(259,'Warsaw',1.81,'Celsius','Rain','light rain','2023-11-17 23:31:56'),(260,'Hamburg',4.74,'Celsius','Clouds','overcast clouds','2023-11-17 23:31:56'),(261,'Budapest',7.52,'Celsius','Rain','light intensity shower rain','2023-11-17 23:31:56'),(262,'Belgrade',9.6,'Celsius','Clouds','broken clouds','2023-11-17 23:31:56'),(263,'Munich',4.35,'Celsius','Clouds','overcast clouds','2023-11-17 23:31:56'),(264,'Barcelona',17.6,'Celsius','Clouds','scattered clouds','2023-11-17 23:31:56'),(265,'Vilnius',0.23,'Celsius','Clouds','overcast clouds','2023-11-17 23:31:57'),(266,'Milan',15.76,'Celsius','Clear','clear sky','2023-11-17 23:31:57'),(267,'Kharkiv',4.8,'Celsius','Clouds','overcast clouds','2023-11-17 23:31:57'),(268,'Moscow',-5.84,'Celsius','Clear','clear sky','2023-11-18 16:13:11'),(269,'Istanbul',11.87,'Celsius','Rain','shower rain','2023-11-18 16:13:11'),(270,'London',11.7,'Celsius','Rain','light rain','2023-11-18 16:13:11'),(271,'Berlin',4.77,'Celsius','Clouds','scattered clouds','2023-11-18 16:13:11'),(272,'Saint Petersburg',-5.28,'Celsius','Clouds','broken clouds','2023-11-18 16:13:11'),(273,'Madrid',9.29,'Celsius','Mist','mist','2023-11-18 16:13:11'),(274,'Kyiv',1.74,'Celsius','Clouds','overcast clouds','2023-11-18 16:13:12'),(275,'Rome',15.7,'Celsius','Clouds','overcast clouds','2023-11-18 16:13:12'),(276,'Bucharest',7.86,'Celsius','Clouds','overcast clouds','2023-11-18 16:13:12'),(277,'Paris',9.08,'Celsius','Mist','mist','2023-11-18 16:13:12'),(278,'Minsk',-2.14,'Celsius','Clouds','overcast clouds','2023-11-18 16:13:13'),(279,'Vienna',4.98,'Celsius','Clouds','broken clouds','2023-11-18 16:13:13'),(280,'Warsaw',0.27,'Celsius','Snow','light snow','2023-11-18 16:13:13'),(281,'Hamburg',3.05,'Celsius','Clouds','broken clouds','2023-11-18 16:13:13'),(282,'Budapest',5.8,'Celsius','Clouds','few clouds','2023-11-18 16:13:13'),(283,'Belgrade',5.03,'Celsius','Clouds','few clouds','2023-11-18 16:13:13'),(284,'Barcelona',14.57,'Celsius','Clouds','scattered clouds','2023-11-18 16:13:14'),(285,'Munich',4.28,'Celsius','Clouds','overcast clouds','2023-11-18 16:13:14'),(286,'Kharkiv',1.43,'Celsius','Clouds','overcast clouds','2023-11-18 16:13:14'),(287,'Milan',7.23,'Celsius','Clear','clear sky','2023-11-18 16:13:14'),(288,'Vilnius',-1.35,'Celsius','Clouds','broken clouds','2023-11-18 16:13:14'),(289,'London',11.7,'Celsius','Clouds','broken clouds','2023-11-18 16:24:08'),(290,'Moscow',-5.57,'Celsius','Clear','clear sky','2023-11-18 16:24:08'),(291,'Istanbul',11.73,'Celsius','Rain','shower rain','2023-11-18 16:24:08'),(292,'Berlin',4.59,'Celsius','Clouds','scattered clouds','2023-11-18 16:24:09'),(293,'Saint Petersburg',-4.94,'Celsius','Clouds','broken clouds','2023-11-18 16:24:09'),(294,'Madrid',9.59,'Celsius','Mist','mist','2023-11-18 16:24:09'),(295,'Kyiv',1.74,'Celsius','Clouds','overcast clouds','2023-11-18 16:24:09'),(296,'Bucharest',7.95,'Celsius','Clouds','overcast clouds','2023-11-18 16:24:09'),(297,'Rome',15.61,'Celsius','Clouds','overcast clouds','2023-11-18 16:24:09'),(298,'Minsk',-2.14,'Celsius','Clouds','overcast clouds','2023-11-18 16:24:09'),(299,'Paris',9.12,'Celsius','Rain','light rain','2023-11-18 16:24:10'),(300,'Vienna',5.14,'Celsius','Clouds','broken clouds','2023-11-18 16:24:10'),(301,'Warsaw',0.22,'Celsius','Snow','light snow','2023-11-18 16:24:10'),(302,'Budapest',5.93,'Celsius','Clouds','few clouds','2023-11-18 16:24:10'),(303,'Hamburg',3.24,'Celsius','Clouds','broken clouds','2023-11-18 16:24:10'),(304,'Belgrade',5.19,'Celsius','Clouds','few clouds','2023-11-18 16:24:11'),(305,'Barcelona',14.5,'Celsius','Clouds','scattered clouds','2023-11-18 16:24:11'),(306,'Munich',4.56,'Celsius','Clouds','overcast clouds','2023-11-18 16:24:11'),(307,'Kharkiv',1.43,'Celsius','Clouds','overcast clouds','2023-11-18 16:24:11'),(308,'Milan',8.06,'Celsius','Clear','clear sky','2023-11-18 16:24:11'),(309,'Vilnius',-1.35,'Celsius','Clouds','broken clouds','2023-11-18 16:24:11'),(310,'London',12.7,'Celsius','Rain','light rain','2023-11-18 17:24:05'),(311,'Istanbul',10.87,'Celsius','Rain','shower rain','2023-11-18 17:24:05'),(312,'Moscow',-4.43,'Celsius','Clear','clear sky','2023-11-18 17:24:05'),(313,'Saint Petersburg',-4.36,'Celsius','Clear','clear sky','2023-11-18 17:24:05'),(314,'Madrid',11.77,'Celsius','Clear','clear sky','2023-11-18 17:24:05'),(315,'Berlin',5.17,'Celsius','Clouds','overcast clouds','2023-11-18 17:24:05'),(316,'Bucharest',8.07,'Celsius','Drizzle','light intensity drizzle','2023-11-18 17:24:06'),(317,'Kyiv',3.17,'Celsius','Clouds','overcast clouds','2023-11-18 17:24:06'),(318,'Rome',15.62,'Celsius','Clouds','overcast clouds','2023-11-18 17:24:06'),(319,'Paris',9.43,'Celsius','Rain','light rain','2023-11-18 17:24:06'),(320,'Minsk',-2.14,'Celsius','Clouds','overcast clouds','2023-11-18 17:24:06'),(321,'Vienna',5.89,'Celsius','Clouds','broken clouds','2023-11-18 17:24:06'),(322,'Warsaw',0.37,'Celsius','Snow','light snow','2023-11-18 17:24:07'),(323,'Budapest',6.92,'Celsius','Clouds','few clouds','2023-11-18 17:24:07'),(324,'Belgrade',6.49,'Celsius','Clouds','few clouds','2023-11-18 17:24:07'),(325,'Barcelona',16.34,'Celsius','Clouds','few clouds','2023-11-18 17:24:07'),(326,'Hamburg',4.26,'Celsius','Clear','clear sky','2023-11-18 17:24:07'),(327,'Munich',5.36,'Celsius','Clouds','overcast clouds','2023-11-18 17:24:08'),(328,'Milan',10.03,'Celsius','Clear','clear sky','2023-11-18 17:24:08'),(329,'Kharkiv',1.76,'Celsius','Clouds','overcast clouds','2023-11-18 17:24:08'),(330,'Vilnius',-0.86,'Celsius','Clouds','broken clouds','2023-11-18 17:24:08'),(331,'Istanbul',10.73,'Celsius','Rain','light intensity shower rain','2023-11-18 18:24:05'),(332,'Moscow',-3.75,'Celsius','Clear','clear sky','2023-11-18 18:24:05'),(333,'London',13.51,'Celsius','Drizzle','drizzle','2023-11-18 18:24:05'),(334,'Saint Petersburg',-4.39,'Celsius','Clear','clear sky','2023-11-18 18:24:05'),(335,'Berlin',5.49,'Celsius','Clouds','overcast clouds','2023-11-18 18:24:05'),(336,'Madrid',13.52,'Celsius','Clear','clear sky','2023-11-18 18:24:06'),(337,'Kyiv',3.17,'Celsius','Clouds','overcast clouds','2023-11-18 18:24:06'),(338,'Rome',15.57,'Celsius','Clouds','overcast clouds','2023-11-18 18:24:06'),(339,'Bucharest',8.07,'Celsius','Mist','mist','2023-11-18 18:24:06'),(340,'Paris',9.64,'Celsius','Rain','light rain','2023-11-18 18:24:06'),(341,'Minsk',-2.14,'Celsius','Clouds','overcast clouds','2023-11-18 18:24:06'),(342,'Vienna',6.06,'Celsius','Clouds','scattered clouds','2023-11-18 18:24:07'),(343,'Warsaw',0.5,'Celsius','Snow','light snow','2023-11-18 18:24:07'),(344,'Budapest',7.05,'Celsius','Clouds','few clouds','2023-11-18 18:24:07'),(345,'Hamburg',5.5,'Celsius','Clear','clear sky','2023-11-18 18:24:07'),(346,'Belgrade',7,'Celsius','Clouds','scattered clouds','2023-11-18 18:24:08'),(347,'Barcelona',17.46,'Celsius','Clouds','few clouds','2023-11-18 18:24:08'),(348,'Munich',6.39,'Celsius','Clouds','overcast clouds','2023-11-18 18:24:08'),(349,'Vilnius',-0.39,'Celsius','Clouds','overcast clouds','2023-11-18 18:24:09'),(350,'Kharkiv',2,'Celsius','Clouds','overcast clouds','2023-11-18 18:24:09'),(351,'Milan',11.47,'Celsius','Clear','clear sky','2023-11-18 18:24:09'),(352,'Moscow',-3.7,'Celsius','Clear','clear sky','2023-11-18 20:24:11'),(353,'Istanbul',8.87,'Celsius','Rain','light intensity shower rain','2023-11-18 20:24:11'),(354,'London',14.54,'Celsius','Clouds','overcast clouds','2023-11-18 20:24:11'),(355,'Berlin',5.79,'Celsius','Clouds','overcast clouds','2023-11-18 20:24:12'),(356,'Saint Petersburg',-4.19,'Celsius','Clear','clear sky','2023-11-18 20:24:12'),(357,'Madrid',16.48,'Celsius','Clear','clear sky','2023-11-18 20:24:12'),(358,'Rome',14.77,'Celsius','Clear','clear sky','2023-11-18 20:24:13'),(359,'Bucharest',7.43,'Celsius','Clouds','broken clouds','2023-11-18 20:24:13'),(360,'Kyiv',2.61,'Celsius','Clouds','overcast clouds','2023-11-18 20:24:13'),(361,'Paris',11.13,'Celsius','Rain','light rain','2023-11-18 20:24:14'),(362,'Minsk',-1.14,'Celsius','Clouds','overcast clouds','2023-11-18 20:24:14'),(363,'Vienna',6.53,'Celsius','Clouds','broken clouds','2023-11-18 20:24:14'),(364,'Warsaw',0.53,'Celsius','Snow','light snow','2023-11-18 20:24:15'),(365,'Hamburg',6.05,'Celsius','Clear','clear sky','2023-11-18 20:24:15'),(366,'Budapest',7.77,'Celsius','Clouds','scattered clouds','2023-11-18 20:24:15'),(367,'Munich',7.23,'Celsius','Clouds','overcast clouds','2023-11-18 20:24:16'),(368,'Belgrade',7.56,'Celsius','Clouds','broken clouds','2023-11-18 20:24:16'),(369,'Barcelona',19.36,'Celsius','Clear','clear sky','2023-11-18 20:24:16'),(370,'Milan',14.59,'Celsius','Clear','clear sky','2023-11-18 20:24:17'),(371,'Vilnius',-0.25,'Celsius','Clouds','overcast clouds','2023-11-18 20:24:17'),(372,'Kharkiv',1.95,'Celsius','Clouds','overcast clouds','2023-11-18 20:24:17'),(373,'Istanbul',1.68,'Celsius','Rain','light intensity shower rain','2023-11-19 12:36:40'),(374,'London',11.66,'Celsius','Clouds','overcast clouds','2023-11-19 12:36:40'),(375,'Moscow',-9.21,'Celsius','Clouds','broken clouds','2023-11-19 12:36:40'),(376,'Berlin',4.43,'Celsius','Drizzle','light intensity drizzle rain','2023-11-19 12:36:41'),(377,'Madrid',9.22,'Celsius','Clear','clear sky','2023-11-19 12:36:41'),(378,'Saint Petersburg',-5.76,'Celsius','Clear','clear sky','2023-11-19 12:36:41'),(379,'Rome',11.23,'Celsius','Clear','clear sky','2023-11-19 12:36:41'),(380,'Kyiv',-1.1,'Celsius','Clouds','scattered clouds','2023-11-19 12:36:41'),(381,'Bucharest',3.71,'Celsius','Clear','clear sky','2023-11-19 12:36:41'),(382,'Paris',13.98,'Celsius','Clouds','broken clouds','2023-11-19 12:36:42'),(383,'Vienna',2.84,'Celsius','Rain','light rain','2023-11-19 12:36:42'),(384,'Minsk',-1.14,'Celsius','Clouds','overcast clouds','2023-11-19 12:36:42'),(385,'Warsaw',-0.28,'Celsius','Clouds','overcast clouds','2023-11-19 12:36:42'),(386,'Budapest',1.11,'Celsius','Clear','clear sky','2023-11-19 12:36:42'),(387,'Hamburg',6.65,'Celsius','Clouds','overcast clouds','2023-11-19 12:36:42'),(388,'Belgrade',0.37,'Celsius','Clear','clear sky','2023-11-19 12:36:42'),(389,'Munich',8.06,'Celsius','Rain','moderate rain','2023-11-19 12:36:43'),(390,'Barcelona',14.72,'Celsius','Clouds','broken clouds','2023-11-19 12:36:43'),(391,'Milan',5.26,'Celsius','Clear','clear sky','2023-11-19 12:36:43'),(392,'Kharkiv',-0.05,'Celsius','Clouds','overcast clouds','2023-11-19 12:36:43'),(393,'Vilnius',-0.72,'Celsius','Clouds','overcast clouds','2023-11-19 12:36:43'),(394,'London',11.6,'Celsius','Clouds','scattered clouds','2023-11-19 13:46:48'),(395,'Moscow',-8.68,'Celsius','Clouds','broken clouds','2023-11-19 13:46:48'),(396,'Istanbul',2.68,'Celsius','Snow','light shower sleet','2023-11-19 13:46:48'),(397,'Saint Petersburg',-5.43,'Celsius','Clear','clear sky','2023-11-19 13:46:49'),(398,'Berlin',4.36,'Celsius','Rain','moderate rain','2023-11-19 13:46:49'),(399,'Madrid',8.4,'Celsius','Fog','fog','2023-11-19 13:46:49'),(400,'Rome',10.07,'Celsius','Clear','clear sky','2023-11-19 13:46:49'),(401,'Kyiv',-1.1,'Celsius','Clouds','scattered clouds','2023-11-19 13:46:49'),(402,'Bucharest',4.09,'Celsius','Clear','clear sky','2023-11-19 13:46:49'),(403,'Paris',13.62,'Celsius','Clouds','broken clouds','2023-11-19 13:46:49'),(404,'Minsk',-1.14,'Celsius','Clouds','overcast clouds','2023-11-19 13:46:49'),(405,'Vienna',3.01,'Celsius','Rain','light rain','2023-11-19 13:46:50'),(406,'Warsaw',-0.18,'Celsius','Clouds','overcast clouds','2023-11-19 13:46:50'),(407,'Budapest',0.76,'Celsius','Clear','clear sky','2023-11-19 13:46:50'),(408,'Belgrade',-0.04,'Celsius','Clear','clear sky','2023-11-19 13:46:50'),(409,'Hamburg',8.32,'Celsius','Clouds','overcast clouds','2023-11-19 13:46:50'),(410,'Barcelona',14.41,'Celsius','Clouds','broken clouds','2023-11-19 13:46:50'),(411,'Munich',9.36,'Celsius','Rain','heavy intensity rain','2023-11-19 13:46:50'),(412,'Kharkiv',0.11,'Celsius','Clouds','overcast clouds','2023-11-19 13:46:51'),(413,'Vilnius',-0.86,'Celsius','Clouds','overcast clouds','2023-11-19 13:46:51'),(414,'Milan',5.14,'Celsius','Clear','clear sky','2023-11-19 13:46:51'),(415,'London',11.65,'Celsius','Clouds','scattered clouds','2023-11-19 13:56:13'),(416,'Moscow',-8.56,'Celsius','Clouds','broken clouds','2023-11-19 13:56:13'),(417,'Istanbul',2.68,'Celsius','Snow','light shower sleet','2023-11-19 13:56:13'),(418,'Saint Petersburg',-5.43,'Celsius','Clear','clear sky','2023-11-19 13:56:13'),(419,'Madrid',8.4,'Celsius','Fog','fog','2023-11-19 13:56:13'),(420,'Berlin',4.36,'Celsius','Rain','moderate rain','2023-11-19 13:56:13'),(421,'Kyiv',-1.1,'Celsius','Clouds','scattered clouds','2023-11-19 13:56:13'),(422,'Rome',10.07,'Celsius','Clear','clear sky','2023-11-19 13:56:13'),(423,'Bucharest',4.09,'Celsius','Clear','clear sky','2023-11-19 13:56:14'),(424,'Paris',13.62,'Celsius','Clouds','broken clouds','2023-11-19 13:56:14'),(425,'Minsk',-1.14,'Celsius','Clouds','overcast clouds','2023-11-19 13:56:14'),(426,'Vienna',3.01,'Celsius','Rain','light rain','2023-11-19 13:56:14'),(427,'Warsaw',-0.18,'Celsius','Clouds','overcast clouds','2023-11-19 13:56:14'),(428,'Hamburg',8.32,'Celsius','Clouds','overcast clouds','2023-11-19 13:56:14'),(429,'Budapest',0.76,'Celsius','Clear','clear sky','2023-11-19 13:56:14'),(430,'Belgrade',-0.04,'Celsius','Clear','clear sky','2023-11-19 13:56:15'),(431,'Barcelona',14.42,'Celsius','Clouds','broken clouds','2023-11-19 13:56:15'),(432,'Munich',9.41,'Celsius','Rain','light rain','2023-11-19 13:56:15'),(433,'Kharkiv',0.11,'Celsius','Clouds','overcast clouds','2023-11-19 13:56:15'),(434,'Milan',5.14,'Celsius','Clear','clear sky','2023-11-19 13:56:15'),(435,'Vilnius',-0.86,'Celsius','Clouds','overcast clouds','2023-11-19 13:56:15'),(436,'London',11.65,'Celsius','Clouds','scattered clouds','2023-11-19 14:00:05'),(437,'Moscow',-8.56,'Celsius','Clouds','broken clouds','2023-11-19 14:00:05'),(438,'Saint Petersburg',-5.43,'Celsius','Clear','clear sky','2023-11-19 14:00:05'),(439,'Madrid',8.38,'Celsius','Fog','fog','2023-11-19 14:00:06'),(440,'Berlin',4.21,'Celsius','Mist','mist','2023-11-19 14:00:06'),(441,'Rome',10,'Celsius','Clear','clear sky','2023-11-19 14:00:08'),(442,'Kyiv',-1.1,'Celsius','Clouds','scattered clouds','2023-11-19 14:00:08'),(443,'Bucharest',4.09,'Celsius','Clear','clear sky','2023-11-19 14:00:08'),(444,'Istanbul',2.68,'Celsius','Snow','light shower sleet','2023-11-19 14:00:08'),(445,'Minsk',-1.14,'Celsius','Clouds','overcast clouds','2023-11-19 14:00:09'),(446,'Warsaw',-0.18,'Celsius','Clouds','overcast clouds','2023-11-19 14:00:09'),(447,'Vienna',2.92,'Celsius','Rain','light rain','2023-11-19 14:00:10'),(448,'Paris',13.48,'Celsius','Clouds','broken clouds','2023-11-19 14:00:11'),(449,'Budapest',0.77,'Celsius','Clear','clear sky','2023-11-19 14:00:11'),(450,'Barcelona',14.42,'Celsius','Clouds','broken clouds','2023-11-19 14:00:11'),(451,'Munich',9.41,'Celsius','Rain','light rain','2023-11-19 14:00:12'),(452,'Hamburg',8.36,'Celsius','Clouds','overcast clouds','2023-11-19 14:00:12'),(453,'Kharkiv',0.06,'Celsius','Clouds','overcast clouds','2023-11-19 14:00:15'),(454,'Belgrade',-0.05,'Celsius','Clear','clear sky','2023-11-19 14:00:16'),(455,'Milan',5.05,'Celsius','Clear','clear sky','2023-11-19 14:00:16'),(456,'Vilnius',-0.86,'Celsius','Clouds','overcast clouds','2023-11-19 14:00:18'),(457,'Moscow',-8.34,'Celsius','Clouds','overcast clouds','2023-11-19 15:00:07'),(458,'London',11.93,'Celsius','Clouds','broken clouds','2023-11-19 15:00:07'),(459,'Istanbul',3.68,'Celsius','Rain','light intensity shower rain','2023-11-19 15:00:07'),(460,'Saint Petersburg',-5.63,'Celsius','Clear','clear sky','2023-11-19 15:00:07'),(461,'Madrid',8.63,'Celsius','Clouds','few clouds','2023-11-19 15:00:07'),(462,'Berlin',4.64,'Celsius','Rain','moderate rain','2023-11-19 15:00:08'),(463,'Rome',8.85,'Celsius','Clear','clear sky','2023-11-19 15:00:08'),(464,'Paris',12.84,'Celsius','Clouds','few clouds','2023-11-19 15:00:09'),(465,'Minsk',-1.14,'Celsius','Clouds','overcast clouds','2023-11-19 15:00:09'),(466,'Vienna',2.92,'Celsius','Rain','moderate rain','2023-11-19 15:00:12'),(467,'Kyiv',-1.12,'Celsius','Clear','clear sky','2023-11-19 15:00:12'),(468,'Hamburg',10.16,'Celsius','Rain','light intensity shower rain','2023-11-19 15:00:13'),(469,'Bucharest',4.93,'Celsius','Clear','clear sky','2023-11-19 15:00:13'),(470,'Warsaw',-0.21,'Celsius','Clouds','overcast clouds','2023-11-19 15:00:19'),(471,'Budapest',1.33,'Celsius','Mist','mist','2023-11-19 15:00:20'),(472,'Belgrade',0.97,'Celsius','Clear','clear sky','2023-11-19 15:00:20'),(473,'Munich',9.79,'Celsius','Clouds','overcast clouds','2023-11-19 15:00:20'),(474,'Kharkiv',0.38,'Celsius','Clouds','overcast clouds','2023-11-19 15:00:20'),(475,'Milan',5.22,'Celsius','Clear','clear sky','2023-11-19 15:00:21'),(476,'Vilnius',-0.86,'Celsius','Clouds','overcast clouds','2023-11-19 15:00:22'),(477,'Barcelona',14.12,'Celsius','Clouds','broken clouds','2023-11-19 15:00:23');
/*!40000 ALTER TABLE `weather_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `city_rain_stats`
--

/*!50001 DROP VIEW IF EXISTS `city_rain_stats`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `city_rain_stats` AS with `rain_1d` as (select `weather_data`.`city_name` AS `city_name`,count(distinct date_format(`weather_data`.`timestamp`,'%Y-%m-%d %H')) AS `rain_hours_1d` from `weather_data` where ((`weather_data`.`condition` = 'Rain') and (cast(`weather_data`.`timestamp` as date) = curdate())) group by `weather_data`.`city_name`), `rain_7d` as (select `weather_data`.`city_name` AS `city_name`,count(distinct date_format(`weather_data`.`timestamp`,'%Y-%m-%d %H')) AS `rain_hours_7d`,rank() OVER (ORDER BY count(distinct date_format(`weather_data`.`timestamp`,'%Y-%m-%d %H')) desc )  AS `raininess_rank_7d` from `weather_data` where ((`weather_data`.`condition` = 'Rain') and (cast(`weather_data`.`timestamp` as date) >= (curdate() - interval 7 day))) group by `weather_data`.`city_name`) select `c`.`city_name` AS `city_name`,coalesce(`ld`.`rain_hours_1d`,0) AS `rain_hours_1d`,coalesce(`lw`.`rain_hours_7d`,0) AS `rain_hours_7d`,`lw`.`raininess_rank_7d` AS `raininess_rank_7d` from ((`cities` `c` left join `rain_1d` `ld` on((`c`.`city_name` = `ld`.`city_name`))) left join `rain_7d` `lw` on((`c`.`city_name` = `lw`.`city_name`))) order by -(`lw`.`raininess_rank_7d`) desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `city_temperature_overview`
--

/*!50001 DROP VIEW IF EXISTS `city_temperature_overview`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `city_temperature_overview` AS select `t`.`city_name` AS `city_name`,`t`.`min_temperature` AS `min_temp_today`,`t`.`max_temperature` AS `max_temp_today`,`t`.`stddev_temperature` AS `stddev_temp_today`,`y`.`min_temperature` AS `min_temp_yesterday`,`y`.`max_temperature` AS `max_temp_yesterday`,`y`.`stddev_temperature` AS `stddev_temp_yesterday`,`cw`.`min_temperature` AS `min_temp_current_week`,`cw`.`max_temperature` AS `max_temp_current_week`,`cw`.`stddev_temperature` AS `stddev_temp_current_week`,`ls`.`min_temperature` AS `min_temp_last_7days`,`ls`.`max_temperature` AS `max_temp_last_7days`,`ls`.`stddev_temperature` AS `stddev_temp_last_7days` from (((`city_temperature_stats_today` `t` left join `city_temperature_stats_yesterday` `y` on((`t`.`city_name` = `y`.`city_name`))) left join `city_temperature_stats_current_week` `cw` on((`t`.`city_name` = `cw`.`city_name`))) left join `city_temperature_stats_7days` `ls` on((`t`.`city_name` = `ls`.`city_name`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `city_temperature_stats_7days`
--

/*!50001 DROP VIEW IF EXISTS `city_temperature_stats_7days`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `city_temperature_stats_7days` AS select `weather_data`.`city_name` AS `city_name`,min(`weather_data`.`temperature`) AS `min_temperature`,max(`weather_data`.`temperature`) AS `max_temperature`,round(std(`weather_data`.`temperature`),2) AS `stddev_temperature` from `weather_data` where (cast(`weather_data`.`timestamp` as date) >= (curdate() - interval 7 day)) group by `weather_data`.`city_name` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `city_temperature_stats_current_week`
--

/*!50001 DROP VIEW IF EXISTS `city_temperature_stats_current_week`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `city_temperature_stats_current_week` AS select `weather_data`.`city_name` AS `city_name`,min(`weather_data`.`temperature`) AS `min_temperature`,max(`weather_data`.`temperature`) AS `max_temperature`,round(std(`weather_data`.`temperature`),2) AS `stddev_temperature` from `weather_data` where (yearweek(`weather_data`.`timestamp`,1) = yearweek(curdate(),1)) group by `weather_data`.`city_name` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `city_temperature_stats_today`
--

/*!50001 DROP VIEW IF EXISTS `city_temperature_stats_today`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `city_temperature_stats_today` AS select `weather_data`.`city_name` AS `city_name`,min(`weather_data`.`temperature`) AS `min_temperature`,max(`weather_data`.`temperature`) AS `max_temperature`,round(std(`weather_data`.`temperature`),2) AS `stddev_temperature` from `weather_data` where (cast(`weather_data`.`timestamp` as date) = curdate()) group by `weather_data`.`city_name` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `city_temperature_stats_yesterday`
--

/*!50001 DROP VIEW IF EXISTS `city_temperature_stats_yesterday`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `city_temperature_stats_yesterday` AS select `weather_data`.`city_name` AS `city_name`,min(`weather_data`.`temperature`) AS `min_temperature`,max(`weather_data`.`temperature`) AS `max_temperature`,round(std(`weather_data`.`temperature`),2) AS `stddev_temperature` from `weather_data` where (cast(`weather_data`.`timestamp` as date) = (curdate() - interval 1 day)) group by `weather_data`.`city_name` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `min_max_temp_daily`
--

/*!50001 DROP VIEW IF EXISTS `min_max_temp_daily`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `min_max_temp_daily` AS select `ranked_temps`.`t_day` AS `t_day`,max((case when (`ranked_temps`.`rank_hotness_day` = 1) then `ranked_temps`.`city_name` end)) AS `city_hottest`,round(max((case when (`ranked_temps`.`rank_hotness_day` = 1) then `ranked_temps`.`temperature` end)),2) AS `highest_temp`,max((case when (`ranked_temps`.`rank_coldness_day` = 1) then `ranked_temps`.`city_name` end)) AS `city_coldest`,round(max((case when (`ranked_temps`.`rank_coldness_day` = 1) then `ranked_temps`.`temperature` end)),2) AS `lowest_temp` from `ranked_temps` group by `ranked_temps`.`t_day` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `min_max_temp_hourly`
--

/*!50001 DROP VIEW IF EXISTS `min_max_temp_hourly`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `min_max_temp_hourly` AS select `ranked_temps`.`t_hour` AS `t_hour`,max((case when (`ranked_temps`.`rank_hotness_hour` = 1) then `ranked_temps`.`city_name` end)) AS `city_hottest`,round(max((case when (`ranked_temps`.`rank_hotness_hour` = 1) then `ranked_temps`.`temperature` end)),2) AS `highest_temp`,max((case when (`ranked_temps`.`rank_coldness_hour` = 1) then `ranked_temps`.`city_name` end)) AS `city_coldest`,round(max((case when (`ranked_temps`.`rank_coldness_hour` = 1) then `ranked_temps`.`temperature` end)),2) AS `lowest_temp` from `ranked_temps` group by `ranked_temps`.`t_hour` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `min_max_temp_weekly`
--

/*!50001 DROP VIEW IF EXISTS `min_max_temp_weekly`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `min_max_temp_weekly` AS select `ranked_temps`.`t_week` AS `t_week`,max((case when (`ranked_temps`.`rank_hotness_week` = 1) then `ranked_temps`.`city_name` end)) AS `city_hottest`,round(max((case when (`ranked_temps`.`rank_hotness_week` = 1) then `ranked_temps`.`temperature` end)),2) AS `highest_temp`,max((case when (`ranked_temps`.`rank_coldness_week` = 1) then `ranked_temps`.`city_name` end)) AS `city_coldest`,round(max((case when (`ranked_temps`.`rank_coldness_week` = 1) then `ranked_temps`.`temperature` end)),2) AS `lowest_temp` from `ranked_temps` group by `ranked_temps`.`t_week` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `ranked_temps`
--

/*!50001 DROP VIEW IF EXISTS `ranked_temps`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `ranked_temps` AS select `weather_data`.`city_name` AS `city_name`,`weather_data`.`temperature` AS `temperature`,date_format(`weather_data`.`timestamp`,'%Y-%m-%d %H') AS `t_hour`,cast(`weather_data`.`timestamp` as date) AS `t_day`,yearweek(`weather_data`.`timestamp`,1) AS `t_week`,rank() OVER (PARTITION BY date_format(`weather_data`.`timestamp`,'%Y-%m-%d %H') ORDER BY `weather_data`.`temperature` desc )  AS `rank_hotness_hour`,rank() OVER (PARTITION BY date_format(`weather_data`.`timestamp`,'%Y-%m-%d %H') ORDER BY `weather_data`.`temperature` )  AS `rank_coldness_hour`,rank() OVER (PARTITION BY cast(`weather_data`.`timestamp` as date) ORDER BY `weather_data`.`temperature` desc )  AS `rank_hotness_day`,rank() OVER (PARTITION BY cast(`weather_data`.`timestamp` as date) ORDER BY `weather_data`.`temperature` )  AS `rank_coldness_day`,rank() OVER (PARTITION BY yearweek(`weather_data`.`timestamp`,1) ORDER BY `weather_data`.`temperature` desc )  AS `rank_hotness_week`,rank() OVER (PARTITION BY yearweek(`weather_data`.`timestamp`,1) ORDER BY `weather_data`.`temperature` )  AS `rank_coldness_week` from `weather_data` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-19 15:26:42
