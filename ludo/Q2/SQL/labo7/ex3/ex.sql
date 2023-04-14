--1
SELECT DISTINCT Ville FROM Clients ORDER BY Ville ASC;

--2
SELECT Nom, Prénom, Fonction FROM Employés ORDER BY Nom ASC, Prénom ASC;

--3
SELECT NomProduit, PrixUnitaire FROM Produits WHERE NomProduit LIKE '_a%' ORDER BY PrixUnitaire DESC;

-- Note : La requête utilise le joker _ qui représente un seul caractère et le % qui représente un ou plusieurs caractères. Ainsi, _a% signifie un caractère, suivi de la lettre 'a', suivi de zéro ou plusieurs caractères.
