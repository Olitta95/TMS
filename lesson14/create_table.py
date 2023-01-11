CREATE TABLE students(
 id serial PRIMARY KEY,
 first_name VARCHAR(30) NOT NULL,
 last_name VARCHAR(30) NOT NULL,
 birthday date NOT NULL,
 course INTEGER NOT NULL,
 city TEXT
);


CREATE TABLE exam_grades(
 exam_id serial PRIMARY KEY,
 subject_name varchar(40),
 grades integer,
 exam_date date,
 student_id integer,
 FOREIGN KEY(student_id)
 REFERENCES students(id)
);