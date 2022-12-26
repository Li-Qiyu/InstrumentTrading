/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 5.7.35-log : Database - seproject2
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`seproject2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;

USE `seproject2`;

/*Table structure for table `address` */

DROP TABLE IF EXISTS `address`;

CREATE TABLE `address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `addressName` varchar(100) DEFAULT NULL,
  `userPhone` varchar(100) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `town` varchar(50) DEFAULT NULL,
  `detailedAddress` varchar(200) DEFAULT NULL,
  `postCode` varchar(50) DEFAULT NULL,
  `note` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `address` */

insert  into `address`(`id`,`username`,`addressName`,`userPhone`,`country`,`town`,`detailedAddress`,`postCode`,`note`) values (1,'19206168','home','11111111111','Nipo','fjwphbj20','8h90awbhotpiwjh3wj0-mtb 5v0wjm-e0  btwoijemohl hb wa.','111111',NULL);

/*Table structure for table `blog` */

DROP TABLE IF EXISTS `blog`;

CREATE TABLE `blog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `username` varchar(20) COLLATE utf8mb4_bin NOT NULL,
  `titleImage` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `content` varchar(4000) COLLATE utf8mb4_bin DEFAULT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `tag1` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `tag2` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `tag3` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

/*Data for the table `blog` */

insert  into `blog`(`id`,`title`,`username`,`titleImage`,`content`,`date`,`tag1`,`tag2`,`tag3`) values (1,'blog1','qwerty','/static/images/blog-image/4.webp','This is blog1. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod temporahpovbhqpojtj0j 25vh30n95jhj b3j b7iu 3jywvowj6by2i3j b3jjbj-[kopkrjbkpokjrnbe n7p[k[ekspkoytbe.','2022-05-09 21:31:33','t1','t2','t3'),(2,'blog2','qwerty123','/static/images/blog-image/2.webp','This is blog2.','2022-05-09 21:29:59','t1','t2','t3'),(3,'blog3','123','/static/images/blog-image/1.webp','This is blog3.','2022-05-09 21:30:04','t1','t2','t3'),(4,'blog4','123321','/static/images/blog-image/5.webp','This is blog4.','2022-05-09 21:30:10','t1','t2','t3'),(5,'blog5','asdfgh','/static/images/blog-image/3.webp','This is blog5.','2022-05-09 21:31:20','t1','t2','t3'),(6,'blog6','123321','/static/images/blog-image/3.webp','This is blog6.','2022-05-09 21:31:21','t1','t2','t3'),(7,'blog7','123','/static/images/blog-image/4.webp','This is blog7.','2022-05-09 21:31:21','t1','t2','t3'),(8,'blog8','qwerty','/static/images/blog-image/2.webp','This is blog8.','2022-05-09 21:31:22','t1','t2','t3'),(9,'blog9','123321','/static/images/blog-image/1.webp','This is blog9.','2022-05-09 21:31:22','t1','t2','t3'),(10,'blog10','qwerty','/static/images/blog-image/5.webp','This is blog10.','2022-05-09 21:31:23','t1','t2','t3'),(11,'blog11','qwerty123','/static/images/blog-image/4.webp','This is blog11.','2022-05-09 21:31:24','t1','t2','t3'),(12,'blog12','qwerty123','/static/images/blog-image/2.webp','This is blog12.','2022-05-09 21:31:25','t1','t2','t3');

/*Table structure for table `blog_reviews` */

DROP TABLE IF EXISTS `blog_reviews`;

CREATE TABLE `blog_reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bid` int(11) DEFAULT NULL,
  `username` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `review` varchar(1000) COLLATE utf8mb4_bin DEFAULT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

/*Data for the table `blog_reviews` */

insert  into `blog_reviews`(`id`,`bid`,`username`,`review`,`date`) values (1,1,'19206168','b0h98en,bww8-jn9sj wn-j9ijwssnjem3jj4e.','2022-05-09 21:49:54'),(2,1,'19206168','qg0h62 m3bu 9bwme0 neb6py,kofdhgxl. ','2022-05-30 23:05:49'),(3,1,'19206168','fqej90wmtki7mnr mk6nt,0tm7. ','2022-05-30 23:07:17');

/*Table structure for table `cart` */

DROP TABLE IF EXISTS `cart`;

CREATE TABLE `cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` varchar(1500) COLLATE utf8mb4_bin DEFAULT NULL,
  `username` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `productName` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `productName2` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `price` double DEFAULT NULL,
  `images` varchar(50) COLLATE utf8mb4_bin DEFAULT 'xxx.png',
  `productDescription` varchar(2000) COLLATE utf8mb4_bin DEFAULT NULL,
  `productNum` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

/*Data for the table `cart` */

insert  into `cart`(`id`,`pid`,`username`,`productName`,`productName2`,`price`,`images`,`productDescription`,`productNum`) values (1,'1','123321','qwerty','商品1',10,'/static/images/product-image/1.webp','123456',1),(2,'2','123321','asdfgh','商品2',30,'/static/images/product-image/2.webp','098765',1),(3,'1','123321','qwerty','商品1',10,'/static/images/product-image/1.webp','123456',1),(4,'2','123321','asdfgh','商品2',30,'/static/images/product-image/2.webp','098765',1),(6,'1','123321','qwerty','商品1',33,'/static/images/product-image/1.webp','123456',1),(11,'1','123321','qwerty','商品1',33,'/static/images/product-image/1.webp','123456',1),(12,'1','123321','qwerty','商品1',33,'/static/images/product-image/1.webp','123456',1),(13,'1','123321','qwerty','商品1',33,'/static/images/product-image/1.webp','123456',1),(14,'19','123321','ABC432','商品18',349,'/static/images/product-image/5.webp','nwmwh 123456 qwerty',1),(15,'1','123321','qwerty','商品1',33,'/static/images/product-image/1.webp','123456',1),(19,'1','19206168','qwerty','商品1',33,'/static/images/product-image/1.webp','123456\r\n            ',1),(20,'15','19206168','jpoqbnmpkoq','商品15',826,'/static/images/product-image/6.webp','mvqbojkq jpoqjbmq jpijwbhjw 21409',1);

/*Table structure for table `order` */

DROP TABLE IF EXISTS `order`;

CREATE TABLE `order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` varchar(1500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `username` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `productName` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `productName2` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `dispatched` tinyint(1) DEFAULT NULL,
  `received` tinyint(1) DEFAULT NULL,
  `createTime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `order` */

