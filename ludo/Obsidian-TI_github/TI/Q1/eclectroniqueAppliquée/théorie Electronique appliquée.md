# Intro
## Contenu partie théorie
•Introduction: origines et découvertes de l’électricité
•Loi de Pouillet, loi d’Ohm, effet joule
•Lois de Kirchhoff (nœuds et mailles)
•Résistances équivalentes (série/parallèle)
•Semiconducteurs (intrinsèque, extrinsèque)
•Jonction PN
•LED
## Origine de l’électricité
## Qu’est ce que l’électricité?
## Bandes de conductions: métaux
# Electronique appliquée théorie ch1
## Qu’est ce que l’électricité?
Courant électrique:  
  Ensemble de particules chargées (positivement ou négativement) qui en moyenne se déplacent dans un sens privilégié.
## Force électrique
Loi de Coulomb:
![[Pasted image 20230418202528.png]]
Loi de Newton:
![[Pasted image 20230418202603.png]]
## Champ électrique
Champ Electrique:
![[Pasted image 20230418202632.png]]
Champ Gravitationnel:
![[Pasted image 20230418202645.png]]
## Potentiel Electrique
Potentiel Electrique:
![[Pasted image 20230418202710.png]]
Potentiel Gravitationnel:
![[Pasted image 20230418202719.png]]
## Energie potentielle
Energie potentielle Electrique:
	Travail pour déplacer la charge hors de l’influence du champ (r = infini   )
	![[Pasted image 20230418202850.png]]
Energie potentielle gravitationnelle:
	Travail pour déplacer la charge hors de l’influence du champ (r = infini   )
	![[Pasted image 20230418202904.png]]
Energie = Joule
## Potentiel
Potentiel: version de l'énergie potentielle où la charge/masse de la particule/objet n’est pas définie.
Masse ponctuelle:
![[Pasted image 20230418202951.png]]
Masse non ponctuelle
![[Pasted image 20230418202958.png]]
## Courant ou Intensité
•Courant électrique représente le débit en charges (+) passant à travers une surface par unité de temps
![[Pasted image 20230418203034.png]]
Débit massique: quantité de matière traversant une surface par unité de temps
![[Pasted image 20230418203046.png]]
## Différence de potentiel et tension
![[Pasted image 20230418203058.png]]
## Résistance
![[Pasted image 20230418203116.png]]
## Loi d’Ohm
![[Pasted image 20230418203127.png]]
## Conductance
Resistance R = Potentiel d’un composant à résister au passage du courant lorsqu’il est sous tension
Conductance  G = Potentiel d’un composant à laisser passer le courant lorsqu’il est sous tension
![[Pasted image 20230418203155.png]]
## Puissance, Effet Joule
•Effet joule: en se déplaçant les électrons percutent les atomes, transférant une partie de leur énergie à Vibration à Chaleur
![[Pasted image 20230418203229.png]]
## Résistances équivalentes
•Résistances en série
![[Pasted image 20230418203255.png]]
•Résistances en parallèle
![[Pasted image 20230418203317.png]]
# Electronique appliquée théorie ch2
## Résistances équivalentes
•Plusieurs résistances résumées en une seule
![[Pasted image 20230418203535.png]]
## Mesures
•Mesures de Tension.
•Mesures de Courant.
•Mesures de Résistance.
![[Pasted image 20230418203612.png]]
## Mesure de Résistance
•Résistance: composant créé ayant une certaine valeur
![[Pasted image 20230418203633.png]]
•Ohmmètre:
–R=U/I
–Applique une tension
–~Mesure du courant
	•Pont diviseur de tension
