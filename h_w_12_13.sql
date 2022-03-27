DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS audience;

CREATE TABLE audience
(
    id_group SERIAL PRIMARY KEY,
    name CHARACTER VARYING(20) NOT NULL,
    format CHARACTER VARYING(20) NOT NULL
);

insert into audience (name, format) values ('Z21-onl/Python', 'online');
insert into audience (name, format) values ('H23-onl/JS', 'online');

CREATE TABLE students
(
    id SERIAL PRIMARY KEY,
    firstName CHARACTER VARYING(20) NOT NULL,
    lastName CHARACTER VARYING(20) NOT NULL,
    gender CHARACTER VARYING(10) NOT NULL,
    age INTEGER NOT NULL,
    audience_id INTEGER,
    FOREIGN KEY (audience_id) REFERENCES audience(id_group) ON DELETE SET NULL
);

insert into students (firstName, lastName, gender, age, audience_id) values ('Dima','Anikeenko', 'Man', 34, 1);
insert into students (firstName, lastName, gender, age, audience_id) values ('Ivan','Ivanov', 'Man', 26, 2);
insert into students (firstName, lastName, gender, age, audience_id) values ('Kirill','Overin', 'Man', 43, 1);
insert into students (firstName, lastName, gender, age, audience_id) values ('Dima','Zuk', 'Man', 29, 1);
insert into students (firstName, lastName, gender, age, audience_id) values ('Oleg','Luganov', 'Man', 37, 2);


select students.audience_id,audience.name, students.firstName, students.lastName, students.age
from students
join audience on audience.id_group = students.id
