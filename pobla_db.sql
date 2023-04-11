
INSERT INTO region (region_id, region_name)
VALUES
(1,'Arica y Parinacota'),
	(2,'Tarapacá'),
	(3,'Antofagasta'),
	(4,'Atacama'),
	(5,'Coquimbo'),
	(6,'Valparaiso'),
	(7,'Metropolitana de Santiago'),
	(8,'Libertador General Bernardo OHiggins'),
	(9,'Maule'),
	(10,'Ñuble'),
	(11,'Biobío'),
	(12,'La Araucanía'),
	(13,'Los Ríos'),
	(14,'Los Lagos'),
	(15,'Aysén del General Carlos Ibáñez del Campo'),
	(16,'Magallanes y de la Antártica Chilena');


INSERT INTO provincia (provincia_id, provincia_name,region_id) 
VALUES
    (1,'Arica',1),
	(2,'Parinacota',1),
	(3,'Iquique',2),
	(4,'El Tamarugal',2),
	(5,'Tocopilla',3),
	(6,'El Loa',3),
	(7,'Antofagasta',3),
	(8,'Chañaral',4),
	(9,'Copiapó',4),
	(10,'Huasco',4),
	(11,'Elqui',5),
	(12,'Limarí',5),
	(13,'Choapa',5),
 	(14,'Petorca',6),
	(15,'Los Andes',6),
 	(16,'San Felipe de Aconcagua',6),
 	(17,'Quillota',6),
	(18,'Valparaiso',6),
	(19,'San Antonio',6),
	(20,'Isla de Pascua',6),
	(21,'Marga Marga',6),
	(22,'Chacabuco',7),
	(23,'Santiago',7),
	(24,'Cordillera',7),
	(25,'Maipo',7),
	(26,'Melipilla',7),
	(27,'Talagante',7),
	(28,'Cachapoal',8),
	(29,'Colchagua',8),
	(30,'Cardenal Caro',8),
	(31,'Curicó',9),
	(32,'Talca',9),
 	(33,'Linares',9),
	(34,'Cauquenes',9),
	(35,'Diguillín',10),
	(36,'Itata',10),
	(37,'Punilla',10),
	(38,'Bio Bío',11),
	(39,'Concepción',11),
	(40,'Arauco',11),
	(41,'Malleco',12),
	(42,'Cautín',12),
	(43,'Valdivia',13),
	(44,'Ranco',13),
	(45,'Osorno',14),
	(46,'Llanquihue',14),
	(47,'Chiloé',14),
	(48,'Palena',14),
	(49,'Coyhaique',15),
	(50,'Aysén',15),
	(51,'General Carrera',15),
	(52,'Capitán Prat',15),
	(53,'Última Esperanza',16),
	(54,'Magallanes',16),
	(55,'Tierra del Fuego',16),
	(56,'Antártica Chilena',16);


