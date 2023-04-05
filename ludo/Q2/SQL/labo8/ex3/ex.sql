--1
SELECT *
FROM Produits
WHERE LOWER(SUBSTR(NomProduit, 2)) LIKE '%c%'
ORDER BY ID_Fournisseur, QuantiteParUnite DESC;

--2
SELECT NomProduit, UnitesEnStock, SUM(Quantite) AS UnitesCommandees, (SUM(Quantite) * PrixUnitaire) AS PrixTotalCommande
FROM Produits
JOIN DetailsCommandes ON Produits.ID_Produit = DetailsCommandes.ID_Produit
WHERE (UnitesEnStock + SUM(Quantite)) > 50
GROUP BY NomProduit, UnitesEnStock, PrixUnitaire;

--3
SELECT Clients.CodeClient, COUNT(*) AS NombreCommandes
FROM Clients
JOIN Commandes ON Clients.CodeClient = Commandes.CodeClient
WHERE Commandes.ID_Employe = 4 AND Commandes.DateCommande BETWEEN '2010-01-01' AND '2010-12-31'
GROUP BY Clients.CodeClient
HAVING COUNT(*) >= 2
ORDER BY Clients.CodeClient;

--4
SELECT Nom, Prenom, DateNaissance, (Salaire * 0.1 + 250) AS Prime
FROM Employes
WHERE (YEAR(DateNaissance) BETWEEN 1960 AND 1969 OR YEAR(DateEmbauche) = 1994) AND ID_Superviseur IS NOT NULL;
