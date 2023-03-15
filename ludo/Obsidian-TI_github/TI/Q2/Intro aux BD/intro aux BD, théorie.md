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
