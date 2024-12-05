INSERT INTO Students (student_id, name, age, gender) VALUES
(1, 'Louis', 22, 'M'),
(2, 'Noah', 21, 'M'),
(3, 'Thomas', 23, 'M'),
(4, 'Sophie', 20, 'F'),
(5, 'Camille', 22, 'M');

INSERT INTO Courses (course_id, course_name, credits, capacity) VALUES
(1, 'Python', 3, 5),
(2, 'Django', 4, 4),
(3, 'SQL', 2, 6),
(4, 'PHP', 3, 5);

INSERT INTO Enrollments (student_id, course_id) VALUES
(1, 1),
(1, 3),
(2, 2),
(3, 3),
(3, 4),
(4, 1),
(5, 4),
(5, 2);