
/*SCRIPTS CREATION*/

CREATE DATABASE exercice1;
CREATE DATABASE exercice2;

GO
--permet de lancer les premieres lignes avant de continuer (sinon probleme d'existance des DB)

USE exercice1;
-- pour utiliser la bonne BD
CREATE TABLE PAYS (
Nom varchar(30) PRIMARY KEY
);
CREATE TABLE MARQUE (
Nom varchar(30) PRIMARY KEY,
Origine varchar(30) not null,
FOREIGN KEY (Origine) REFERENCES PAYS(Nom)
);
CREATE TABLE MODELE (
Nom varchar(30) PRIMARY KEY,
Marque varchar(30) not null,
FOREIGN KEY (Marque) REFERENCES MARQUE(Nom)
);
CREATE TABLE PERSONNE (
Id int PRIMARY KEY,
Nom varchar(30) not null,
Prenom varchar(30) not null,
Email varchar(100) not null,
telephone varchar(20) not null,
marie int,
FOREIGN KEY (marie) REFERENCES PERSONNE(Id)
);
CREATE TABLE VOITURE (
NumChassis varchar(30) PRIMARY KEY,
Immat varchar(15) not null,
Modele varchar(30) not null,
proprio int not null,
FOREIGN KEY (Modele) REFERENCES MODELE(Nom),
FOREIGN KEY (Proprio) REFERENCES PERSONNE(Id)
);
CREATE TABLE CONDUCTEUR (
Conducteur int,
Voiture varchar(30),
PRIMARY KEY (Conducteur, Voiture),
FOREIGN KEY (Conducteur) REFERENCES PERSONNE(Id),
FOREIGN KEY (Voiture) REFERENCES VOITURE(NumChassis));

use exercice2;
-- pour utiliser la bonne BD
create table EMPLOYE (
NumId int primary key,
Prenom varchar(30) not null,
Nom varchar(30) not null,
Adresse varchar(100),
Telephone varchar(20) not null,
DateArrivee date not null,
DateSortie date) ;

create table CHEF(
Employe int primary key,
DateArrivee date not null,
DateSortie date,
foreign key (Employe) REFERENCES employe(NumId));

create table GARDIEN(
Employe int primary key,
DateArrivee date not null,
DateSortie date,
foreign key (Employe) REFERENCES employe(NumId));

create table secteur(
numero int primary key,
nom varchar(30) not null,
Description varchar(200) not null,
chef int not null,
foreign key (chef) references chef(employe));

create table parcelle(
numero int primary key,
nom varchar(30) not null,
Description varchar(200) not null,
gardien int not null,
secteur int not null,
foreign key (gardien) references gardien(employe),
foreign key (secteur) references secteur(numero));

GO
