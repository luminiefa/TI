CREATE TABLE Employe
(
Numid decimal(10) PRIMARY KEY,
Prenom varchar(50),
Nom varchar(50),
Adresse varchar(50),
Telephone varchar(50),
DateArrivée varchar(50),
DateSortie varchar(50),
);

CREATE TABLE Chef
(
Employe decimal(10) NOT NULL FOREIGN KEY REFERENCES Employe(Numid),
DateArrivee varchar(50),
DateSortie varchar(50)
);

CREATE TABLE Gardien
(
Employe decimal(10) NOT NULL FOREIGN KEY REFERENCES Employe(Numid),
DateArrivee varchar(50),
DateSortie varchar(50)
);

CREATE TABLE Secteur
(
Numero decimal(10) PRIMARY KEY,
Nom varchar(50),
Description varchar(50),
Chef decimal(10) NOT NULL FOREIGN KEY REFERENCES Employe(Numid)
);

CREATE TABLE Parcelle
(
Numero decimal(10) PRIMARY KEY,
Nom varchar(50),
Description varchar(50),
Gardien decimal(10) NOT NULL FOREIGN KEY REFERENCES Employe(Numid),
Secteur decimal(10) NOT NULL FOREIGN KEY REFERENCES Secteur(Numero)
);