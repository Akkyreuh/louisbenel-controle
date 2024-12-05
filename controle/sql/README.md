
README - Base de données étudiants et cours

Ce fichier explique le schéma de la base de données, les données d'exemple et les requêtes SQL associées.

----------------------
1. Schéma de la base de données
----------------------

La base de données est composée de trois tables : 

1. **Students** (Étudiants) :
   - **student_id** (INTEGER) : Identifiant unique de l'étudiant.
   - **name** (VARCHAR(50)) : Nom de l'étudiant.
   - **age** (INTEGER) : Âge de l'étudiant.
   - **gender** (VARCHAR(10)) : Sexe de l'étudiant (M ou F).

2. **Courses** (Cours) :
   - **course_id** (INTEGER) : Identifiant unique du cours.
   - **course_name** (VARCHAR(50)) : Nom du cours.
   - **credits** (INTEGER) : Nombre de crédits associés au cours.
   - **capacity** (INTEGER) : Capacité maximale d'inscription au cours.

3. **Enrollments** (Inscriptions) :
   - **enrollment_id** (INTEGER) : Identifiant unique de l'inscription.
   - **student_id** (INTEGER) : Identifiant de l'étudiant inscrit (clé étrangère vers la table Students).
   - **course_id** (INTEGER) : Identifiant du cours suivi (clé étrangère vers la table Courses).

----------------------
2. Données d'exemple
----------------------

Les tables sont peuplées avec les données suivantes :

**Students** (Étudiants) :

| student_id | name    | age | gender |
|------------|---------|-----|--------|
| 1          | Louis   | 22  | M      |
| 2          | Noah    | 21  | M      |
| 3          | Thomas  | 23  | M      |
| 4          | Sophie  | 20  | F      |
| 5          | Camille | 22  | M      |

**Courses** (Cours) :

| course_id | course_name | credits | capacity |
|-----------|-------------|---------|----------|
| 1         | Python      | 3       | 5        |
| 2         | Django      | 4       | 4        |
| 3         | SQL         | 2       | 6        |
| 4         | PHP         | 3       | 5        |

**Enrollments** (Inscriptions) :

| enrollment_id | student_id | course_id |
|---------------|------------|-----------|
| 1             | 1          | 1         |
| 2             | 1          | 3         |
| 3             | 2          | 2         |
| 4             | 3          | 3         |
| 5             | 3          | 4         |
| 6             | 4          | 1         |
| 7             | 5          | 4         |
| 8             | 5          | 2         |

----------------------
3. Requêtes SQL
----------------------

Voici les requêtes SQL permettant d'extraire différentes informations de la base de données :

1. **Liste des étudiants inscrits à des cours :**
```sql
SELECT Students.student_id, Students.name, Courses.course_name, Courses.credits 
FROM Students 
JOIN Enrollments ON Students.student_id = Enrollments.student_id 
JOIN Courses ON Enrollments.course_id = Courses.course_id;
```

2. **Liste des étudiants non inscrits à un cours :**
```sql
SELECT Students.student_id, Students.name 
FROM Students 
LEFT JOIN Enrollments ON Students.student_id = Enrollments.student_id 
WHERE Enrollments.student_id IS NULL;
```

3. **Nombre d'étudiants inscrits par cours :**
```sql
SELECT Courses.course_id, Courses.course_name, COUNT(Enrollments.student_id) 
FROM Courses 
LEFT JOIN Enrollments ON Courses.course_id = Enrollments.course_id 
GROUP BY Courses.course_id;
```

4. **Cours ayant plus de la moitié de leur capacité d'inscription atteinte :**
```sql
SELECT Courses.course_id, Courses.course_name, COUNT(Enrollments.student_id) AS num_enrolled, Courses.capacity 
FROM Courses 
JOIN Enrollments ON Courses.course_id = Enrollments.course_id 
GROUP BY Courses.course_id, Courses.course_name, Courses.capacity 
HAVING COUNT(Enrollments.student_id) > Courses.capacity / 2;
```

5. **Nombre de cours suivis par chaque étudiant :**
```sql
SELECT Students.student_id, Students.name, COUNT(Enrollments.course_id) AS num_courses 
FROM Students 
JOIN Enrollments ON Students.student_id = Enrollments.student_id 
GROUP BY Students.student_id;
```

6. **Total des crédits accumulés par chaque étudiant :**
```sql
SELECT Students.student_id, Students.name, SUM(Courses.credits) AS total_credits 
FROM Students 
JOIN Enrollments ON Students.student_id = Enrollments.student_id 
JOIN Courses ON Enrollments.course_id = Courses.course_id 
GROUP BY Students.student_id;
```

7. **Cours sans étudiants inscrits :**
```sql
SELECT Courses.course_id, Courses.course_name 
FROM Courses 
LEFT JOIN Enrollments ON Courses.course_id = Enrollments.course_id 
WHERE Enrollments.student_id IS NULL;
```

----------------------
4. Conclusion
----------------------

Ce fichier fournit une vue d'ensemble de la base de données des étudiants, des cours et des inscriptions. Vous pouvez adapter et étendre ces requêtes pour répondre à des besoins spécifiques d'analyse ou de gestion des données dans votre projet.
