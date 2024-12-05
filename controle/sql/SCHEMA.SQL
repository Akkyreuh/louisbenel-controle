CREATE TABLE Students ( student_id INTEGER PRIMARY KEY, name VARCHAR(50), age INT, gender VARCHAR(10) );

CREATE TABLE Courses ( course_id INTEGER PRIMARY KEY, course_name VARCHAR(50), credits INT, capacity INT );

CREATE TABLE Enrollments ( enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER, course_id INTEGER, FOREIGN KEY (student_id) REFERENCES Students(student_id), FOREIGN KEY (course_id) REFERENCES Courses(course_id) );