–Mesure hors circuit (pas de courant/tension dans le circuit)
![[Pasted image 20230418203717.png]]
## Mesure de courant
![[Pasted image 20230418203737.png]]
## Mesure de tension
![[Pasted image 20230418203753.png]]
## Lois de Kirchhoff
- Loi des nœuds: Ce qui rentre = ce qui sort
![[Pasted image 20230418203846.png]]
- En définissant les courants tous entrant ou tous sortant:
![[Pasted image 20230418203901.png]]
•Loi des mailles: Une boucle permet de revenir à la même position
![[Pasted image 20230418203937.png]]
En choisissant un sens pour la boucle et le sens des tension positives
![[Pasted image 20230418204011.png]]
## Equation circuit
![[Pasted image 20230418204040.png]]
# Electronique appliquée théorie ch3
## Application des lois de Kirchoff
•Loi des Nœuds:
•  Is=IR2+IR5
•  IR2=IR3+IR1
•  IR3+IR5=IR4
•  IR1+IR4=IS
![[Pasted image 20230418204150.png]]
![[Pasted image 20230418204200.png]]
![[Pasted image 20230418204214.png]]
## Relation I-V Composant
![[Pasted image 20230418204230.png]]
## Résolution
![[Pasted image 20230418204247.png]]
## Méthode subtile
![[Pasted image 20230418204301.png]]
## Structure d’un solide (cristal)
•Cristal : structure régulière d’atome
![[Pasted image 20230418204330.png]]
•Types de liaison :
–Liaisons Ioniques: échanges d’électrons entre atome d’électronégativité différentes (attraction colombienne)  
–Liaison Covalentes: paires d’électrons partagés entres deux atomes pour compléter la dernière 
–Liaison Métallique: électrons mis en commun par un grand nombre d’atomes (Ex: Or)
–Liaison de Vander Waals: Charge partielle sur les molécules pour former des dipôles. (Ex: Plastiques)
## Cristal: Liaisons covalentes
![[Pasted image 20230418204410.png]]
## Structure électronique: niveaux d’énergies
•Electrons répartis en couches
•Couches situées à des niveaux d’énergie précis
![[Pasted image 20230418204432.png]]
## Théorie des bandes
https://www.youtube.com/watch?v=g8CwSCepwD8
•En ajoutant des atomes au système, le nombre de niveaux d’énergie possible augmente.
• Pour un cristal suffisamment grand: les niveaux se regroupent en bandes
![[Pasted image 20230418204509.png]]
•Métaux : bande de valence et conduction se superposent
•Isolant : grand écart entre les bandes
•Semiconducteur : Faible écart entre ces deux bandes
![[Pasted image 20230418204536.png]]
## Semiconducteur intrinsèque
•Semiconducteur pur : isolant à base température
->Energie thermique permet de déplacer certains électrons dans la couche de conduction
![[Pasted image 20230418204614.png]]
## Semiconducteur extrinsèque
•Semiconducteur extrinsèque :
-> Plus ou moins d’électrons que prévu dans la structure électronique
![[Pasted image 20230418204642.png]]
•Semiconducteur extrinsèque :
-> Ajout d’impureté ayant plus ou moins d’électrons dans le cristal
-> Electron ou trou (charge positive) dans la bande de conduction
![[Pasted image 20230418204715.png]]
![[Pasted image 20230418204850.png]]
# Electronique appliquée théorie ch4
## Jonction PN
![[Pasted image 20230418204946.png]]
## Génération et recombinaison
![[Pasted image 20230418205000.png]]
## Jonction PN
Les électrons (-) attirés par les trous (+)  se déplacent pour se recombiner.  
Les charges mobiles disparaissent et créées des ions à la jonction
![[Pasted image 20230418205030.png]]
•Zone de déplétion:
–Créée recombinaison des charges libres type N et P au niveau de la jonction.
–Ne contient plus de charges mobiles, seulement des ions (atomes ayant gagné ou perdu des électrons)
–Zone de déplétion = isolant
![[Pasted image 20230418205103.png]]
## Bandes jonction PN
•Structure de bande:
–Type P: énergie de fermi plus proche de la bande de valence
–Type N: énergie de fermi plus proche de la bande de conduction
–L’énergie de fermi reste au même niveau et les bandes s’adaptent
![[Pasted image 20230418205130.png]]
## Bandes et équilibre des courants
•Deux courants s’équilibrent:
–Courant de diffusion: les porteurs de charges se diffusent vers des zones où la concentration est plus basse
–Courant de dérive: le fort champ électrique dû aux ions de la jonction pousse les charges à se déplacer
Idif+Ider=0
![[Pasted image 20230418205206.png]]
## Polarisation
•Polarisation dans le sens PàN (direct)
![[Pasted image 20230418205225.png]]
•Polarisation dans le sens N à P (inverse)
![[Pasted image 20230418205242.png]]
## Diode
•La jonction PN forme une diode (à jonction)
–Il existe beaucoup d’autre type de diode
–Les diodes à jonction au silicium ont une tension  
seuil de 0,7 Volts
![[Pasted image 20230418205308.png]]
![[Pasted image 20230418205323.png]]
## Relation courant tension
En inverse: La diode ne conduit pas, elle est bloquante.
En direct: La diode conduit lorsque la tension seuil est dépassée (zone de déplétion réduite au max)
Breakdown/Claquage: La électrons ont suffisamment d’énergie pour passer (effet avalanche et tunnel), cela détruit généralement le composant.
•Graphe courant vs tension
![[Pasted image 20230418205356.png]]
# Electronique appliquée théorie ch5
## Diodes électroluminescentes (LED)
![[Pasted image 20230418205814.png]]
## Lumière: onde et particule
•Lumière: onde électromagnétique:
	  un photon est le quantum d'énergie associé
	  ![[Pasted image 20230418205844.png]]