INSERT INTO comuna (comuna_id, comuna_name, provincia_id)
VALUES
   (1,'Arica',1),
	(2,'Camarones',1),
	(3,'General Lagos',2),
	(4,'Putre',2),
	(5,'Alto Hospicio',3),
	(6,'Iquique',3),
	(7,'Camiña',4),
	(8,'Colchane',4),
	(9,'Huara',4),
	(10,'Pica',4),
	(11,'Pozo Almonte',4),
  	(12,'Tocopilla',5),
  	(13,'María Elena',5),
	(14,'Calama',6),
	(15,'Ollague',6),
	(16,'San Pedro de Atacama',6),
  	(17,'Antofagasta',7),
	(18,'Mejillones',7),
	(19,'Sierra Gorda',7),
	(20,'Taltal',7),
	(21,'Chañaral',8),
	(22,'Diego de Almagro',8),
  	(23,'Copiapó',9),
	(24,'Caldera',9),
	(25,'Tierra Amarilla',9),
  	(26,'Vallenar',10),
	(27,'Alto del Carmen',10),
	(28,'Freirina',10),
	(29,'Huasco',10),
	(30,'La Serena',11),
  	(31,'Coquimbo',11),
  	(32,'Andacollo',11),
  	(33,'La Higuera',11),
  	(34,'Paihuano',11),
	(35,'Vicuña',11),
	(36,'Ovalle',12),
  	(37,'Combarbalá',12),
  	(38,'Monte Patria',12),
  	(39,'Punitaqui',12),
	(40,'Río Hurtado',12),
	(41,'Illapel',13),
	(42,'Canela',13),
	(43,'Los Vilos',13),
	(44,'Salamanca',13),
	(45,'La Ligua',14),
  	(46,'Cabildo',14),
	(47,'Zapallar',14),
  	(48,'Papudo',14),
	(49,'Petorca',14),
	(50,'Los Andes',15),
	(51,'San Esteban',15),
  	(52,'Calle Larga',15),
  	(53,'Rinconada',15),
	(54,'San Felipe',16),
  	(55,'Llaillay',16),
  	(56,'Putaendo',16),
	(57,'Santa María',16),
	(58,'Catemu',16),
	(59,'Panquehue',16),
  	(60,'Quillota',17),
  	(61,'La Cruz',17),
	(62,'La Calera',17),
	(63,'Nogales',17),
  	(64,'Hijuelas',17),
	(65,'Valparaíso',18),	
  	(66,'Viña del Mar',18),
	(67,'Concón',18),
 	(68,'Quintero',18),
  	(69,'Puchuncaví',18),
	(70,'Casablanca',18),
	(71,'Juan Fernández',18),
	(72,'San Antonio',19),
  	(73,'Cartagena',19),
	(74,'El Tabo',19),
	(75,'El Quisco',19),
	(76,'Algarrobo',19),
	(77,'Santo Domingo',19),
	(78,'Isla de Pascua',20),
	(79,'Quilpué',21),
	(80,'Limache',21),
	(81,'Olmué',21),
	(82,'Villa Alemana',21),
	(83,'Colina',22),
	(84,'Lampa',22),
	(85,'Tiltil',22),
	(86,'Santiago',23),
	(87,'Vitacura',23),
  	(88,'San Ramón',23),
	(89,'San Miguel',23),
	(90,'San Joaquín',23),
  	(91,'Renca',23),
	(92,'Recoleta',23),
  	(93,'Quinta Normal',23),
	(94,'Quilicura',23),
  	(95,'Pudahuel',23),
  	(96,'Providencia',23),
	(97,'Peñalolén',23),
  	(98,'Pedro Aguirre Cerda',23),
	(99,'Ñuñoa',23),
	(100,'Maipú',23),
	(101,'Macul',23),
	(102,'Lo Prado',23),
	(103,'Lo Espejo',23),
	(104,'Lo Barnechea',23),
	(105,'Las Condes',23),
	(106,'La Reina',23),
	(107,'La Pintana',23),
	(108,'La Granja',23),
	(109,'La Florida',23),
  	(110,'La Cisterna',23),
  	(111,'Independencia',23),
  	(112,'Huechuraba',23),
	(113,'Estación Central',23),
  	(114,'El Bosque',23),
  	(115,'Conchalí',23),
  	(116,'Cerro Navia',23),
  	(117,'Cerrillos',23),
	(118,'Puente Alto',24),
	(119,'San José de Maipo',24),
  	(120,'Pirque',24),
	(121,'San Bernardo',25),
	(122,'Buin',25),
  	(123,'Paine',25),
	(124,'Calera de Tango',25),
	(125,'Melipilla',26),
	(126,'Alhué',26),
	(127,'Curacaví',26),
	(128,'María Pinto',26),
	(129,'San Pedro',26),
	(130,'Isla de Maipo',27),
  	(131,'El Monte',27),
	(132,'Padre Hurtado',27),
	(133,'Peñaflor',27),
	(134,'Talagante',27),
	(135,'Codegua',28),
	(136,'Coínco',28),
	(137,'Coltauco',28),
	(138,'Doñihue',28),
	(139,'Graneros',28),
	(140,'Las Cabras',28),
	(141,'Machalí',28),
	(142,'Malloa',28),
	(143,'Mostazal',28),
	(144,'Olivar',28),
	(145,'Peumo',28),
	(146,'Pichidegua',28),
	(147,'Quinta de Tilcoco',28),
	(148,'Rancagua',28),
	(149,'Rengo',28),
	(150,'Requínoa',28),
	(151,'San Vicente de Tagua Tagua',28),
	(152,'Chépica',29),
	(153,'Chimbarongo',29),
	(154,'Lolol',29),
  	(155,'Nancagua',29),
  	(156,'Palmilla',29),
  	(157,'Peralillo',29),
	(158,'Placilla',29),
 	(159,'Pumanque',29),
	(160,'San Fernando',29),
	(161,'Santa Cruz',29),
	(162,'La Estrella',30),
	(163,'Litueche',30),
	(164,'Marchigüe',30),
	(165,'Navidad',30),
	(166,'Paredones',30),
	(167,'Pichilemu',30),
	(168,'Curicó',31),
	(169,'Hualañé',31),
	(170,'Licantén',31),
 	(171,'Molina',31),
	(172,'Rauco',31),
	(173,'Romeral',31),
	(174,'Sagrada Familia',31),
	(175,'Teno',31),
	(176,'Vichuquén',31),
	(177,'Talca',32),
	(178,'San Clemente',32),
	(179,'Pelarco',32),
	(180,'Pencahue',32),
	(181,'Maule',32),
	(182,'San Rafael',32),
	(183,'Curepto',33),
	(184,'Constitución',32),
	(185,'Empedrado',32),
	(186,'Río Claro',32),
  	(187,'Linares',33),
	(188,'San Javier',33),
	(189,'Parral',33),
	(190,'Villa Alegre',33),
	(191,'Longaví',33),
	(192,'Colbún',33),
	(193,'Retiro',33),
	(194,'Yerbas Buenas',33),
  	(195,'Cauquenes',34),
	(196,'Chanco',34),
	(197,'Pelluhue',34),
	(198,'Bulnes',35),
	(199,'Chillán',35),
	(200,'Chillán Viejo',35),
	(201,'El Carmen',35),
	(202,'Pemuco',35),
	(203,'Pinto',35),
	(204,'Quillón',35),
	(205,'San Ignacio',35),
	(206,'Yungay',35),
	(207,'Cobquecura',36),
	(208,'Coelemu',36),
	(209,'Ninhue',36),
	(210,'Portezuelo',36),
	(211,'Quirihue',36),
	(212,'Ránquil',36),
	(213,'Treguaco',36),
	(214,'San Carlos',37),
	(215,'Coihueco',37),
	(216,'San Nicolás',37),
	(217,'Ñiquén',37),
	(218,'San Fabián',37),
	(219,'Alto Biobío',38),
	(220,'Antuco',38),
	(221,'Cabrero',38),
	(222,'Laja',38),
	(223,'Los Ángeles',38),
	(224,'Mulchén',38),
	(225,'Nacimiento',38),
	(226,'Negrete',38),
	(227,'Quilaco',38),
	(228,'Quilleco',38),
	(229,'San Rosendo',38),
	(230,'Santa Bárbara',38),
	(231,'Tucapel',38),
	(232,'Yumbel',38),
	(233,'Concepción',39),
	(234,'Coronel',39),
	(235,'Chiguayante',39),
	(236,'Florida',39),
	(237,'Hualpén',39),
	(238,'Hualqui',39),
	(239,'Lota',39),
	(240,'Penco',39),
	(241,'San Pedro de La Paz',39),
	(242,'Santa Juana',39),
	(243,'Talcahuano',39),
	(244,'Tomé',39),
	(245,'Arauco',40),
	(246,'Cañete',40),
	(247,'Contulmo',40),
	(248,'Curanilahue',40),
	(249,'Lebu',40),
	(250,'Los Álamos',40),
	(251,'Tirúa',40),
	(252,'Angol',41),
	(253,'Collipulli',41),
	(254,'Curacautín',41),
	(255,'Ercilla',41),
	(256,'Lonquimay',41),
	(257,'Los Sauces',41),
	(258,'Lumaco',41),
	(259,'Purén',41),
	(260,'Renaico',41),
	(261,'Traiguén',41),
	(262,'Victoria',41),
	(263,'Temuco',42),
	(264,'Carahue',42),
	(265,'Cholchol',42),
	(266,'Cunco',42),
	(267,'Curarrehue',42),
	(268,'Freire',42),
	(269,'Galvarino',42),
	(270,'Gorbea',42),
	(271,'Lautaro',42),
	(272,'Loncoche',42),
	(273,'Melipeuco',42),
	(274,'Nueva Imperial',42),
	(275,'Padre Las Casas',42),
	(276,'Perquenco',42),
	(277,'Pitrufquén',42),
	(278,'Pucón',42),
	(279,'Saavedra',42),
	(280,'Teodoro Schmidt',42),
	(281,'Toltén',42),
	(282,'Vilcún',42),
	(283,'Villarrica',42),
	(284,'Valdivia',43),
	(285,'Corral',43),
	(286,'Lanco',43),
	(287,'Los Lagos',43),
	(288,'Máfil',43),
	(289,'Mariquina',43),
	(290,'Paillaco',43),
	(291,'Panguipulli',43),
	(292,'La Unión',44),
	(293,'Futrono',44),
	(294,'Lago Ranco',44),
	(295,'Río Bueno',44),
	(296,'Osorno',45),
	(297,'Puerto Octay',45),
	(298,'Purranque',45),
	(299,'Puyehue',45),
	(300,'Río Negro',45),
	(301,'San Juan de la Costa',45),
	(302,'San Pablo',45),
	(303,'Calbuco',46),
	(304,'Cochamó',46),
	(305,'Fresia',46),
	(306,'Frutillar',46),
	(307,'Llanquihue',46),
	(308,'Los Muermos',46),
	(309,'Maullín',46),
	(310,'Puerto Montt',46),
	(311,'Puerto Varas',46),
	(312,'Ancud',47),
	(313,'Castro',47),
	(314,'Chonchi',47),
	(315,'Curaco de Vélez',47),
	(316,'Dalcahue',47),
	(317,'Puqueldón',47),
	(318,'Queilén',47),
	(319,'Quellón',47),
	(320,'Quemchi',47),
	(321,'Quinchao',47),
	(322,'Chaitén',48),
	(323,'Futaleufú',48),
	(324,'Hualaihué',48),
	(325,'Palena',48),
	(326,'Lago Verde',49),
	(327,'Coihaique',49),
	(328,'Aysén',50),
	(329,'Cisnes',50),
	(330,'Guaitecas',50),
	(331,'Río Ibáñez',51),
	(332,'Chile Chico',51),
	(333,'Cochrane',52),
	(334,'OHiggins',52),
	(335,'Tortel',52),
	(336,'Natales',53),
	(337,'Torres del Paine',53),
	(338,'Laguna Blanca',54),
	(339,'Punta Arenas',54),
	(340,'Río Verde',54),
	(341,'San Gregorio',54),
	(342,'Porvenir',55),
	(343,'Primavera',55),
	(344,'Timaukel',55),
	(345,'Cabo de Hornos',56),
	(346,'Antártica',56);

