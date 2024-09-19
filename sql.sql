CREATE DATABASE Ecole;

\c Ecole;

CREATE TABLE eleves (
    student_id SERIAL PRIMARY KEY,
    prenom VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    numero_salle VARCHAR(20),
    telephone VARCHAR(15) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE,
    annee_obtention INT NOT NULL,
    numero_classe INT NOT NULL
);

CREATE TABLE enseignants (
    teacher_id SERIAL PRIMARY KEY,
    prenom VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    numero_salle VARCHAR(20),
    departement VARCHAR(50),
    annee_obtention INT NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telephone VARCHAR(15) UNIQUE NOT NULL,
    numero_classe INT NOT NULL
);
