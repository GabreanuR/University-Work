--Crearea unei secvențe ce va fi utilizată în inserarea înregistrărilor în tabele
CREATE SEQUENCE ZONE_SEQ START WITH 1;
CREATE SEQUENCE STRAZI_SEQ START WITH 1;
CREATE SEQUENCE CAMERE_SEQ START WITH 1;
CREATE SEQUENCE VEHICULE_SEQ START WITH 1;
CREATE SEQUENCE TRECERI_VEHICULE_SEQ START WITH 1;
CREATE SEQUENCE STATII_TRANSPORT_SEQ START WITH 1;
CREATE SEQUENCE LINII_TRANSPORT_COMUN_SEQ START WITH 1;
CREATE SEQUENCE TRASEE_STATIE_SEQ START WITH 1;
CREATE SEQUENCE INCIDENTE_SEQ START WITH 1;
CREATE SEQUENCE INTERVENTII_SEQ START WITH 1;
CREATE SEQUENCE ECHIPE_SEQ START WITH 1;
CREATE SEQUENCE REPARTIZARI_SEQ START WITH 1;
CREATE SEQUENCE PERSOANE_SEQ START WITH 1;
CREATE SEQUENCE SESIZARI_SEQ START WITH 1;

--11.Crearea tabelelor în SQL si inserarea de date coerente în fiecare dintre acestea
--(minimum 5 înregistrari în fiecare tabel neasociativ;
--minimum 10 înregistrari în tabelele asociative).

--1. ZONE:

--Creare tabel

CREATE TABLE ZONE(
    id_zona INT DEFAULT ZONE_SEQ.NEXTVAL PRIMARY KEY,
    nume_zona VARCHAR(30)
);

--Aduagare inregistrari

INSERT INTO ZONE (nume_zona) VALUES ('Obor');
INSERT INTO ZONE (nume_zona) VALUES ('Universitatea');
INSERT INTO ZONE (nume_zona) VALUES ('Unirii');
INSERT INTO ZONE (nume_zona) VALUES ('Rahova');
INSERT INTO ZONE (nume_zona) VALUES ('Ferentari');

SELECT * 
FROM ZONE
ORDER BY ID_ZONA;

--2. STRAZI:

--Creare tabel

CREATE TABLE STRAZI (
    id_strada INT DEFAULT STRAZI_SEQ.NEXTVAL PRIMARY KEY,
    id_zona INT,
    nume VARCHAR(30),
    sector INT,
    tip VARCHAR(30),
    FOREIGN KEY (id_zona) REFERENCES ZONE(id_zona)
);

--Aduagare inregistrari

INSERT INTO STRAZI (id_zona, nume, sector, tip) VALUES (28,'Basarab',2,'Rezidential');
INSERT INTO STRAZI (id_zona, nume, sector, tip) VALUES (28,'Zborului',2,'Rezidential');
INSERT INTO STRAZI (id_zona, nume, sector, tip) VALUES (29,'Academiei',1,'Rezidential');
INSERT INTO STRAZI (id_zona, nume, sector, tip) VALUES (29,'Rosetti',1,'Rezidential');
INSERT INTO STRAZI (id_zona, nume, sector, tip) VALUES (29,'Arghezi',1,'Rezidential');
INSERT INTO STRAZI (id_zona, nume, sector, tip) VALUES (30,'Coposu',3,'Bulevard');
INSERT INTO STRAZI (id_zona, nume, sector, tip) VALUES (30,'Concordiei',3,'Rezidential');
INSERT INTO STRAZI (id_zona, nume, sector, tip) VALUES (30,'Liveni',4,'Rezidential');
INSERT INTO STRAZI (id_zona, nume, sector, tip) VALUES (30,'Georgescu',4,'Rezidential');
INSERT INTO STRAZI (id_zona, nume, sector, tip) VALUES (31,'Justitiei',5,'Rezidential');
INSERT INTO STRAZI (id_zona, nume, sector, tip) VALUES (32,'Viilor',5,'Bulevard');
INSERT INTO STRAZI (id_zona, nume, sector, tip) VALUES (32,'Rahovei',5,'Bulevard');
INSERT INTO STRAZI (id_zona, nume, sector, tip) VALUES (28,'Calarasi',3,'Bulevard');
INSERT INTO STRAZI (id_zona, nume, sector, tip) VALUES (31,'Progresului',5,'Rezidential');
INSERT INTO STRAZI (id_zona, nume, sector, tip) VALUES (32,'Sincai',4,'Bulevard');

