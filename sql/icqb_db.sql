-- MySQL dump 10.13  Distrib 5.1.73, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: icqb_db
-- ------------------------------------------------------
-- Server version	5.1.73

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('dw4lj7qtbkkma2o2gfdpkdoemymesq6h','ZjBkOTg3OGRkMjk2Y2VlMTM0ZDFiYzNjMjQ4MmI1N2ZiMGQzNTM3Yzp7InVzZXJuYW1lcyI6ImFkbWluIiwiTUQ1IjoiNzk5M2IyNzg5MjhiMDRmMTViOGMxN2I1YzMwNDU1YjcifQ==','2016-05-23 16:50:46');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userpro_accountuser`
--

DROP TABLE IF EXISTS `userpro_accountuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userpro_accountuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `userpasswd` varchar(50) NOT NULL,
  `is_lock` tinyint(1) NOT NULL,
  `in_group_id` int(11) NOT NULL,
  `is_superman` int(11) NOT NULL,
  `lastlogin_host` varchar(50) NOT NULL,
  `create_time` datetime NOT NULL,
  `lastlogin_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `userpro_accountuser_bc3757f9` (`in_group_id`),
  CONSTRAINT `in_group_id_refs_id_65e7bead` FOREIGN KEY (`in_group_id`) REFERENCES `userpro_usergroup` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userpro_accountuser`
--

LOCK TABLES `userpro_accountuser` WRITE;
/*!40000 ALTER TABLE `userpro_accountuser` DISABLE KEYS */;
INSERT INTO `userpro_accountuser` VALUES (1,'admin','21232f297a57a5a743894a0e4a801fc3',1,1,1,'127.0.0.1','2015-09-10 16:30:30','2015-09-10 16:30:33');
/*!40000 ALTER TABLE `userpro_accountuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userpro_usergroup`
--

DROP TABLE IF EXISTS `userpro_usergroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userpro_usergroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `permission` varchar(500) NOT NULL,
  `is_doc` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userpro_usergroup`
--

LOCK TABLES `userpro_usergroup` WRITE;
/*!40000 ALTER TABLE `userpro_usergroup` DISABLE KEYS */;
INSERT INTO `userpro_usergroup` VALUES (1,'运维相关','9999,9998,1,101,1003,1004,1005,1006,105,1007,1008,2,102,3,106','运维相关'),(2,'运营相关','0,2,102','运营相关'),(3,'开发组','0,1,2,3,101,102,104,105,106,1001,1002,1003,1004,1005,1006','开发相关');
/*!40000 ALTER TABLE `userpro_usergroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userpro_usersessioncache`
--

DROP TABLE IF EXISTS `userpro_usersessioncache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userpro_usersessioncache` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `session_key` varchar(40) NOT NULL,
  `username` varchar(50) NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `session_key` (`session_key`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userpro_usersessioncache`
--

LOCK TABLES `userpro_usersessioncache` WRITE;
/*!40000 ALTER TABLE `userpro_usersessioncache` DISABLE KEYS */;
INSERT INTO `userpro_usersessioncache` VALUES (78,'dw4lj7qtbkkma2o2gfdpkdoemymesq6h','admin','2016-05-09 16:49:02');
/*!40000 ALTER TABLE `userpro_usersessioncache` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userpro_vieperurl`
--

DROP TABLE IF EXISTS `userpro_vieperurl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userpro_vieperurl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `url` varchar(50) NOT NULL,
  `menu_type` int(11) NOT NULL,
  `in_menu` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10000 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userpro_vieperurl`
--

LOCK TABLES `userpro_vieperurl` WRITE;
/*!40000 ALTER TABLE `userpro_vieperurl` DISABLE KEYS */;
INSERT INTO `userpro_vieperurl` VALUES (1,'系统管理','0',1,0),(2,'资产管理','0',1,0),(3,'运维管理','0',1,0),(101,'用户列表','/ShowUserList/',2,1),(102,'列表管理','/ServerList/',2,2),(105,'角色管理','/ShowGroupList/',2,1),(106,'执行命令','/lll/',2,3),(1003,'删除用户','/DelUser/',3,101),(1004,'增加用户','/AddUser/',3,101),(1005,'修改用户','/EditUser/',3,101),(1006,'获取修改用户json','/EditUserJson/',3,101),(1007,'获取修改组权限json','/EditGroupJson/',3,105),(1008,'提交组权限','/EditGroupPro/',3,105),(9998,'登出操作不能修改','/LoginOut/',0,0),(9999,'首页不能改','/home/',0,0);
/*!40000 ALTER TABLE `userpro_vieperurl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `works_hostgroup`
--

DROP TABLE IF EXISTS `works_hostgroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `works_hostgroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `AnHost` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `works_hostgroup`
--

LOCK TABLES `works_hostgroup` WRITE;
/*!40000 ALTER TABLE `works_hostgroup` DISABLE KEYS */;
INSERT INTO `works_hostgroup` VALUES (1,'测试大区','1'),(2,'正式大区','2');
/*!40000 ALTER TABLE `works_hostgroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `works_serverlist`
--

DROP TABLE IF EXISTS `works_serverlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `works_serverlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `ServerId` varchar(20) NOT NULL,
  `Flag` varchar(2) NOT NULL,
  `Ip` varchar(20) NOT NULL,
  `InGroup_id` int(11) NOT NULL,
  `Type` varchar(20) NOT NULL,
  `Status` int(11) NOT NULL,
  `WorkNow` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `works_serverlist_585726c1` (`InGroup_id`),
  CONSTRAINT `InGroup_id_refs_id_6c104861` FOREIGN KEY (`InGroup_id`) REFERENCES `works_hostgroup` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `works_serverlist`
--

LOCK TABLES `works_serverlist` WRITE;
/*!40000 ALTER TABLE `works_serverlist` DISABLE KEYS */;
INSERT INTO `works_serverlist` VALUES (1,'测试1区','1001','1','127.0.0.1',1,'1',1,'HF:BQu97d22DbaU6WRKimIY'),(2,'测试2区','1002','1','127.0.0.2',1,'1',1,'HF:BQu97d22DbaU6WRKimIY'),(3,'测试3区','1003','1','127.0.0.3',1,'1',1,'HF:BQu97d22DbaU6WRKimIY'),(4,'测试4区','1004','1','127.0.0.4',1,'1',1,'HF:BQu97d22DbaU6WRKimIY'),(5,'测试5区','1005','1','127.0.0.5',1,'1',1,'HF:BQu97d22DbaU6WRKimIY'),(6,'正式1区','101','1','128.0.0.1',2,'1',1,'HF:lKecF4l7mSORmrbRekeJ'),(7,'正式2区','102','1','128.0.0.1',2,'1',1,'HF:lKecF4l7mSORmrbRekeJ');
/*!40000 ALTER TABLE `works_serverlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-10  0:55:02
