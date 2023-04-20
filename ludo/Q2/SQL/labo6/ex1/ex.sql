USE exercice1;

INSERT INTO PAYS (Nom) VALUES ('Italie');
INSERT INTO PAYS (Nom) VALUES ('France');

-- Effectivement, cela ne fonctionne pas pour 'Lada' car le pays 'Russie' n'est pas encodé dans la table PAYS. Il faut d'abord créer le pays 'Russie' dans la table PAYS avant d'ajouter la marque 'Lada' dans la table MARQUE.
-- Le message d'erreur obtenu est dû au fait que la contrainte de clé étrangère FK__MARQUE__Origine__267ABA7A, qui relie la table MARQUE à la table PAYS via la colonne Origine, est violée car la valeur 'Russie' n'existe pas dans la table PAYS. Le code d'erreur est 547, qui indique une violation de la contrainte de clé étrangère.

USE exercice1;

-- Introduire les pays manquants
INSERT INTO PAYS (Nom) VALUES ('Russie');

-- Introduire les marques
INSERT INTO MARQUE (Nom, Origine) VALUES ('Peugeot', 'France');
INSERT INTO MARQUE (Nom, Origine) VALUES ('Fiat', 'Italie');
INSERT INTO MARQUE (Nom, Origine) VALUES ('Lada', 'Russie');

-- Notez que nous avons ajouté d'abord le pays manquant avant d'ajouter la marque 'Lada'.

-- Pour créer les modèles associés à chaque marque, il faut d'abord s'assurer que les marques existent déjà dans la table MARQUE.
-- Ensuite, on peut utiliser la commande INSERT INTO pour insérer les enregistrements dans la table MODELE en utilisant les noms des marques correspondantes comme clé étrangère.
-- Voici le code pour créer les modèles associés à chaque marque :

-- Pour la marque Fiat
USE exercice1;

-- Vérifier que la marque Fiat existe déjà
IF NOT EXISTS (SELECT * FROM MARQUE WHERE Nom = 'Fiat')
BEGIN
  INSERT INTO PAYS (Nom)
  VALUES ('Italie');
  INSERT INTO MARQUE (Nom, Origine)
  VALUES ('Fiat', 'Italie');
END

-- Insérer les modèles Tipo et Panda pour la marque Fiat
INSERT INTO MODELE (Nom, Marque)
VALUES ('Tipo', 'Fiat');
INSERT INTO MODELE (Nom, Marque)
VALUES ('Panda', 'Fiat');

-- Pour la marque Peugeot
-- Vérifier que la marque Peugeot existe déjà
IF NOT EXISTS (SELECT * FROM MARQUE WHERE Nom = 'Peugeot')
BEGIN
  INSERT INTO PAYS (Nom)
  VALUES ('France');
  INSERT INTO MARQUE (Nom, Origine)
  VALUES ('Peugeot', 'France');
END

-- Insérer les modèles Partner et 308 pour la marque Peugeot
INSERT INTO MODELE (Nom, Marque)
VALUES ('Partner', 'Peugeot');
INSERT INTO MODELE (Nom, Marque)
VALUES ('308', 'Peugeot');

--Notez que nous avons d'abord vérifié si la marque correspondante existait déjà dans la table MARQUE avant de l'insérer. Si elle n'existait pas, nous avons d'abord créé l'enregistrement correspondant dans la table PAYS et dans la table MARQUE avant d'insérer les modèles associés.

-- Il n'est pas possible d'enregistrer le modèle '308' pour la marque Fiat car le modèle '308' est déjà associé à la marque Peugeot dans la table MODELE. Il y a une contrainte d'intégrité référentielle qui empêche d'enregistrer une association entre un modèle et une marque déjà existante dans la table MODELE. Pour associer le modèle '308' à la marque Fiat, il faudrait soit supprimer l'association entre '308' et la marque Peugeot dans la table MODELE, soit renommer le modèle '308' pour éviter le conflit de noms.

--• Enregistrez à présent les propriétaires suivants :
USE exercice1;

