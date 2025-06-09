--12) Formulați în limbaj natural și implementați 5 cereri SQL complexe ce vor utiliza,
-- în ansamblul lor, următoarele elemente:
--a) subcereri sincronizate în care intervin cel puțin 3 tabele
--b) subcereri nesincronizate în clauza FROM
--c) grupări de date, funcții grup, filtrare la nivel de grupuri cu
-- subcereri nesincronizate (în clauza de HAVING) în care intervin cel puțin 3 tabele (in cadrul aceleiași cereri)
--d) ordonări și utilizarea funcțiilor NVL și DECODE (în cadrul aceleiași cereri)
--e) utilizarea a cel puțin 2 funcții pe șiruri de caractere,
-- 2 funcții pe date calendaristice, a cel puțin unei expresii CASE
--f) utilizarea a cel puțin 1 bloc de cerere (clauza WITH)

--Observație: Într-o cerere se vor regăsi mai multe elemente dintre cele enumerate
-- mai sus, astfel încât cele 5 cereri să le cuprindă pe toate


--Cererea 1:

--Afișează numele străzilor și zona în care se află,
-- pentru care camerele de viteză au detectat mai mult de 2 trecere de vehicule
-- cu viteza medie peste 60 km/h. Se vor afișa și: viteza medie, numărul total de treceri.

--Rezolvare:

SELECT Z.NUME_ZONA,
       S.NUME                  AS NUME_STRADA,
       ROUND(AVG(T.VITEZA), 2) AS VITEZA_MEDIE,
       COUNT(*)                AS NUMAR_TRECERI
FROM TRECERI_VEHICULE T
         JOIN CAMERE C ON T.ID_CAMERA = C.ID_CAMERA
         JOIN STRAZI S ON C.ID_STRADA = S.ID_STRADA
         JOIN ZONE Z ON S.ID_ZONA = Z.ID_ZONA
GROUP BY Z.NUME_ZONA, S.NUME
HAVING COUNT(*) > 2
   AND AVG(T.VITEZA) > (SELECT AVG(VITEZA)
                        FROM TRECERI_VEHICULE
                        WHERE VITEZA > 60);

--S-au respectat subpunctele: a, c

--Cererea 2:

--Afișează toate sesizările cu status nesoluționat (nerezolvat), împreună cu numele persoanei
-- care le-a făcut, funcția, numele echipei din care face parte, ziua săptămânii în care
-- a fost făcută sesizarea și o etichetă automată (ex: “Urgent” dacă tipul sesizării e “Penal”
-- și “Ne-urgent” altfel). Ordonează rezultatul după data sesizării descrescător și folosește funcții
-- pe șiruri, calendaristice, NVL, DECODE.

--Rezolvare:

WITH SESIZARI_ACTIVE AS (SELECT S.ID_SESIZARE,
                                S.TIP,
                                S.DESCRIERE,
                                S.DATA_SESIZARII,
                                S.STATUS,
                                P.NUME AS NUME_PERSOANA,
                                P.FUNCTIE,
                                E.NUME_ECHIPA
                         FROM SESIZARI S
                                  JOIN PERSOANE P ON S.ID_PERSOANA = P.ID_PERSOANA
                                  JOIN ECHIPE E ON P.ID_ECHIPA = E.ID_ECHIPA
                         WHERE NVL(S.STATUS, 'nerezolvat') = 'nerezolvat')

SELECT SA.ID_SESIZARE,
       INITCAP(SA.NUME_PERSOANA)                      AS NUME_PERSOANA,
       UPPER(SA.FUNCTIE)                              AS FUNCTIE,
       LOWER(SA.NUME_ECHIPA)                          AS NUME_ECHIPA,
       TO_CHAR(SA.DATA_SESIZARII, 'DAY')              AS ZI_SEMNALARE,
       DECODE(SA.TIP, 'penal', 'URGENT', 'NE-URGENT') AS PRIORITATE
FROM SESIZARI_ACTIVE SA
ORDER BY SA.DATA_SESIZARII DESC;

--S-au respectat subpunctele: d, f

--Cererea 3:

