CREATE DATABASE egertonapi;

USE egertonapi;

-- creating tables for the database
CREATE TABLE faculties(
  faculty_id unsigned int auto increment not null primary key,
  faculty_name varchar(100),
  total_depts int );

CREATE TABLE departments(
  dept_id unsigned int auto increment not null primary key,
  dept_name varchar(100),
  FOREIGN KEY faculty_id REFERENCES faculties(faculty_id));

CREATE TABLE programmes(
  prog_id unsigned int auto increment not null primary key,
  prog_name varchar(100),
  FOREIGN KEY dept_id REFERENCES departments(dept_id));

-- inserting sample data into the tables
INSERT INTO faculties(faculty_name, total_depts) VALUES(
  "Faculty of Agriculture (FoA)", 4, 
  "Faculty of Arts and Social Sciences (FASS)", 4);

INSERT INTO departments(dept_name, faculty_id) VALUES(
  "Department of Animal Sciences", 1,
  "Department of Dairy, Food Science and Technology", 1,
  "Department of Economics", 2,
  "Department of Literature, Languages and Linguistics", 2);

INSERT INTO programmes(prog_name, dept_id) VALUES(
  "BSC. Animal Science and Technology", 1,
  "MSc. Animal Breeding and Genetics", 1,
  "BSc. in Economics and Sociology", 3,
  "Master of Arts in Economics", 3);



