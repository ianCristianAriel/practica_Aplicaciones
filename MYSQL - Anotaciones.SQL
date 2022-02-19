/* Antes de importar los archivos de exel a php my admin hay que asegurarse de que (si son requeridos) esten la fecha en formato aaaa-m-dd y los precios o similar en formato
acounting para que sean identificados como tal y no como texto,ademas luego puede que halla que cambiar desde la estructura en php my admin*/


CREATE DATABASE USUARIOS; /* se crea una base de datos */
USE USUARIOS;/* Se selecciona la base de datos */
CREATE TABLE DATOSUSUARIOS (NOMBRE VARCHAR(10), CLAVE VARCHAR(20));/* Se crea la base de datos */
SELECT NOMBRE FROM DATOSUSUARIOS; /* se seleccionauna clumna de la base de datos */

/* from: Espesifica la tabla de la que se quieren obtener los registros
   where: Espesifica las condiciones o criteriors de los regitros seleccionados
   group by: para agrupar los registros seleccionados en funcion de un campo
   having: Espesifica las condiciones o criterios que deben cumplir los grupos
   order by: ordena los registros seleccionados en funcion de un campo  */

/* Operadores:
and -> y
or -> o
not ->negacion */

/* En el caso de que se usen todas las clausulas este seria el orden: */
/* comando + clausula from + clausula where + clausula group by + clausula having + clausula order by */



/* En este caso se solicita que se muestren las columnas de precio y seccion correspondientes a las secciones en que este ceramica */
SELECT SECCIÓN, PRECIO FROM productos WHERE SECCIÓN = "CERAMICA"; 

/* En este caso se mustra de seccion deportes y seccion ceramica mediante or */
SELECT SECCIÓN, PRECIO FROM productos WHERE SECCIÓN = "CERAMICA" or SECCIÓN="Deportes"; 

/* Aca se muestran mediante el "*" todas las columnas del PAÍSDEORIGEN->usa y de las seccion->deportes;*/
SELECT * FROM productos WHERE PAÍSDEORIGEN = "usa" and SECCIÓN="Deportes";

/* Se selecciona y se muestra entre un rango */
SELECT * FROM PRODUCTOS WHERE FECHA BETWEEN "2000-03-01" AND "2000-04-30";

/* Ordena la lista por la columna que se le pase luego de order by . Ordena por seccion y de menor a mayor*/
SELECT * FROM productos where sección = "deportes" or sección = "ceramica" order by SECCIÓN;

/* Ordena la lista por secciones pero de mayor a menor */
SELECT * FROM productos where sección = "deportes" or sección = "ceramica" order by SECCIÓN desc;

/* Ordena por el parametro que se le pase luego de order by y luego por el segundo parametro */
SELECT * FROM productos where sección = "deportes" or sección = "ceramica" order by SECCIÓN, CÓDIGOARTÍCULO;

/* Se ordenan las seccion y se muestra el total de cada una */
SELECT sección, sum(PRECIO) FROM productos group by SECCIÓN;

/* Agrega un alias mediante "as" y luego se lo llama */
SELECT sección, sum(PRECIO) as suma_articulos FROM productos group by SECCIÓN order by "suma_articulos";

/* Se utiliza avg para obtener la media */
SELECT sección, avg(PRECIO) as media_articulos FROM productos group by sección HAVING SECCIÓN="ceramica" and sección="Deportes";

/* Se cuenta el numero de veces que se repite un item mediante count */
SELECT POBLACIÓN, COUNT(CÓDIGOCLIENTE) as cantidad_clientes FROM clientes group by POBLACIÓN order by cantidad_clientes;

/* Se selecciona el item mayor */
SELECT sección, max(precio) as mas_Caro FROM productos where sección="confección";

/* Se utiliza una exprecion matematica para  agregar otra columna*/
SELECT sección, IMPORTADO, precio, precio*1.21 as precio_con_IVA from productos;

/* Se redondea un valor condecimales. mediante: round() la coma y el numero que le sigue indican el numero de decimales*/
SELECT sección, IMPORTADO, precio, round(precio*1.21,2) as precio_con_IVA from productos;

/* Se utiliza la fecha actual */
SELECT sección, IMPORTADO, precio, round(precio*1.21,2) as precio_con_IVA, now() as dia_consulta from productos;

/* Se hace una diferencia de dias mediande "datediff" se deve utilizar now() como primer parametro, no se puede colocar un aleas*/
SELECT sección, IMPORTADO, precio, round(precio*1.21,2) as precio_con_IVA, now() as dia_consulta, datediff(now(), fecha) as diferencia_de_Dias from productos;

/* Se cambia el formato de la fecha mediante dateformat(, "D-M") */
SELECT sección, IMPORTADO, precio, round(precio*1.21,2) as precio_con_IVA, date_format(now(),"%D-%m") as dia_consulta, datediff(now(), fecha) as diferencia_de_Dias from productos;