SELECT *
FROM STRAZI
ORDER BY ID_STRADA;

--3. CAMERE:

--Creare tabel

CREATE TABLE CAMERE (
    id_camera INT DEFAULT CAMERE_SEQ.NEXTVAL PRIMARY KEY,
    id_strada INT,
    tip VARCHAR(30),
    status VARCHAR(30),
    FOREIGN KEY (id_strada) REFERENCES STRAZI(id_strada)
);

--Aduagare inregistrari

INSERT INTO CAMERE (id_strada, tip, status) VALUES (1,'Viteza','Activ');
INSERT INTO CAMERE (id_strada, tip, status) VALUES (1,'Viteza_si_Monitorizare','Inactiv');
INSERT INTO CAMERE (id_strada, tip, status) VALUES (2,'Viteza_si_Monitorizare','Inactiv');
INSERT INTO CAMERE (id_strada, tip, status) VALUES (5,'Viteza','Activ');
INSERT INTO CAMERE (id_strada, tip, status) VALUES (5,'Viteza','Activ');
INSERT INTO CAMERE (id_strada, tip, status) VALUES (7,'Viteza_si_Monitorizare','Inactiv');
INSERT INTO CAMERE (id_strada, tip, status) VALUES (9,'Viteza_si_Monitorizare','Activ');
INSERT INTO CAMERE (id_strada, tip, status) VALUES (10,'Viteza','Inactiv');
INSERT INTO CAMERE (id_strada, tip, status) VALUES (11,'Viteza_si_Monitorizare','Activ');
INSERT INTO CAMERE (id_strada, tip, status) VALUES (11,'Viteza','Inactiv');
INSERT INTO CAMERE (id_strada, tip, status) VALUES (15,'Viteza_si_Monitorizare','Activ');

SELECT *
FROM CAMERE
ORDER BY ID_CAMERA;

--4. VEHICULE:

--Creare tabel

CREATE TABLE VEHICULE(
    id_vehicul INT DEFAULT VEHICULE_SEQ.NEXTVAL PRIMARY KEY,
    tip VARCHAR(30),
    numar_inmatriculare VARCHAR(30)
);

--Aduagare inregistrari

INSERT INTO VEHICULE (tip, numar_inmatriculare) VALUES ('masina','B123XYZ');
INSERT INTO VEHICULE (tip, numar_inmatriculare) VALUES ('autobuz','B945KRX');
INSERT INTO VEHICULE (tip, numar_inmatriculare) VALUES ('camion','B149SML');
INSERT INTO VEHICULE (tip, numar_inmatriculare) VALUES ('masina','B908VYT');
INSERT INTO VEHICULE (tip, numar_inmatriculare) VALUES ('masina','B305VEM');
INSERT INTO VEHICULE (tip, numar_inmatriculare) VALUES ('camion','B573XXC');
INSERT INTO VEHICULE (tip, numar_inmatriculare) VALUES ('camion','B322VFK');
INSERT INTO VEHICULE (tip, numar_inmatriculare) VALUES ('motocicleta','B121DFD');
INSERT INTO VEHICULE (tip, numar_inmatriculare) VALUES ('autobuz','B945KDG');
INSERT INTO VEHICULE (tip, numar_inmatriculare) VALUES ('masina','B345DSF');