INSERT INTO public."user" (user_id, user_name1, user_name2, user_surname1, user_surname2, user_email, user_last_loc_lat, user_last_loc_long, user_date_lastloc, date_registred, date_last_login, user_score, user_phone, user_active, user_inetrest1, user_interest2, user_photo, user_sells, user_is_premium, user_premium_start, user_premium_ends)
VALUES 
('12345678-9', 'Juan', 'Pablo', 'Pérez', 'García', 'juanpablo@example.com', -33.447487, -70.673676, '2023-04-10', '2023-04-10', '2023-04-10', 0, 987654321, true, 1, 2, 'https://example.com/juanpablo.jpg', 0, false, null, null),
('98765432-1', 'María', null, 'González', 'López', 'mariagonzalez@example.com', -33.424244, -70.608889, '2023-04-09', '2023-04-09', '2023-04-09', 5, 123456789, true, 2, 3, 'https://example.com/mariagonzalez.jpg', 3, true, '2023-04-09', '2024-04-09'),
('19191919-1', 'Carlos', 'Andrés', 'Rodríguez', 'Pérez', 'carlosandres@example.com', -33.452470, -70.661293, '2023-04-08', '2023-04-08', '2023-04-08', 10, 987654321, false, 3, 4, 'https://example.com/carlosandres.jpg', 10, false, null, null),
('34567890-1', 'Pedro', null, 'Martínez', 'González', 'pedromartinez@example.com', -33.437698, -70.635669, '2023-04-07', '2023-04-07', '2023-04-07', 15, 123456789, true, 4, 5, 'https://example.com/pedromartinez.jpg', 5, true, '2023-04-07', '2024-04-07'),
('15678901-2', 'Fernanda', 'Isabel', 'Gómez', 'Pérez', 'fernandagomez@example.com', -33.431405, -70.555106, '2023-04-06', '2023-04-06', '2023-04-06', 20, 987654321, false, 5, 1, 'https://example.com/fernandagomez.jpg', 7, false, null, null),
('16789012-3', 'Luis', null, 'Hernández', 'López', 'luishernandez@example.com', -33.448502, -70.643858, '2023-04-05', '2023-04-05', '2023-04-05', 25, 123456789, true, 1, 2, 'https://example.com/luishernandez.jpg', 2, true, '2023-04-05', '2024-04-05'),
('78701234-5', 'Juan', null, 'Sánchez', 'Ramírez', 'juansanchez@example.com', -33.440042, -70.583871, '2023-04-04', '2023-04-04', '2023-04-04', 30, 987654321, false, 3, 4, 'https://example.com/juansanchez.jpg', 4, false, null, null),
('89012345-6', 'Carla', 'Javiera', 'Torres', null, 'carlatorres@example.com', -33.422466, -70.606408, '2023-04-03', '2023-04-03', '2023-04-03', 35, 123456789, true, 2, 3, 'https://example.com/carlatorres.jpg', 3, true, '2023-04-03', '2024-04-03'),
('90123456-7', 'Diego', 'Andrés', 'Vega', 'González', 'diegovega@example.com', -33.448938, -70.589355, '2023-04-02', '2023-04-02', '2023-04-02', 40, 987654321, false, 5, 1, 'https://example.com/diegovega.jpg', 6, false, null, null),
('1232567-9', 'Pablo', 'Andrés', 'García', 'Castillo', 'pablogarcia@example.com', -33.442790, -70.626125, '2023-04-06', '2023-04-06', '2023-04-06', 45, 123456789, true, 1, 5, 'https://example.com/pablogarcia.jpg', 2, true, '2023-04-06', '2024-04-06'),
('23456789-0', 'Francisco', null, 'López', null, 'franciscolopez@example.com', -33.448212, -70.648741, '2023-04-05', '2023-04-05', '2023-04-05', 50, 987654321, false, 4, 2, 'https://example.com/franciscolopez.jpg', 5, false, null, null),
('34567890-k', 'Javiera', null, 'Peralta', 'Díaz', 'javieraramirez@example.com', -33.435052, -70.562920, '2023-04-04', '2023-04-04', '2023-04-04', 55, 123456789, true, 3, 4, 'https://example.com/javieraramirez.jpg', 3, true, '2023-04-04', '2024-04-04');

INSERT INTO "affinity" ("af_id", "af_name")
VALUES
(1, 'libros'),
(2, 'peliculas'),
(3, 'música'),
(4, 'deportes'),
(5, 'cocina'),
(6, 'tecnología'),
(7, 'pokemon'),
(8, 'ropa'),
(9, 'salud'),
(10, 'arte');
