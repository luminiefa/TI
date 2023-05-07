# CHAPITRE 1 :  SCHÉMA CONCEPTUEL
## 1.2. Formalisme
Il existe plusieurs formalismes possibles  
Nous choisirons les diagrammes entité-relation.  
Entity Relationship Diagram en anglais (ERD)
## 1.3. Entités : notation
![image](https://user-images.githubusercontent.com/19058019/236683377-7e52321f-1044-45b2-b63c-35dc46e0a21a.png)
## 1.4. Relation : cardinalités
![image](https://user-images.githubusercontent.com/19058019/236683389-14d6b3e6-3cda-41f2-8bc7-0607109c2842.png)
![image](https://user-images.githubusercontent.com/19058019/236683401-4cea91ce-4952-4d61-b600-4e4e81b1bd53.png)
## Récap
![image](https://user-images.githubusercontent.com/19058019/236683412-4905c5e4-57f7-4f7f-a362-701dd586df3b.png)
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
![image](https://user-images.githubusercontent.com/19058019/236683422-110a3a72-af5a-4f98-82f3-4b67063c6e95.png)
## 1.7. Normalisation
![image](https://user-images.githubusercontent.com/19058019/236683425-160b188c-5d86-47ff-a26b-000c229763e6.png)
![image](https://user-images.githubusercontent.com/19058019/236683434-d6c3b6ea-68dc-40ad-88c8-92c0ac3400d4.png)
![image](https://user-images.githubusercontent.com/19058019/236683448-dd3082b9-51ce-4e69-839c-7e3b0c882e14.png)
![image](https://user-images.githubusercontent.com/19058019/236683455-7db807f8-c842-4b20-b1dd-c9abddcbc641.png)
![image](https://user-images.githubusercontent.com/19058019/236683462-3e43b6f9-9669-4f34-9599-4eae88ff61bb.png)

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
![image](https://user-images.githubusercontent.com/19058019/236683485-7380547a-e153-4d44-a919-e754d027a30a.png)
## 2.2. Traduire les relations 1-N
![image](https://user-images.githubusercontent.com/19058019/236683500-643027ff-fda2-43b9-a112-a4c5bc4b9e17.png)
## 2.2. Traduire les relations 1-1
![image](https://user-images.githubusercontent.com/19058019/236683509-b6135d2e-85e2-44db-9a28-8575055694ff.png)
## 2.2. Traduire les relations N-N
![image](https://user-images.githubusercontent.com/19058019/236683516-2273a573-2e2b-42a4-94c4-23077ecabebf.png)
![image](https://user-images.githubusercontent.com/19058019/236683524-5736de29-04be-4efb-ae83-d54fd12a4c7c.png)
![image](https://user-images.githubusercontent.com/19058019/236683537-4c9bea62-6c23-49d8-a239-6d5ead1efadc.png)
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
![image](https://user-images.githubusercontent.com/19058019/236683552-aca9fea9-d4ed-4b00-bb98-7c9e429d5053.png)
### Contraintes  
Contraintes d'intégrités à ajouter à la création :  
• PRIMARY KEY : clé primaire  
• UNIQUE : valeur unique  
(appelé aussi clé secondaire, ou clé candidate)  
• NOT NULL : obligatoire  
• FOREIGN KEY : clé étrangère  
• CHECK : contraintes additionnelles
![image](https://user-images.githubusercontent.com/19058019/236683564-9188a4fb-dd10-4ab6-9b26-06a46d6c11e3.png)
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
![image](https://user-images.githubusercontent.com/19058019/236683584-42eb383a-4d97-4fba-a0be-11337f2d7a64.png)
#### 3.1.2. Contraintes : FK multiple
![image](https://user-images.githubusercontent.com/19058019/236683598-a551fb94-61a7-4260-bdae-89eb648d87f7.png)
#### 3.1.2. Contraintes : exemple
![image](https://user-images.githubusercontent.com/19058019/236683608-5cf41ed1-df5a-4153-b2ae-6bf52eee9dd8.png)
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
![image](https://user-images.githubusercontent.com/19058019/236683622-67a589ed-aeda-425c-bee0-bedae014b5d0.png)
### Suppression
![image](https://user-images.githubusercontent.com/19058019/236683634-207e7abd-efee-45e0-9e03-d2a952ff2415.png)
## 3.2. Data manipulation language
### Insertion de données
![image](https://user-images.githubusercontent.com/19058019/236683643-323494d0-5b22-4582-9afc-9d8a6d2e22d3.png)
### Modification de données
![image](https://user-images.githubusercontent.com/19058019/236683650-98e7d1a2-5de4-452e-aa49-11d0509638aa.png)
### Suppression de données
![image](https://user-images.githubusercontent.com/19058019/236683664-1f2fa5fe-bcd5-441c-ba63-647f560447a9.png)
## 3.3. Data query language
### Sélections
![image](https://user-images.githubusercontent.com/19058019/236683677-c2cc75df-0d61-41b8-82c3-d774fb07c86d.png)
![image](https://user-images.githubusercontent.com/19058019/236683692-b0ed2da9-d471-4241-8ac5-200236747ff4.png)
#### 3.3.1. Sélection : Opérateurs
![image](https://user-images.githubusercontent.com/19058019/236683704-cc1abc83-615f-4787-8fff-b8874afce3f8.png)
#### 3.3.1. Sélection : Fonctions
![image](https://user-images.githubusercontent.com/19058019/236683729-945d33ff-a5c9-40bb-af2e-ee9639462f00.png)
![image](https://user-images.githubusercontent.com/19058019/236683737-c4a4e4a0-9ee3-43d8-9a6e-2779054d8c99.png)
#### 3.3.1. Sélection : Fonctions de groupe
![image](https://user-images.githubusercontent.com/19058019/236683755-4b6e6c81-2c89-4f60-bc50-42cad28ec39b.png)
![image](https://user-images.githubusercontent.com/19058019/236683762-a81902a8-3dbc-46f3-81eb-49df62c2f580.png)
#### 3.3.1. Sélection : GROUP BY
![image](https://user-images.githubusercontent.com/19058019/236683774-b71ddf17-5546-4806-adc3-9f81aeb55589.png)
#### 3.3.1. Sélection : HAVING
![image](https://user-images.githubusercontent.com/19058019/236683787-762febcb-4f71-4e5d-a632-3313671684af.png)
#### 3.3.1. Sélection : ORDER
![image](https://user-images.githubusercontent.com/19058019/236683794-725f68a4-4f9d-41d5-b180-2744e1c3c13a.png)
### Jointures
![image](https://user-images.githubusercontent.com/19058019/236683810-9a8e19ea-98db-4d05-ac62-4c63aeac89b3.png)
![image](https://user-images.githubusercontent.com/19058019/236683816-7cf84ddd-c6e2-42a7-804b-099ee480b2ba.png)
![image](https://user-images.githubusercontent.com/19058019/236683833-dd7da96c-12c8-4c29-b99b-8da8ccfd9172.png)
#### 3.3.2. Jointures : Exemple
![image](https://user-images.githubusercontent.com/19058019/236683876-035d4dcb-beba-4b8c-a4dd-55f7cb325519.png)
![image](https://user-images.githubusercontent.com/19058019/236684052-dfd5193e-f784-47a4-9472-c193474e9bbc.png)
#### 3.3.2. Jointures réflexives
![image](https://user-images.githubusercontent.com/19058019/236684069-6ab4be5d-a3ac-46a4-9d8f-7f7e9c404b02.png)
![image](https://user-images.githubusercontent.com/19058019/236684077-8203fd62-33ff-4eef-8047-20d77ddf5b68.png)
![image](https://user-images.githubusercontent.com/19058019/236684090-cc999721-b534-4baa-a3e5-82e65770e266.png)
### Requêtes inbriquées
![image](https://user-images.githubusercontent.com/19058019/236684109-61978338-1683-492d-b5ff-f26d1fd410fe.png)
![image](https://user-images.githubusercontent.com/19058019/236684119-cb12ad54-2aa4-44db-b2df-05b2f10a31e1.png)
#### 3.3.3. Requêtes imbriquées : EXISTS
![image](https://user-images.githubusercontent.com/19058019/236684134-ca1452ae-e6e1-471f-8e6f-b2b799d797a7.png)