SELECT *
FROM VEHICULE
ORDER BY ID_VEHICUL;

--5. TRECERI_VEHICULE:

--Creare tabel

CREATE TABLE TRECERI_VEHICULE (
    id_trecere INT DEFAULT TRECERI_VEHICULE_SEQ.NEXTVAL,
    id_camera INT,
    id_vehicul INT,
    data_trecere DATE,
    viteza INT,
    PRIMARY KEY (id_trecere, id_camera, id_vehicul),
    FOREIGN KEY (id_camera) REFERENCES CAMERE(id_camera),
    FOREIGN KEY (id_vehicul) REFERENCES VEHICULE(id_vehicul)
);

--Aduagare inregistrari

INSERT INTO TRECERI_VEHICULE (id_camera, id_vehicul, data_trecere, viteza)
VALUES (21,1,'20-MAY-2024',60);
INSERT INTO TRECERI_VEHICULE (id_camera, id_vehicul, data_trecere, viteza)
VALUES (21,1,'20-MAY-2024',60);
INSERT INTO TRECERI_VEHICULE (id_camera, id_vehicul, data_trecere, viteza)
VALUES (23,2,'21-MAY-2024',70);
INSERT INTO TRECERI_VEHICULE (id_camera, id_vehicul, data_trecere, viteza)
VALUES (24,2,'21-MAY-2024',70);
INSERT INTO TRECERI_VEHICULE (id_camera, id_vehicul, data_trecere, viteza)
VALUES (25,2,'23-MAY-2024',90);
INSERT INTO TRECERI_VEHICULE (id_camera, id_vehicul, data_trecere, viteza)
VALUES (25,3,'23-MAY-2024',100);
INSERT INTO TRECERI_VEHICULE (id_camera, id_vehicul, data_trecere, viteza)
VALUES (25,3,'23-MAY-2024',100);
INSERT INTO TRECERI_VEHICULE (id_camera, id_vehicul, data_trecere, viteza)
VALUES (27,9,'24-MAY-2024',100);
INSERT INTO TRECERI_VEHICULE (id_camera, id_vehicul, data_trecere, viteza)
VALUES (28,9,'24-MAY-2024',90);
INSERT INTO TRECERI_VEHICULE (id_camera, id_vehicul, data_trecere, viteza)
VALUES (28,9,'24-MAY-2024',80);
INSERT INTO TRECERI_VEHICULE (id_camera, id_vehicul, data_trecere, viteza)
VALUES (28,9,'24-MAY-2024',90);
INSERT INTO TRECERI_VEHICULE (id_camera, id_vehicul, data_trecere, viteza)
VALUES (28,9,'25-MAY-2024',110);
INSERT INTO TRECERI_VEHICULE (id_camera, id_vehicul, data_trecere, viteza)
VALUES (29,9,'25-MAY-2024',120);
INSERT INTO TRECERI_VEHICULE (id_camera, id_vehicul, data_trecere, viteza)
VALUES (29,9,'25-MAY-2024',70);
INSERT INTO TRECERI_VEHICULE (id_camera, id_vehicul, data_trecere, viteza)
VALUES (30,9,'26-MAY-2024',80);
INSERT INTO TRECERI_VEHICULE (id_camera, id_vehicul, data_trecere, viteza)
VALUES (30,10,'27-MAY-2024',60);

SELECT *
FROM TRECERI_VEHICULE
ORDER BY ID_TRECERE;

--6. STATII_TRANSPORT:

--Creare tabel

CREATE TABLE STATII_TRANSPORT (
    id_statie INT DEFAULT STATII_TRANSPORT_SEQ.NEXTVAL PRIMARY KEY,
    id_strada INT,
    nume VARCHAR(30),
    FOREIGN KEY (id_strada) REFERENCES STRAZI(id_strada)
);

--Aduagare inregistrari