## Spectre électromagnétique
![[Pasted image 20230418205910.png]]
## LED fonctionnement
![[Pasted image 20230418205925.png]]
## Effet Photoélectrique
Recombinaison
Un électron libre retombe dans un trou présent dans la bande de valence et restitue l’énergie via l’émission d’un photon
![[Pasted image 20230418210003.png]]
Génération
Un apport d’énergie (ici photon) permet à un électron de liaison de passer dans la bande de conduction
![[Pasted image 20230418210014.png]]
![[Pasted image 20230418210027.png]]
## Niveau d’énergies et photons
Taille de la bande interdite (Gap) à Couleur du photon
![[Pasted image 20230418210044.png]]
## Matériaux
Le choix des matériaux détermine la bande interdite à couleur
  Privilégier les matériaux transparents
  Privilégier les matériaux à gap direct vs indirect
![[Pasted image 20230418210102.png]]
![[Pasted image 20230418210110.png]]
![[Pasted image 20230418210113.png]]
## Photodiode
•Fonctionnement inverse à la LED:
	–Absorption de photons
	–Génération de pair électrons-trous
	–Réponse différente selon la couleur
![[Pasted image 20230418210135.png]]
Capteur photo (CCD, CMOS)
![[Pasted image 20230418210154.png]]
Cellule Photovoltaïque
![[Pasted image 20230418210200.png]]
## Utilisation d’une LED
•Rappel: Graphe courant vs tension
![[Pasted image 20230418210219.png]]
## LED blanche
Lumière blanche
![[Pasted image 20230418210233.png]]
Température de spectre (Kelvin):
• ~1000K, Faible ≈ rouge  
• ~3000K, Moyen ≈ jaune  
• ~5000K, Haut ≈ blanc  
• ~6000K, Très haut ≈ bleu
![[Pasted image 20230418210249.png]]
![[Pasted image 20230418210253.png]]
•Deux méthodes:
Utiliser plusieurs LED différentes
![[Pasted image 20230418210323.png]]
![[Pasted image 20230418210327.png]]
LED bleue + matériau phosphorescent
![[Pasted image 20230418210330.png]]
![[Pasted image 20230418210334.png]]



# Synthèse
## Loi d’ohm INTRODUCTION
![image](https://github.com/luminiefa/TI/assets/19058019/29469102-76b7-4aa8-9baf-6fda30731eed)
## Rappel électricité :
![image](https://github.com/luminiefa/TI/assets/19058019/7ed116ae-1ccd-43c0-ae7c-6b4da3ad7186)
![image](https://github.com/luminiefa/TI/assets/19058019/9ad2d836-7dfa-4a22-a78b-7e6c5a99c71d)
## Loi de Pouillet :
![image](https://github.com/luminiefa/TI/assets/19058019/35542fe2-18e8-4985-9b0d-7682d1ad603a)
## Montage en série :
![image](https://github.com/luminiefa/TI/assets/19058019/ebe028a7-ce02-4f59-85cb-e536275f33fe)
## Montage en parallèle :
![image](https://github.com/luminiefa/TI/assets/19058019/4994fdec-9864-40c9-8cd6-4dde23968216)
## Théorème de millman
![image](https://github.com/luminiefa/TI/assets/19058019/3bcd1686-87fe-467f-aaa7-b66944c09c26)
![image](https://github.com/luminiefa/TI/assets/19058019/76a68ca1-a8e9-4baf-abc0-63c29add8c39)
## Potentiomètre :
![image](https://github.com/luminiefa/TI/assets/19058019/25045219-7af2-414e-b188-ebde0b29891b)
## LOI des nœuds (Kirchhoff)
![image](https://github.com/luminiefa/TI/assets/19058019/6325eac6-8992-42a9-b534-c17a484007ff)