/* Consulta con union. las tablas deben tener la misma cantidad de columnas y por ejemplo la columna 1 sea de tipo monodea/int en ambas y si en la segunda 
hay string tiene que ser en ambas y asi*/
SELECT * FROM PRODUCTOS WHERE SECCIÓN='DEPORTES' UNION SELECT * FROM productosnuevos WHERE SECCIÓN='DEPORTES DE RIESGO';

/* Con "union all" se muestran inclusive aquellos resultados que sean identicos en ambas tablas*/
SELECT * FROM `productosnuevos` union ALL select * from productos;

/* Se muestran resultados que coinciden en dos tablas mediante  "inner join" y una igualacion entre las dos tablas (la primera: left y la segunda: right)*/
SELECT * FROM CLIENTES INNER JOIN PEDIDOS ON CLIENTES.[CODIGO CLIENTE] = pedidos.[CODIGO CLIENTE];
SELECT * FROM CLIENTES INNER JOIN PEDIDOS ON CLIENTES.[CODIGO CLIENTE] = pedidos.[CODIGO CLIENTE] WHERE POBLACION = "MADRID"; /* Con criterio de poblacion */
/* Left join */
SELECT * FROM CLIENTES left JOIN PEDIDOS ON CLIENTES.[CODIGO CLIENTE] = pedidos.[CODIGO CLIENTE];/* Se muestran aquellos resultados que estan en la tabla introducida primero (clientes en este caso) y los que coinciden con la segunda*/
/* Right join */
select * from clientes right join pedidos on clientes.[CODIGO CLIENTE] = pedidos.[CODIGO CLIENTE];/* Se mostraran todos los elementos de la tabla colocada del lado derecho del igual y las que coincidan con la tabla colocada a la izquiera del igual */

/* se realiza una subconsulta. A la primera se le llama "padre" y a la segunda "hija".  */
select avg(precio) from productos /* Esto devuelve un valor en pesos */
select NOMBREARTÍCULO, sección from productos where precio<(select avg(precio) from productos);
select `NOMBREARTÍCULO` from productos where precio > (select max(precio) as precio_Mas_Alto from productos where sección="cerámica");
/* All refiere a todos los elementos de un registro */
select `NOMBREARTÍCULO` from productos where precio > all (select precio from productos where sección="cerámica");
/* En este caso "any",  refiere a cualquiera del registro o seleccion */
select `NOMBREARTÍCULO` from productos where precio > any (select precio from productos where sección="cerámica");
/* Se seleccionan de un registro aquellos que compartan con otro registro mediante "in"*/
select NOMBREARTÍCULO from productos where NOMBREARTÍCULO in (select NOMBREARTÍCULO from productos where precio<100);
/* Not in muestra los que no estan */
select NOMBREARTÍCULO from productos where NOMBREARTÍCULO not in (select NOMBREARTÍCULO from productos where precio<100);


/* REALIZAR UPDATES */
update productos set precio=-10 where SECCIÓN='deportes';/* Asi se le disminuye a un determinado registro */
update productos set sección="deportivos" where sección="deportes"; /* Se actualiza el nombre de la seccion deportes por deportivos*/

/* Creaciones de tabla */
create table clientes_Madrid select * from clientes;
create table clientes_Madrid select * from clientes where población ='Madridi'; /* Se selecciona que se copiara exlusivamente */
create table pruba(nombre VARCHAR (10), edad tinyint, fecha date, carnet boolean);

/* Eliminacion de una tabla */
drop table prueba;

/* Eliminacion de un registro completo de la tabla */
delete from clientes where población="madrid";
delete from productos where sección='Deportivos' and precio BETWEEN 50 and 10;/* Eliminacion mas detallada */

/* Distinct impide que se repitan los resultados */
select DISTINCT empresa from clientes INNER join pedidos ON clientes.CÓDIGOCLIENTE=pedidos.CÓDIGO CLIENTE;

/* distinct row */
select DISTINCTROW * from productos where sección='Ferreteria';

/* Se inserta una tabla dentro de otra */
insert into clientes SELECT * from clientes_madrid;

/* Fijacion de clave primaria y cracion de claves de autoincremento */
create table prueba(id_alumno int AUTO_INCREMENT, edad tinyint, PRIMARY KEY (id_alumno));/* El primary key se asigna luego de darle un dato a la columna */

/* Alterar una tabla */
alter table clientes_madrid add column fecha_baja date; /* Agregar columna a tabla */
alter table clientes modify column fecha_Baja varchar(10);/* Se cambia el tipo de dato de una columna */
alter table clientes_Madrid drop column fecha_baja;/* Se elimina una columna */

