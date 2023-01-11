INSERT INTO students (first_name, last_name, birthday, course, city)
VALUES
  ('Anna', 'Ivanova', '2005-12-15', 1, 'Minsk'),
  ('Artem', 'Petrov', '2003-08-12', 3, 'Vitebsk'),
  ('Lena', 'Andreeva', '2000-07-01', 5, 'Brest'),
  ('Olga', 'Lesnikova', '2002-06-04',2, 'Mogilev');


INSERT INTO exam_grades (subject_name, grades, exam_date, student_id)
VALUES
  ('Law', 9, '2022-12-15', 1),
  ('Law', 7, '2022-08-12', 3),
  ('Law', 8, '2022-07-01', 2),
  ('Law', 5, '2022-06-04', 4);