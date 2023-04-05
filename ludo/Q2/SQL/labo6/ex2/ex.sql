INSERT INTO SECTEUR (Numero, Nom, Description, Chef) VALUES
(1, 'Entree G', 'Secteur entree gauche', 1),
(2, 'Entree D', 'Secteur entree droite', 5),
(3, 'Colline', 'Secteur colline', 1),
(4, 'Vallon', 'Secteur du petit vallon', 1),
(5, 'Pre fleuri', 'Secteur du grand pre', 2);

INSERT INTO PARCELLE (Numero, Nom, Description, Gardien, Secteur) VALUES
(1, 'ParcelleA', 'Cages hautes', 5, 4),
(2, 'ParcelleB', 'Cages fermées', 1, 4),
(3, 'ParcelleC', 'Prairie', 2, 5),
(4, 'ParcelleD', 'Zone de reproduction', 2, 2),
(5, 'ParcelleE', 'Hangar', 5, 1),
(6, 'ParcelleF', 'Aquarium', 3, 3),
(7, 'ParcelleG', 'Zone quarantaine', 5, 3),
(8, 'ParcelleZ', 'Petits animaux', 1, 2);

INSERT INTO EMPLOYE (NumId, Prenom, Nom, Adresse, Telephone, DateArrivee, DateSortie) VALUES
(1, 'Luc', 'Taret', 'R. du Tige 26 - 5300 Andenne', '+3285425698', '2011-12-01', null),
(2, 'Pierre', 'Ranglet', 'R. de la Belle Montage 10 - 5000 Namur', '+3281245978', '2017-02-15', null),
(3, 'Nathalie', 'Foret', 'R. de l''Egouteur 199 - 4000 Liege', '+3245689575', '2020-01-02', null),
(4, 'Francois', 'Pignon', 'R. de France 15a - 5350 Ohey', '+32499854578', '2012-05-16', '2019-12-31'),
(5, 'Laure', 'Langlet', 'R. du Puit 1 - 5000 Erpent', '+3281452689', '2009-09-25', null);

INSERT INTO CHEF (Employe, DateArrivee, DateSortie) VALUES
(1, '2015-02-10', null),
(5, '2011-12-10', null);

INSERT INTO GARDIEN (Employe, DateArrivee, DateSortie) VALUES
(3, '2020-01-10', null),
(5, '2010-01-01', null),
(1, '2011-12-15', null),
(2, '2017-03-01', null);