INSERT INTO STATII_TRANSPORT (id_strada, nume) VALUES (1,'Basarab');
INSERT INTO STATII_TRANSPORT (id_strada, nume) VALUES (1,'Voda');
INSERT INTO STATII_TRANSPORT (id_strada, nume) VALUES (2,'Circului');
INSERT INTO STATII_TRANSPORT (id_strada, nume) VALUES (4,'Complex_LIDL');
INSERT INTO STATII_TRANSPORT (id_strada, nume) VALUES (4,'Ateneu');
INSERT INTO STATII_TRANSPORT (id_strada, nume) VALUES (4,'Muzeu');
INSERT INTO STATII_TRANSPORT (id_strada, nume) VALUES (5,'TNB');
INSERT INTO STATII_TRANSPORT (id_strada, nume) VALUES (6,'Coral');
INSERT INTO STATII_TRANSPORT (id_strada, nume) VALUES (12,'Patriarhie');
INSERT INTO STATII_TRANSPORT (id_strada, nume) VALUES (12,'Regina_Maria');
INSERT INTO STATII_TRANSPORT (id_strada, nume) VALUES (12,'Progresului');
INSERT INTO STATII_TRANSPORT (id_strada, nume) VALUES (12,'Sebastian');
INSERT INTO STATII_TRANSPORT (id_strada, nume) VALUES (12,'Amurgului');
INSERT INTO STATII_TRANSPORT (id_strada, nume) VALUES (12,'Alexandria');
INSERT INTO STATII_TRANSPORT (id_strada, nume) VALUES (15,'Tineretului');

SELECT *
FROM STATII_TRANSPORT
ORDER BY ID_STATIE;

--7. LINII_TRANSPORT_COMUN:

--Creare tabel

CREATE TABLE LINII_TRANSPORT_COMUN(
    id_linie INT DEFAULT LINII_TRANSPORT_COMUN_SEQ.NEXTVAL PRIMARY KEY,
    tip VARCHAR(30),
    linie INT
);

--Aduagare inregistrari

INSERT INTO LINII_TRANSPORT_COMUN (tip, linie) VALUES ('autobuz','101');
INSERT INTO LINII_TRANSPORT_COMUN (tip, linie) VALUES ('autobuz','102');
INSERT INTO LINII_TRANSPORT_COMUN (tip, linie) VALUES ('troleibuz','81');
INSERT INTO LINII_TRANSPORT_COMUN (tip, linie) VALUES ('troleibuz','82');
INSERT INTO LINII_TRANSPORT_COMUN (tip, linie) VALUES ('tramvai','11');

SELECT *
FROM LINII_TRANSPORT_COMUN
ORDER BY ID_LINIE;

--8. TRASEE_STATIE:

--Creare tabel

CREATE TABLE TRASEE_STATIE (
    id_statie INT,
    id_linie INT,
    ordine INT,
    PRIMARY KEY (id_statie, id_linie),
    FOREIGN KEY (id_statie) REFERENCES STATII_TRANSPORT(id_statie),
    FOREIGN KEY (id_linie) REFERENCES LINII_TRANSPORT_COMUN(id_linie)
);

--Aduagare inregistrari