--Afișarea vehiculelor care au trecut prin camere și clasificarea lor după tipul vehiculului și ziua trecerii.

--Rezolvare:

SELECT V.ID_VEHICUL,
       INITCAP(V.TIP)                    AS TIP_VEHICUL,
       UPPER(V.NUMAR_INMATRICULARE)      AS NUMAR,
       TV.DATA_TRECERE,
       EXTRACT(DAY FROM TV.DATA_TRECERE) AS ZI_LUNA,
       CASE
           WHEN TO_CHAR(TV.DATA_TRECERE, 'D') IN ('1', '7') THEN 'WEEKEND'
           ELSE 'ZI DE LUCRU'
           END                           AS ZI_TIP
FROM (SELECT *
      FROM TRECERI_VEHICULE) TV
         JOIN VEHICULE V ON TV.ID_VEHICUL = V.ID_VEHICUL
ORDER BY TV.DATA_TRECERE DESC;

--S-au respectat subpunctele: b, e

--Cererea 4:

--Pentru fiecare linie de transport, sa se afiseze codul format din concatenarea tipului
-- și numărului liniei, numărul total de stații de pe traseu, numele primei și ultimei stații
-- (după ordinea din traseu), și o descriere a tipului folosind decode: tramvai devine ELECTRIC,
-- troleibuz devine MOTORINA, altfel NECUNOSCUT. Rezultatele se vor ordona crescător după tipul descris
-- și descrescător după numărul de stații.

--Rezolvare:

SELECT L.ID_LINIE,
       L.TIP || '-' || L.LINIE            AS COD_LINIE,
       COUNT(TS.ID_STATIE)                AS NR_STATII,
       NVL(PS.NUME, 'STATIE NECUNOSCUTA') AS PRIMA_STATIE,
       NVL(US.NUME, 'STATIE NECUNOSCUTA') AS ULTIMA_STATIE,
       DECODE(L.TIP,
              'tramvai', 'ELECTRIC',
              'autobuz', 'MOTORINA',
              'NECUNOSCUT')               AS TIP_DESCRIS
FROM LINII_TRANSPORT_COMUN L
         JOIN TRASEE_STATIE TS ON L.ID_LINIE = TS.ID_LINIE
         JOIN STATII_TRANSPORT S ON TS.ID_STATIE = S.ID_STATIE
         LEFT JOIN (SELECT T1.ID_LINIE, T1.ID_STATIE
                    FROM TRASEE_STATIE T1
                    WHERE T1.ORDINE = 1) PS_IDX ON L.ID_LINIE = PS_IDX.ID_LINIE
         LEFT JOIN STATII_TRANSPORT PS ON PS_IDX.ID_STATIE = PS.ID_STATIE
         LEFT JOIN (SELECT T2.ID_LINIE, T2.ID_STATIE
                    FROM TRASEE_STATIE T2
                    WHERE T2.ORDINE = (SELECT MAX(T3.ORDINE)
                                       FROM TRASEE_STATIE T3
                                       WHERE T3.ID_LINIE = T2.ID_LINIE)) US_IDX ON L.ID_LINIE = US_IDX.ID_LINIE
         LEFT JOIN STATII_TRANSPORT US ON US_IDX.ID_STATIE = US.ID_STATIE
GROUP BY L.ID_LINIE, L.TIP, L.LINIE, PS.NUME, US.NUME
ORDER BY TIP_DESCRIS,
         NR_STATII DESC;

--S-au respectat subpunctele: b, d

--Cererea 5:

--Afișează pentru fiecare stradă, numele, numărul de camere, numărul de stații,
-- lungimea numelui și un tip de zonă („MIXTA” dacă are și camere și stații, altfel „NEDEFINIT”).

--Rezolvare:

SELECT INITCAP(NVL(C.NUME, STRS.NUME)) AS NUME_STRADA,
       NVL(C.NR_CAMERE, 0)             AS NUMAR_CAMERE,
       NVL(S.NR_STATII, 0)             AS NUMAR_STATII,
       LENGTH(NVL(C.NUME, STRS.NUME))  AS LUNGIME_NUME,
       CASE
           WHEN NVL(C.NR_CAMERE, 0) > 0 AND NVL(S.NR_STATII, 0) > 0 THEN 'MIXTA'
           ELSE 'NEDEFINIT'
           END                         AS TIP_ZONA
