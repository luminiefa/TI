CREATE TABLE Personnel
(
id int PRIMARY KEY,
Prenom varchar(50) NOT NULL,
Nom varchar(50) NOT NULL,
DateEmbauche varchar(50) NOT NULL,
DateSortie varchar(50),
Superviseur int FOREIGN KEY REFERENCES Personnel(id)
);

CREATE TABLE Chauffeur
(
Personnel int FOREIGN KEY REFERENCES Personnel(id),
Type_Permis varchar(50),
Date_Permis varchar(50),
Date_Embauche varchar(50),
CONSTRAINT PK_CHAUFFEUR PRIMARY KEY (Personnel)
);

CREATE TABLE Vehicule
(
Num_Chassis int PRIMARY KEY,
Immat varchar(50),
Couleur varchar(50),
Contenance int
);

CREATE TABLE Conducteur
(
Vehicule int FOREIGN KEY REFERENCES Vehicule(Num_Chassis),
Chauffeur int FOREIGN KEY REFERENCES Chauffeur(Personnel),
CONSTRAINT PK_CONDUCTEUR PRIMARY KEY (Vehicule,Chauffeur)
);


CREATE TABLE Zone
(
Nom varchar(50) PRIMARY KEY,
Description varchar(50)
);

CREATE TABLE Type_Collecte
(
Mnemonique varchar(50) PRIMARY KEY,
Description varchar(50)
);

CREATE TABLE Planning_Collecte
(
Id int PRIMARY KEY,
date varchar(50),
Vehicule int FOREIGN KEY REFERENCES Vehicule(Num_Chassis),
Chauffeur int FOREIGN KEY REFERENCES Chauffeur(Personnel),
Zone varchar(50) FOREIGN KEY REFERENCES Zone(nom)
);

CREATE TABLE Planning_Type
(
Collecte varchar(50) FOREIGN KEY REFERENCES Type_Collecte(Mnemonique),
Type_Collecte int FOREIGN KEY REFERENCES Type_Collecte(Mnemonique),
CONSTRAINT PK_PLANNING_TYPE PRIMARY KEY (Collecte,Chauffeur)
);