INSERT INTO TRASEE_STATIE (id_statie, id_linie, ordine) VALUES (1,1,1);
INSERT INTO TRASEE_STATIE (id_statie, id_linie, ordine) VALUES (2,1,2);
INSERT INTO TRASEE_STATIE (id_statie, id_linie, ordine) VALUES (3,1,3);
INSERT INTO TRASEE_STATIE (id_statie, id_linie, ordine) VALUES (4,2,1);
INSERT INTO TRASEE_STATIE (id_statie, id_linie, ordine) VALUES (5,2,2);
INSERT INTO TRASEE_STATIE (id_statie, id_linie, ordine) VALUES (6,2,3);
INSERT INTO TRASEE_STATIE (id_statie, id_linie, ordine) VALUES (7,3,1);
INSERT INTO TRASEE_STATIE (id_statie, id_linie, ordine) VALUES (8,3,2);
INSERT INTO TRASEE_STATIE (id_statie, id_linie, ordine) VALUES (9,3,3);
INSERT INTO TRASEE_STATIE (id_statie, id_linie, ordine) VALUES (10,4,1);
INSERT INTO TRASEE_STATIE (id_statie, id_linie, ordine) VALUES (11,4,2);
INSERT INTO TRASEE_STATIE (id_statie, id_linie, ordine) VALUES (12,4,3);
INSERT INTO TRASEE_STATIE (id_statie, id_linie, ordine) VALUES (13,5,1);
INSERT INTO TRASEE_STATIE (id_statie, id_linie, ordine) VALUES (14,5,2);
INSERT INTO TRASEE_STATIE (id_statie, id_linie, ordine) VALUES (15,5,3);

SELECT *
FROM TRASEE_STATIE
ORDER BY ID_STATIE;

--9. INCIDENTE:

--Creare tabel

CREATE TABLE INCIDENTE (
    id_incident INT DEFAULT INCIDENTE_SEQ.NEXTVAL PRIMARY KEY,
    id_strada INT,
    tip VARCHAR(30),
    data DATE,
    gravitate VARCHAR(30),
    FOREIGN KEY (id_strada) REFERENCES STRAZI(id_strada)
);

--Aduagare inregistrari

INSERT INTO INCIDENTE (id_strada, tip, data, gravitate)
VALUES (1,'incendiu','15-MAY-2020','maxima');
INSERT INTO INCIDENTE (id_strada, tip, data, gravitate)
VALUES (2,'incendiu','23-AUG-2019','medie');
INSERT INTO INCIDENTE (id_strada, tip, data, gravitate)
VALUES (2,'incendiu','13-FEB-2023','medie');
INSERT INTO INCIDENTE (id_strada, tip, data, gravitate)
VALUES (5,'medical','10-JAN-2012','mica');
INSERT INTO INCIDENTE (id_strada, tip, data, gravitate)
VALUES (7,'viol','19-JUN-2014','medie');
INSERT INTO INCIDENTE (id_strada, tip, data, gravitate)
VALUES (8,'medical','23-NOV-2019','maxima');
INSERT INTO INCIDENTE (id_strada, tip, data, gravitate)
VALUES (9,'jaf','29-OCT-2024','mica');
INSERT INTO INCIDENTE (id_strada, tip, data, gravitate)
VALUES (11,'viol','10-DEC-2017','maxima');
INSERT INTO INCIDENTE (id_strada, tip, data, gravitate)
VALUES (15,'incendiu','25-APR-2018','maxima');

SELECT *
FROM INCIDENTE
ORDER BY ID_INCIDENT;

--10. INTERVENTII:

--Creare tabel

CREATE TABLE INTERVENTII(
    id_interventie INT DEFAULT INTERVENTII_SEQ.NEXTVAL PRIMARY KEY,
    data_inceput DATE,
    data_sfarsit DATE
);

--Aduagare inregistrari

INSERT INTO INTERVENTII (data_inceput, data_sfarsit) VALUES ('15-MAY-2020','17-MAY-2020');
INSERT INTO INTERVENTII (data_inceput, data_sfarsit) VALUES ('13-FEB-2023','13-FEB-2023');
INSERT INTO INTERVENTII (data_inceput, data_sfarsit) VALUES ('23-NOV-2019','25-NOV-2019');
INSERT INTO INTERVENTII (data_inceput, data_sfarsit) VALUES ('10-DEC-2017','11-DEC-2017');
INSERT INTO INTERVENTII (data_inceput, data_sfarsit) VALUES ('25-APR-2018','29-APR-2018');

SELECT *
FROM INTERVENTII
ORDER BY ID_INTERVENTIE;

--11. ECHIPE:

--Creare tabel

