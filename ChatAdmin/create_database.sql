create database support_chat;
use support_chat;

create table people
(id int not null auto_increment primary key,
name varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
ip varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci,
email varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci,
is_block int(1) ,
started timestamp,
date TIMESTAMP) CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `support_chat`.`people`
ADD CONSTRAINT `FK_people_id`
  FOREIGN KEY (`id`)
  REFERENCES `support_chat`.`message` (`people_id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;



create table room
(id int not null auto_increment primary key,
title varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
user_key int not null,
date timestamp) CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `support_chat`.`room`
ADD INDEX `FK_user_key_idx` (`user_key` ASC);
ALTER TABLE `support_chat`.`room`
ADD CONSTRAINT `FK_user_key`
  FOREIGN KEY (`user_key`)
  REFERENCES `support_chat`.`message` (`room_id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;


create table message
(id int not null auto_increment primary key,
name varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
text varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci,
date timestamp,
people_id  int not null,
room_id int not null) CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `support_chat`.`message`
ADD INDEX `message_people_id` (`people_id` ASC),
ADD INDEX `message_room_id` (`room_id` ASC);
