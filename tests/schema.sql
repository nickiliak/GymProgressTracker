-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: gym_logger
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `exerciselogs`
--

DROP TABLE IF EXISTS `exerciselogs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exerciselogs` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `exercise_name` varchar(255) NOT NULL,
  `kg` float DEFAULT NULL,
  `reps` int DEFAULT NULL,
  `sets` int DEFAULT NULL,
  `category` varchar(45) DEFAULT NULL,
  `day_number` int DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exerciselogs`
--

LOCK TABLES `exerciselogs` WRITE;
/*!40000 ALTER TABLE `exerciselogs` DISABLE KEYS */;
INSERT INTO `exerciselogs` VALUES (16,'RDL',70,5,3,'Legs',1),(17,'Deadlift',100,5,3,'Legs',1),(18,'Squat',80,5,3,'Chest',1),(19,'Crunch',10,12,3,'Core',1),(20,'Tricep Ext.',15,8,3,'Arms',1),(21,'Overhead Press',40,10,3,'Shoulders',2),(22,'Bicep Curl',15,12,3,'Arms',2),(23,'Forearm',10,10,8,'Arms',2),(24,'Lateral Raise',15,10,3,'Shoulders',2),(25,'Bench Press',0,10,1,'Chest',2),(26,'Pull up',0,8,3,'Back',3),(27,'Leg Raise',0,9,3,'Core',3),(28,'Squat',39,10,3,'Legs',3),(29,'Leg extension',15,10,3,'Legs',3),(30,'Hamstring ext.',39,15,3,'Legs',3);
/*!40000 ALTER TABLE `exerciselogs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weightlogs`
--

DROP TABLE IF EXISTS `weightlogs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `weightlogs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `weight_kg` float NOT NULL,
  `logged_at` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weightlogs`
--

LOCK TABLES `weightlogs` WRITE;
/*!40000 ALTER TABLE `weightlogs` DISABLE KEYS */;
INSERT INTO `weightlogs` VALUES (1,70.2798,'2025-09-01'),(2,70.2798,'2025-09-02'),(3,70.2798,'2025-09-03'),(4,70.6865,'2025-09-04'),(5,70.6865,'2025-09-05'),(6,70.9387,'2025-09-06'),(7,70.9387,'2025-09-07'),(8,70.9387,'2025-09-08'),(9,70.9387,'2025-09-09'),(10,70.9387,'2025-09-10'),(11,71.1952,'2025-09-11'),(12,71.1952,'2025-09-12'),(13,71.1952,'2025-09-13'),(14,71.1952,'2025-09-14'),(15,71.3344,'2025-09-15'),(16,71.3344,'2025-09-16'),(17,71.6649,'2025-09-17'),(18,71.6649,'2025-09-18'),(19,71.7899,'2025-09-19'),(20,72.0579,'2025-09-20'),(21,72.4522,'2025-09-21'),(22,72.9093,'2025-09-22'),(23,72.9093,'2025-09-23'),(24,73.2857,'2025-09-24'),(25,73.2857,'2025-09-25'),(26,73.2857,'2025-09-26'),(27,73.7431,'2025-09-27'),(28,73.7431,'2025-09-28'),(29,73.9652,'2025-09-29'),(31,80,'2025-10-01');
/*!40000 ALTER TABLE `weightlogs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-04 17:04:30
