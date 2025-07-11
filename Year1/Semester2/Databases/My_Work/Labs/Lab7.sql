--EXEMPLU 1
SELECT
    E.DEPARTMENT_ID, SUM(E.SALARY)
FROM EMPLOYEES E
GROUP BY E.DEPARTMENT_ID;

--EX 1
SELECT COUNT(DISTINCT E.MANAGER_ID)
FROM EMPLOYEES E;

--EX2
SELECT EMPLOYEE_ID, LAST_NAME, SALARY
FROM EMPLOYEES
WHERE SALARY > (SELECT AVG(SALARY) FROM EMPLOYEES);

--EX3
SELECT MANAGER_ID, MIN(SALARY)
FROM EMPLOYEES
WHERE MANAGER_ID IS NOT NULL
GROUP BY MANAGER_ID
HAVING MIN(SALARY) >= 4000
ORDER BY MIN(SALARY) DESC;

--EX4
SELECT MAX(MEDIE)
FROM
(SELECT AVG(SALARY) MEDIE
FROM EMPLOYEES
GROUP BY DEPARTMENT_ID);

--SAU
SELECT
    MAX(AVG(SALARY))
FROM EMPLOYEES
GROUP BY DEPARTMENT_ID;

--EX5
SELECT D.DEPARTMENT_NAME, E.JOB_ID, SUM(E.SALARY)
FROM EMPLOYEES E
JOIN DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
WHERE E.DEPARTMENT_ID > 80
GROUP BY D.DEPARTMENT_NAME, E.JOB_ID;

--EX6
SELECT AVG(NVL(E.COMMISSION_PCT*E.SALARY,0))
FROM EMPLOYEES E;

--EX7
SELECT D.DEPARTMENT_ID, D.DEPARTMENT_NAME, COUNT(E.EMPLOYEE_ID)
FROM DEPARTMENTS D
JOIN EMPLOYEES E ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
GROUP BY D.DEPARTMENT_ID, D.DEPARTMENT_NAME
HAVING COUNT(E.EMPLOYEE_ID) < 4;

--EX8
SELECT J.JOB_ID, J.JOB_TITLE, AVG(E.SALARY)
FROM JOBS J
JOIN EMPLOYEES E ON E.JOB_ID = J.JOB_ID
GROUP BY J.JOB_ID, J.JOB_TITLE, J.MIN_SALARY
HAVING AVG(E.SALARY) = MIN(E.SALARY);

--CREATE TABLE nume_tabel_nou AS
--SELECT * FROM alt_tabel
--WHERE conditie;

-- ALTER TABLE table
--     ADD CONSTRAINT pk PRIMARY KEY (id1, id2);
--
-- ALTER TABLE table
--     ADD CONSTRAINT fk FOREIGN KEY (id) REFERENCES entity(id);
--
-- ALTER TABLE table
--     ADD CONSTRAINT fk FOREIGN KEY (id) REFERENCES entity(id);
--
-- ALTER TABLE table
--     ADD CONSTRAINT fk FOREIGN KEY (id) REFERENCES entity(id);

--EX9
SELECT D.DEPARTMENT_NAME, MIN(E.SALARY)
FROM EMPLOYEES E
JOIN DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
GROUP BY D.DEPARTMENT_NAME
HAVING AVG(E.SALARY) = (
    SELECT MAX(AVG_SAL)
    FROM (
             SELECT AVG(SALARY) AS AVG_SAL
             FROM EMPLOYEES
             GROUP BY DEPARTMENT_ID
         )
);

--EX10
SELECT D.DEPARTMENT_ID, D.DEPARTMENT_NAME, COUNT(E.EMPLOYEE_ID), ROUND(AVG(E.SALARY),2), E.FIRST_NAME || ' ' || E.LAST_NAME AS NAME, E.SALARY, E.JOB_ID
FROM DEPARTMENTS D
LEFT JOIN EMPLOYEES E ON D.DEPARTMENT_ID = E.DEPARTMENT_ID
GROUP BY D.DEPARTMENT_ID, D.DEPARTMENT_NAME, E.FIRST_NAME, E.SALARY, E.JOB_ID, E.LAST_NAME;