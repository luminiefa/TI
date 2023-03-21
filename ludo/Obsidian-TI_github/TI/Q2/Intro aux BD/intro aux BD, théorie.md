- [[#CHAPITRE 1 :  SCHÉMA CONCEPTUEL|CHAPITRE 1 :  SCHÉMA CONCEPTUEL]]
	- [[#CHAPITRE 1 :  SCHÉMA CONCEPTUEL#1.2. Formalisme|1.2. Formalisme]]
	- [[#CHAPITRE 1 :  SCHÉMA CONCEPTUEL#1.3. Entités : notation|1.3. Entités : notation]]
	- [[#CHAPITRE 1 :  SCHÉMA CONCEPTUEL#1.4. Relation : cardinalités|1.4. Relation : cardinalités]]
	- [[#CHAPITRE 1 :  SCHÉMA CONCEPTUEL#Récap|Récap]]
	- [[#CHAPITRE 1 :  SCHÉMA CONCEPTUEL#1.5. Etapes|1.5. Etapes]]
	- [[#CHAPITRE 1 :  SCHÉMA CONCEPTUEL#1.6. Contraintes d'intégrité|1.6. Contraintes d'intégrité]]
	- [[#CHAPITRE 1 :  SCHÉMA CONCEPTUEL#1.7. Normalisation|1.7. Normalisation]]
- [[#CHAPITRE 2 :  SCHÉMA RELATIONNEL|CHAPITRE 2 :  SCHÉMA RELATIONNEL]]
	- [[#CHAPITRE 2 :  SCHÉMA RELATIONNEL#2.1. BD relationnelles : Valeur|2.1. BD relationnelles : Valeur]]
	- [[#CHAPITRE 2 :  SCHÉMA RELATIONNEL#2.1. BD relationnelles : notion d'ordre|2.1. BD relationnelles : notion d'ordre]]
	- [[#CHAPITRE 2 :  SCHÉMA RELATIONNEL#2.2. Traduire les relations|2.2. Traduire les relations]]
	- [[#CHAPITRE 2 :  SCHÉMA RELATIONNEL#2.2. Traduire les relations : règles|2.2. Traduire les relations : règles]]
	- [[#CHAPITRE 2 :  SCHÉMA RELATIONNEL#2.2. Traduire les relations 1-N|2.2. Traduire les relations 1-N]]
	- [[#CHAPITRE 2 :  SCHÉMA RELATIONNEL#2.2. Traduire les relations 1-1|2.2. Traduire les relations 1-1]]
	- [[#CHAPITRE 2 :  SCHÉMA RELATIONNEL#2.2. Traduire les relations N-N|2.2. Traduire les relations N-N]]
- [[#CHAPITRE 3 : SQL|CHAPITRE 3 : SQL]]
	- [[#CHAPITRE 3 : SQL#SQL|SQL]]
	- [[#CHAPITRE 3 : SQL#Outil|Outil]]
	- [[#CHAPITRE 3 : SQL#Convention de nommage|Convention de nommage]]
	- [[#CHAPITRE 3 : SQL#3.1. Data definition language|3.1. Data definition language]]
		- [[#3.1. Data definition language#Création|Création]]
		- [[#3.1. Data definition language#Contraintes|Contraintes]]
			- [[#Contraintes#3.1.2. Contraintes sur une colonne|3.1.2. Contraintes sur une colonne]]
			- [[#Contraintes#3.1.2. Contraintes sur une table|3.1.2. Contraintes sur une table]]
			- [[#Contraintes#3.1.2. Contraintes : FK simple|3.1.2. Contraintes : FK simple]]
			- [[#Contraintes#3.1.2. Contraintes : FK multiple|3.1.2. Contraintes : FK multiple]]
			- [[#Contraintes#3.1.2. Contraintes : exemple|3.1.2. Contraintes : exemple]]
		- [[#3.1. Data definition language#Modification|Modification]]
			- [[#Modification#3.1.3. Modification : exemple|3.1.3. Modification : exemple]]
		- [[#3.1. Data definition language#Suppression|Suppression]]
	- [[#CHAPITRE 3 : SQL#3.2. Data manipulation language|3.2. Data manipulation language]]
		- [[#3.2. Data manipulation language#Insertion de données|Insertion de données]]
		- [[#3.2. Data manipulation language#Modification de données|Modification de données]]
		- [[#3.2. Data manipulation language#Suppression de données|Suppression de données]]
	- [[#CHAPITRE 3 : SQL#3.3. Data query language|3.3. Data query language]]
		- [[#3.3. Data query language#Sélections|Sélections]]
			- [[#Sélections#3.3.1. Sélection : Opérateurs|3.3.1. Sélection : Opérateurs]]
			- [[#Sélections#3.3.1. Sélection : Fonctions|3.3.1. Sélection : Fonctions]]
			- [[#Sélections#3.3.1. Sélection : Fonctions de groupe|3.3.1. Sélection : Fonctions de groupe]]
			- [[#Sélections#3.3.1. Sélection : GROUP BY|3.3.1. Sélection : GROUP BY]]
			- [[#Sélections#3.3.1. Sélection : HAVING|3.3.1. Sélection : HAVING]]
			- [[#Sélections#3.3.1. Sélection : ORDER|3.3.1. Sélection : ORDER]]
		- [[#3.3. Data query language#Jointures|Jointures]]
			- [[#Jointures#3.3.2. Jointures : Exemple|3.3.2. Jointures : Exemple]]
			- [[#Jointures#3.3.2. Jointures réflexives|3.3.2. Jointures réflexives]]
		- [[#3.3. Data query language#Requêtes inbriquées|Requêtes inbriquées]]
			- [[#Requêtes inbriquées#3.3.3. Requêtes imbriquées : EXISTS|3.3.3. Requêtes imbriquées : EXISTS]]

# CHAPITRE 1 :  SCHÉMA CONCEPTUEL
## 1.2. Formalisme
Il existe plusieurs formalismes possibles  
Nous choisirons les diagrammes entité-relation.  
Entity Relationship Diagram en anglais (ERD)
## 1.3. Entités : notation
![[Pasted image 20230315113737.png]]
## 1.4. Relation : cardinalités
![[Pasted image 20230315114251.png]]
![[Pasted image 20230315114308.png]]
## Récap
![[Pasted image 20230315114348.png]]
## 1.5. Etapes
Pour élaborer un schéma conceptuel, il existe  
plusieurs méthodes... En voilà une :  
1. Identifier les entités  
2. Identifier les relations  
3. Identifier les attributs (et id)  
4. Décorer les relations (cardinalité)  
5. Donner d'éventuelles contraintes d'intégrité  
6. Vérifier  
	1. La cohérence du schéma  
	2. La normalisation
## 1.6. Contraintes d'intégrité
![[Pasted image 20230315114449.png]]
## 1.7. Normalisation
![[Pasted image 20230315114516.png]]
![[Pasted image 20230315114531.png]]
![[Pasted image 20230315114541.png]]
![[Pasted image 20230315114557.png]]
![[Pasted image 20230315114611.png]]

# CHAPITRE 2 :  SCHÉMA RELATIONNEL
## 2.1. BD relationnelles : Valeur
valeur particulière : la valeur null  
→ trois significations :  
- La valeur de l’attribut est inconnue pour certaines  
occurrences  
- L’attribut ne s’applique pas à certaines occurrences  
- Certaines occurrences ne possèdent pas de valeur  
pour l’attribut
## 2.1. BD relationnelles : notion d'ordre
Dans une BD relationnelle, l'ordre des lignes et  
des colonnes n'a pas d'importance  
→ Impossible d'accéder à la 1ère ou 5ème colonne d'une table ou  
à la 42ème ligne...
## 2.2. Traduire les relations
→ Que deviennent les relations?  
	→Des clés étrangères
C'est quoi une clé étrangère?  
Il s'agit d'une colonne additionnelle  
dans une table.  
Cette colonne va référencer l'identifiant (la  
clé primaire) de la table qu'on veut relier.
## 2.2. Traduire les relations : règles
Pour savoir où mettre la clé étrangère,  
il y a des règles simples à suivre :
![[Pasted image 20230315111955.png]]
## 2.2. Traduire les relations 1-N
![[Pasted image 20230315112029.png]]
## 2.2. Traduire les relations 1-1
![[Pasted image 20230315112055.png]]
## 2.2. Traduire les relations N-N
![[Pasted image 20230315112121.png]]
![[Pasted image 20230315112140.png]]
![[Pasted image 20230315112203.png]]
# CHAPITRE 3 : SQL
## SQL
• Insensible à la case  
• Les requêtes finissent par ; et peuvent s'écrire en plusieurs ligne  
Sous langages :  
- DDL (Data Definition Language) : définit les structures de base de données.  
- DML (Data Manipulation Language) : manipule les données (INSERT, UPDATE,  
DELETE).  
- DQL (Data Query Language) : permet de sélectionner (SELECT) les données,  
souvent incluse dans le DML.  
- DCL (Data Control Language) : gère l'accès utilisateur.  
- TCL (Transactional Control Language) : gère les transactions de base de  
données.
## Outil
SQL Server Management Studio (SSMS) :  
La fonctionnalité centrale de SSMS est  
l’Explorateur d’objets:  
1. qui permet à l’utilisateur de naviguer ;  
2. de sélectionner ;  
3. de gérer chacun des objets du serveur ;  
4. aussi bien en mode graphique qu’en mode  
commandes (QBE ou Query by Example).
## Convention de nommage
Les noms de colonne et tables doivent :  
– Commencer avec une lettre  
– Faire entre 1 et 30 caractères  
– Contenir seulement A–Z, a–z, 0–9, _, $, et #  
– Être différents (pour un même utilisateur)  
– Être différents des mots-réservés
## 3.1. Data definition language
### Création  
CREATE DATABASE <base de données> ;
![[Pasted image 20230321195355.png]]
### Contraintes  
Contraintes d'intégrités à ajouter à la création :  
• PRIMARY KEY : clé primaire  
• UNIQUE : valeur unique  
(appelé aussi clé secondaire, ou clé candidate)  
• NOT NULL : obligatoire  
• FOREIGN KEY : clé étrangère  
• CHECK : contraintes additionnelles
![[Pasted image 20230321195431.png]]
#### 3.1.2. Contraintes sur une colonne
	Se note juste après la définition de la colonne :  
	• PRIMARY KEY : définit la colonne comme clé primaire  
	• UNIQUE : interdit à 2 valeurs de la colonne d'être les  
	mêmes  
	• NOT NULL : rend la colonne obligatoire  
	• FOREIGN KEY : défini la colonne comme clé étrangère  
	→ [FOREIGN KEY] REFERENCES <table>(<colonne ref>)  
	• CHECK : pour définir des contraintes additionnelles  
	→ CHECK <condition>
#### 3.1.2. Contraintes sur une table
	Se note à la fin de la création de la table:  
	• PRIMARY KEY : définit un ensemble de colonnes comme  
	identifiant  
	→ PRIMARY KEY (<colonnes>)  
	• UNIQUE : interdit que 2 lignes aient les mêmes valeurs pour  
	un ensemble de colonnes  
	→ UNIQUE (<colonnes>)  
	• FOREIGN KEY : définit un ensemble de colonnes comme clés  
	étrangères référençant des colonnes d'une autre table  
	→ FOREIGN KEY (<colonnes>) REFERENCES <table>(<colonnes>)  
	• CHECK : pour définir des contraintes additionnelles  
	→ CHECK (<condition>)
#### 3.1.2. Contraintes : FK simple
![[Pasted image 20230321195645.png]]
#### 3.1.2. Contraintes : FK multiple
![[Pasted image 20230321195706.png]]
#### 3.1.2. Contraintes : exemple
![[Pasted image 20230321195727.png]]
### Modification  
	Modifier la structure d'une table :  
	ALTER TABLE <table>  
	– ADD ( <colonnes>)  
	– ALTER COLUMN ( <colonnes>)  
	– DROP ( <colonnes>)  
	ou DROP COLUMN <colonne>  
	Renommer une table :  
	EXEC sp_rename '<ancien nom>', '<nouveau nom>';  
	Renommer une colonne :  
	EXEC sp_rename '<table>.<ancien nom> ', '<nouveau nom> ', 'COLUMN';
#### 3.1.3. Modification : exemple
![[Pasted image 20230321195802.png]]
### Suppression
![[Pasted image 20230321195818.png]]
## 3.2. Data manipulation language
### Insertion de données
![[Pasted image 20230321200028.png]]
### Modification de données
![[Pasted image 20230321200043.png]]
### Suppression de données
![[Pasted image 20230321200054.png]]
## 3.3. Data query language
### Sélections
![[Pasted image 20230321200143.png]]
![[Pasted image 20230321200156.png]]
#### 3.3.1. Sélection : Opérateurs
![[Pasted image 20230321200220.png]]
#### 3.3.1. Sélection : Fonctions
![[Pasted image 20230321200247.png]]
![[Pasted image 20230321200305.png]]
#### 3.3.1. Sélection : Fonctions de groupe
![[Pasted image 20230321200326.png]]
![[Pasted image 20230321200340.png]]
#### 3.3.1. Sélection : GROUP BY
![[Pasted image 20230321200358.png]]
#### 3.3.1. Sélection : HAVING
![[Pasted image 20230321200415.png]]
#### 3.3.1. Sélection : ORDER
![[Pasted image 20230321200445.png]]
### Jointures
![[Pasted image 20230321200458.png]]
![[Pasted image 20230321200513.png]]
![[Pasted image 20230321200536.png]]
#### 3.3.2. Jointures : Exemple
![[Pasted image 20230321200601.png]]
![[Pasted image 20230321200619.png]]
#### 3.3.2. Jointures réflexives
![[Pasted image 20230321200641.png]]
![[Pasted image 20230321200652.png]]
![[Pasted image 20230321200704.png]]
### Requêtes inbriquées
![[Pasted image 20230321200718.png]]
![[Pasted image 20230321200728.png]]
#### 3.3.3. Requêtes imbriquées : EXISTS
![[Pasted image 20230321200804.png]]