INSERT INTO PERSONNE(Id, Nom, Prenom, Email, Telephone, Marie)
VALUES
(10, 'Smal', 'Anne', 'anne.smal@skynet.be', '0499.88.77.66', NULL),
(20, 'Peten', 'Jean-Pol', 'jeanpol.peten@hotmail.com', '0488/11.22.33', NULL),
(30, 'Bouraada', 'Mohamed', 'Mohamed.bouraada@gmail.com', '0477/77.88.99', NULL),
(40, 'Dupont', 'Marc', 'marc.dupont@gmail.com', '0475/12.34.56', 10),
(50, 'Dupuis', 'Corinne', 'Co.dupuis@hotmail.com', '0495.45.63.98', NULL);

-- Notez que pour l'attribut "Marie" correspondant à l'ID de l'époux/épouse, nous avons indiqué la valeur NULL pour les personnes non mariées.
-- à corriger ici !!
-- Enregistrez ensuite le couple suivant :
INSERT INTO personne (Nom, Prenom, Email, Telephone) VALUES ('Cote', 'Isabelle', 'c.isa@gmail.com', '0478/11.44.56');
INSERT INTO personne (Nom, Prenom, Email, Telephone, Mari) VALUES ('Tombal', 'Pierre', 'p.tombal@hotmail.com', '0497.19.78.55', 10);
UPDATE personne SET Mari = 60 WHERE Id = 10;

-- La première commande ajoute l'enregistrement Cote sans référence à un autre enregistrement. La deuxième commande ajoute l'enregistrement Tombal en faisant référence à l'enregistrement Cote (ID=60). La troisième commande met à jour l'enregistrement Marie (ID=10) pour faire référence à l'enregistrement Cote (ID=60).

--Enregistrez les voitures suivantes :
INSERT INTO voiture (Marque, Modèle, Immatriculation, NumChassis, Proprietaire)
VALUES
('Fiat', 'Tipo', '1-PFT600', 'ASR123658ERT-1256', 10),
('Peugeot', '308', '1-ABC999', 'XYZ123658ABC-9876', 30);

--Et finalement, encodez les conducteurs suivants :
-- Pour encoder les conducteurs pour chaque voiture, il faut créer une nouvelle table 'conducteur_voiture' qui fait le lien entre la table 'voiture' et la table 'personne'. Cette table aura deux colonnes: 'id_voiture' (clé étrangère vers la table 'voiture') et 'id_personne' (clé étrangère vers la table 'personne'). Ensuite, il suffit d'insérer les enregistrements correspondants.
CREATE TABLE conducteur_voiture (
    id_voiture INT NOT NULL,
    id_personne INT NOT NULL,
    PRIMARY KEY (id_voiture, id_personne),
    FOREIGN KEY (id_voiture) REFERENCES voiture(id),
    FOREIGN KEY (id_personne) REFERENCES personne(id)
);

-- Et voici le code SQL pour insérer les enregistrements de conducteurs pour chaque voiture :
INSERT INTO conducteur_voiture (id_voiture, id_personne)
VALUES
    (1, 10), -- Anne Smal pour la Fiat Tipo
    (1, 40), -- Marc Dupont pour la Fiat Tipo
    (1, 30), -- Mohamed Bouraada pour la Fiat Tipo
    (2, 30), -- Mohamed Bouraada pour la Peugeot 308
    (2, 20), -- Jean-Pol Peten pour la Peugeot 308
    (2, 10); -- Anne Smal pour la Peugeot 308

-- Pour mettre à jour le statut d'Anne Smal en tant que mariée avec Marc Dupont, nous devons d'abord trouver l'ID de Marc Dupont dans la table "personne" en utilisant sa valeur de téléphone :
SELECT id_personne FROM personne WHERE telephone = '0475/12.34.56';

-- Nous obtenons l'ID 40 pour Marc Dupont. Nous pouvons maintenant mettre à jour le statut d'Anne Smal en utilisant l'ID correspondant :
UPDATE personne SET statut = 'marié(e)' WHERE id_personne = 10;
UPDATE personne SET partenaire = 40 WHERE id_personne = 10;

