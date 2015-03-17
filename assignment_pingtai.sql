create database assignment_pingtai;

use assignment_pingtai;

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `name` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `image` longblob,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;