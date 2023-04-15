--1
SELECT UPPER(nom) AS nom_maj, prenom
FROM employes
WHERE fonction = 'Représentant(e)';

--2
SELECT societe
FROM clients
WHERE LENGTH(societe) < 12;

--3
SELECT MIN(salaire) AS Minimum, MAX(salaire) AS Maximum
FROM employes
WHERE fonction != 'Représentant(e)';

--4
SELECT fonction, AVG(salaire) AS salaire_moyen
FROM employes
GROUP BY fonction;

--5
SELECT categorie, AVG(prix_unitaire) AS prix_moyen, SUM(prix_unitaire) AS prix_total
FROM produits
GROUP BY categorie;

--6
SELECT categorie, COUNT(*) AS nb_produits_dispo
FROM produits
WHERE stock > 0
GROUP BY categorie
HAVING COUNT(*) >= 10;