-- Pour mettre à jour les statuts de Jean-Pol Peten et Corinne Dupuis, nous devons d'abord trouver leurs ID dans la table "personne" en utilisant leurs valeurs de téléphone :
SELECT id_personne FROM personne WHERE telephone = '0488/11.22.33';
SELECT id_personne FROM personne WHERE telephone = '0495.45.63.98';

-- Nous obtenons les ID 20 pour Jean-Pol Peten et 50 pour Corinne Dupuis. Nous pouvons maintenant mettre à jour leurs statuts en utilisant les ID correspondants :
UPDATE personne SET statut = 'marié(e)' WHERE id_personne = 20;
UPDATE personne SET partenaire = 50 WHERE id_personne = 20;
UPDATE personne SET statut = 'marié(e)' WHERE id_personne = 50;
UPDATE personne SET partenaire = 20 WHERE id_personne = 50;

-- En ce qui concerne la modification du numéro de châssis de la Peugeot 308, cela est possible en utilisant la commande suivante :
UPDATE voiture SET chassis = 'YYY123658ABC-9876' WHERE immatriculation = '1-ABC999';

-- Cela est possible car le numéro de châssis est stocké dans la table "voiture" et peut être modifié à tout moment tant que les clés étrangères ne sont pas affectées. Dans ce cas, le numéro de châssis modifié n'affecte pas les autres tables, il peut donc être modifié sans problème.

--Effectivement, c'est une bonne observation. Dans ce cas, il faudrait supprimer les enregistrements liés au numéro de châssis erroné dans la table CONDUCTEUR, puis modifier le numéro de châssis dans la table VOITURE et enfin réinsérer les enregistrements dans la table CONDUCTEUR avec le nouveau numéro de châssis. Mais il est important de noter que cette méthode peut être risquée et complexe, et qu'il est préférable d'utiliser des identifiants techniques pour éviter ce genre de situations.

-- Avant de répondre à cette question, il est important de noter que la suppression d'un modèle de voiture peut avoir des conséquences sur les enregistrements dans les autres tables. Par exemple, si un modèle est lié à des enregistrements dans la table VOITURE, la suppression du modèle entraînera la suppression de ces enregistrements également.
-- En ce qui concerne la suppression du modèle "Panda", voici la commande SQL à utiliser :
DELETE FROM MODELE WHERE NomModele = 'Panda';
-- Si le modèle "Panda" n'est lié à aucun enregistrement dans les autres tables, il sera supprimé avec succès.
-- En ce qui concerne la suppression du modèle "Tipo", cela dépend de s'il est lié à d'autres enregistrements dans les autres tables. Si le modèle "Tipo" est lié à des enregistrements dans la table VOITURE ou la table CONDUCTEUR, la suppression du modèle entraînera la suppression de ces enregistrements également. Dans ce cas, il est préférable de d'abord supprimer les enregistrements liés à "Tipo" avant de supprimer le modèle lui-même.
--Voici la commande SQL pour supprimer le modèle "Tipo" :
DELETE FROM MODELE WHERE NomModele = 'Tipo';
-- Avant de l'exécuter, il est conseillé de vérifier s'il y a des enregistrements liés à "Tipo" dans d'autres tables, et de les supprimer en premier si nécessaire.

-- Pour ajouter une nouvelle colonne 'description' à la table 'PAYS', vous pouvez utiliser la commande SQL suivante :
ALTER TABLE pays ADD COLUMN description TEXT;
-- Ensuite, pour encoder une courte description pour chaque pays, vous pouvez utiliser la commande SQL suivante pour chaque pays :
UPDATE pays SET description = 'description du pays' WHERE nom = 'nom du pays';
-- Par exemple, pour ajouter une description pour la France :
UPDATE pays SET description = 'Pays de la gastronomie, de la mode et de l\'amour' WHERE nom = 'France';


ALTER TABLE conducteur ADD COLUMN description VARCHAR(255);