alter session set "_oracle_script"=true;
CREATE USER prograweb IDENTIFIED BY "prograweb"
DEFAULT TABLESPACE USERS
TEMPORARY TABLESPACE TEMP;
ALTER USER prograweb QUOTA UNLIMITED ON USERS;
GRANT CREATE SESSION TO prograweb ;
GRANT RESOURCE TO prograweb ;
ALTER USER prograweb DEFAULT ROLE RESOURCE;


Insert into "_JUEGOS_JUEGOS" (NOMBRE,TITULO,TIPO,IMAGEN,LINK) values ('formite','Fortnite','D','juego/fortnite.jpg','https://www.epicgames.com/fortnite/es-ES/download');
Insert into "_JUEGOS_JUEGOS" (NOMBRE,TITULO,TIPO,IMAGEN,LINK) values ('Mario vs Sonic','Super Smash Bros Ultimate','D','noticias/smash.jpg','https://smashbros.nintendo.com/es/buy/');
Insert into "_JUEGOS_JUEGOS" (NOMBRE,TITULO,TIPO,IMAGEN,LINK) values ('gtav','Grand Theft Auto V','D','noticias/003.jpg','https://store.steampowered.com/agecheck/app/271590/');
Insert into "_JUEGOS_JUEGOS" (NOMBRE,TITULO,TIPO,IMAGEN,LINK) values ('lol','League of Legends','D','noticias/004.jpg','https://www.leagueoflegends.com/es-mx/');
Insert into "_JUEGOS_JUEGOS" (NOMBRE,TITULO,TIPO,IMAGEN,LINK) values ('maincra','Minecraft','D','noticias/005.jpg','https://www.minecraft.net/es-es/download');
Insert into "_JUEGOS_JUEGOS" (NOMBRE,TITULO,TIPO,IMAGEN,LINK) values ('genshin','Genshin Impact','D','noticias/006.jpg','https://genshin.hoyoverse.com/es/download?gclid=EAIaIQobChMI4oObrazE-AIVBfnICh0VLA10EAAYASABEgIYaPD_BwE');


Insert into PROGRAWEB."_NOTICIAS_NOTICIAS" (ID,NOMBRE,TITULO,IMAGEN,CUERPO,LINK) values ('4','LOL_cosplay','LEYENDAS DEL COSPLAY-ESCUADR�N ANIMALIA 2022','noticias/lol.jpeg','�Ha llegado el momento de deslumbrar a todos! El segundo concurso del a�o est� por comenzar. Llena el formulario, toma tu foto, comparte tu talento �y convi�rtete en la pr�xima leyenda!','https://www.leagueoflegends.com/es-mx/news/community/leyendas-del-cosplay-escuadron-animalia-2022/');
Insert into PROGRAWEB."_NOTICIAS_NOTICIAS" (ID,NOMBRE,TITULO,IMAGEN,CUERPO,LINK) values ('1','Deporte','LOS MEJORES JUEGOS PARA HACER','noticias/just.jpeg','Te traemos una selecci�n de 8 t�tulos para que vayas poni�ndote forma con tu Switch.','https://www.ubisoft.com/es-mx/game/just-dance/2022');
Insert into PROGRAWEB."_NOTICIAS_NOTICIAS" (ID,NOMBRE,TITULO,IMAGEN,CUERPO,LINK) values ('3','KRU','VALORANT:KR� Esports fuera de Champions 2021 tras un quinto �overtime�','noticias/kru.jpeg','El club de Sergio Ag�ero qued� en la tercera posici�n del Mundial tras haber enfrentado a Gambit Esports. Sin duda la mejor serie de todo el torneo, hasta el momento.','https://depor.com/depor-play/esports/valorant-kru-esports-fuera-de-champions-2021-tras-un-quinto-overtime-esports-videojuegos-riot-games-noticia/');
Insert into PROGRAWEB."_NOTICIAS_NOTICIAS" (ID,NOMBRE,TITULO,IMAGEN,CUERPO,LINK) values ('5','FFire_bts','Free Fire:recompensas, eventos y todo sobre la colaboraci�n con BTS','noticias/freefire.jpg','�La actualizaci�n H�roes (OB33) lleg� acompa�ada por una de las agrupaciones musicales m�s populares de los �ltimos tiempos! Ya tenemos el calendario de eventos que revela la fecha, cosm�ticos, aspectos y recompensas de la colaboraci�n de Free Fire con el grupo de K-Pop BTS.','https://www.gamerfocus.co/juegos/free-fire-bts-atuendos-recompensas-calendario-eventos-colaboracion-banda-k-pop/');
Insert into PROGRAWEB."_NOTICIAS_NOTICIAS" (ID,NOMBRE,TITULO,IMAGEN,CUERPO,LINK) values ('7','Champ_abril','MAPA DE CAMPEONES: ABRIL 2022','noticias/nuevoscampeones.jpg','�No te atrevas a cerrar los ojos! El equipo de campeones se trae algo entre manos. Algo hermoso, algo inevitable, algo vaticinado. Una nueva contendiente para todos los jugadores de la jungla. Una nueva emperatriz a la que someterse... y te someter�s.','https://www.leagueoflegends.com/es-mx/news/dev/mapa-de-campeones-abril-2022/');
Insert into PROGRAWEB."_NOTICIAS_NOTICIAS" (ID,NOMBRE,TITULO,IMAGEN,CUERPO,LINK) values ('8','Valo_update','ACTUALIZACIONES VALORANT','noticias/valorant.jpg','�No te pierdas ninguna actualizaci�n en este link.','https://playvalorant.com/es-es/news/game-updates/');

insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,2,'Ivysaur','Planta','Veneno',13,1);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,3,'Venusaur','Planta','Veneno',100,2);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,4,'Charmander','Fuego','Ninguno',8.5,0.6);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,5,'Charmeleon','Fuego','Ninguno',19,1.1);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,6,'Charizard','Fuego','Volador',90.5,1.7);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,7,'Squirtle','Agua','Ninguno',9,0.5);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,8,'Wartortle','Agua','Ninguno',22.5,1);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,9,'Blastoise','Agua','Ninguno',85.5,1.6);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,10,'Caterpie','Bicho','Ninguno',2.9,0.3);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,11,'Metapod','Bicho','Ninguno',9.9,0.7);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,12,'Butterfree','Bicho','Volador',32,1.1);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,13,'Weedle','Bicho','Veneno',3.2,0.3);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,14,'Kakuna','Bicho','Veneno',10,0.6);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,15,'Beedrill','Bicho','Veneno',29.5,1);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,16,'Pidgey','Normal','Volador',1.8,0.3);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,17,'Pidgeotto','Normal','Volador',30,1.1);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,18,'Pidgeot','Normal','Volador',39.5,1.5);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,19,'Rattata','Normal','Ninguno',3.5,0.3);
insert into rest_pokemon_pokemon values("PROGRAWEB"."ISEQ$$_78338".NEXTVAL,20,'Raticate','Normal','Ninguno',18.5,0.7);