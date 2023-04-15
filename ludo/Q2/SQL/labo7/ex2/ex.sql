--1
SELECT Societe, Telephone 
FROM Clients 
WHERE Pays = 'Belgique';

--2
SELECT * 
FROM Fournisseurs 
WHERE Fax IS NOT NULL;

--3
SELECT Ref_Produit, Nom_Produit 
FROM Produits 
WHERE Ref_Produit <= 50 AND Nom_Produit LIKE 'S%e';

--4
SELECT Societe, Telephone 
FROM Fournisseurs 
WHERE Pays IN ('France', 'Belgique', 'Suisse', 'Canada');

--5
SELECT Nom_Produit, Quantite_par_unite, Prix_unitaire 
FROM Produits 
WHERE Prix_unitaire BETWEEN 50 AND 100;
