CREATE TABLE Personnel
(
id int PRIMARY KEY,
Prenom varchar(50) NOT NULL,
Nom varchar(50) NOT NULL,
DateEmbauche varchar(50) NOT NULL,
DateSortie date,
Superviseur int FOREIGN KEY REFERENCES Personnel(id),
CONSTRAINT UQ_PERSONNEL UNIQUE (Prenom,Nom)
);

CREATE TABLE Vehicule
(
Num_Chassis varchar(17) PRIMARY KEY,
Immat varchar(20) NOT NULL,
Couleur varchar(20) NOT NULL,
Contenance varchar(20) NOT NULL
);

CREATE TABLE Chauffeur
(
Personnel int FOREIGN KEY REFERENCES Personnel(id),
Type_Permis varchar(50) NOT NULL,
Date_Permis varchar(50) NOT NULL,
Date_Embauche varchar(50) NOT NULL,
CONSTRAINT PK_CHAUFFEUR PRIMARY KEY (Personnel)
);

CREATE TABLE Conducteur
(
Vehicule varchar(17) FOREIGN KEY REFERENCES Vehicule(Num_Chassis),
Chauffeur int FOREIGN KEY REFERENCES Chauffeur(Personnel),
CONSTRAINT PK_CONDUCTEUR PRIMARY KEY (Vehicule,Chauffeur)
);

CREATE TABLE Zone
(
Nom varchar(50) PRIMARY KEY,
Description text NOT NULL,
);

CREATE TABLE Type_Collecte
(
Mnemonique varchar(10) PRIMARY KEY,
Description text NOT NULL
);

CREATE TABLE Planning_Collecte
(
Id int PRIMARY KEY,
date date NOT NULL,
Vehicule varchar(17) NOT NULL FOREIGN KEY REFERENCES Vehicule(Num_Chassis),
Chauffeur int NOT NULL FOREIGN KEY REFERENCES Chauffeur(Personnel),
Zone varchar(50) NOT NULL FOREIGN KEY REFERENCES Zone(nom)
);

CREATE TABLE Planning_Type
(
Collecte int FOREIGN KEY REFERENCES Planning_Collecte(Id),
Type_Collecte varchar(10) FOREIGN KEY REFERENCES Type_Collecte(Mnemonique),
CONSTRAINT PK_PLANNING_TYPE PRIMARY KEY (Collecte,Type_Collecte)
);