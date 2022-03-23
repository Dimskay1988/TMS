CREATE TABLE students
(
    id SERIAL PRIMARY KEY,
    firstName CHARACTER VARYING(20) NOT NULL,
    lastName CHARACTER VARYING(20) NOT NULL,
    gender CHARACTER VARYING(10) NOT NULL,
    age INTEGER NOT NULL

);
insert into students (firstName, lastName, gender, age) values ('Dima','Anikeenko', 'Man', 34);

CREATE TABLE audience
(
    id SERIAL PRIMARY KEY,
    name CHARACTER VARYING(20) NOT NULL,
    format CHARACTER VARYING(20) NOT NULL
);
insert into audience (name, format) values ('Z21-onl/Python', 'online');

select audience.name, students.firstName, students.lastName, students.age
from students
join audience on audience.id = students.id