FROM (SELECT STR.ID_STRADA, STR.NUME, COUNT(*) AS NR_CAMERE
      FROM STRAZI STR
               JOIN CAMERE CA ON STR.ID_STRADA = CA.ID_STRADA
      GROUP BY STR.ID_STRADA, STR.NUME) C
         FULL OUTER JOIN
     (SELECT ID_STRADA, COUNT(*) AS NR_STATII
      FROM STATII_TRANSPORT
      GROUP BY ID_STRADA) S
     ON C.ID_STRADA = S.ID_STRADA
         LEFT JOIN STRAZI STRS
                   ON STRS.ID_STRADA = NVL(C.ID_STRADA, S.ID_STRADA);

--S-au respectat subpunctele: a, b

--13) Implementarea a 3 operații de actualizare și de suprimare a datelor utilizând subcereri.

--1) Schimbă statusul camerelor inactive de pe străzile fără incidente

--Rezolvare:

UPDATE CAMERE
SET STATUS = 'Inactiv'
WHERE ID_STRADA IN (SELECT ID_STRADA
                    FROM STRAZI
                    WHERE ID_STRADA NOT IN (SELECT DISTINCT ID_STRADA
                                            FROM INCIDENTE));

--2) Șterge toate sesizările făcute de persoane care au funcția sef și fac parte din echipa de tip pompieri.

--Rezolvare:

DELETE
FROM SESIZARI
WHERE ID_PERSOANA IN (SELECT P.ID_PERSOANA
                      FROM PERSOANE P
                               JOIN ECHIPE E ON P.ID_ECHIPA = E.ID_ECHIPA
                      WHERE P.FUNCTIE = 'sef'
                        AND E.TIP = 'pompieri');

--3) Toate camioanele care nu au depasit limita de viteza devin camion_electric

--Rezolvare:

UPDATE VEHICULE
SET TIP = 'camion_electric'
WHERE TIP = 'camion'
  AND ID_VEHICUL NOT IN (SELECT DISTINCT ID_VEHICUL
                         FROM TRECERI_VEHICULE);


--14) Crearea unei vizualizări complexe. Dați un exemplu de operație LMD permisă pe
-- vizualizarea respectivă și un exemplu de operație LMD nepermisă.

--VIEW-UL

CREATE VIEW V_SESIZARI_PERSOANE AS
SELECT S.ID_SESIZARE,
       S.TIP  AS TIP_SESIZARE,
       S.DESCRIERE,
       S.STATUS,
       S.DATA_SESIZARII,
       P.ID_PERSOANA,
       P.NUME AS NUME_PERSOANA,
       P.FUNCTIE,
       E.ID_ECHIPA,
       E.NUME_ECHIPA,
       E.TIP  AS TIP_ECHIPA
FROM SESIZARI S
         JOIN PERSOANE P ON S.ID_PERSOANA = P.ID_PERSOANA
         JOIN ECHIPE E ON P.ID_ECHIPA = E.ID_ECHIPA;

--LMD PERMIS:

UPDATE V_SESIZARI_PERSOANE
SET STATUS = 'rezolvat'
WHERE ID_SESIZARE = 9;

--LMD NEPERMIS:

INSERT INTO V_SESIZARI_PERSOANE (ID_SESIZARE, TIP_SESIZARE, DESCRIERE, STATUS, DATA_SESIZARII,
                                 ID_PERSOANA, NUME_PERSOANA, FUNCTIE, ID_ECHIPA, NUME_ECHIPA, TIP_ECHIPA)
VALUES (999, 'coruptie', 'cineva a primit mita', 'nerezolvat',
        SYSDATE, 24, 'Simi', 'politist',
        7, 'EchipaSOC', 'politie');

--15) Formulați în limbaj natural și implementați în SQL: o cerere ce utilizează operația
-- outerjoin pe minimum 4 tabele, o cerere ce utilizează operația division și o
-- cerere care implementează analiza top-n.

