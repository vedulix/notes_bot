CREATE TABLE `bot_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `chat_id` varchar(30) DEFAULT NULL,
  `nickname` varchar(30) DEFAULT 'anonim',
  `gender` varchar(30) DEFAULT 'anonimus',
  `scheduler` varchar(30) DEFAULT '20:00',
  `username` varchar(40) DEFAULT '@N',
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `user_photo` varchar(100) NOT NULL,
  `last_notes` varchar(70) NOT NULL,
  `achieve_method` varchar(100) NOT NULL DEFAULT 'voice',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14207 DEFAULT CHARSET=utf8mb4

CREATE TABLE `notes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `note` longtext NOT NULL,
  `chat_id` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=185917 DEFAULT CHARSET=utf8mb4

CREATE TABLE `texts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `trigger` int(10) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `chat_id` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=299 DEFAULT CHARSET=utf8mb4

CREATE TABLE `video_notes` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `chat_id` varchar(30) NOT NULL,
  `file_id` longtext NOT NULL,
  `trigger` int(10) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4

CREATE TABLE `voices` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `chat_id` varchar(30) NOT NULL,
  `file_id` longtext NOT NULL,
  `trigger` int(10) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4
