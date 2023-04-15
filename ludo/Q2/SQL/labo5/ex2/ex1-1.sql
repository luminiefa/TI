CREATE TABLE pays
(
Nom varchar(50) PRIMARY KEY
);

CREATE TABLE Marque
(
nom varchar(50) PRIMARY KEY,
Origine varchar(50) NOT NULL FOREIGN KEY REFERENCES Pays(nom)
);

CREATE TABLE Modele
(
nom varchar(50) PRIMARY KEY,
Marque varchar(50) NOT NULL FOREIGN KEY REFERENCES Marque(nom)
);

CREATE TABLE Personne
(
Id int PRIMARY KEY,
Nom varchar(50) NOT NULL,
Prenom varchar(50) NOT NULL,
Email varchar(150) NOT NULL,
Telephone varchar(20),
Marie int FOREIGN KEY REFERENCES Personne(id),
CONSTRAINT UQ_PERSONNE UNIQUE (Nom,prenom)
);

CREATE TABLE Voiture
(
Num_Chassis varchar(17) PRIMARY KEY,
Immat varchar(20) NOT NULL,
Modele varchar(50) NOT NULL FOREIGN KEY REFERENCES Modele(nom),
Proprietaire int NOT NULL FOREIGN KEY REFERENCES Personne(id)
);

CREATE TABLE Conducteur
(
Conducteur int FOREIGN KEY REFERENCES Personne(id),
Voiture varchar(17) FOREIGN KEY REFERENCES Voiture(Num_Chassis),
CONSTRAINT PK_CONDUCTEUR PRIMARY KEY (Conducteur,Voiture)
);