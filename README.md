# Bancolombia
Prueba Bancolombia
1. Es necesario crear una base de datos y una tabla de prueba en Mysql con la siguiente Query

CREATE TABLE IF NOT EXISTS `consultas` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Clave primaria',
  `producto` varchar(100) NOT NULL COMMENT 'Titulo del producto',
  `precio` varchar(50) NOT NULL COMMENT 'Precio del producto',
  `envio` int(9) NOT NULL COMMENT 'si tiene envio gratis',
  PRIMARY KEY (`id`),
  ) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='tabla de clientes';
  
  2. descargar el proyecto y abrirlo en su editor de preferencia
  3. Ejecutar el scritp main.py