CREATE TABLE ECHIPE(
    id_echipa INT DEFAULT ECHIPE_SEQ.NEXTVAL PRIMARY KEY,
    tip VARCHAR(30),
    nume_echipa VARCHAR(30)
);

--Aduagare inregistrari

INSERT INTO ECHIPE (tip, nume_echipa) VALUES ('ambulanta','Soimii15');
INSERT INTO ECHIPE (tip, nume_echipa) VALUES ('pompieri','Vulturii98');
INSERT INTO ECHIPE (tip, nume_echipa) VALUES ('pompieri','Lupii24');
INSERT INTO ECHIPE (tip, nume_echipa) VALUES ('politie','Leii05');
INSERT INTO ECHIPE (tip, nume_echipa) VALUES ('politie','Tigrii97');

SELECT *
FROM ECHIPE
ORDER BY ID_ECHIPA;

--12. REPARTIZARI:

--Creare tabel

CREATE TABLE REPARTIZARI (
    id_incident INT,
    id_interventie INT,
    id_echipa INT,
    PRIMARY KEY (id_incident, id_interventie, id_echipa),
    FOREIGN KEY (id_incident) REFERENCES INCIDENTE(id_incident),
    FOREIGN KEY (id_interventie) REFERENCES INTERVENTII(id_interventie),
    FOREIGN KEY (id_echipa) REFERENCES ECHIPE(id_echipa)
);

--Aduagare inregistrari

INSERT INTO REPARTIZARI (id_incident, id_interventie, id_echipa) VALUES (10,1,2);
INSERT INTO REPARTIZARI (id_incident, id_interventie, id_echipa) VALUES (10,1,3);
INSERT INTO REPARTIZARI (id_incident, id_interventie, id_echipa) VALUES (3,2,2);
INSERT INTO REPARTIZARI (id_incident, id_interventie, id_echipa) VALUES (3,2,3);
INSERT INTO REPARTIZARI (id_incident, id_interventie, id_echipa) VALUES (6,3,1);
INSERT INTO REPARTIZARI (id_incident, id_interventie, id_echipa) VALUES (6,3,4);
INSERT INTO REPARTIZARI (id_incident, id_interventie, id_echipa) VALUES (8,4,5);
INSERT INTO REPARTIZARI (id_incident, id_interventie, id_echipa) VALUES (8,4,4);
INSERT INTO REPARTIZARI (id_incident, id_interventie, id_echipa) VALUES (9,5,2);
INSERT INTO REPARTIZARI (id_incident, id_interventie, id_echipa) VALUES (9,5,3);

SELECT *
FROM REPARTIZARI
ORDER BY ID_INCIDENT;

--13. PERSOANE:

--Creare tabel

CREATE TABLE PERSOANE (
    id_persoana INT DEFAULT PERSOANE_SEQ.NEXTVAL PRIMARY KEY,
    id_echipa INT,
    nume VARCHAR(30),
    functie VARCHAR(30),
    FOREIGN KEY (id_echipa) REFERENCES ECHIPE(id_echipa)
);

--Aduagare inregistrari

INSERT INTO PERSOANE (id_echipa, nume, functie) VALUES (1,'Popescu','sef');
INSERT INTO PERSOANE (id_echipa, nume, functie) VALUES (1,'Mihai','paramedic');
INSERT INTO PERSOANE (id_echipa, nume, functie) VALUES (1,'Anca','paramedic');
INSERT INTO PERSOANE (id_echipa, nume, functie) VALUES (2,'Maria','sef');
INSERT INTO PERSOANE (id_echipa, nume, functie) VALUES (2,'George','pompier');
INSERT INTO PERSOANE (id_echipa, nume, functie) VALUES (2,'Anghel','pompier');
INSERT INTO PERSOANE (id_echipa, nume, functie) VALUES (3,'Andreea','sef');
INSERT INTO PERSOANE (id_echipa, nume, functie) VALUES (3,'Radu','pompier');
INSERT INTO PERSOANE (id_echipa, nume, functie) VALUES (3,'Tina','pompier');
INSERT INTO PERSOANE (id_echipa, nume, functie) VALUES (4,'George','sef');
INSERT INTO PERSOANE (id_echipa, nume, functie) VALUES (4,'Paul','politist');
INSERT INTO PERSOANE (id_echipa, nume, functie) VALUES (4,'Matei','politist');
INSERT INTO PERSOANE (id_echipa, nume, functie) VALUES (5,'Luca','sef');
INSERT INTO PERSOANE (id_echipa, nume, functie) VALUES (5,'Elena','politist');
INSERT INTO PERSOANE (id_echipa, nume, functie) VALUES (5,'Mircea','politist');