insert  into `order`(`id`,`pid`,`username`,`productName`,`productName2`,`price`,`dispatched`,`received`,`createTime`) values (1,'1','123321','qwerty','商品1','33',1,1,'2022-05-11 22:10:29'),(2,'2','123321','asdfgh','商品2','30',1,0,'2022-05-11 22:11:01'),(3,'2','123','asdfgh','商品2','30',0,0,'2022-05-11 22:12:05'),(4,'1','19206168','qwerty','商品1','33',0,0,'2022-05-12 15:03:24'),(5,'2','100000','asdfgh','商品2','30',1,0,'2022-05-12 15:04:28'),(6,'2','19206168','asdfgh','商品2','30',0,0,'2022-05-30 17:54:29'),(7,'23','19206168','hg8-92twbpj','商品21','72',0,0,'2022-05-30 17:54:29'),(8,'22','19206168','qh9-wbjop','商品20','267',0,0,'2022-05-30 17:54:29'),(9,'2','19206168','asdfgh','商品2','30',0,0,'2022-05-30 17:55:34'),(10,'23','19206168','hg8-92twbpj','商品21','72',0,0,'2022-05-30 17:55:34'),(11,'22','19206168','qh9-wbjop','商品20','267',0,0,'2022-05-30 17:55:34'),(12,'2','19206168','asdfgh','商品2','30',0,0,'2022-05-30 17:59:33'),(13,'23','19206168','hg8-92twbpj','商品21','72',0,0,'2022-05-30 17:59:33'),(14,'22','19206168','qh9-wbjop','商品20','267',0,0,'2022-05-30 17:59:33'),(15,'2','19206168','asdfgh','商品2','30',0,0,'2022-05-30 18:02:56'),(16,'23','19206168','hg8-92twbpj','商品21','72',0,0,'2022-05-30 18:02:56'),(17,'22','19206168','qh9-wbjop','商品20','267',0,0,'2022-05-30 18:02:56');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `productName` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `productName2` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `images` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` varchar(2000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description2` varchar(2000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `score` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category2` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `createTime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `product` */

insert  into `product`(`id`,`productName`,`productName2`,`price`,`images`,`description`,`description2`,`score`,`category`,`category2`,`createTime`) values (1,'qwerty','商品1','33','/static/images/product-image/1.webp','123456\r\n            ','这是商品1。\r\n            ',NULL,'C1','种类1','2022-05-13 11:19:54'),(2,'asdfgh','商品2','30','/static/images/product-image/2.webp','098765','这是商品2。','4','C2','种类2','2022-05-12 20:20:31'),(3,'qazwsx','商品3','43','/static/images/product-image/3.webp','qwedsa','这是商品3。','0','C3','种类3','2022-05-11 11:29:16'),(4,'123456','商品4','24','/static/images/product-image/4.webp','123456','这是商品4。','0','C4','种类4','2022-05-11 11:29:19'),(5,'ijqof0','商品5','73','/static/images/product-image/5.webp','123456','这是商品5。','3','C5','种类5','2022-05-11 11:29:21'),(6,'fqih0q','商品6','234','/static/images/product-image/6.webp','109gjnlq','这是商品6。','4','C3','种类3','2022-05-11 11:29:24'),(7,'fi0qnlm','商品7','15','/static/images/product-image/7.webp','rq0hjhk','这是商品7。','2','C2','种类2','2022-05-11 11:29:26'),(8,'ABC','商品8','88','/static/images/product-image/3.webp','fqtehbwn','这是商品8。','3','C4','种类4','2022-05-11 11:29:29'),(9,'qwer','商品9','33','/static/images/product-image/1.webp','123456','这是商品9。','5','C1','种类1','2022-05-11 11:28:52'),(10,'qwe123','商品10','33','/static/images/product-image/1.webp','123456','这是商品10。','5','C1','种类1','2022-05-11 11:28:52'),(11,'qwerty654','商品11','33','/static/images/product-image/1.webp','123456','这是商品11。','5','C1','种类1','2022-05-11 11:28:52'),(12,'asd234','商品12','82','/static/images/product-image/5.webp','mrnoqbinpq','这是商品12。','2','C6','种类6','2022-05-11 11:29:36'),(13,'asdvfrgfd','商品13','26','/static/images/product-image/3.webp','vnjfrikmtg','这是商品13。','1','C6','种类6','2022-05-11 11:29:39'),(14,'vqnqnye5m','商品14','985','/static/images/product-image/7.webp','wnymkwnmyr5j3q4h45ujwh 2y4h5qnnnq','这是商品14。','4','C2','种类2','2022-05-11 11:29:41'),(15,'jpoqbnmpkoq','商品15','826','/static/images/product-image/6.webp','mvqbojkq jpoqjbmq jpijwbhjw 21409','这是商品15。','3','C4','种类4','2022-05-11 11:29:43'),(16,'qnpqbompqbqbq','商品16','73','/static/images/product-image/4.webp','nqnt hq4jj6 2ujw 62771y hh','这是商品16。','2','C5','种类5','2022-05-11 11:29:46'),(17,'wntb4qh','商品17','82','/static/images/product-image/2.webp','nqpb qpoqhj qqbqq 10g gqgqbqn','这是商品17。','4','C2','种类2','2022-05-11 11:29:48'),(18,'ABC432','商品18','349','/static/images/product-image/5.webp','nwmwh 123456 qwerty','这是商品18。','1','C1','种类1','2022-05-11 11:28:57'),(19,'ionqab','商品19','73','/static/images/product-image/7.webp','\r\n            h-qin 2h0j-39 n 2h0njbknye yennkw.','这是商品19。','3','C4','种类4','2022-05-11 11:29:53'),(22,'qh9-wbjop','商品20','267','/static/images/product-image/5.webp','tbuw90;j, iwjpoiejo, twbiojpmoqv. ','这是商品20.',NULL,'C3','种类3','2022-05-13 11:50:10'),(23,'hg8-92twbpj','商品21','72','/static/images/product-image/3.webp','82u940bwjipjohe, vgtewgviotgvevt. ','这是商品21。',NULL,'C5','种类5','2022-05-13 11:50:07');

/*Table structure for table `product_reviews` */

DROP TABLE IF EXISTS `product_reviews`;

CREATE TABLE `product_reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` varchar(1500) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `review` varchar(1000) DEFAULT NULL,
  `score` int(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `product_reviews` */

insert  into `product_reviews`(`id`,`pid`,`username`,`review`,`score`) values (1,'1','123321','vq2r0n4bq2uupi',3),(2,'4','edcvfr','qhbp42-29pbj1j b2j b2bvbbmymn',4),(3,'4','123321','nbp9h82njk 2hnjn2k n 3ik76.',5),(5,'1','19206168','arngiw tv4m0-24j qw 5vtqw p. ',NULL),(6,'1','19206168','w erj8-m9t 4neb0kvi-jd9m nr6. asjo-nwvs . ',NULL);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(30) COLLATE utf8mb4_bin NOT NULL,
  `username` varchar(20) COLLATE utf8mb4_bin NOT NULL,
  `password` varchar(32) COLLATE utf8mb4_bin NOT NULL,
  `login_salt` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL,
  `email` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `admin` varchar(50) COLLATE utf8mb4_bin NOT NULL DEFAULT 'no',
  `status` tinyint(3) NOT NULL DEFAULT '1',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_email` (`email`),
  UNIQUE KEY `uk_nickname` (`nickname`),
  UNIQUE KEY `uk_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

/*Data for the table `user` */

insert  into `user`(`id`,`nickname`,`username`,`password`,`login_salt`,`email`,`admin`,`status`,`updated_time`,`created_time`) values (1,'qwerty','19206168','123456','qqtbtbq','123@example6.com','yes',1,'2022-05-04 15:57:24','2022-05-04 15:57:24'),(2,'asdfgh','100000','123456','bqtbqqn','123@example.com','no',1,'2022-05-03 17:08:39','2022-05-03 17:08:39'),(3,'qwerty123','qwedsa','123456','nwrnwnw','123@example1.com','no',1,'2022-04-13 18:52:47','2022-04-13 18:52:47'),(4,'123','123','123456','nwtn24c','123@example3.com','no',1,'2022-04-13 18:52:49','2022-04-13 18:52:49'),(5,'123321','123321','123321',NULL,'123@example2.com','no',1,'2022-04-13 18:52:52','2022-04-13 18:52:52'),(15,'edcvfr','edcvfr','123456',NULL,'123@example4.com','no',1,'2022-04-07 18:44:58','2022-04-07 18:44:58');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