--Observație: Cele 3 cereri sunt diferite de cererile de la exercițiul 12.

--Cerere 1 OUTER JOIN (LEFT):

-- Afișează toate sesizările, cu detalii precum numele persoanei,
-- echipa din care face parte și descrierea sesizării.

--Rezolvare:

SELECT S.ID_SESIZARE,
       S.DESCRIERE,
       P.NUME AS NUME_PERSOANA,
       P.FUNCTIE,
       E.NUME_ECHIPA,
       I.TIP  AS TIP_INCIDENT
FROM SESIZARI S
         LEFT JOIN PERSOANE P ON S.ID_PERSOANA = P.ID_PERSOANA
         LEFT JOIN ECHIPE E ON P.ID_ECHIPA = E.ID_ECHIPA
         LEFT JOIN REPARTIZARI R ON R.ID_ECHIPA = E.ID_ECHIPA
         LEFT JOIN INCIDENTE I ON R.ID_INCIDENT = I.ID_INCIDENT;

--Cerere 2 DIVISION:

--Afișează toate vehiculele care au trecut prin toate camerele de pe strada cu ID = 5.

--Rezolvare:

SELECT V.ID_VEHICUL, V.NUMAR_INMATRICULARE
FROM VEHICULE V
WHERE EXISTS (SELECT 1
              FROM TRECERI_VEHICULE T
                       JOIN CAMERE C ON C.ID_CAMERA = T.ID_CAMERA
              WHERE T.ID_VEHICUL = V.ID_VEHICUL
                AND C.ID_STRADA = 5)
  AND NOT EXISTS (SELECT *
                  FROM (SELECT C.ID_CAMERA
                        FROM CAMERE C
                        WHERE C.ID_STRADA = 5) CAMERE_STRADA
                           CROSS JOIN (SELECT V2.ID_VEHICUL
                                       FROM VEHICULE V2
                                       WHERE V2.ID_VEHICUL = V.ID_VEHICUL) VEHICUL_SELECTAT
                  MINUS
                  SELECT T.ID_CAMERA, T.ID_VEHICUL
                  FROM TRECERI_VEHICULE T
                  WHERE T.ID_VEHICUL = V.ID_VEHICUL);

--Cerere 3 TOP-N:

--Afișează cele mai recente 3 sesizări înregistrate, împreună cu numele persoanei care le-a făcut și data sesizării.

--Rezolvare:

SELECT *
FROM (SELECT S.ID_SESIZARE,
             S.DESCRIERE,
             S.DATA_SESIZARII,
             P.NUME AS NUME_PERSOANA
      FROM SESIZARI S
               JOIN PERSOANE P ON S.ID_PERSOANA = P.ID_PERSOANA
      ORDER BY S.DATA_SESIZARII DESC)
WHERE ROWNUM <= 3;



ROLLBACK;

--STRAZI SI NR TOTAL DE INCIDENTE DE GRAV MAXIMA PE ACEA STRADA, DIN 2018

SELECT S.NUME AS NUME_STRADA,
       Z.NUME_ZONA,
       MAX_INCIDENTE.NR_INCIDENTE_MAXIMA
FROM STRAZI S
         JOIN ZONE Z ON S.ID_ZONA = Z.ID_ZONA
         JOIN (SELECT I.ID_STRADA,
                      COUNT(*) AS NR_INCIDENTE_MAXIMA
               FROM INCIDENTE I
               WHERE GRAVITATE = 'maxima'
                 AND TRUNC(DATA, 'YYYY') = DATE '2018-01-01'
               GROUP BY I.ID_STRADA) MAX_INCIDENTE ON S.ID_STRADA = MAX_INCIDENTE.ID_STRADA
WHERE Z.ID_ZONA IN (SELECT S2.ID_ZONA
                    FROM STRAZI S2
                             JOIN INCIDENTE I2 ON S2.ID_STRADA = I2.ID_STRADA
                    WHERE I2.GRAVITATE = 'maxima'
                    GROUP BY S2.ID_ZONA);