SELECT *
FROM PERSOANE
ORDER BY ID_PERSOANA;

--14. SESIZARI:

--Creare tabel

CREATE TABLE SESIZARI (
    id_sesizare INT DEFAULT SESIZARI_SEQ.NEXTVAL PRIMARY KEY,
    id_persoana INT,
    tip VARCHAR(30),
    descriere VARCHAR(255),
    data_sesizarii DATE,
    status VARCHAR(30),
    FOREIGN KEY (id_persoana) REFERENCES PERSOANE(id_persoana)
);

--Aduagare inregistrari

INSERT INTO SESIZARI (id_persoana, tip, descriere, data_sesizarii, status)
VALUES (1,'penal','Pacientul a fost injunghiat de mai multe ori','13-FEB-2023','rezolvat');
INSERT INTO SESIZARI (id_persoana, tip, descriere, data_sesizarii, status)
VALUES (1,'neregulamentara','Au fost gasiti gandaci in ambulanta','17-MAY-2023','rezolvat');
INSERT INTO SESIZARI (id_persoana, tip, descriere, data_sesizarii, status)
VALUES (4,'coruptie','Seful a luat mita','27-MAY-2024','nerezolvat');
INSERT INTO SESIZARI (id_persoana, tip, descriere, data_sesizarii, status)
VALUES (4,'penal','Nu are autorizatie de incendiu','30-DEC-2024','rezolvat');
INSERT INTO SESIZARI (id_persoana, tip, descriere, data_sesizarii, status)
VALUES (4,'neregulamentara','Iesirea este blocata','19-NOV-2024','nerezolvat');
INSERT INTO SESIZARI (id_persoana, tip, descriere, data_sesizarii, status)
VALUES (10,'penal','Un om a fost prins la volan sub influenta drogurilor','27-APR-2025','nerezolvat');
INSERT INTO SESIZARI (id_persoana, tip, descriere, data_sesizarii, status)
VALUES (10,'neregulamentara','Nu a platit taxa de drum','19-JAN-2019','nerezolvat');
INSERT INTO SESIZARI (id_persoana, tip, descriere, data_sesizarii, status)
VALUES (10,'penal','Un om a condus fara permis','19-OCT-2018','rezolvat');
INSERT INTO SESIZARI (id_persoana, tip, descriere, data_sesizarii, status)
VALUES (11,'neregulamentara','Nu avem teste pentru droguri','12-NOV-2000','nerezolvat');
INSERT INTO SESIZARI (id_persoana, tip, descriere, data_sesizarii, status)
VALUES (11,'coruptie','Seful a luat mita','15-JUN-2005','nerezolvat');
INSERT INTO SESIZARI (id_persoana, tip, descriere, data_sesizarii, status)
VALUES (13,'neregulamentara','Un vehicul are frane omologate','19-OCT-2009','rezolvat');
INSERT INTO SESIZARI (id_persoana, tip, descriere, data_sesizarii, status)
VALUES (13,'coruptie','Seful a luat mita','13-FEB-2008','nerezolvat');

SELECT *
FROM SESIZARI
ORDER BY ID_SESIZARE;