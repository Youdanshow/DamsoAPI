CREATE TABLE IF NOT EXISTS `drinks` (
  `drink_id` int(11) NOT NULL COMMENT 'if of the drink',
  `name` varchar(50) COLLATE utf8_bin NOT NULL COMMENT 'name of the drink',
  `description` varchar(50) COLLATE utf8_bin NOT NULL COMMENT 'description of the drink',
  PRIMARY KEY (`drink_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

INSERT INTO `drinks` (`drink_id`, `name`, `description`) VALUES
(0, 'soda de chien', 'boisson de chien'),
(1, 'Sprite', 'Soda au citron'),
(2, 'Limonade', 'boisson fraiche'),
(3, 'dog', 'dog drink'),
(4, 'catou', 'boisson de chat');
