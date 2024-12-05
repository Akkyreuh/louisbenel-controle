SELECT Students.student_id, Students.name, Courses.course_name, Courses.credits FROM Students JOIN Enrollments ON Students.student_id = Enrollments.student_id JOIN Courses ON Enrollments.course_id = Courses.course_id;

SELECT Students.student_id, Students.name FROM Students LEFT JOIN Enrollments ON Students.student_id = Enrollments.student_id WHERE Enrollments.student_id IS NULL;


-- //  4

SELECT Courses.course_id, Courses.course_name, COUNT(Enrollments.student_id) FROM Courses LEFT JOIN Enrollments ON Courses.course_id = Enrollments.course_id GROUP BY Courses.course_id;

SELECT Courses.course_id, Courses.course_name, COUNT(Enrollments.student_id) AS num_enrolled, Courses.capacity FROM Courses JOIN Enrollments ON Courses.course_id = Enrollments.course_id GROUP BY Courses.course_id, Courses.course_name, Courses.capacity HAVING COUNT(Enrollments.student_id) > Courses.capacity / 2;

-- // QUERY 5 : 

pas fini

SELECT Students.student_id, Students.name, COUNT(Enrollments.course_id) AS num_courses FROM Students JOIN Enrollments ON Students.student_id = Enrollments.student_id GROUP BY Students.student_id

-- QUERY 6 

SELECT Students.student_id, Students.name, SUM(Courses.credits) AS total_credits FROM Students JOIN Enrollments ON Students.student_id = Enrollments.student_id JOIN Courses ON Enrollments.course_id = Courses.course_id GROUP BY Students.student_id;


-- QUERY 7

SELECT Courses.course_id, Courses.course_name FROM Courses LEFT JOIN Enrollments ON Courses.course_id = Enrollments.course_id WHERE Enrollments.student_id IS NULL;

-- TASK 6 :

élément non appris