/* Creacion de indice */
alter table ejemplo add primary key (nombre, edad);/* Indice de clave primaria, se le agregs una clave primaria, no permite espacios null. */
create index mi_Indice on ejemplo (edad); /* Indice ordinario */
create unique INDEX mi_indice on product (nombre);/* indice unico, no permite que dos campos sean iguales */
create unique index mi_Indice3 on product (dni, edad);/* Indice compuesto, permite multiples columnas  */

/* Eliminacion de indices */
alter table ejemplo drop PRIMARY KEY;/* Eliminacion de clave primaria */
drop index mi_indice on ejemplo;/* Eliminacion de cualquier otro tipo de indice */ 

/* Triggers */
/* Trigger de insert */
create trigger reg_productos_AI after insert on productos for each row insert into reg_productos(codigo_articulo, nombre_articulo, precio, insertado) values (new.codigo_articulo, new.nombre_articulo, new.precio, now());
/* creacion de trigger. La "A" y la "i" corresponden a "after" y "insert" respectivamente, varia dependiedno de la accion que realize*/
/* Dentro del primer parentecis se coloca lo que ira en el registro donde se almacenan los registros  y en el segundo los nombres de las 
columnas del registro  emisor acompañados por "new."...*/
create table productos_Actualizados (anterior_codigoArticulo varchar(10), anterior_nombreArticulo varchar(10), anterior_precioArticulo int, anterior_fechaArticulo datetime, nuevo_codigoArticulo varchar(10), nuevo_nombreArticulo varchar(10), nuevo_precioArticulo int, nuevo_fechaArticulo datetime, usuario varchar(20),f_modif datetime);
/* Creacion de trigger con valores antiguos "old." y valores nuevos "new."*/
/* "Current_user()" hace referencia a el usuario que realizo la modificacion
   "now()" hace referencia a la fecha de la modificacion */
/* Trigger de actualizacion*/
create trigger productos_Actualizados_BU before update on productos for each row insert into productos_Actualizados (anterior_codigoArticulo, anterior_nombreArticulo, anterior_precioArticulo, anterior_fechaArticulo nuevo_codigoArticulo, nuevo_nombreArticulo, nuevo_precioArticulo, nuevo_fechaArticulo, USUARIO, f_modif) values(old.CÓDIGOARTÍCULO, old.NOMBREARTÍCULO, old.precio, old.fecha, new.CÓDIGOARTÍCULO, new.NOMBREARTÍCULO, new.precio, new.fecha, current_user(), now());
/* Trigger de eliminacion.  */
/* En este caso solo se presiza ".old", ya que es de eliminacion y no hay un nuevo valor */
create trigger productoselim_AD after delete on productos for each row insert into productos_eliminados (anterior_codigoArticulo, anterior_nombreArticulo, anterior_precioArticulo, anterior_fechaArticulo, nuevo_codigoArticulo, nuevo_nombreArticulo, nuevo_precioArticulo, nuevo_fechaArticulo, USUARIO, f_modif) values(old.CÓDIGOARTÍCULO, old.NOMBREARTÍCULO, old.precio, old.fecha, current_user(), now());

/* Eliminar trigger */
drop trigger productoselim_AD;
/* Modificacion de trigger */
/* Se comprueba que exista el trigger y si es asi, se elimina y se crea nuevamente pero con las modificaciones que se le quieran hacer */
drop trigger if exist productoselim_AD; create trigger productoselim_AD after delete on productos for each row insert into productos_eliminados (anterior_codigoArticulo, anterior_nombreArticulo, anterior_precioArticulo, anterior_fechaArticulo, nuevo_codigoArticulo, nuevo_nombreArticulo, nuevo_precioArticulo, nuevo_fechaArticulo, USUARIO, f_modif) values(old.CÓDIGOARTÍCULO, old.NOMBREARTÍCULO, old.precio, old.fecha, current_user(), now());

/* Procedimientos */
/* Creacion  */
create prosedure select * from clientes where POBLACIón='madrid';/* Procedimientos sin parametro */
create procedure actualiza_Productos(precio_N int (4), codigo_Articulo varchar(4)) update productos set precio=precio_N where códigoartículo=codigo_Articulo;/* Procedimiento con parametros */
/* con bloques */
DELIMITER $$ /* Se utiliza para definir un deliitador que indicara el fin del bloque begin - end */
create procedure calcula_edad(anio_nacimiento int)
	BEGIN
    	DECLARE anio_actual=2022; /* Termina en punto y coma cada linea de codigo */
        declare edad=int;
        set edad=agno_actual-agno_nacimiento;
        select edad;
    end;$$
DELIMITER ; /* Se recetea el delimitador dejando ";" */

/* VISTAS */
/* Creacion */
create view art_deportes as select nombreartículo, sección, precio from productos where sección= "deportes";
/* Eliminacion */
drop art_deportes;
/* modificacion */
alter view art_deportes as select nombreartículo, precio from productos where sección= "deportes";