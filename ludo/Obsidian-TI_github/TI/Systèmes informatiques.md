Systèmes d'exploitation:
5 chapitres:
1: Introduction aux systèmes d'exploitation
-------------------------------------------------------------------------------------------------------------
**Mode de fonctionnement des processeurs récents :**
	Mode noyau : accès total
	Mode utilisateur : accès restreint
	
**STRUCTURE DES SE:**
**Différentes manières de concevoir un SE existent:**

Monolithiques:
	- Les plus répandus
	- Collection de procédure appelant des routines systèmes
	- L’ensemble de ces routines forme un exécutable : le Noyau
		- D’où les appels système pour passer en mode noyau
		- Fonctionnement :
			1. Envoie des paramètres  
			2. Appel au noyau  
			3. Analyse des paramètres  
			4. Sélection de la routine  
			5. Exécution de la routine  
			6. Retour en mode utilisateur
			schéma !!! ( notion)
			Application
			|                |
			Noyau Monolithique
			|                |
			Matériel
En couches,
	 Le système est construit en couches ayant chacune une fonction propre:  
		 Allocation du processeur aux différents processus (multiprogramming),  
		 Gestion de la mémoire,  
		 Communication processus-console d’un opérateur (multiusers),  
			 Chaque utilisateur dispose de sa console  
		 Gestion des entrées/sorties (I/O),  
		 Programmes des utilisateurs,  
		 Opérateur  
	 Avantage : droit par niveau de sécurité
A micro-noyau,
	 Noyaux monolithiques de plus en plus volumineux  
	 Appel système courant ou rare dans le noyau  
	 Solution:  
		 μNoyau : contient les quelques routines courantes  
		 Routines rares : dans des programmes système  
			 Réduit le nombre de ligne de code dans le kernel
Schéma !!! (lien notion)
Machines virtuelles
	 IBM 360 (1964), composé de 2 parties :  
		 un moniteur de machine virtuelle  
		 un ensemble de machines virtuelles  
	 Revenu à la mode...

2: HISTOIRE DE SYSTÈME D’EXPLOITATION
-------------------------------------------------------------------------------------------------------------
PLAN DU COURS:
	 Qu’est ce qu’un système d’exploitation ?  
	 Pourquoi les étudier ?  
	 Historique des systèmes  
	 Historique : UNIX  
	 Historique : Les micros  
	 Historique : DOS / Windows

QU’EST CE QU’UN SYSTÈME D’EXPLOITATION ?
	 Interface  
		 Convivialité  
		 Gestion des ressources  
	 Lien entre matériel et utilisateur  
	 Pas d’OS = Danger  
	 Généralisation (Unix Windows)  
	 Besoin professionel

HISTORIQUE DES SYSTÈMES
	 Utilisation des ordinateurs de 1ère génération  
		 Pas d’OS au début  
		 1956 : Input Output System  
		 1ier coprocesseur mathématique  
		 Début des super-ordinateurs  
		 Mémoire à tores de ferrite  
		 Concepteur = Programmeur = Utilisateur = ...  
		 Langage machine...
	 Utilisation des ordinateurs de 2ième génération  
		 1959 : IBM 7090 : Transistor  
		 5 fois plus rapide  
		 Plus fiable  
		 Personnel dédié à chaque tâche
	 Utilisation des ordinateurs de 3ème génération  
		 Le circuit intégré
	Jack KILBY
	Robert NOYCE
	 Compatible Time Sharing System  
		 1961  
		 CTSS  
		 Multi-utilisateur
	 MULTIplexed Information and Computing Service  
		 MULTICS

HISTORIQUE : UNIX
	 UNplexed Information and Computing Service
		Ken thompson, Dennis Ritchie, Brian Kernighan
	 1970 : 1ière version  
	 1973 : Langage C  
		 Distribution libre  
			 Amélioration rapide  
	 1975 : version 6  
		 Base commune,  
			 1978 : BSD  
			 1984 : System III, IV et V  
	 1991 : Linux
		 Normalisation  
		 1990  
		 POSIX  
		 IEEE 1003,1

HISTORIQUE : LES MICROS
	 Utilisation des micros :  
		 l’Intel 4004 – 1971  
		 2300 transistors  
		 4 bits  
		 4ième Génération d’ordinateurs  
		 Micro-ordinateurs
	 Utilisation des micros :  
		 IBM-PC : août 1981
	 Utilisation des micros :  
		 le CP/M

HISTORIQUE : DOS / WINDOWS
	 Utilisation des micros :  
		 le MS-DOS  
			 V1.0 : 1981
	 Utilisation des micros : Windows  
		 3 branches (principales)  
			 Windows 1 à 3.11  
			 NT, 2000  
			 95, 98, Me  
		 Fusion XP  
			 CE  
			 RT

3: PROCESSUS ET THREADS
-------------------------------------------------------------------------------------------------------------
PLAN DU MODULE
	 Les processus  
	 Etats des processus  
	 Préemption  
	 Les processus et les threads.

DÉFINITIONS
	 Programme = Ligne de code  
	 Processus = Code en exécution

NOTION DE PROCESSUS
	DEUX TYPES DE PROCESSUS:
		Utilisateur:
			Office, etc
		Daemon:
			Apache, samba, etc

CRÉATION DES PROCESSUS
	 Initialisation système  
	 Processus parent  
	 Requête  
	 Batch

CRÉATION SOUS UNIX / LINUX
 Unix : base processus  
	 Processus 0  
		 Processus 1 : Init  
			 /etc/inittab

CRÉATION PROCESSUS
	 Fork()
		La fonction fork() est utilisée pour créer un processus enfant à partir d'un processus parent existant. Elle crée une copie exacte de l'environnement de processus parent, y compris les données et les variables. Une fois qu'un nouveau processus est créé, il peut être utilisé pour exécuter un nouveau programme ou pour effectuer une tâche différente de celle du processus parent.  
	 Exec()
		La fonction exec() est utilisée pour remplacer le programme en cours d'exécution dans un processus par un autre programme. Une fois appelée, elle remplace complètement le programme en cours d'exécution dans le processus par le nouveau programme spécifié. Les données et les variables du processus en cours sont remplacées par celles du nouveau programme.
	Il est important de noter que fork() crée un nouveau processus indépendant, tandis que exec() remplace complètement un processus existant par un autre programme.
	![[Pasted image 20230115133311.png]]

CRÉATION SOUS WINDOWS
	 Une fonction Win32 s’appelant CreateProcess se charge à la fois de la création du nouveau processus et de sa personnalisation. Pour cela, elle utilise une dizaine de paramètres tels que  
		 Le programme à charger,  
		 Les paramètres de la ligne de commandes,  
		 Les éventuelles fenêtres à mettre en œuvre,  
		 Des paramètres liés à la sécurités,  
		 ...

LA FIN D’UN PROCESSUS
	 Les conditions suivantes peuvent entrainer la fin d’un processus:  
		 Normal exit (voluntary).  
		 Error exit (voluntary).  
		 Fatal error (involuntary).  
		 Killed by another process (involuntary).

PROCESSUS NORMAL EXIT
	 Fin de programme  
	 Intervention utilisateur  
	 Linux : appel exit  
	 Windows : ExitProcess  
	 Libération des ressources  
	 PCB effacé

PROCESSUS ERROR EXIT
	 Mauvais paramètre  
	 Fichier absent,...

FATAL ERROR - KILL
	 Bug  
	 Kill – TerminateProcess

ÉTAT DES PROCESSUS
	schéma !!!
	 Etat élu: Exécution  
	 Etat bloqué : ? ressources  
	 Etat prêt : ? processeur

PROCESSUS : CHANGEMENT D’ÉTAT
	![[Pasted image 20230115133239.png]]

IMPLÉMENTATION DES PROCESSUS
	 Changement d’état  
	 Récupération  
		 Sauvegarde du contexte  
			 Table des processus
	![[Pasted image 20230115133220.png]]

PROCESSUS : ÉTATS PARTICULIER
	 Initialisation  
	 Teminé  
	 Zombie  
	 Swappé  
	 Préempté  
	 Utilisateur  
	 Noyau

LA PRÉEMPTION
	![[Pasted image 20230115133007.png]]

PROCESSUS / THREAD
	![[Pasted image 20230115133028.png]]

LIMITES DES PROCESSUS
	![[Pasted image 20230115133058.png]]

CONCEPT DE THREAD
	![[Pasted image 20230115133119.png]]
	![[Pasted image 20230115133136.png]]

COMPARAISON PROCESSUS – THREAD
	![[Pasted image 20230115133155.png]]

4: La communication interprocessus
-------------------------------------------------------------------------------------------------------------
Objectifs
	◼ Comprendre la problématique de l'accès concurrent.  
	◼ Comprendre les algorithmes de résolution.  
	◼ Trouver des solutions optimisées.

Plan du module
	◼ Blocage et interblocage.  
	◼ Supprimer l'attente active.  
	◼ Les signaux.  
	◼ Les tuyaux

Blocage et interblocage:
Plan de la partie
	◼ Notion de ressources  
	◼ Exclusion mutuelle entre processus  
	◼ Définitions de la section critique  
	◼ Généralisation du problème  
	◼ Première solution algorithmique  
	◼ L'excès de courtoisie  
	◼ Nécessité d'utiliser d'autres méthodes

Notion de ressources:
	Définitions:
		❑ Une ressource désigne toute entité dont a besoin  
			un processus pour s'exécuter.  
			• Ressource matérielle (processeur, périphérique)  
			• Ressource logicielle (variable)  
		❑ Une ressource est caractérisée  
			• par un état : libre /occupée  
			• par son nombre de points d'accès (nombre de  
			processus pouvant l'utiliser en même temps)
	Utilisation d'une ressource par un processus:
		❑Trois étapes :  
			• Allocation  
			• Utilisation  
			• Restitution  
		❑Les phases d'allocation et de restitution doivent assurer que le ressource est utilisée conformément à son nombre de points d'accès  
		❑ Une ressource critique à un seul point d'accès

Interblocage, Famine, Coalition:
	Interblocage  
		Ensemble de n processus attendant chacun une ressource  
		déjà possédée que par un autre processus de l'ensemble.  
		R1 et R2 à  
		un seul point  
		d'accès  
		Aucun processus ne peut poursuivre son exécution  
		→ Attente Infinie
	Coalition  
		Ensemble de n processus monopolisant les ressources au  
		détriment de p autres processus  
		→ Famine  
		→ Attente finie mais indéfinie
	Conditions nécessaires à l'obtention d'un interblocage
		• Ressource critique : Une ressource au moins doit se trouver  
		dans un mode non partageable  
		• Occupation et attente : Un processus au moins occupant  
		une ressource attend d'acquérir des ressources  
		supplémentaires détenues par d'autres processus  
		• Pas de réquisition : Les ressources sont libérées sur seule  
		volonté des processus les détenant  
		• Attente circulaire : au moins un processus P1 attend une  
		ressource détenue par un autre processus P2, P2 attend lui-  
		même une ressource détenue par P1

l'exclusion mutuelle entre processus
	Les processus disposent chacun d'un espace  
	d'adressage protégé inaccessible aux autres processus.  
	Pour communiquer et s'échanger des données, les  
	processus peuvent utiliser des outils de communications  
	offerts par le système.  
	La manipulation de ces outils de communication doit se  
	faire dans le respect de règles de synchronisation qui  
	vont assurer que les données échangées entre les  
	processus restent cohérentes et ne sont pas  
	perdues.
	Un premier problème de synchronisation est celui de l'accès par  
	un ensemble de processus à une ressource critique, c'est-à-dire  
	une ressource à un seul point d'accès donc utilisable par un  
	seul processus à la fois.

Définitions de la section critique
	schéma !!!
	Section critique :  
	Partie d’un programme dont l’exécution ne  
	doit pas s'entrelacer avec autres  
	programmes.  
	
	Une fois qu’une tâche y entre, il faut lui  
	permettre de terminer cette section sans  
	permettre à d'autres tâches de jouer sur les  
	mêmes données.

Généralisation du problème
	◼ Repeat  
		◼ Section d’entrée  
		◼ Section critique  
		◼ Section de sortie  
		◼ Section restante  
	◼ Forever
	On retrouve cette problématique dans:  
	 Les bases de données  
	 Le partage des ressources (fichiers, connections, réseaux, ...)  
	 Les automates (exemple du GAB)  
	 Le Hardware (Disque dur, ...)  
	 Le développement (MMORPG, clients/serveur, ...)  
	 Etc...
	On peut envisager plusieurs types de solutions
		 Solutions matérielles  
			Masquage des interruptions
				❑Une solution pour réaliser une section critique est donc d'interdire  
				la prise en compte des interruptions durant l'utilisation de la  
				ressource critique.  
				❑ Mais cette solution présente des inconvénients majeurs :  
				Elle provoque l’attente de tous les processus car le processeur  
				est monopolisé  
				Elle ne peut s’effectuer qu’en mode superviseur  
			Il faut trouver une solution bloquant seulement les processus  
			concernés : solution algorithmique ou solution par le système  
			d’exploitation.
			schéma !!!
		 Solutions algorithmiques  
			Solution par logiciel
				Il existe plusieurs solutions algorithmiques permettant de  
				palier à la problématique (algorithme de Dekker, de Peterson, etc)  
				Blocage et interblocage  
				Solution par logiciel  
				Solution algorithmique  
				L'inconvénient majeur de ces solutions logicielles est  
				l'attente active. Il est donc nécessaire de trouver  
				d’autres méthodes.  
				Une autre solution est d'utiliser un outil de  
				synchronisation offert par le système :  
				→ les sémaphores.
		 Solutions fournies pas le Système

Supprimer l’attente active :  l'emploi des sémaphores
Plan de la partie
	◼ Définition d’un sémaphore  
	◼ Section critique avec sémaphore  
	◼ L’allocation de ressources  
	◼ Les lecteurs/Rédacteurs  
	◼ Le Producteur/Consommateur

Définition d’un sémaphore
	Un sémaphore S peut être vu comme un distributeur de  
	Jetons  
	❑ l'opération INIT (S, Val) fixe le nombre de jetons Initial  
	❑ l'opération P(S) attribue un jeton au processus appelant si  
	il en reste sinon bloque le processus  
	❑ l'opération V(S) restitue un jeton et débloque un processus  
	de S.L si il en existe un.

Section critique avec sémaphore
	schéma !!!
	Exemple réservation places d'avions:  
	P(Mutex)  
	Si nb_place > 0  
	alors  
	Réserver une place  
	nb_place = nb_place - 1  
	fsi  
	V(Mutex)
	schéma !!!

L’allocation de ressources
	-Accès à un ensemble de n ressources critiques  
	-Un deuxième problème de synchronisation est celui de  
	l'accès par un ensemble de processus à un ensemble  
	de n ressources critiques :  
	→ c'est une généralisation du cas précédent.
	N ressources exclusives de même type  
	Allouer une ressource = prendre un jeton Res  
	Rendre une ressource = rendre un jeton Res
	schéma !!!

Les Lecteurs/Rédacteurs
	Le contenu du fichier doit rester cohérent :  
	→ pas d'écritures simultanées  
	Les lectures doivent être cohérentes :  
	→ pas de lectures en même temps que les  
	écritures
	schéma !!!
	Ecriture seule - Lectures simultanées  
	Un écrivain exclut  
	→ les écrivains  
	→les lecteurs  
	Un lecteur exclut  
	→ les écrivains
	schéma !!!
	Un écrivain exclut les écrivains et les lecteurs  
	→ Un écrivain accède toujours seul  
	→ Un écrivain effectue des accès en exclusion  
	mutuelle des autres écrivains et des lecteurs  
	Sémaphore d'exclusion mutuelle Accès initialisé à 1
	schéma !!!
	Un lecteur exclut les écrivains  
	→ Un premier lecteur doit s'assurer qu'il n'y a pas  
	d'accès en écriture en cours  
	→ Le dernier lecteur doit réveiller un éventuel  
	Écrivain  
	NL, nombre de lecteurs courants, initialisé à 0
	schéma !!!

le producteur/consommateur
	schéma !!!
	Gestion en FIFO (ex : buffer réseau TCP)
		• Un producteur ne doit pas produire si le tampon est plein  
		• Un consommateur ne doit pas faire de retrait si le  
		tampon est vide  
		• Producteur et consommateur ne doivent jamais travailler  
		dans une même case
	• Producteur  
		Si il n'y a pas de case libre  
		alors  
		attendre  
		sinon  
		déposer le message  
		fi
	• Consommateur  
		Si il y a pas de case pleine  
		alors  
		attendre  
		sinon  
		prendre le message  
		fi
	On associe un ensemble de jetons aux cases vides : N jetons VIDE  
	deposer le message = prendre un jeton VIDE  
	On associe un ensemble de jetons aux cases pleines : 0 jetons PLEIN  
	prendre le message = prendre un jeton PLEIN
	• Producteur  
		Si il n'y a pas de case libre  
		alors  
		attendre  
		sinon  
		déposer le message  
		Nouvelle case pleine  
		fi
	• Consommateur  
		Si il y a pas de case pleine  
		alors  
		attendre  
		sinon  
		prendre le message  
		nouvelle case vide  
		fi
	On associe un ensemble de jetons aux cases vides : N jetons VIDE  
	deposer le message = prendre un jeton VIDE et génerer un jeton PLEIN  
	On associe un ensemble de jetons aux cases pleines : 0 jetons PLEIN  
	prendre le message = prendre un jeton PLEIN et générer un jeton VIDE
	Producteur  
	Si il n'y a pas de case libre  
	alors  
	attendre  
	sinon  
	déposer le message  
	nouvelle case pleine  
	fsi
		allocation de ressources cases vides P (Sémaphore Vide)
		une ressource case pleine disponible V (Sémaphore Plein)
	allocation de ressources  
	cases pleines  
	P (Sémaphore Plein)  
	une ressource  
	case vide disponible  
	V (SémaphoreVide)
	Consommateur  
	Si il y a pas de case pleine  
	alors  
	attendre  
	sinon  
	prendre le message  
	nouvelle case vide  
	fsi

En résumé
	❑ Les exécutions de processus ne sont pas indépendantes :  
	les processus peuvent vouloir communiquer et accéder de  
	manière concurrente à des ressources  
	❑ Le sémaphore S est un outil système de synchronisation  
	assimilable à un distributeur de jeton et manipulable par  
	seulement trois opérations atomiques : P(S), V(S) et Init(S)  
	❑ Il existe plusieurs schémas typiques de synchronisation à  
	partir desquels sont élaborés des outils de communication  
	entre processus :
		– l'exclusion mutuelle  
		– les lecteurs/rédacteurs  
		– les producteur/consommateur

Les signaux
Notions et sémantique

Plan de la partie
	◼ Définition et contexte  
	◼ Présentation des différents signaux  
	◼ Envoi de signaux  
	◼ Utilisation des signaux pour la  
	programmation  
	◼ Un exemple précis

Définition et contexte
	Signaux :  
	Un signal est une information atomique envoyée  
	à un processus ou à un groupe de processus  
	par le système d'exploitation ou par un autre  
	processus.  
	Le signal constitue un système de  
	communication entre processus qui peut les  
	amener à réagir en conséquence.  
	→ les signaux sont des outils qui permettent la  
	gestion des processus (par l'utilisateur, le  
	système ou un autre processus)

	Lorsqu'il reçoit un signal, un processus peut réagir  
	de trois façons :  
	 Il est immédiatement dérouté vers une fonction  
	spécifique, qui réagit au signal  
	 Le signal est tout simplement ignoré (si cela  
	n'est pas prévu dans le code du processus).  
	 Le signal provoque l'arrêt du processus (avec ou  
	sans génération d'un fichier core dump).

	Vous avez certainement toutes et tous déjà utilisé des  
	signaux :  
	❑ consciemment, en tapant Control-C, en employant la commande  
	kill, ou en utilisant le gestionnaire de tâches  
	❑ ou inconsciemment, lorsqu'un de vos programme a affiché  
	segmentation fault (core dumped).  
	Envoi de signaux :  
	❑ Depuis un interpréteur de commandes  
	Depuis un programme en C  
	Etc.

Présentation des différents signaux
	La liste des signaux sous Unix dépend de la version. On peut  
	néanmoins dégager un grand nombre de signaux communs. Voici  
	des exemples :  
	On peut aussi obtenir la liste des signaux du système avec kill -l.  
	SIGINT - provoqué par le caractère associé à intr sur le clavier du  
	terminal de contrôle, (Voir: stty(1))  
	SIGQUIT- provoqué par le caractère associé à quit sur le clavier  
	du terminal de contrôle, (Voir: stty(1))  
	SIGILL - Instruction illégale.  
	SIGFPE - erreur arithmétique, division par zéro par exemple.  
	SIGKILL - signal de terminaison, son gestionnaire ne peut pas être  
	remplacé.  
	SIGSEGV - violation mémoire.  
	SIGCHLD - terminaison d'un fils.

Les tuyaux (Pipes)
Notions et sémantique

Plan de la partie
	◼ Définition et contexte  
	◼ L’appel système  
	◼ L’implémentation d’un tuyau  
	◼ Redirections  
	◼ Synchronisation à l’aide des tuyaux  
	◼ Exemple du signal SIGPIPE  
	◼ Les tuyaux nommées

Définition et contexte
	Pipes :  
	Les pipes (tuyaux) permettent à un groupe de  
	processus d'envoyer des données à un autre  
	groupe de processus.  
	Ces données sont envoyées directement en  
	mémoire sans être stockées temporairement  
	sur disque, ce qui est donc très rapide.

	Tout comme un tuyau de plomberie, un tuyau de  
	données a deux côtés :  
	❑ un côté permettant d'écrire des données  
	❑ un côté permettant de les lire.  
	Chaque côté du pipe est un descripteur de fichier  
	ouvert soit en lecture soit en écriture, ce qui  
	permet de s'en servir très facilement, au moyen  
	des fonctions d'entrée / sortie classiques.

Caractéristiques :
	La lecture d'un tuyau est bloquante, c'est-à-dire que  
	si aucune donnée n'est disponible en lecture, le  
	processus essayant de lire le tuyau sera suspendu (il  
	ne sera pas pris en compte par l'Ordonnanceur et  
	n'occupera donc pas inutilement le processeur)  
	jusqu'à ce que des données soient disponibles.  
	L'utilisation de cette caractéristique comme effet de  
	bord peut servir à synchroniser des processus entre  
	eux (les processus lecteurs étant synchronisés sur  
	les processeur écrivains).

	La lecture d'un tuyau est destructrice, c'est-à-dire que si  
	plusieurs processus lisent le même tuyau, toute donnée lue  
	par l'un disparaît pour les autres.  
	Par exemple, si un processus écrit les deux caractères ab  
	dans un tuyau lu par les processus A et B et que A lit un  
	caractère dans le tuyau, il lira le caractère a qui disparaîtra  
	immédiatement du tuyau sans que B puisse le lire.  
	Si B lit alors un caractère dans le tuyau, il lira donc le caractère  
	b que A, à son tour, ne pourra plus y lire. Si l'on veut donc  
	envoyer des informations identiques à plusieurs processus, il  
	est nécessaire de créer un tuyau vers chacun d'eux.

	 De même qu'un tuyau en cuivre a une longueur finie, un  
	tuyau de données à une capacité finie. Un processus  
	essayant d'écrire dans un tuyau plein se verra suspendu en  
	attendant qu'un espace suffisant se libère.  
	 Vous avez sans doute déjà utilisé des tuyaux. Par  
	exemple, avec les redirections :lorsque vous tapez ls |  
	wc –l  
	L'interprèteur de commandes relie la sortie standard de la  
	commande ls à l'entrée standard de la commande wc au  
	moyen d'un tuyau.

	 Les tuyaux sont très utilisés sous UNIX pour faire  
	communiquer des processus entre eux. Ils ont cependant  
	deux contraintes :  
	 Les tuyaux ne permettent qu'une communication  
	unidirectionnelle  
	 Les processus pouvant communiquer au moyen d'un  
	tuyau doivent être issus d'un ancêtre commun(ex : le  
	processus de la console).

Synchronisation à l’aide des tuyaux
	 Un effet de bord intéressant des tuyaux est la possibilité  
	de synchroniser deux processus.  
	 En effet, un processus tentant de lire un tuyau dans  
	lequel il n'y a rien est suspendu jusqu'à ce que des données  
	soient disponibles.  
	 Donc, si le processus qui écrit dans le tuyau ne le fait pas  
	très rapidement que celui qui lit, il est possible de  
	synchroniser le processus lecteur sur le processus écrivain.

Les tuyaux souffrent de deux limitations :
	 ils ne permettent qu'une communication unidirectionnelle ;  
	 les processus pouvant communiquer au moyen d'un  
	tuyau doivent être issus d'un ancêtre commun.

	Ainsi, d'autres moyens de communication entre processus  
	ont été développés pour pallier ces inconvénients recontrés  
	avec la redirection :  
	 Les tuyaux nommés  
	(ex : fichier pipe Unix pour 2 processus les serveur de  
	courriels : le pour un courriel local, le MTA transfère via le  
	pipe le courriel au MDA qui va gérer également le stockage)  
	 Les sockets qui permettent une communication  
	bidirectionnelle entre divers processus, fonctionnant sur la  
	même machine ou sur des machines reliées par un réseau  
	(ex : socket TCP, UDP).

Les Pipes nommés
	 Comme on vient de le voir, l'inconvénient principal des  
	tuyaux est de ne fonctionner qu'avec des processus issus  
	d'un ancêtre commun.  
	Les tuyaux  
	Les Pipes nommés  
	 Pour s'en affranchir, il faut que les processus désirant  
	communiquer puissent désigner le pipe qu'ils souhaitent  
	utiliser. Ceci se fait grâce au système de fichiers.  
	 Un tuyau nommé est donc un fichier :  
	user@ubuntu$ mkfifo fifo  
	user@ubuntu$ ls -l fifo  
	prw-r--r-- 1 in201 in201 0 Jan 10  
	17:22 fifo

	 Il s'agit d'un fichier d'un type particulier, comme le montre  
	le p dans l'affichage de ls.  
	 Une fois créé, un tuyau nommé s'utilise très facilement :  
	user@ubuntu$ echo coucou > fifo &  
	[1] 25312  
	user@ubuntu$ cat fifo  
	[1] + done echo coucou > fifo  
	Coucou

Les tuyaux nommés
	Si l'on fait abstraction des affichages parasites du shell, le  
	tuyau nommé se comporte tout à fait comme on s'y attend.  
	Bien que la façon de l'utiliser puisse se révéler trompeuse,  
	un tuyau nommé transfère bien ses données d'un processus  
	à l'autre en mémoire, sans les stocker sur disque.  
	La seule intervention du système de fichiers consiste à  
	permettre l'accès au tuyau par l'intermédiaire de son nom.
	
	Un processus tentant d'écrire dans un tuyau nommé ne  
	possédant pas de lecteurs sera suspendu jusqu'à ce qu'un  
	processus ouvre le tuyau nommé en lecture.  
	C'est pourquoi, dans l'exemple, echo a été lancé en tâche  
	de fond, afin de pouvoir récupérer la main dans le shell et  
	d'utiliser cat.  
	(ex serveur mail : il faut créer le fichier pipe , configurer le  
	MTA pour écrire dans le pipe, et le MDA pour lire)  
	On peut étudier ce comportement en travaillant dans deux  
	fenêtres différentes.
	
	De même, un processus tentant de lire dans un tuyau  
	nommé ne possédant pas d'écrivains se verra suspendu  
	jusqu'à ce qu'un processus ouvre le tuyau nommé en  
	écriture.  
	On peut étudier ce comportement en reprenant l'exemple  
	mais en lançant d'abord cat puis echo.
	
	 En particulier, ceci signifie qu'un processus ne peut pas  
	utiliser un tuyau nommé pour stocker des données afin de  
	les mettre à la disposition d'un autre processus une fois le  
	premier processus terminé.  
	On retrouve le même phénomène de synchronisation  
	qu'avec les tuyaux classiques.

Résumé du module
	❑ Les tuyaux  
	❑ Le principe d’interruption et blocage  
	❑ Le principe de la section critique  
	❑ Les signaux  
	❑ La problématique de l’attente active







4: La communication interprocessus NEW
-------------------------------------------------------------------------------------------------------------
OBJECTIFS
	 Comprendre la problématique de l'accès concurrent.  
	 Comprendre les algorithmes de résolution.  
	 Trouver des solutions optimisées

BLOCAGE ET INTERBLOCAGE NOTION DE RESSOURCES
	 Définitions  
		 Entité Nécessaire au processus.  
			 Matérielle  
			 Logicielle  
	 Caractéristiques  
		 Son état  
		 Son nombre de points d'accès
	 Utilisation d’une ressource  
		 Trois étapes :  
			 Allocation  
			 Utilisation  
			 Restitution  
		 Points d’accès  
			 Ressources critiques

BLOCAGE ET INTERBLOCAGE GÉNÉRALISATION DU PROBLÈME
	 On retrouve cette problématique dans:  
		 Les bases de données  
		 Le partage des ressources (fichiers, connections, réseaux, ...)  
		 Les automates (exemple du GAB)  
		 Le Hardware (Disque dur, ...)  
		 Le développement (MMORPG, clients/serveur, ...)  
		 Etc...

La communication Interprocessus INTERPROCESS COMMUNICATION: IPC
 3 types d’évènements  
	 Processus 1 vers processus 2  
	 1 ressource – 2 processus  
	 2 processus liés  
 Remarque  
	 S’applique au thread

RACE CONDITION
 Exemple:  
	 Gestion de l’impression  
	 File d’attente (Spooler directory)  
	 In/Out
	![[Pasted image 20230115133438.png]]

EXCLUSION MUTUELLE
	 1ière piste de solution:  
		 Bloquer la ressource

RÉGION CRITIQUE
	 Accès ponctuel aux ressources  
		 = critical region ou critical section  
	 Solution  
		 Éviter 2 critical region simultanées
	![[Pasted image 20230115133458.png]]

CE N’EST PAS SUFFISANT
	 4 conditions  
		- Éviter 2 RC simulyanées  
		- ? Nbr et vitesse processeurs  
		- Processus hors RC non bloquant  
		- Pas de boucle indéfinie

DISABLING INTERRUPTS
	 Système à processeur unique  
		 Désactive les interruptions  
		 Exécution  
		 Réactive les interruptions  
	 Dangereux  
		 Boucle  
	 ? Multiprocesseur  
		 Conflit

LOCK VARIABLES
	 Lock = 0  
		 Ressource libre  
	 Solution type software  
	 Pas efficace (voir spooler d’impression)

STRICT ALTERNATION
	 Soit, les deux processus A et B ci-dessous
		![[Pasted image 20230115133515.png]]

INTERBLOCAGE
	Processus 1  
		 Début  
		 P(SR1);  
		 P(SR2);  
		 Utilisation de R1 et R2;  
		 V(SR2);  
		 V(SR1);  
		 Fin
	Processus 2  
		 Début  
		 P(SR2);  
		 P(SR1);  
		 Utilisation de R1 et R2;  
		 V(SR1);  
		 V(SR2);  
		 Fin

PETERSON’S SOLUTION
	![[Pasted image 20230115133531.png]]

TSL INSTRUCTION
	 Solution Hardware  
		 Idem Peterson  
		 Gaspillage CPU

INVERSION DE PRIORITÉ
	Processus High Level  
		 Début  
		 Calcul (10ms)  
		 Lire_disque (5ms)  
		 P(R1)  
		 Utiliser R1  
		 V(R1)  
		 Fin
	Processus Low Level  
		 Début  
		 P(R1)  
		 Utiliser R1  
		 V(R1)  
		 Fin

PRODUCER-CONSUMER PROBLEM
	 2 processeurs  
		 Producteur (doc à imprimer)  
		 Consommateur (deamon d’impression)  
	 1 ressource : le spooler d’impression (FIFO)  
	 Problèmes  
		 Spooler plein ou vide  
		 Variable Count (0 à N)

PRODUCER-CONSUMER PROBLEM
	![[Pasted image 20230115133549.png]]

LES SÉMAPHORES
	utilité ?
		Les sémaphores sont des outils de synchronisation utilisés pour gérer l'accès concurrent à des ressources partagées, comme les variables de mémoire, les fichiers ou les imprimantes. Ils permettent de gérer les conflits d'accès concurrents en donnant un accès exclusif à une ressource donnée à un seul processus à la fois.
		-
		Les sémaphores ont pour but de gérer les accès concurrents aux ressources, en évitant les erreurs de concurrence ou les conflits d'accès. Ils peuvent être utilisés pour gérer les accès concurrents à des variables de mémoire, des fichiers, des imprimantes, etc.
		-
		Les sémaphores sont généralement utilisés pour gérer les opérations de lecture/écriture, les opérations de synchronisation entre processus et les opérations de synchronisation entre threads.
		-
		Un exemple d'utilisation de sémaphore est lorsque plusieurs processus sont en concurrence pour accéder à une même ressource, un sémaphore peut être utilisé pour gérer l'accès à cette ressource de manière à ce qu'un seul processus puisse y accéder à la fois, évitant ainsi les conflits d'accès.
	 Signaux  
		 Full  
		 Empty  
		 mutex
		![[Pasted image 20230115133606.png]]
	 Signaux  
		 Full  
		 Empty  
		 mutex
		![[Pasted image 20230115133622.png]]


5: L'ordonnancement
-------------------------------------------------------------------------------------------------------------
Objectifs
	• Comprendre les objectifs et le besoin  
	d’ordonnancement des processus  
	• Découvrir les différents mécanismes  
	permettant l’ordonnancement

Plan du module
	• Définition. Définitions du problème et des objectif de l’ordonnancement.  
	• Les mécanismes . Présentation des différents algorithmes d’ordonnancement.  
	• La planification . Apprendre à déterminer les priorités d’ordonnancement.

1: Définition Problèmes et objectifs
	Plan de la partie  
		• Le problème  
		• Les objectifs  
		• Les critères d’ordonnancement  
		• Ordonnanceur et répartiteur  
		• Parallélisme réel et pseudo parallélisme

Le problème
	• Quand doit-on stopper un processus s'exécutant sur un CPU ?  
	• Quel processus va continuer sur ce CPU ?  
	• Mêmes questions pour les threads d'un processus.  
	• Que se passe t’il avec plusieurs processeurs ?

L’objectif
	✓ Maximiser le taux d'occupation du processeur  
	✓ Minimiser le temps de réponse des processus  
	Critères d'évaluations de l’ordonnancement :  
		• Temps d'attente des processus  
		• Débit du processeur  
		• Temps de réponse moyen  
		• Temps de traitement d'un ensemble de processus

Les critères d’ordonnancement
	Il y aura normalement plusieurs processus dans la file prêt  
	Quand le CPU devient disponible, lequel choisir?  
	Critères généraux:  
		• Bonne utilisation du CPU  
		• Réponse rapide à l’usager
	Il y a aussi des critères spécifiques d’ordonnancement :  
	Utilisation UCT: pourcentage d’utilisation (à maximiser).  
	Débit = Throughput: nombre de processus qui s’exécutent complètement dans l’unité  
	de temps (à maximiser).  
	Temps de rotation = turnaround: le temps pris par le processus de son arrivée à sa  
	fin (à minimiser).  
	Temps d’attente: attente dans la file prêt (somme de tout le temps passé en file prêt)  
	(à minimiser).  
	Temps de réponse (pour les systèmes interactifs): le temps entre une demande et la  
	réponse (à minimiser).
	Nous distinguons deux types d’ordonnancement (concerne l’ordonnancement a court  
	terme) :  
		• Les mécanismes non-préemptifs qui n’interrompent pas le fonctionnement d’un  
		processus : seul l’attente sur une entrée/sortie (qui peut stopper le fonctionnement  
		d’un processus) et la fin d’un processus peuvent provoquer l’appel de l’ordonnanceur.  
		• Les mécanismes préemptifs qui peuvent interrompre le fonctionnement d’un  
		processus ce qui suppose la mise en place d’un timer et des méthodes plus  
		complexes de gestion des changements de contexte.

Ordonnanceur et répartiteur
	Un processus est un programme en cours d ’exécution auquel est associé un  
	environnement processeur (CO, PSW, RSP, registres généraux) et un environnement  
	mémoire appelés contexte du processus.  
	-
	L'ordonnanceur est un programme système dont le rôle est d'allouer le processeur à un  
	processus prêt.
	-  	
	La politique d'ordonnancement détermine le choix d'un processus à élire parmi tous ceux qui sont prêts.
	-  
	Un processus dans un système multiprogrammé suit le graphe d'états suivant :
	![[Pasted image 20230115112645.png]]
	![[Pasted image 20230115112712.png]]


Parallélisme et pseudo-parallélisme
	![[Pasted image 20230115112743.png]]

Différence Parallélisme et pseudo-parallélisme
	Le parallélisme est la capacité d'un système informatique à effectuer plusieurs tâches en même temps. Cela peut être réalisé en utilisant plusieurs processeurs physiques ou en divisant une tâche en plusieurs sous-tâches qui peuvent être exécutées simultanément sur un seul processeur.
	-
	Le pseudo-parallélisme, d'autre part, est la capacité d'un système informatique à simuler l'exécution simultanée de plusieurs tâches en utilisant des techniques de programmation telles que la multitâche ou la multithreading. Cependant, contrairement au parallélisme, les tâches ne sont pas réellement exécutées en même temps, mais plutôt en alternance rapidement, donnant l'impression qu'elles le sont.

2: Les mécanismes

Plan de la partie
	• Premier arrivé, premier servi FCFS (ou FIFO) sans ou avec réquisition  
	• Plus court d'abord  
	• Par priorités constantes  
	• Par tourniquet (round robin)  
	• Par files de priorités de priorités constantes multiniveaux avec ou sans extinction de  
	priorité

FCFS : Premier Arrivé, Premier Servi
	• Pour comprendre cet algorithme « naturel », considérons les processus P1 (de durée  
	24UT), P2 (de durée 3UT) et P3 (de durée 3UT) arrivés dans l’ordre P1, P2, P3.  
	• Si nous reportons les différents processus sur le diagramme de Gantt, nous  
	constatons que P1 n’attend pas, que P2 doit attendre 24 UT et que P3 doit attendre  
	27 UT.  
	• Le temps moyen d’attente est donc de T = (0 + 24 + 27) / 3 = 17 UT.
	![[Pasted image 20230115112836.png]]

autre ex:
	• Si nous considérons les mêmes processus P1, P2 et P3 arrives dans un ordre différent  
	P2, P3, P1. Le diagramme de Gantt sera naturellement différent mais le temps moyen  
	d’attente aura également changé :  
	• Le temps moyen d’attente : T = (0 + 3 + 6) / 3 = 3 UT
	![[Pasted image 20230115112911.png]]

• Donc dans un sens FCFS favorise les processus tributaires du CPU et peut conduire à une très mauvaise utilisation des ressources tant du CPU que de périphériques.  

• Une possibilité: interrompre de temps en temps les processus tributaires du CPU pour  
permettre aux autres processus d’exécuter (préemption)

FSJ : le plus court d’abord
	Ce mécanisme consiste à sélectionner le processus nécessitant le moins de temps  
	d’exécution (le prochain Burst CPU le plus court). Il existe deux approches :  
		• Non-préemptive ; le processus qui prend le contrôle de l’UC ne le quitte qu’à la fin de  
		la rafale.  
		• Préemptive : si un nouveau processus arrive dont la durée prévue est inférieure au  
		temps restant d’exécution du processus en cours, ce nouveau processus obtient le  
		contrôle du CPU (on parle alors de SRIF, Shortest Remaining Time First)
	exemple :
		![[Pasted image 20230115113018.png]]
		![[Pasted image 20230115113100.png]]
		Si nous considérons la version préemptive du mécanisme, nous obtenons le  
		diagramme ci-dessous :
		![[Pasted image 20230115113258.png]]
		![[Pasted image 20230115113335.png]]
	Exercice 1:
		– Donner le diagramme de Gantt (FJS non-préemptif)  
		des processus suivants :
		![[Pasted image 20230115113425.png]]
		– Calculer les temps d’attente moyens
	 Exercice 1: Non-préemptif
		 ![[Pasted image 20230115113521.png]]
		 ![[Pasted image 20230115113539.png]]
	• Exercice 2:
		– Donner le diagramme de Gantt (FJS préemptif) des  
		processus suivants :
		![[Pasted image 20230115113617.png]]
		– Calculer les temps d’attente moyens
	• Exercice 2: Préemptif
		![[Pasted image 20230115113819.png]]
		![[Pasted image 20230115113832.png]]
		-
		![[Pasted image 20230115113923.png]]
		![[Pasted image 20230115113932.png]]
		-
		![[Pasted image 20230115113959.png]]
		![[Pasted image 20230115114010.png]]
		-
		![[Pasted image 20230115114029.png]]
		![[Pasted image 20230115114055.png]]
		-
		![[Pasted image 20230115114141.png]]
		![[Pasted image 20230115114156.png]]
		-
		![[Pasted image 20230115114213.png]]
		![[Pasted image 20230115114231.png]]
		-
		![[Pasted image 20230115114251.png]]
		![[Pasted image 20230115114308.png]]
		![[Pasted image 20230115114326.png]]
		-
		![[Pasted image 20230115114350.png]]
		![[Pasted image 20230115114403.png]]

Par priorité constante
	![[Pasted image 20230115114527.png]]
	Par priorités constantes
		• chaque processus reçoit une priorité  
		• le processus de plus forte priorité est élu  
		Avec ou sans réquisition (préemption)
		•  Exercice 3:
			– Donner le diagramme de Gantt (Priorité constante avec réquisition) des processus suivants :  
				–La priorité la plus élevée correspond à la valeur 1
				![[Pasted image 20230115114658.png]]
				– Calculer les temps d’attente moyens
		• Exercice : Préemptif
			![[Pasted image 20230115114807.png]]
			![[Pasted image 20230115114823.png]]
Par priorité : Rate Monotonic
	![[Pasted image 20230115115034.png]]

RR : le tourniquet
	• Ce mécanisme est particulièrement utilisé  
	dans les systèmes a temps partage. Le  
	planificateur alloue à tour de rôle à chaque  
	processus un quota de temps du CPU (10 –  
	100 ms).  
	• Le processus en cours peut s'interrompre  
	pour des raisons internes (ex : accès a un  
	périphérique, fin du processus, etc) ou  
	parce que le quota de temps alloué s'est  
	écoulé. Dans le second cas il est remis  
	dans la queue des processus prêts.
	exemple:
	![[Pasted image 20230115115101.png]]
	Un autre exemple
		Quantum = 4
		![[Pasted image 20230115115159.png]]


Par files de priorités constantes multiniveaux avec ou sans extinction de priorité
	• Chaque file est associée à un quantum de temps éventuellement différent  
	• sans extinction : un processus garde toujours la même priorité  
	• avec extinction : la priorité d'un processus décroit en fonction de son utilisation du cpu
	![[Pasted image 20230115115241.png]]
	![[Pasted image 20230115115300.png]]

Ordonnancement : système LINUX
	Trois classes d ’ordonnancement (norme POSIX) :  
		SCHED_FIFO : processus temps réel non préemptif                              +++
		SCHED_RR (Tourniquet (quantum)) : processus temps réel préemptif  ++
		SCHED_OTHER : processus classique                                                     +

Résumé du module
	Dans ce module, nous avons abordé :  
	• Les différents critères d’ordonnancement  
	• L’algorithme du « tourniquet »  
	• Les algorithmes avec ou sans réquisition  
	• Parallélisme  
	• Répartitions


Initiation aux systèmes informatiques:
-----------------------------------------------------------------------------------------------------------------------------
8 séances:
Séance 1: Initiation à la virtualisation
-----------------------------------------------------------------------------------------------------------------------------
	Objectifs
		Découverte de la virtualisation  
		Maîtriser la création et la gestion d’une machine virtuelle avec Oracle VM Virtual Box  
		Se familiariser avec la procédure d'installation d'un OS (Windows 10 et Linux)
	Quelques avantages de la virtualisation :
		• Consolidation d’infrastructure  
		• Facilité d'installation, importation et exportation des machines virtuelles d'une machine  
		physique à une autre  
		• Création d’environnement de test et de développement  
		• Économie sur le matériel (consommation électrique, entretien physique)  
		Parmi les inconvénients, on peut remarquer qu'en cas de panne d'un serveur hôte,  
		l'ensemble des machines virtuelles reliées au serveur seront affectées.
	Hyperviseur Type 1 et Type 2
		Un hyperviseur de type 1, illustré à la figure 1, s'exécute sur le matériel, il s'agit d'un  
		système très léger et optimisé pour la gestion de machines virtuelles. Ce type d'hyperviseur  
		est principalement utilisé dans les environnements de production.
		Un hyperviseur de type 2, illustré à la figure 2, correspond à un logiciel tournant sur l'OS  
		hôte. Cela est comparable à une simple application s'exécutant dans un contexte qui n'est  
		forcément dédié à l'hyperviseur. Oracle VM Virtual Box est un hyperviseur de type 2. Ce  
		type d'hyperviseur est principalement utilisé dans les environnements de test.
	Configurations liées au disque dur virtuel de la VM :
		Il est possible de créer une VM sans disque dur (très peu utilisé), de créer un nouveau  
		disque dur ou encore d'utiliser un disque dur virtuel déjà existant.  
		Pour en créer un nouveau, il faudra indiquer son emplacement sur la machine physique, sa  
		taille en Go et son type.  
		Un disque dynamiquement alloué grossira en fonction de l'utilisation du disque dur virtuel.  
		C'est un avantage de la virtualisation, si on choisit 10 Go mais que seulement 3 Go sont  
		utilisés, le disque virtuel fera 3 Go.  
		Une fois ces étapes complétées notre VM est créée et prête à l'emploi
	Il existe une alternative plus rapide à l'exportation-importation qui consiste à récupérer  
	uniquement les paramètres du disque dur virtuel
		On peut ensuite créer ensuite une nouvelle machine en utilisant un fichier de disque dur  
		virtuel déjà existant :
Séance 2: Partitionnement, dual boot et analyse hardware
-----------------------------------------------------------------------------------------------------------------------------
	Objectifs
		A la fin de la première manipulation, vous vous êtes familiarisés avec la notion de virtualisation  
		et vous êtes à présent capable d’installer un système d’exploitation de type Windows ou Linux.  
		L’avantage de la virtualisation est que vous allez pouvoir tester différentes manipulations sans  
		avoir la crainte d’abimer le support physique.  
		Dans cette manipulation, nous allons :  
		• Introduire les notions de disque dur, de partitionnement et de différence entre le BIOS  
		et UEFI, basé respectivement sur les schémas de partitionnements MBR et le GPT  
		• Se familiariser avec la procédure d’un dual boot, c’est à dire l'installation de deux OS  
		(Windows 10 et Linux) sur un même disque dur  
		• Récupérer des informations sur le matériel d'un ordinateur via divers logiciels
	-
	Master boot record (MBR)
		Le master boot record ou MBR (512 ko) est le premier secteur d'un disque dur qui contient des  
		informations permettant d'identifier l'emplacement et le statut d'un système d'exploitation afin  
		de l'amorcer (le charger) dans la mémoire principale ou la mémoire vive (RAM) de l'ordinateur.  
		Le MBR est subdivisé en deux parties :  
			• La table des partitions contient les informations concernant la localisation et la taille de  
			chaque partition sur l'espace global du périphérique de stockage. Elle définit les  
			informations suivantes :  
				o Type de partition (SWAP, NTFS, Linux, etc.)  
				o Statut : active ou pas  
				o Emplacement du 1er secteur de la partition  
				o Emplacement du dernier secteur de la partition  
				o Nombre de secteurs de la partition  
				• Bootstrap code qui contient soit le chain loader par défaut, soit un boot manager. En  
				effet, le secteur de démarrage est bien trop petit pour contenir le kernel d'un OS (Noyau  
				de système d'exploitation)  
		Chain loader : programme se contentant de charger en mémoire et de mettre en exécution le  
		secteur de démarrage de la partition marquée active dans la table des partitions.  
		Boot manager : Il s’agit d’un gestionnaire de démarrage. Il existe plusieurs boot manager.  
		Pour Linux, il y’a par exemple Lilo et GRUB. Mais aussi Isolinux pour les démarrages sur les  
		Cd's. Le boot manager est composé de deux parties :  
		La première partie du gestionnaire de démarrage est chargée en mémoire. C'est le morceau de  
		code qui a été placé dans le MBR. Il ne sert en général qu'à effectuer une seule action : charger  
		en mémoire et lancer l'exécution de la 2ème moitié du gestionnaire. Par exemple avec LILO  
		lors de cette étape s'affiche "LI". Si la suite ne s'affiche pas ("LO") c'est que le chargement de  
		la 2ème partie a échoué. Le phénomène est identique avec GRUB. Cela signifie que la 2ème  
		partie n'a pas été trouvée, parce qu'elle est abîmée, ou ne se trouve pas à l'endroit recherché.  
		La deuxième partie du boot manager va s'occuper de gérer les différentes actions possibles, puis décompresser, charger en mémoire et lancer l'exécution du kernel. Il va également s'occuper de l'éventuel ramdisk (initramfs). Le gestionnaire en passant des options au kernel, permet notamment de choisir entre plusieurs options de démarrage, de préciser au kernel l'emplacement de la racine, etc
		- résumé !!!
		Le MBR contient un programme de démarrage appelé boot loader qui est chargé en mémoire par le BIOS (ou UEFI) lorsque l'ordinateur démarre. Ce boot loader lit la table des partitions contenue dans le MBR pour déterminer quelle partition contient le système d'exploitation à démarrer. Il charge ensuite le système d'exploitation à partir de cette partition en utilisant un autre programme de démarrage appelé chain loader qui est généralement situé dans la racine de cette partition. Le chain loader termine par charger le noyau du système d'exploitation qui va finalement démarrer la session utilisateur.
		-
		Il y a généralement deux parties dans un programme de démarrage (boot loader) : la première partie est appelée le "stage 1" ou "bootstrap", c'est un code qui est exécuté par le BIOS (ou UEFI) lorsque l'ordinateur démarre. Il se charge en mémoire à l'adresse 0x7C00 et lit le MBR pour récupérer la table des partitions et déterminer la partition qui contient le système d'exploitation à démarrer.
		-
	La deuxième partie est appelée le "stage 2" ou "chain loader". Il est chargé par la première partie une fois qu'elle a déterminé la partition contenant le système d'exploitation. Il est généralement situé dans la racine de cette partition et charge le système d'exploitation en utilisant les informations de configuration contenues dans le MBR. Il est souvent utilisé pour gérer les systèmes d'exploitation multiples (dual boot) en permettant à l'utilisateur de choisir le système d'exploitation à démarrer lorsque l'ordinateur démarre.
	UEFI/BIOS
		Les nouveaux ordinateurs utilisent le microprogramme UEFI au lieu du BIOS traditionnel. Les  
		deux sont des logiciels de bas niveau qui se lancent au démarrage du PC avant la mise en route  
		du système d'exploitation. UEFI est cependant une solution plus moderne, prenant en charge  
		des disques durs plus gros, des temps de démarrage plus rapides, plus de fonctionnalités.  
		Le BIOS est l’acronyme de Basic Input-Output System (système élémentaire d'entrée/sortie).  
		C'est un logiciel de faible niveau qui réside dans une puce sur la carte mère de l’ordinateur. Le  
		BIOS est responsable du réveil des composants matériels, s’assure du bon fonctionnement, puis  
		exécute le chargeur de démarrage qui démarre le système d'exploitation installé.  
		Malheureusement, le BIOS traditionnel a eu quelques limites. Il ne peut démarrer qu'à partir de  
		lecteurs de 2.1 To ou moins. Or, les lecteurs de 3 To sont maintenant communs et un ordinateur  
		avec un BIOS ne peut pas démarrer à partir d'eux. Cette limitation est due à la manière dont  
		fonctionne le système de démarrage principal du BIOS.  
		UEFI remplace le BIOS traditionnel. Ce dernier est écrit en C, tandis que le BIOS l'est en  
		assembleur. UEFI fournit très souvent une émulation BIOS afin de pouvoir installer et démarrer  
		d'anciens systèmes d'exploitation qui s'attendent à un BIOS.  
		UEFI peut démarrer à partir de lecteurs de 2,2 To ou plus, la limite étant de 9,4 zettabytes. La  
		raison est que UEFI utilise le schéma de partitionnement GPT au lieu de MBR. Il démarre  
		également de manière plus standardisée, en lançant des exécutables EFI plutôt que d'exécuter  
		du code à partir d'un enregistrement de démarrage principal d'un lecteur.
		GPT est une norme plus récente qui remplace progressivement MBR. C'est ce qu'on appelle la  
		table de partition GUID. Chaque partition de votre lecteur possède ainsi un « identifiant  
		globalement unique » ou GUID.  
		De plus, si les données sont corrompues, GPT peut remarquer le problème et essayer de  
		récupérer les données endommagées à partir d'un autre emplacement sur le disque. MBR n'avait aucun moyen de savoir si ses données étaient corrompues.
		schéma !!!
	
	Partitionnement
		Le partitionnement est la façon d'organiser un disque dur en unités de stockages logique  
		appelées partitions.  
		Un disque dur est une unité de stockage physique. Afin de pouvoir utiliser un disque dur, on  
		définira une ou plusieurs partitions qui peuvent être destinées à un OS, ou à des données.  
		Par exemple une partition pour Windows, une pour Linux et une autre pour stocker des données.  
		De plus, lorsque plusieurs systèmes d'exploitation sont installés sur l'ordinateur, il est nécessaire  
		de définir plusieurs partitions, chacune contenant un système d'exploitation.  
		Une partition permet  
		• d'installer plusieurs systèmes d'exploitation sur une seule machine (multi-boot)  
		• de séparer l'OS des données (récupération plus facile en cas de crash de l'OS.  
		• de créer une partition dédiée au SWAP (mémoire virtuelle sur disque)  
		• de faciliter les opérations de maintenance (backup, défragmentation...)  
		• etc.  
		Il existe plusieurs types de partitions. Trois types de partitions peuvent coexister sur un disque  
		physique : primaire, étendue et logique. Le plus souvent, on définira une ou plusieurs partitions  
		primaires. En raison de la taille limitée de la table des partitions (qui doit tenir dans lsecteur  
		d'amorçage), il n'est possible de définir qu'un maximum de quatre partitions primaires sur un  
		disque dur. Donc, si l'on a besoin de plus de partitions, il sera nécessaire de définir à la place  
		de la dernière partition primaire une partition étendue. Dans celle-ci, il sera possible de créer  
		des partitions logiques. Une partition étendue ne sert donc que de conteneur aux partitions  
		logiques. Il ne peut y en avoir qu'une seule.  
		Les partitions primaires sont définies par le MBR. Vu le manque de place dans le MBR pour  
		stocker les informations, les partitions logiques sont chaînées. Donc, en cas de perte d'une  
		partition logique, l'information pour savoir où débute la suivante est perdue.
	
	Dual boot
		créer 2 partitions depuis windows
		pour le linux --> 
			Pour ce faire, lors de l'installation, utilisez un partitionnement manuel. Créez une partition  
			• Boot de 100Mo (système de fichier : ext4)
				Point de montage : /boot  
				Utilité : Il arrive que certains ordinateurs ne puissent pas à lire les fichiers de démarrage si ceux-  
				ci sont trop loin du début du disque. Il est alors préférable de créer une partition /boot en début  
				de disque. Mais cette partition /boot séparée n'est généralement pas utile sur une machine  
				récente  
				Taille : 100Mo~1Go  
				Type : on choisira généralement EXT4  
			• Swap de 1 Go
				Point de montage : swap (ne se voit pas à la racine)  
				Utilité : La partition swap est une extension de la mémoire vive (RAM) de l’ordinateur. Afin  
				d'éviter un blocage de l’ordinateur lorsque sa RAM est pleine, Debian se sert de cette partition  
				pour décharger temporairement la RAM.  
				Taille : La taille de swap fait idéalement le double de celle de la RAM, ici 1 Go  
				Type : SWAP
			• Home de 5 Go (système de fichier : ext4)
				Point de montage : /home  
				Utilité : Pour les disques durs suffisamment grands, une partition /home séparée permet d'isoler  
				les paramètres personnels et les dossiers personnels des utilisateurs du reste du système. Par  
				défaut, ce dossier fait partie de la partition racine.  
				Taille : Selon votre usage.  
				Type : on choisira généralement EXT4 pour une installation sur disque dur.  
				On remarque qu’il existe d’autres types de partitions telles que /var, /tmp, /usr etc. N’hésitez  
				pas à consulter les sources pour plus d’informations.  
			• Reste pour la racine (système de fichier : ext4)  
				Point de montage : /  
				Utilité : La partition racine est la base de l'arborescence du système Debian. Par défaut, si aucun  
				réglage n'est changé, c'est dans celle-ci que tous les fichiers vont être placés : fichiers de  
				configuration, programmes, documents personnels, etc.  
				Taille : Le minimum est 8 Go. Cependant, pour une question de confort, sa taille devrait être  
				d'au moins 15 Go. Si cette partition est pleine, le système ne pourra plus démarrer.  
				Type : on choisira généralement EXT4 pour une installation sur disque dur
		On remarque qu’il existe d’autres types de partitions telles que /var, /tmp, /usr etc. N’hésitez  
		pas à consulter les sources pour plus d’informations.
		- résumé:
			Voici un guide simplifié pour configurer un dual boot :

			1.  Créez 2 partitions depuis Windows :
			
			-   Une partition "Boot" de 100 Mo (système de fichier : ext4)
			-   Une partition "Swap" de 1 Go
			-   Une partition "Home" de 5 Go (système de fichier : ext4)
			-   Une partition "Racine" pour le reste de l'espace disponible (système de fichier : ext4)
			
			2.  Lors de l'installation de Linux, utilisez un partitionnement manuel :
			
			-   Utilisez la partition "Boot" pour stocker les fichiers de démarrage de Linux (point de montage : /boot). Cette partition est optionnelle et n'est généralement pas nécessaire sur les machines récentes.
			-   Utilisez la partition "Swap" comme extension de la mémoire vive (point de montage : swap). Elle est utilisée pour éviter un blocage de l'ordinateur lorsque la RAM est pleine.
			-   Utilisez la partition "Home" pour stocker les paramètres personnels et les dossiers personnels des utilisateurs (point de montage : /home).
			-   Utilisez la partition "Racine" comme base de l'arborescence du système Linux (point de montage : /).
			
			Remarque : Il existe d'autres types de partitions comme /var, /tmp, /usr, etc. Il est recommandé de consulter des sources pour plus d'informations.
	Diagnostic et analyse matérielle sous Windows
		De nombreux outils de diagnostic, d'analyse et/ou de benchmark sont également disponibles  
		pour Windows. Ils se distinguent par leur type de licence (freeware, open source, payant...) ainsi  
		que par leurs fonctionnalités (utilisation en réseau, collecte des informations dans une BD,  
		déploiement par GPO...). Il en existe beaucoup trop que pour pouvoir les tester tous. Un choix  
		parmi les plus « connu » vous est donc proposé :  
		• SiSoftware Sandra Lite (freeware)  
		• Aida64 Business (évaluation)  
		Testez les fonctionnalités de détection hardware de ces logiciels sur votre Windows fraîchement  
		installé. Découvrez également leurs autres fonctionnalités.  
		Sur le site web des éditeurs, vous trouverez également des comparatifs entre les différentes  
		versions de ces produits. Ce type de comparatif vous permettra de choisir en toute connaissance  
		de cause la version qui conviendra le mieux à votre utilisation.  
		Pour terminer, nous vous rappelons également que de nombreux outils inclus directement dans  
		Windows peuvent également vous apporter des informations sur votre plate-forme :  
		• le gestionnaire de périphériques,
		
		• l'outil de diagnostic dxdiag,  
		• msinfo32.exe.  
		Si ces outils ne vous sont pas familiers, c'est le moment de les tester
	
	Diagnostic et analyse matérielle sous Linux
		Deux possibilités s'offrent à vous : l'utilisation de la ligne de commandes (terminal) ou  
		l'installation d'un outil graphique. De nombreuses commandes sous Linux permettent de  
		découvrir le matériel. Attention, elles ne sont pas toutes installées par défaut.  
		En général, une application "Information système" est disponible pour l'interface graphique.  
		Récupérez les informations complètes sur le matériel à partir de cette application. Si besoin,  
		l'installer.  
		Dans certaines circonstances la ligne de commande reste la seule solution envisageable.  
		Vous trouverez, ci-dessous, certaines commandes incontournables dans la détection hardware  
		ainsi qu'une rapide explication de leur rôle. Vérifiez que leur utilisation procure bien les mêmes  
		résultats que l'outil graphique utilisé précédemment.  
		Dmidecode : informations bios et carte mère  
		lshw : liste le hardware  
		lspci : liste les contrôleurs PCI et les matériels connectés sur ce bus  
		lsusb : idem pour l'usb  
		lsscsi :idem pour scsi  
		lspcmcia : idem pour les cartes d'extension pour pc portable  
		lsblk : liste les périphériques de types bloc (ex : disque dur) et les partitions vues par le kernel  
		lscpu : liste les processeurs et les cœurs  
		cat /proc/cpuinfo : informations détaillées sur le(s) processeur(s) et cœur(s)  
		uname -a : informations détaillées sur le kernel  
		On remarque que certaines commandes ne sont pas encore installées. Il est possible de les  
		installer directement à partir du terminal.  
		Sous Debian, les logiciels se composent d'un ou plusieurs paquets. L'installation d'un paquet  
		(applications, bibliothèques, etc.) est une tâche qui s'effectue avec les droits d'administrateur.  
		Votre mot de passe vous sera demandé. L'utilisateur concerné sera obligatoirement  
		administrateur du système.  
		Pour ce faire il faut se connecter à l’aide de la commande su (super utilisateur) et entrer le mot  
		de passe de l’utilisateur root.  
		L’apt va alors pouvoir gérer les paquets Debian.  
		Ainsi pour installer la commande lshw il suffit de taper la commande : apt-get update && apt-  
		get install lsh
Séance 3: Initiation Red hat - 1 ière partie
-----------------------------------------------------------------------------------------------------------------------------
	$ = user normal, # = user root
	Consoles Virtuelles
		Si l'environnement graphique est disponible, il s'exécutera sur la première console virtuelle dans Red Hat Enterprise Linux 7. Cinq invites de connexion textuelle supplémentaires sont disponibles sur les consoles deux à six (ou un à cinq, si l'environnement graphique est désactivé). Dans un environnement graphique en cours d'exécution, ouvrez une invite de connexion textuelle sur une console virtuelle en appuyant sur les touches Ctrl+Alt et sur une touche de fonction (F2 à F6). Appuyez sur Ctrl+Alt+F1 pour retourner à la première console virtuelle et au bureau graphique.

Séance 4: Initiation Red hat - 2 ième partie
-----------------------------------------------------------------------------------------------------------------------------
	Objectifs
		Après avoir terminé cette section, les étudiants devraient être en mesure de comprendre les bases de la disposition et de l'organisation du système de fichiers, et l'emplacement des principaux types de fichiers.
	Hiérarchie du système de fichiers
		Tous les fichiers d'un système Linux sont stockés sur des systèmes de fichiers organisés dans une arborescence de répertoires _inversée_, appelée _hiérarchie du système de fichiers_. On dit que cette arborescence est inversée, car la racine de l'arbre se trouve en _haut_ de la hiérarchie, et les branches des répertoires et sous-répertoires s'étendent _sous_ la racine.
		-
		Le répertoire `/` est le répertoire root situé au sommet de la hiérarchie du système de fichiers. Le caractère `/` est également utilisé comme _séparateur de répertoires_ dans les noms de fichiers. Par exemple, si `etc` est un sous-répertoire du répertoire `/`, ce répertoire peut se nommer `/etc`. De même, si le répertoire `/etc` contient un fichier nommé `issue`, nous pouvons faire référence à ce fichier sous le nom `/etc/issue`.
		-
		Les sous-répertoires de `/` sont utilisés à des fins de standardisation, pour organiser les fichiers par type et par utilisation. Cela facilite la recherche des fichiers. Par exemple, dans le répertoire racine, le sous-répertoire `/boot` contient les fichiers nécessaires pour démarrer le système.
	Note
		Les termes suivants sont utilisés pour décrire le contenu des répertories du système de fichiers :
			- _statique_ : contenu qui reste inchangé jusqu'à ce qu'il soit explicitement modifié ou reconfiguré.
			- _dynamique_ ou _variable_ : contenu qui est généralement modifié ou complété par des processus actifs.
			- _persistant_ : contenu qui persiste après un redémarrage, en particulier les réglages de configuration
			- _runtime_ : contenu ou attributs spécifiques à un processus ou au système, effacés lors du redémarrage.
	Principaux répertoires Red Hat Enterprise Linux
		Emplacement    Objectif
		`/usr`
		- `/usr/bin` : _commandes utilisateur_.
		- `/usr/sbin` : _commandes d'administration du système_.
		- `/usr/local` : _logiciels personnalisés localement_.
		`/etc`
		Fichiers de configuration spécifiques à ce système.
		`/var`
		Données variables spécifiques à ce système, qui doivent persister d'un démarrage à l'autre. Les fichiers qui changent de manière dynamique (par ex. les bases de données, les répertoires cache, les fichiers journaux, les documents du spool d'impression, le contenu des sites Web) se trouvent dans `/var`.
		`/run`
		Données d'exécution des processus démarrés depuis le dernier démarrage. Cela comprend les fichiers d'identification et de verrouillage des processus, entre autres. Le contenu de ce répertoire est recréé au redémarrage. (Ce répertoire regroupe `/var/run` et `/var/lock`, présents dans les versions plus anciennes de Red Hat Enterprise Linux.)
		`/home`
		Les _répertoires personnels_ où les utilisateurs standard stockent leurs données personnelles et leurs fichiers de configuration.
		`/root`
		Répertoire personnel du super utilisateur administratif, root.
		`/tmp`
		Un espace ouvert à tous pour les fichiers temporaires. Les fichiers qui n'ont pas été ouverts, changés ou modifiés depuis 10 jours sont automatiquement supprimés de ce répertoire. Il existe un autre répertoire temporaire, `/var/tmp`, dans lequel les fichiers qui n'ont pas été ouverts, changés ou modifiés depuis plus de 30 jours sont automatiquement supprimés.
		`/boot`
		Fichiers nécessaires au lancement du processus de démarrage.
		`/dev`
		Contient les _fichiers de périphériques_ spéciaux, utilisés par le système pour accéder au matériel.
	 Important
		 Dans Red Hat Enterprise Linux 7, quatre anciens répertoires `/` ont désormais un contenu identique à celui de leurs homologues de `/usr`:
		- `/bin` et `/usr/bin`.
		- `/sbin` et `/usr/sbin`.
		- `/lib` et `/usr/lib`.
		- `/lib64` et `/usr/lib64`.
		Dans les anciennes versions de Red Hat Enterprise Linux, il s'agissait de répertoires distincts, qui contenaient des ensembles de fichiers différents. Dans RHEL 7, les répertoires de `/` sont des liens symboliques vers les répertoires correspondant de `/usr`.
	Note
		Pour obtenir un descriptif des répertoires du système de fichier, utiliser la commande : man hier		
	Localisation de fichiers par leur nom
		Interpréter et utiliser correctement la syntaxe des chemins d'accès complet et partiel.
	Objectifs
		Après avoir terminé cette section, les étudiants seront en mesure d'utiliser correctement les noms de chemin absolus, de changer de répertoire de travail et d'utiliser des commandes pour déterminer l'emplacement et le contenu d'un répertoire.
	Chemins absolus et relatifs
		schéma !!!
	Chemins absolus
		Un _chemin absolu_ est un nom _complètement qualifié_ qui commence par le répertoire root (`/`) et qui spécifie chaque sous-répertoire traversé pour atteindre et représenter de manière unique un fichier. Chaque fichier d'un système de fichiers possède un nom de chemin absolu, reconnaissable à une règle simple : un nom de chemin qui commence par une barre oblique (`/`) est un nom de chemin absolu. Par exemple, le nom de chemin absolu pour le fichier journal des messages du système est `/var/log/messages`. Comme les noms de chemins absolus peuvent être longs à taper, on peut aussi localiser les fichiers de manière _relative_.
		Lorsqu'un utilisateur se connecte et ouvre une fenêtre de terminal, l'emplacement initial est normalement le répertoire personnel de l'utilisateur. Les processus système ont également un répertoire initial. Les utilisateurs et les processus naviguent à travers les répertoires au besoin ; les termes _répertoire de travail_ ou _répertoire de travail actuel_ font référence à leur emplacement _actuel_.
	Chemins relatifs
		Tout comme un chemin absolu, un chemin _relatif_ identifie un fichier unique, ne spécifiant que le chemin nécessaire pour atteindre le fichier depuis le répertoire de travail. L'identification des noms de chemins relatifs suit une règle simple : un nom de chemin qui commence par un caractère quelconque _différent de la barre oblique_ (`/`) est un nom de chemin relatif. Un utilisateur dans le répertoire `/var` peut se référer de manière relative au fichier journal des messages de cette façon : `log/messages`.
		Pour les systèmes de fichiers Linux standard, le nom de chemin d'un fichier, y compris tous les caractères `/`, ne doit pas dépasser 4095 octets. Aucun des composants du nom de chemin séparés par des caractères `/` ne doit pas dépasser 255 octets. Les noms de fichiers peuvent utiliser n'importe quel caractère Unicode encodé en UTF-8, sauf `/` et le caractère `NUL`. (Les caractères ASCII requièrent un octet ; les autres caractères latins, grecs, hébreux ou cyrilliques prennent deux octets ; les caractères restants dans le Plan multilingue de base Unicode en prennent trois ; et aucun caractère ne prendra plus de quatre octets.)
		Les systèmes de fichiers Linux —y compris mais non limités à ext4, XFS, BTRFS, GFS2 et GlusterFS—sont sensibles à la casse. Le fait de créer `FileCase.txt` et `filecase.txt` dans le même répertoire génère deux fichiers uniques. Bien que de nombreux systèmes de fichiers non Linux soient reconnus par Linux, chacun respecte des règles uniques de nommage de fichier. Par exemple, le système de fichiers VFAT, omniprésent, n'est pas sensible à la casse et ne permet la création que d'un des deux fichiers d'exemple. Cependant, VFAT ainsi que les systèmes de fichiers NTFS de Microsoft et HFS+ d'Apple présentent un comportement de _conservation de la casse_. Bien que ces systèmes de fichiers ne soient _pas_ sensibles à la casse (mise en œuvre principalement pour prendre en charge la compatibilité ascendante), ils affichent bien les noms de fichiers en respectant la casse d'origine telle qu'elle était à la création du fichier.
	Chemins de navigation
		La commande **pwd** affiche le nom de fichier complet de l'emplacement actuel, ce qui permet de déterminer la syntaxe appropriée pour atteindre les fichiers à l'aide de noms de chemins relatifs. La commande **ls** affiche la liste du contenu du répertoire spécifié ou, si aucun répertoire n'est indiqué, celle du répertoire courant.
![](data:image/png;base64,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)
		Utilisez la commande **cd** pour changer de répertoire. Dans le répertoire de travail `/home/``user`, le chemin relatif est le plus court pour atteindre le sous-répertoire `Videos`. On parvient ensuite au sous-répertoire `Documents` en utilisant le chemin absolu.
		![](data:image/png;base64,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)
		L'invite du programme shell n'affiche, par souci de concision, que le dernier composant du chemin d'accès au répertoire courant. Pour `/home/student/Videos`, seul `Videos` s'affiche. À tout moment, vous pouvez retourner au répertoire personnel de l'utilisateur en utilisant **cd** sans spécifier de destination. L'invite affiche le caractère _tilde_ (`~`) lorsque le répertoire courant de l'utilisateur est son répertoire personnel.
		-
		Normalement, la commande **touch** met à jour l'horodatage d'un fichier à la date et à l'heure courantes, sans rien y modifier. Cette commande est utile pour créer des fichiers vides, qui peuvent être utilisés pour des exercices pratiques, puisque l'exécution de la commande touch sur un nom de fichier qui n'existe pas entraîne la création de celui-ci. Avec **touch**, on crée des fichiers d'exercices pratiques dans les sous-répertoires `Documents` et `Videos`.
		![](data:image/png;base64,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)
		La commande **ls** comporte de multiples options pour afficher les attributs des fichiers. Les options les plus courantes et les plus utiles sont `-l` (format de liste long), `-a` (tous les fichiers, y compris les fichiers _masqués_), et `-R` (récursif, pour inclure le contenu de tous les sous-répertoires).
		![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAd8AAADMCAIAAAC9Vz6OAAA4V0lEQVR4nO2dB1gURxuAP+nVhqiIKChWLAj2XrDFir39Gisq2DC22LtiNxZULIgiYAU1dhMTNZbYxdiNiklEBQVRLMg/wx7HcdzO7e0tx6Lf6z4+e7e7s98Nu9/OtnlNXr9+DQD58uUDBEEQRDaY5HQACIIgiAYwOyMIgsgRzM4IgiByBLMzgiCIHMHsjCAIIkcwOyMIgsgRzM4IgiByREN2Hv3DuF9/+z1PnjxzZ874rlVLw8fEoK1356cxMWSkR9cuk8aPy6l1zZgz93ls7NqVK7I1AD1Zs279hk2bv3z5MnhAf79hQ7POMGzkKOE/QSY1jyDfDprbzt+1bDlv9kwDh6LK1evXN2zcfO3GDTLuWc194g8/ODgUJeMH9u4m/w8Z7meAGAy5Lo5GXi1IGu3auZMkpQ33GUKGnn378c2Q+uWL8NK+7ppHEBkixysbx06cnLswYLSfLzlCpKamBodsI628naHbTE1Nczq0rwFSpVtCtu2NjCLt08YtWjmXLPHj+PFly7jmdFwIgmRCaHZWO5cnLbLaNWuO8vPlPoaE7gjfuYvMkDdv3hqeHgvmzFYueODnQ5uCt5JEULRI4c7e3n179zIyMuIm7dy9Z9XawEXz5y1evuLho0cF8udfvjjAsVixWfPm/bRsqXuVKtxsZC1n/jh38c9LdevUZkRIkg5ZUcSu3S9fvXIqXnzIwAGql2XIlytWrT599mzS2yQXF5fhPoMbNWhAvr9y9dq6oKC/7txNSkoqWaLEgO/7tmnVSmCdrN+4KTQ8gqy3i3fHEcOHCQlDY0UlJibWb+rFzTBnwUIykJHpk3/s1LGDwEh0Yl/U/pDtoZvWBy5csnTxgvmXLl02MTHWs0zGBoAgiDgkaDufu3Bh6YqVAfPmVq1S+dWruN9Pn1ZO2rMvcvGy5ZMnTSCp9u/Hj6fNmmNmatqrR3flDO+Tk1evWz998qRSLi537t61trbef/Dn6h4eZH6SLpcsX3nx0qVyZcsULVLkSUxMXWYYkfsPBG4ImjpponvVKkeOHZ80dRpJjpUruZFJycnJA4YMtTA3J1nDoajD7Tt3njyN4ZaKfRFbp3btEb7D8+XNe/rsH5OnzShW1KGae1Wtv/rqtWskm29Ys/r8xYuLli6rV6eORzV3dhh8FWVra3vt4nmQ+soGH9F//VWxQnnnkiXJuLWVVcMG9fUskLEBIAgiGgmyc0zMMwsL8/p161haWha2t69QvpxyEslTgwb051qjpFFMGs57IiNVs/OHDx/G+492q1iRjLtXpTmRtHBJpiMjcxcEJCa9Xbl08b37D36cNr1mjersMEgzlrRS27dtQ8YHD+j/y6nfQsPD51eaRT4ePnY85tmzA3t3F3NwIB9LOBVXLtWyeXPleI+uXfZFRf12+rSQ7GxrYzvefww5DyjjWnpb6I7rN29y2ZkRBqOiRPD6zRtyVCBnFZYWFm1at+rcsSM5tkUdPFizenX2ZYq6tWuNmzQ5aPOWhITElJQUY2N9G87S/i4EQTgkyM6NGzUk5/JtOnaqXbOmm1vFls29CtnZke/j4uLJqS7JtmRQzkx2YNVlTU1NK5Qvr/rNi5cvixQpkpqaeuLXX8O3bSVNPBdn52MnTmoN42nMU+/27ZQfK5Qr+9ftO9w4aSwXd3TkUrMabxISNgdvJe3fly9fkVSVkJhYuVIlIb+aBKa8RFOgQH5SjtYw+CpKHGfOni1SuPCygIVx8XHkhOO7jt5fvnwhJXdIOzAwaNq48aL58yJ277577179ps2aN23mP3pkfj06KRT9u0K2hy5d+RM3vmbF8jq1a4mOAUG+PoRm5zx58qh+TEnJuN1PdsXIXRF/Xr5y+erVsIiI9Rs37QnfYVewYCqkkqnLFgU0bdyIr1hyZq3MccoVcc8SkARtbmbOfUmaZgKjVI6mpqp8TE1Vi1/JxClT37x+M3bUKCen4qQVOWrsuC/CnmQwVrtWS9enJQy+ihKyuqy0btlSWXXNmjRJTEz8kpqaL29eIcuSvwgZho0c5Tds6Ox586fPmr1iyWJxYYAev6t9u7b16ymuVxUtUkR0AAjyVSI0O+e1tX348BE3TvIXaRSrTiVN4Dq1apLh+z696zf1unL1mlfTJmT/JOe5Fy5eZGTnrDgUdXj67BlJpo0a1N8SEjJ+rP/fjx+f/PVUubJllfNYWVkmf/igtqBTcSfSRlZ+vH33rvIKRvny5SN27/n33/+4x/KUkB9y/sLFRfPnVvf0IB8/ffoU8+xZ+XJlVefRuC4GjDCAp6IyppqZfv78WeCK1I5qtra2woNU4lahQueOHVeuWSNwfr7aYP8uPsixhHE40bXmEeQrQ2h2dqtYMTQ84uGjRy7Oztt3hCWkn8hD2gNwr+LiqntUs7GxOXrsOEmsrqVLcZN8Bg+atzDA3t6eJOiPHz+S5lVcXJzy8QaN1K5ZI+rgwd49uk+ZNHHhoiXtOnUp7uhYs7qnmcrjdFUqVdoeHvHX7Tv29oVsbWzMzWnLukfXLvMXLfasVo27HRd969aEH/y5+Vs199q0JXjM+PH+I0cWK+bw4OHDf/75t2f3biTBlXByOnfhYpNGjUimJmfZqr+LsS4GjDAYFcXhXLLkb2fOtGze3NrG2tTERC3/SsWWkG3kwOnpUY2co/z3/PmhI0c93N0FLquxNrT+LnHoWvMI8pUhNDuTptD5ixf7DRpsY23T9rvWqg1Msk9uDwtbtTaQtD1dnEsuWbiAex6A0MW7o6WFefC20MANQZYWFmXKuPbs1o29ojatW5FT48gDBzq0bcv3RgxJrHfv3x/g4/Pu3fspEydwDzl4d2j/8tUrEgb5nyT0OTOmV61cmZvfwsJi0/rAFatWj5885V1SEglv+FAfbtLCubPnLVzU/Lu2ZOdv3bIFyVlC1sWAEQajojjIwWPO/AWt2rX/8PFj9j1RR1YaGha+ZMXK+Pj47r3/V69OnfFjxwhcVmNtaP1d4tC15hHkK0NodibtuKmTJpKB++ibnt0I3Ckt34JtWrcmg8ZJZH/LusuRLLkkYMGI0f5///2YZLpiDg5x8fHWBCsr5TyWlpZZn6glTbYhAweQQeO6CtnZzZ4+Lev35cqWDd64gS94vnXNmDJZ9eOOrcFCwmBXFKFihfKhW7cwZpCExg0bkIGMDPUbEbjqJ52W1VgbWn+XODSuC0G+HTRkZyMj4yPHjx87eXLWtKmkOWn4mNwqVAjfFrJ561bfUWNiX7wgTbPZ06ayX0VBskLOVzZuCU5JSWlQr57GGfJkz5UTBEEkQUN2XhqwwPBxqGFvX2j8WH8y5HQguZihgweRgTGDzHtxQpBvHDn2s4EgCIJgdkYQBJEjmJ0RBEHkCGZnBEEQOZJj2Rn9FwiCIAw0ZGdx/VjqupSe/oujx4+PmzS5Qf16q5YtFVcCgiCInMmVVzae/fPPytVry7iWzulAEARBsouM7Mw2dPApP9hL6WMe4SMlJWXC5CmjR/iRYPQsCkEQRLZkZGe2oYNP+cFeSrR5hMFPa9aSRO/VtAlmZwRBvmKEXtlgKD8YiDaP8PHHufOHjx7btWO76BIQBEFyBUKzM0P5wUC0eUQj8fHxU2bMnDd7po2NjehCEARBcgW63BXkM4/wI9o8opE79+69fPXKb7Si8w2uo/oa9RpE7dqp1q0+giBIbkdDdtZo6GArPzQuJbl5xL1KlX07w5Ufp8+aQ1Y6ZeIEe/tCAktAEATJLWjIzhoNHQzlB99SkptHLCwsXJydVT+amZupfoMgCPLVoCE7azR0MJQfjKUkN48gCIJ8I2jIzhoNHWzzCN9S4swjAlm/ZpW4BREEQeRPrnxXEEEQ5KsHszOCIIgcweyMIAgiRzA7IwiCyBHMzgiCIHIEszOCIIgcYWXntt6dO3VoP+D7fgaLBkEQRHL2XQbvlZAYCDYWOR2KLmDb2XDs239gb2TUg4cPyXj5cmV9fXz07EwVkYSb0dErV6+9EX0T6N+l3KplS62trdmLfPj4MWjT5kNHjsbGxubPn79qlcr+I0fmSGcvIoL/99//VqxeHX3r1pOnMd4d2s+YMlnIJAar1gZu2LRZ+dGuYMGTRw6pzSNcZvQ5BUwH0hEzE3AsAK2rwNT2UDSfkEDEU8gP5nSGoU2ydy26gtnZcBw5dqxOrZo+AweYmZlt2bbNx29EWMjWUi7OOR3XN839Bw8G+Axr3LBhwLx5tjbW9+4/ENK9V8DiJb/+fnq8/+jSpUq9ePnq1G+/xcXHGT47iwv+fXJygQIFhg4eFLghSPgkNqVcXBbMUfQnbGKinlVEyIwmtYUeteD2vzD/ANSaBZdngt231zFlpnr89OnToqXLDx4+bGxk1KdnD7VZd+7eQw6Si+bPW7x8xcNHjwrkz798cYD/+ImDB/Tv0slbdc75AYvI32P54kX9h/gUd3ScP5v+2T5+/Pi/AYPI1jxv1gxGgW4VK/LF+vnzZwMXKC1rV65QjpO2c/2mXqfPnNGanWfMmfs8Nla5bM++/WrXrDnKz5f7GBK6I3znLjJD3rx5a3h6qL54eeDnQ5uCtz6NiSlapHBnb+++vXtxXaaA7hUlnzAkZ/3Gze5VqgTMm8N9dK8q6Gzm2ImTQwYN5Lovdy1dmhx0Vafy/eQfp04nSdzOzu70mbMkhfXp1bN/3/8ZPniyyU0YSzvJCQ5R7yedMYkjKSnpbVISOV0wNzNT/d7Cwrxc2bIaFxEnMyqcF6o40aFpBSgxFlYchVnpvTyEnIWFB+H+c3CygyGNYWwrMEo/JC07AqtPQEwcFLSBxuUhdKiGkh++gGYLoU1V+KkPvHkPBYYrvh8WTAfChv4wqBEdSU2FBQdh7Un47w2ULgxTO0Cv2oqZ+6yD2ATaov/5Opgaw5iWMP474T9OKJmyc9DmLYeOHiG5iSSsZSt/IhlWbW5yaF29bv30yZPIofLO3bvkHMq9apXrN26qZefrN296NW1Ktr+AeXO79/7fvqj9Hdu3W7pi5YcPH6ZOmsAukBVrThSYTSS+fZuamkraKfoUcu7CBRIz+QnkzPrVq7jfT59WTtqzL3LxsuWTJ00ge+/fjx9PmzXHzNS0V4/uyhl0qqhcEYY4Lvz5Z69uXUf/MO7q9RuF7e27dencxbuj1qXy5ct76fKVrp28s/bbxf7Jf5y/MHXSxDkzpv91+87AoUNLlijRtHEjAwevD1u3h5Jm9bJFAWphP3z0d8NmzY1NjMnBdcwIP9LEUU7SU2ZUyBbqusKxaEV2DjoF/jtgbT/65Z3/YMBGMDeBkWmSj+PR8EMYhA+HOq7wPAEOXtNQGlmEpObedWBhN/oxvxWkbklbi6YrG5tPw8x9sO57qFsGIi5A70AobQ+10k8ASEiB/SB4MFx+DI0XQNmi0NFDxO9jkSk7h+/a3bNbt0YNGpDxKZMmtmrXQW1ukrzI2RzXuuEO1NXc3cN37oS0P8+6oKCZU6fkMTK6e+/+uDFjyJcORYuSDXH85Cmv37zZG7V/2+ZNlpaW7ALZGL7AbGJ14DrSTmnZ3EufQmJinpE2S/26dUjMZOesUL6cchLZhQYN6M9ZHB2LFSPNtz2RkappUdeKkn8YIiAnT/Hx8cHbQwf06ztsyOA/L1+Zu2ChjbV1qxbN2QtO+/HHiVOnNW7R0sO9Wu2aNVq1aKHsxpb9k8k3XFOmYoXyzZs2i9i1S3R2Fh285FRyc5sxZXIJp+KxL15u2Lip36Ahe8PDuAqRRGbkkB9+va0YnxkJk9vR9EpwsQf/ljRfc9n5QSxYmdPr1Nbm9IK1R0n1cm7EQMeV4NsMpqknNs38dIyuqF99Ok5WGnkZVh6D7enZmazdJy2bezpDl+qw5kR2ZufExETyxy5Xtgz3sWiRIvnyqV+KNzU1rVC+vOo31dyrLli0+O3btyd//fXX336/eOmyrY11njx53NwU56cNG9T37tCetMSnTJyQ9cJT1gI5QraHLl35Eze+ZsXyOrVrKScZuMDsYO36DWSr3RK03izz6aGuNG7UkJxBt+nYqXbNmqTCSa4vZGdHvo+Li38eG7ti1WoyKGdWO+rwVVTuDUMEnAuiSuVKA9MeTCLn5mf/OLcvKkprgqtR3fNw1L7LV69evnL1wKHD5A/60/KlntWqaf3JJUo4qY5fvHTJ8MHrAzkMkEHty8YNG3AjbiQhVK3Som37ffv3Dx7QXyqZkVGeNN0H0IsJMXEwcScdlFinn7108ICFP0PpceDlBjVcoHst9XuJrZdAYjK4lxC63vuxMKBhxsdqJWkzWUmZIpnGlccPCcnIznnS7ieoXtHPenXf2spKedFQEVbp0uRs9MbNaLJlDOzX98wffxQrWtStQgXlZSlyhL9x8yZJQ2RTztpBaNYCOdq3a1u/Xl1unBwnVCcZuEDJIa3mPZFRQYFrnIoX1z53+t9FSUpKhlyGJMHIXRGk0UQiD4uIWL9x057wHXYFC6YC3Zaznn6qwldRMg9DWsgfnQTgUjKjleVU3PH8xYtCliXHlVo1apBh6OBBw0eNXrdh4/o1q7T+ZFVDRUpKCje/4YPPPvLnz1/MweHp0xiQTmb0LB6KF6QjXGXtHam5lUpy8e35cOoO/H4HVp2AOfvh5lwokjdjhqW9aPu6fxBcm60oUCuqGz05Qqh+/JSSMf75i+L4IS0Z+Zcc3woUKPAkrVoJpDkcFxendXmya1WtXPnchQtx8fHk9K3vwMGlS7moPii2dMXKhITE7Vs2fz94yO59+zp37CgkrHx585JB4yQDF0hOKRLfvi1YoICFhQSPSpJ1kRO9zesDSzg5aZ87jby2tg8fPuLGSXOJNM1Up5IcUadWTTJ836d3/aZeV65e82rahGTGwvb2Fy5e1OeapjzDkJwKFco/efpU+fHZv/8WKVxYpxLIccuxWLFbf9G2k9af/ODhQ5KUjY2Nyfidu/dKOgluyGlC/+B1Revu8CYh4Z9//23WpDFIJDN6mQhn79NbfwSSah0LwIlbvNcQzEyguRsdfmhNb/edvgudq2dM7VYDLEzp4r0C4ZeJYKzSKjA3yZRtOVwLwxWVxvLVJ+Cq0q6LfkYf/jOhf0m49gTKZMMDO5lax927dI7YtatV8+Z2dgXJyZpAByDJxZu3hrRv8x3J72TBM2f/mJ/+bM2JX37ZuWdvyKagsmVcp0+eNHXGrEpubuXKlBEdruEL3LYjTONtEBEELFm6L2r/nJnT379/f+fuXUhraGjdndwqVgwNj3j46JGLs/P2HWGqfpljJ06+iour7lGN1PzRY8dJmnAtrbgb4zN40LyFAfb29iTsjx8/koYtOdaOGD5MdPAyCUNyunXuNGHy1O1h4fXq1L505crpM2fnzpyhdakhw/3q161DNhXyk8kZQ9T+A4P6f89NYv/k16/fLFq6rEe3rlevXT/1++/Kxy0MGTzZr+/dv09Gkj98ePMmgWyKpBnOOYYYkzg07g4TJk9p1KCBo2OxuLj4TcHBJsbGnHxDH5lRbAK9THz7X5i3H+xtYXQLxffTOoBvCBTLD96ekPwJTt2G2ESY25lO2nWR3gxsVA7yWdGbeOSUrFKWs1OSTEOHgvtUertvlsp5cjkHehexe03Ia0mfweASt28z8AuBhuUUdwUvPoIVvTMWefUWxuwAPy84cw/2X4Ww4err0p9M2ZlsYaQJ3KlHj/z58nk1bUpaBEKK8KjmvmptIHfdoGG9ehf/vMTd3ol59mzarDkjfYeXL0dvE7Vs3vz8hT/HTfxxR0gwOSMTEav8C2RDWs1J796NGZfxTEiXTt5TJ01kL0UaoeR0td+gwTbWNm2/a60qZiSpYXtYGKn8T58+uTiXXLJwgXP6eW4X746WFubB2+gddksLizJlXHt266ZP8DIJQ3LIH/31mzch23cs/2kVOSWf8MPY71q11LpUg3p1jxw/vn7TZvKTizkUHTp40Pfpz8axfzJJo2Qb6N6nL9nAhvsMadZEr/cfxAWflJTUrbci2sdPnpz89Vfy94rcFcGexODLl9QlK1a+efOGnGBVrVJ55tSpAlMHg/kHYPEhxdsoJCMrH3Ye0hiszGDJYZperc3pI3d+6XfWSVJecQym7IaPn6G8A+zyhXKa2rOl7GFNX+i3AZpWpE/dcSzqDkODoeRYmvGVT9QNbEifpZuyh/5PlgoeTJ8GUdKyEr2K7TENbC1gpjd08tTzF2sgU3Ym56eTJ4wnA/dR+TQrR9fOnTRelvWsVu3axfPc+P969yIDN17c0fHMLydU55w2eZKQAvkwfIHAcxtEHFlfoBKCkZERyeDKJO471Ec5ibuYwLdgm9atyaBxkq4VJZ8wsoPuXbqQQadFVLfzrDB+somJyezp08igW4j8iAje1tZWucMKn8ShcXdYNH+ukPUKlBmR5i33lBsfferSISvcNQ2NdPTIVGbWEjyd4eJ09aXy5IEp7emgEVMT2DKIDtkHviuIIAgiRzA7IwiCyBHMzghiIObNnpnTISDSsM1H+zz6g9kZQRBEjmB2RhAEkSOYnREEQeQIulEQBEHkCLadDQe6UXIQhkNkX9T+oM1b/nv+vJSzs//okbVr8j67rcSQbhQhm41w8wgwBShCLCc6RVi1Ri21mRs2qP/T0iWM0nLEjSI5kshWMDsbDnSj5BQMh8jps2enz57jO9SHTN0eFjZyzNhdYaFae0ExpBtF62ajq3mELUBhW050jTBie4hytrdJSYOH+bb0EtRrLrpRAN0o6Eb5FtwoDIfI9rDw6p4eQwYOANpr86TTZ87u2rPXf9RIdoGGdKOwNxsR5hG2AIVhOQEeNwojQtWiSFXbWFs392omJEg+NwrDV0IgX07cCYeuQ8J7qFCMvmDdzp1+P2gTxMTD4bGK2arPoL2MLugK5x5A/bm0E+cDV2F0S7j8N+0IdEIbmNhGMSefh4UU+PgVVCwG4echJZVO4vr6eP2OJVsBYfYWJehGQTfK1+9GYThEbtyM7tld0Q+GsbFxlcqVbkRHay0wp9woWTcbPc0jWWFYToDfjcKIkIN8SY7f7du1NdexT3M1NwrDV/LuIzSaD5amNOWVtIMrT2hW1UrKF/qet5sjTIiAjQNpJ9F+IVRDRbIww8NC+OUv2un+PytoQm+2EFpVhgZltchWhNhbVEE3CrpRvnI3CsMhQiYlJiYWLFDg0JGjcxcGrF+9qmDBgg/SO0plkFNuFLXNRhLziCoMy4m4CJWcPXfuydOnXTM34wSi6kZh+EpIM/bhC7i3EJzT4nUtwlNcFtq60+5ASXYmDe0PnyDpA+22lDTeGR4WSOtNiXOjkNZ9mSK0Gd6A95RDgVZ7ixroRkE3ir7IJAw+GA6R1LQu01NSUqytrByKFiHHmM+fPgkpM0fcKGqbjVTmEVX4LCfKGdidgjE27B0RO2tWr06a+SKiUrpRgOkrufKYZkxnHQ4lFGMj2mWohSkdJ+1u7nbE+09aPCwE1RXltYS4t9rXpdXeoga6UdCNIgiZhCEChkOEHBtsbW3j4uL69OxBDtLkm/jXb+zsBGkzDOxGybrZSGUe4UPVciIuQiUxz56dOftHwDxBXdllRelG4eDzlaRmnqRK5o0XUrR1XJ+aqsXDArTXxsyLaCmSotXeoga6UdCNkpvCEAfDIVK5ktuly1e4cZIur1671qF9O50KN4AbReNmI4l5hIGq5UQJ3+7A3rDDdu4iizRp1DDrJK2oulGA6SvxKAmBv9CbdSXt1AspYAW3ninGv6TSO4Ra0ephYaNRtgLa7C1qoBsF3SiCkEkY4mA4RHr36O47akzQ5i2NGjQIDQ9/n5ws5NqoId0ofJuNaPMIQ4DCZzlRonF3YG/YycnJZGqPrl0EPp/HwedGYfhKuteij3N0WgmLetDLDtHP4O+XMCLtAniNUvTy9K1/oIIDLD8C8UmCYmB4WLSiUbYixN6iCrpR0I0iCJmEIQ6GQ6R+3bozpkwm2ZlESIJfuXSJkNMaQ7pRxG02DBgCFHGWE3aEBw4dJmvsnP6QjED43CgMX4mVGZyaRC8T91hDrSXlima4qTp5wokG9OG5fJa0332BWm6Gh0UrGmUrAu0tStCNgm6U3BSGaBgOEe8O7cmgU2mGdKMI3GwEmkeAKUDRajnRuDuwIySHqy66pGa2G4XtKymaT7OshDRdA/vRgWN2+kZXuzR83kRHSK7kVmpjocWiwhE0INPHP2eoz6BRtsKwt2gE3xVEEASRI5idEQRB5AhmZwQxEOhGQXQCszOCIIgcweyMIAgiRzA7IwiCyBF0oyAI8u3iOp52TgRp77ms0t6fq5jyBzXK6JJUJ7DtbDjQjSJPGNoUPgzpRmEjIniGG4UxiYEQo4pwe4uB3Sj3A+j/XgHZVb4+YHY2HOhGkSEMbQoDQ7pRGIgLnuFGYWtTGLCNKrraWwDdKGmgGwXdKF+/G4UBQ5vCwJBuFMmDZ7hR2NoU4HGjANOoIsLeArq7UUr4076YfTK/GO8XAo9ewEF/XpUJG4aH5fRdmBVJO/hPeA9li9ILF1w30ISPn2HMDth+lr6gOLqlepnoRkE3CrpRhMLQpjDIKTeKJMHrA58bhWFU0dPeItCNUq8M7f9eLTuTb5Q9wGlUmbBheFiexUOLSjCvC02yh67D/9bTjvHqpxU47wDsOAchPrQbkPHhtCcmJehGQTcKBd0oQmBoU9gL5pQbRZLgJYdhVJHE3iLEjUIy4+q0LnP++oe2ajcOpH32X38Ky9J7QxGhMmF4WLqrqMZ9m8Gm3+DANUV2XnOCdozH+QwDv6cdISlBNwq6UdCNIhSGNoW9YI64UaQKXh809oLEZ1SRyt4ixI1CMuOIbfDmPey9BFFXaDbPZ0kvwtdwUcwpQmXC8LDEJVEb7Ilb9KLH5xSIf6doU79+By8SoWp6H3hOBTNdLkc3CrpR0I0iFIY2RSsGdqNIG3z2oWpUkcreIsSNUrk45LWA8w/gyE2Y2BYOX4eShaC6s0JJBaJUJnzrIvQKhFdvYXEPagMwMYYOK2in/pAuYTE1zlhKdRzdKBIXiG4UWYUhOQxtikAM4EbhQ//gdUXr7qBqVJHE3iLQjULa13Vc6YXd2AQqZq03h94DrK/t2oUSGwt4/1H9S751kURMWs3hw+ltPUi7DfjwBW1ZE0iD3d42wwVO2vKxCZnKRDeKlAWiG0VWYUgOQ5vCwJBuFMmDZ7hRGJM4NO4OfEYV0fYWEOVGIbk44GfoW4+mSNIgPXwDtjOfiFCldml6TfnyY2pCIYtbmrHWRY4EJHGTI0FHD6ooHBee6TrJ8Gaw5qTiqsWMvZkchuhGyckC2aAbJafcKAwY2hQGhnSjSB48w43CmMRAnFGFjQg3SoOyVDvyXRU63qYq/HKbPsghkBFe9BZio/nwNhnW9oOhTbSsa8cw8N0KjqNpHu9ZGxqp3Dr5sS09tFSaTGMm7WIX+4xJ6EZBN4oCdKMIhKFN4cOQbhQ2IoJnuFEYkzg07g5ajSocAu0tot0opJGrXNC/FR2UaFWZWJtrePSYsS73EnBmiuYIzUxgTV86cCzomjEJ3SgIgiBfA5idEQRB5AhmZwQxEOhGQXQCszOCIIgcweyMIAgiRzA7IwiCyBF0oyAIIke+pMKwYPoGR1wSffRY7am4bwFsO0vMth1hUQcOxsTEQJ48Zcu4+gwapHwWWIhCAhGIRtfGvqj9QZu3/Pf8eSlnZ//RI2vXVNT8m4SEFT+t/u3M6TdvElxLlxo9wq9WjRrKpWTuRpFcZcJeSkRtAH/NM3YHrRy4CsGn6WPFpQuDuRSJqpAfzOmseNMkV4DZWWLMTE179+xe3NExD+TZExnpN3rMjq3BZLvkprIVEohANLo2Tp89O332HN+hPo0bNtweFjZyzNhdYaFcfyYzZs+5e+/+gtmzCxcuvC8qym+0/+70SfJ3o0iuMmEsJa42GDXP3h3Y3P2Pvivo6Sz8l31tyM6NIivZigi6dcmQLlSpXOngocN/Xrqk3BwZCgk+ZCIlkUkYwO/a2B4WXt3TY8hAegI87cdJp8+c3bVnr/+okeSv/NvpM+PHjiFTyaSRvsOPnTi5NzKKC17+bhR9VCa6Fqi1NjS6UfhqHrTtDnwM2gQbf1OM5/me/q+8ssHwlfAJUF6/o/0NcQwLpgNhQ38qY+XQyVdiSGTnRpGbbEU07969j9i9OzU1tZJbxsubDIWECGQiJTFwGHyujRs3o3t2V/RoYWxsTHLBjehoMp7yhWJqYqqc09zc7OatW9x4rnajSI7W2tDoRuGreVU07g58kERMBpKFg04prKxKGL4S4BGg5LdSvOGt8cqGrr4SQyI7N4rcZCsiePDwYZeevUlGyJc376rlS8nGyn3PUEiIQyZSEkOGwefaIA3kxMTEggUKHDpydO7CgPWrVxUsWPBBWpenpJVHDhs79+ypX69uITs70rAlm1ap9KVyrxtFcsTVBqPmOfh2B3EwfCUgSoCiq6/EkMjOjSI32YoInIoX3xm67U1CQtT+AzPnzAsKXEOaSMCvkBC9IplISQwWBsO1kZomz0hJSbG2snIoWoQcLT5/+qScOmvatKkzZjb/rq2RkRE5OWverOmjR39DLnejSI6Q2sjaCxK75oF/dxAHw1cCogQouvpKDIns3Chyk62IgBTlWppmebK7du3Vm2QucgagNo+qQoKNTKQkcgiD7dqwtbWNi4vr07MHOdyS7+Nfv7GzUxg1yPlK8MYN5OSa/CPR+o4aU7gI7VY7V7tRJEdcbZB6YNQ8CNsddILPVwKiBCi6+koMiezcKHKTrejpRvnyJfX9++Ss36sqJNjIREoihzDYro3KldwuXb7CTSKJ7+q1ax3at1Nd3MrKkgz/PX/+x/nzY0aO4L7M1W4UydFaGxp3B601r4RvdxAOn69ECOYm8ClFw/c6+UoMiRzdKLKSrejkRiE1Nm7Sj02bNC7u6JicnHzg50P3HzwY7qM4E+RTSLCRiZREDmGwXRu9e3QnjeKgzVtIJYeGh79PTu6afm/5ZnT0X7fvlC1b5tWruNWB68jJk7Lm5e9G0UdlomuBWmtD4+7AV/Ps3UEcDDeKVso50Jt+3WvSix6mxmCc1tDW1VdiSOToRsm9shWSmKytrAPXb3ge+4I0J12cSy6aP1fpvxCnkJCJlEQmYTCoX7fujCmTSY4g6yJhrFy6RClvNDY2idi9+/HjJySh16ldizSclX9f+btRJFeZMJYSVxt8Nc/eHcTB8JVoZVF3GBoMJcdC8qeMJ+p09ZUYEjm6UeQjWwEd3Shkc5w1fSrfVIEKCTVkIiWRSRiqZHVteHdoT4asc1YoX25nKO8TwTJ3o+ijMhGxFLs2+HYHjTXP3h20MrENHbKUyesr0SpA8XSGi9PVv9TVV2JI8HU1BEEQOYLZGUEQRI5gdkYQA4FuFEQnMDsjCILIEczOCIIgcgSzM4IgiBxBNwqCIN8EMXHg5E8fqqvuktOhCAPbzoZj3/4DeyOjHjx8CNQ6UdbXx0f1DXUkp5C5G4WNiOAll60Ikf5odNloJOgUDN5Mn0E+Oo5+TPkCxcfQd0/0z6rW5rRzu0K2ehViSDA7G44jx47VqVXTZ+AAMzOzLdu2+fiNCAvZWsrFOafj+qaRvxuFgbjgJZetgDbpj0aXDQNLM7j5DP55DcXyw7FoabRVhALWsGWQNEUZBtm5UfRRmcjBjcJAKRaBtLZz/aZep8+c0ZqdZSIlkUkYkiN/N4rkwesjW9HoRgGm9IfPZcPAKA90rQHb/4BxrWHrGehTF+buV0watAli4uHwWMXH6jNoz58Luio+8llObsZA5fR+8bK2wUnDfOJOOHQdEt5DhWIw0xvauQuMNHuRnRuFFWuucqOwSXz7NjU1lbRT9Cnk23SjSEuudqOIC14fNLpRgCn94XPZsPlfXRiwkXpMjt6EY+MysjMDhuWkUnGqR+GuO6vx7iM0mg+WpjSVl7SDK0/g/nPhYWYvsnOjsMkVbhQhrA5cR9opLZt76VPIN+hGkZZc7UYRHbzkMKQ/fC4brZDm7acU2jlRczewFdZ3rzjLSfh5ePgC7i1U9NwvvD9SAyA7NwqHaJWJHNwoWlm7fgPZarcErTfLfHqoK9+aG0VycrUbRXTw+qCxFyQ+6Q/DZSOEPnVpdj6YpbXLhzjLyZXHtK87VamKfJCdG4VDtMpEDm4UNqTVvCcyKihwjVNxQf3IykFKIp8wpCVXu1H0CT77UJX+sF02Wosa2BBszKGFG/z9MuNLtbueKpuhSMtJambZiqyQnRuFQ7TKRPIC9XSjZF0XOdHbvD5Q2fWwVuQgJZFPGJKTq90o+gevK1p3B1XpD9tloxWSbUe1UP+ygBXceqYY/5JK7xCqIsJy4lESAn+Bx6/oRWe5IUc3CgOZu1HYBCxZui9q/5yZ09+/f3/n7l1Ia2ho3Z3kICWRTxiSI383iuTB6yNb0bg78El/2C4bcdQoRSXct/6BCg6w/AjEJ2VMEmc56V4LFhyETithUQ96fSP6GW2qj9DrfpBkyNGNwof8C2RDWs1J796NGZfxTEiXTt7K/uz5kImURCZhSI783SiSBy+5bEWc9EccnTzhRAOoPxfyWdIL0+4q5x4My0mrJXDkhmK8RlpHgW6O9LoHwcoMTk2iT9T1WAOJyXSRWdl+dVMocnSj8CF/NwqbrC9QCUEmUhKZhJEdyNyNwkZE8PrIVjTuDgKlP1ldNhoZ1EjhlFLiWoQ+D8dhbASB/ejAMVtl82FYTpTPR2ukaD6ZvqWC7woiCILIEczOCIIgcgSzM4IYCHSjIDqB2RlBEESOYHZGEASRI5idEQRB5Ai6URAEyWXkOsuJOLDtbDjQjSJP0I0iZBIDad0ohKHBsO4XOmJsRHuba1WZPtdcWKUjBnGWk0J+MKcz7ZU0t4DZ2XCgG0WGoBtF4CQ20rpRCCXs4MgPtJOjK49hdCjcew4nVfpdz3WWE3GgGwXdKOhGQTeK9kkchnGjEEyN6dvYkPbK9T+vYUIE7VKDJGURlpPX72iPSBzDgulA2NBf8UYiW7YS+At9NTzCF8buoJ172NvC3pG0e1JCyFlYeJB21e9kB0Maw9hWVOnCwado0RV0o6AbBd0o6EYRisHcKKpYp9Vx8if6vwjLSX4rxYvg4q5skGKn7YH1/aFiMbj6BPKmddYddAr8d8DaflDXFe78RzUu5iYwMq1jbYaiRVfQjYJuFHSjoBtFL7LDjcLxJRWuP4XlR2lD2CG/lpmzyXLy/iMs66VoL9dL77xyZiRMbge969BxF3vwb0nzNZedxSlaNIJuFHSj6ItMwhABulF0xWBuFJLjTAZAaipN0KQRGjRA+yLZZDkxMwFP50zfxCbQxvvEnXRQYp1+EiVO0aIRdKOgG0UQMglDWtCNIjlSuVGcCsLP/mBiTJufAr2C4iwnDNkKB1m7UeZ5uL/Z3pHQ0UNDgeIULRpBNwq6UXJTGJKDbhSdMJgbhbRYhfSdr4pWy4m5CTXJqsGWrWiEpFpyzDhxS3N2BlGKFo2gGwXdKIKQSRiSg26U3OVGYaDVclLOgd6j616T3tkzNaYPUwNTtsJgWgfwDYFi+cHbk96uPHUbYhNhbmc6SZyiRSPoRkE3iiBkEobkoBsld7lR9LGcLOpO33MpOZbmU+UTdQzZCoMhjenqlhyGmfvoFecqTuCXfhhgKFp0Bd0o6EbJTWFkB+hGETKJwwBuFIJSfZIVfSwnns70EWk1GLIVwtAmvE/gkVTep66G7xmKFl3BdwURBEHkCGZnBEEQOYLZGUEMBLpREJ3A7IwgCCJHMDsjCILIEczOCIIgcgTdKAiCfA18HwQvE+HAGA2TXMfTjjsIvs1glaZOW+UpW8G2s+FAN4o8QTeKkEkMDO9G0ZX7AfR/rwDeGcTJVrIbzM6GA90oMgTdKAInsTGwG0Vy5ClbQTcKulHQjYJuFO2TOHLcjcJWmXz+AkM2Q+g52hYe4QVT2mtfkQjZisFANwq6UdCNgm4UoeS4G4XN8WgY3hQuzYTzD2DwZihThHaNxEaEbMVgoBsF3SjoRkE3il7IxI1CsLOBpT1pr9DlisLhG1TupzU7M8gm2Ypw0I2CbhR9kUkYIkA3iq7I2Y1CIEncxFgxXsUJfvlL19VmIptkK8JBNwq6UQQhkzCkBd0okpPdbhS2ykR1Yqr4qk0vQZRsRULQjYJulNwUhuSgG0UnctyNwlaZ3PoHPqcoms83Ymh3+6rYWFCFq3C0ylayG3SjoBtFEDIJQ3LQjZK73Chslcmrt+C/A3y96F3B3X/CNp9MU2uXpstefkydJvkswVLbZUWtspXsBt0o6EYRhEzCkBx0o+QuNwpbZeLlBu8/ged0+pjH9A7QtUamqSSxXn9KH8N4mwxr+ym61ddHtpLdoBsF3Si5KYzsAN0oQiZx5LgbhaEyUb5OsqG/5mVJyg4dqv6lPrKV7AbfFUQQBJEjmJ0RBEHkCGZnBDEQ6EZBdAKzM4IgiBzB7IwgCCJHMDsjCILIEXSjIAjy7aJVm5KDYNvZcKAbRZ6gG0XIJAbSulF6rKWdw2VlekeY0VFIOLqhVZvCoJAfzOmseKslO8DsbDjQjSJD0I0icBIbCd0oC7vBxDZ05Pe7MHIb7B2p6CWuqHqPmV8/6EZBNwq6UdCNon0ShwHcKCXtFL0OxaR1wlbeQSFJURJyFhYepB3hO9nBkMYwthUY5YFzD+jr3b3rwIGrMLolXP4bfr0NE9ooEn2fdRCbQPP7z9epdWVMSxj/nfZITt+FWZG00/2E91C2KC2KlE94/Q4KDFfMMyyYDpD2guKg9K5HNEbIsewI7XWa/LSCNtC4vIZ3F1VBNwq6UdCNgm4UoeSIG0WVoFO0n6O1/aCuK9z5DwZsBHMTGJnWo3XKF+joQXvJmBABGwdCBw/wC6FZmMuMx6Lp+9/Bg2kvSI0X0GxLZmbzLB5aVIJ5XWgmPXQd/reeHjbql4X8VlSnAjxXNhgRHo+GH8IgfDjtsfp5Ahy8piUAdKOgGwXdKOhG0Yvsc6NkZWYkTG6naMO62IN/S5oNR6b/4rbutCc5kp3bucOHT5D0AV4mKmTeZGaftDTq6QxdqsOaE9qzs6pXxbcZbPoNDlyj2Vl0hA9iwcocWlehPX44FqA9lLJBNwq6UfRFJmGIAN0oumIwN4pGYhPoNYGJO+mgxDr97MXYiF61sDCl45amio7z36fbCMuoKDfI+K+3ta8uLoleoDhxi7pfP6dA/DuopS09sCMkzfmFP0PpcbQvvRouNPuzL6ajGwXdKIKQSRjSgm4UyZHKjaIRrrL2jtTe7M1YJL2CP6VkfPn5iyBzSq9A2mH04h7gWpj26N9hBe3vX58ISS6+PR9O3YHf78CqEzBnP+2qtIhmKQgF3SjoRslNYUgOulF0wmBuFI2QROZYgDZmhWdnJdHPMrQp155AmcxHh6zaFJKIyYrCh9N7d4SPn6kBtlrmaxHmJpmSvpAIzUyguRsdfmhNby2evgudq/PGjG4UdKMIQiZhSA66UXKXG2VaB/ANoXITb09I/gSnbkNsIsztrH1B0goeswP8vODMPdh/FcKGZ5qaVZtilIc2mY9H0zxLThTHhUPcW/UyyznQO3vda0JeS3pRxdhIS4S7LtKbgY3KQT4riLhAmraa7VxK0I2CbhRByCQMyUE3Su5yowxpTJUlSw7DzH30em4VJ5pwhdCyEvWbeEyjDtmZ3tSxoopGbcqOYeC7FRxH02TdszY0ynJ/ZFF3GBoMJcfSLKx8oo4RIUnKK47BlN20JV7eAXb5Ut8KA3SjoBslN4WRHaAbRcgkDsO4UTjauiseXFOjT106qEEav5830RGS9bilbCwyLW5qQi0nfKITjdoU9xJwZgorQk9nuDhdaIQE7pqGcPBdQQRBEDmC2RlBEESOYHZGEAOBbpScYpuP9nlkCGZnBEEQOYLZGUEQRI5gdkYQBJEj6EZBECSXERMHTv70abbqLrzzuI6nDyBzPYjmUrDtbDjQjZJTSCvvAMO6UYRsNjoFzxCgCKkoXSPU1d6y7AiMj4BXq+gLeBznH0Dt2XB8PDRL7/rb2hz61YdCtlpDy91gdjYc6EbJQSSUd4Bh3ShaNxtdg2cLUNgVpWuEIuwt3p60f+Rf/qI9unEcjYYC1vQFaCXkI997JV8T6EZBN8o34UaRUN4BhnWjsDcbEcGzBSiMigIeNwojQhH2FudC9O1nkpEzsvNNaFNV0YHRzRionP7+ntqVjY+faU8a28/S/i5GZ3mhnc9XkpoKCw7C2pO0m9DShWFqB+hVO2MpnVQmkoNuFHSjfBNuFGnlHTnlRsm62UhrHgFmRQG/G4UvQnH2lo4esONceoHJ1Eo1uoXiY6Xi9P1s7rqzGvMO0KVCfKCUPYwPh79fZkxi+Eo2n6YdYqz7HuqWoT0T9Q6E0vaKfpx1VZlIDrpR0I3y9btRJJd35JQbRW2zkdw8wqgoERGKtreQ7DwrkqZX0o4+eQtMjKBVZe2rXnOCdmbUzp2OB35POydSwvCV/HSMft+vPh0n80Repp3VbU/LzrqqTCQH3SjoRtEXmYTBilBqeUeOuFHUNhvJzSPAX1HKGdidgqlFKNreUq0kNfgdi4bBjeglDi+3DL0IH6/fwYtEqJreXbZTQbBLrxW2r+R+LAxomGnVlx8rxnVVmUgOulHQjSIImYShP1LJOwzsRsm62UhuHlFDtaLERaiPvYVkxmM307LzTUFPxXGbp6lxxjfKca1GFdUtOzU146OuKhPJQTcKulFyUxj6I7m8wwBuFI2bjeTmETVUK0oJ3+7At2GLtreQTNplFdWRPIxVXKxgk88S7G3pTT9F8O9pk5mD7StxLQxXHmd8vPoEXFUabzqpTCQH3SjoRhGETMIQh+TyDkO6Ufg2G9HBMwQofBWlROPuwNiwxdlbCA3L0ebw/AP0Zl1hYc3V4c1gzUnF9YcZe0Hl7I7lK/FtBn4hdHXcXcGLj2BFb8VSuqpMJAfdKOhGEYRMwhCH5PIOQ7pRxG02DBgCFHEVxYhQnL0F0gTbbd1h8++wMPP20moJHLmhGK+R1uWfmyO94ED4sS1tL1eaTK84kxaui33GUgxfycCG9Fm6KXvo/6XsIXgwfUKDQ1eVieSgGwXdKLkpDHFILu8wpBtF4GYjPHiGAEVrRWncHdgRirC3cGhUmRweq2nWNMxMYE1fOnAs6JppKp+vhLTQp7SnQ1Z0VZlIDr4riCAIIkcwOyMIgsgRzM4IYiDQjYLoBGZnBEEQOfJ/RDer2avM5WAAAAAASUVORK5CYII=)
		-
		![](data:image/png;base64,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)
		Les deux répertoires spéciaux en début de liste font référence au répertoire courant (`.`) et au répertoire _parent_ (`..`). Ces répertoires spéciaux existent dans chaque répertoire du système. Leur utilité sera démontrée lors de la mise en pratique des commandes de gestion des fichiers.
		Important
		Les noms de fichier qui commencent par un point (`.`) indiquent des fichiers _cachés_ lors de l'affichage des résultats de **ls** ou d'autres commandes. Il ne s'agit _pas_ d'une fonction de sécurité. Les fichiers cachés évitent que les fichiers de configuration nécessaires à l'utilisateur n'encombrent les répertoires personnels. De nombreuses commandes ne traitent les fichiers cachés qu'avec des options de ligne de commande, ce qui évite la copie accidentelle de la configuration d'un utilisateur vers d'autres répertoires ou utilisateurs.
		-
		Pour protéger le _contenu_ d'un fichier contre les consultations indues, il faut recourir aux _permissions de fichier_.
		![](data:image/png;base64,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)
		La commande **cd** comporte de nombreuses options. Quelques-unes sont suffisamment utiles pour qu'il soit rentable de les maîtriser rapidement et les utiliser souvent. La commande **cd -** sert à passer du répertoire où se trouvait l'utilisateur _avant_ de passer au répertoire courant. Regardez comment cet utilisateur tire parti de ce comportement pour passer d’un répertoire à l’autre, ce qui est utile lors du traitement d'une série de tâches similaires.
		![](data:image/png;base64,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)
		La commande **cd ..** utilise le répertoire masqué `..` pour passer au niveau supérieur, répertoire _parent_, sans avoir à connaître le nom exact du parent. L'autre répertoire caché (`.`) spécifie le _répertoire courant_ pour les commandes dans lesquelles l'emplacement actuel constitue l'argument source ou de destination, ce qui évite d'avoir à taper le nom de chemin absolu du répertoire.
		![](data:image/png;base64,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)

Séance 5: Raid Windows & Linux + CloneZilla Live
-----------------------------------------------------------------------------------------------------------------------------
	Objectifs
		Deux techniques de sécurisation des données vont être abordés lors de ce labo. Le RAID  
		software, et l'approche "backup-restauration"
1. Introduction
	RAID  
		Le RAID (Redondant Array of Inexpensive/Independent Disk) est un ensemble de techniques  
		de virtualisation du stockage permettant de répartir des données sur plusieurs disques durs  
		afin d'améliorer soit les performances, soit la sécurité ou la tolérance aux pannes de  
		l'ensemble du ou des systèmes.  
		Selon le besoin, il existe différents types de RAID. Dans le cadre de notre manipulation, nous  
		allons travailler avec le RAID1, dit RAID miroir.  
	RAID logiciel  
		Il existe deux types de RAID.  
		• Physique, où la gestion du RAID sera gérée par un hardware spécifique. Du point de vue de  
		l’utilisateur et du système d’exploitation, la redondance est abstraite. Il ne voit qu’un seul  
		disque.  
		• Dans le cadre d’un RAID logiciel, celui-ci sera géré par le système d’exploitation à l’aide  
		d’outils.  
	Les différents RAID
		Le RAID 1 (miroir)
		Le RAID 0 (performence)
		Le RAID 5
			Le RAID 5 utilise au minimum 3 disques durs. Il  
			combine les bénéfices des deux types de RAID vus  
			précédemment. Il résiste à la panne d'un seul disque  
			dur. La capacité totale de stockage équivaut à l'addition  
			de l'espace de chaque disque – 1.  
			Pour 5 disques de 1To, la capacité totale sera donc de 4  
			To.
	L'approche "backup-restauration"
		Dans cette approche, l'image va être créée et utilisée dans un scénario de sauvegarde-  
		restauration. L'utilisateur utilise un logiciel de création d'images pour sauvegarder son disque  
		dur entier, une partition ou plus simplement quelques dossiers et fichiers importants. Il pourra  
		dès lors, à tout moment, restaurer ces données telles qu'elles ont été capturées lors du backup.  
		Les logiciels couramment utilisés sont Norton Ghost, Acronis, Clonezilla, ...  
		-
		Selon le logiciel choisi, les fonctionnalités divergent :  
			 Planification ou sauvegarde manuelle,  
			 Sauvegarde en réponse à des événements particuliers (ex : lancement d'une  
			application)  
			 Sauvegarde en fonction de la quantité de données présentes sur le disque ou ajoutées  
			depuis la dernière sauvegarde,  
			 Types de sauvegardes possibles : totale, incrémentielle ou différentielle  
			 Taux de compression de l'image créée,  
			 Convivialité des assistants,  
			 ...  
		Selon Symantec, l'éditeur du célèbre Ghost, ces outils permettent de résoudre un bon nombre  
		de problèmes pouvant affecter un ordinateur :
			 Attaques virales : les dégâts peuvent se produire avant qu'un virus ne soit mis en  
			quarantaine
			 Installations défectueuses de logiciels : certains logiciels peuvent nuire aux  
			performances de votre ordinateur et le ralentir au point que l'ouverture des  
			programmes ou des documents nécessite énormément de temps. Mais une foisle  
			programme installé, sa suppression ne permet pas toujours de réparer les dégâts  
			involontaires provoqués par l'installation.  
			 Panne de disque dur : les données peuvent être endommagées sur votre lecteur  
			système (généralement C), rendant impossible le démarrage de votre système  
			d'exploitation.  
			 Fichiers supprimés ou écrasés accidentellement : la suppression accidentelle de  
			fichiers est fréquente et souvent coûteuse.  
			 Fichiers corrompus : des fichiers et dossiers peuvent être endommagés par un virus ou  
			provoquer une erreur lorsqu'un programme les modifie.
	L'approche "déploiement d'images"
		Dans cette deuxième approche, l'idée n'est pas de réaliser un backup mais d'aider un adminis-  
		trateur d'un parc informatique dans une de ses tâches les plus répétitives : l'installation de sys-  
		tèmes d'exploitation sur un grand nombre de machines.  
		-
		L'idée est assez simple et peut se résumer en 3 grandes étapes :
		-  
			1. Réaliser l'installation et la finalisation d'installation d'une machine modèle. Il peaufine  
			donc l'installation de cette machine dans ses moindres détails : installation des drivers,  
			des applications, création des comptes utilisateurs, réglage fin des différents para-  
			mètres, ...  
			2. Il réalise ensuite l'image de cette machine modèle (généralement le disque dur entier)  
			et stocke cette image sur un serveur central (le serveur de déploiement),  
			3. Depuis le serveur, il pousse l'image (en multicast) vers les machines cibles de son parc  
			qui reçoivent alors la même configuration que la machine modèle.  
		Bien que très simple à comprendre dans ses grands principes, ce mode de fonctionnement  
		peut réserver quelques mauvaises surprises à l’administrateur. Celui-ci devra notamment tenir  
		compte des observations suivantes :
			 L'image de la machine modèle est intimement liée au hardware de cette machine (pen-  
			sez simplement aux drivers...). Son déploiement sur une machine ne présentant pas les  
			mêmes caractéristiques matérielles peut s'avérer des plus aléatoire... (bien que les dé-  
			veloppeurs d'application aient beaucoup travailler pour rendre possible le déploiement  
			d'images dans des parcs hétérogènes).  
			 L'image de la machine modèle est intimement liée à l'os installé et aux paramètres  
			créés lors de son installation. Notamment, le SID, un numéro généré de manière aléa-  
			toire et qui permet d'identifier de manière unique la machine sur un réseau. Ce SID est  
			également utilisé dans la création de l’identifiant des utilisateurs. Il est donc très im-  
			portant de ne pas déployer le même SID sur toutes les machines. Il en est de même  
			pour le nom de la machine. Des utilitaires complémentaires tels que sysprep ou ghost-  
			walker doivent donc fréquemment être utilisés pour s'assurer de l'unicité des machines  
			sur le réseau.  
		Néanmoins, hormis ces quelques considérations pratiques, le déploiement d'images reste  
		une méthode qui rend bien des services aux administrateurs d'un parc informatique. Les
2. Manipulation
		RAID Windows 10
			On démarre la machine est on ouvre l’outil disk management (diskmgmt.msc).  
			Les nouveaux disques doivent être initialisés, les paramètres par défaut conviennent à la  
			manipulation
			![[Pasted image 20230114161441.png]]
			![[Pasted image 20230114161618.png]]
	Disk Management – Simulation d'un problème de disque
		1. On éteint la VM  
		2. On retire le disque qui contenait initialement la partition D :  
		3. On redémarre la machine
		Un disque est marqué "Missing"  
		Le miroir est marqué "Failed Redundancy"  
		MAIS LES DONNEES SONT TOUJOURS DISPONIBLES POUR L’UTILISATEUR.
	Disk management – Comment "réparer" le miroir
		En deux étapes :
		Etape 1 : retirer le miroir
			Pour retirer le miroir, on part du volume marqué « Missing »
			![[Pasted image 20230114161944.png]]
		Etape 2 : recréer un nouveau miroir (comme expliqué ci-dessus)
	Création d'un RAID sous Linux (Debian)
		apt-get install mdadm
		cat /proc/mdstat
		![[Pasted image 20230114162235.png]]
		Préparation des disques
			Maintenant que l’outil mdadm est installé, nous allons préparer les disques avant la mise en  
			place du RAID. Pour vérifier l’état des disques sur la machine tapez  
			fdisk -l
			![[Pasted image 20230114162330.png]]
			Les deux disques que nous avons ajoutés sont bien présents (sdb et sdc). Mais ils ne sont pas  
			prêts à être utilisé. Nous allons devoir les formater.
			Toujours avec la commande fdisk tapez  
			fdisk /dev/sdb  
			Vous rentrez ensuite dans une commande interactive. Tapez n et choisissez les entrées par dé-  
			faut.  
			Une partition primaire de 8Gb sera ajoutée. Sauvegardez et quittez avec la commande w.
			![[Pasted image 20230114162426.png]]
			Une fois la manipulation effectuée pour les disques sdb et sdc, vérifiez le résultat avec la com-  
			mande fdisk -l.
			![[Pasted image 20230114162454.png]]
			On va maintenant modifier le type de partition en « raid auto-detect ». Pour cela tapez de  
			nouveau fdisk /dev/sdb et utilisez la commande t. Choisissez le type de partition « fd » pour  
			le raid. Sauvegardez et faites la même manipulation pour le second disque
			![[Pasted image 20230114162518.png]]
			Mise en place du RAID 1 Mirror
			Nous allons maintenant créer un nouveau disque virtuel /dev/md0 qui correspond au miroir  
			créé avec nos deux partitions sdb et sdc. Tapez la commande  
			mdadm --create /dev/md0 --level=1 --raid-devices=2 --name=DataRaid1 /dev/sdb1 /dev/sdc1
			![[Pasted image 20230114162608.png]]
			La synchronisation entre vos deux partitions va commencer. Vous pouvez vérifier la  
			progression avec la commande : cat /proc/mdstat
			![[Pasted image 20230114162638.png]]
			Une fois la synchronisation terminée vous devez observer cela avec la commande précédente
			![[Pasted image 20230114162701.png]]
			Pour des informations sur votre nouveau disque virtuel md0 vous pouvez utiliser la  
			commande suivante  
			mdadm --detail /dev/md0
			![[Pasted image 20230114162728.png]]
	Préparation du nouveau disque et test du raid
		Préparation de md0
			Nous avons créé un nouveau disque avec nos deux partitions sdb1 et sdc1. Celui-ci s’appelle  
			md0. De votre point de vue il s’agit d’un seul disque. Mais derrière sont présents deux disques  
			distincts où chaque information est dupliquée sur chacun des disques. Cela permet une  
			certaine sécurité si un de vos disques venait à tomber en panne. Comme chaque donnée est  
			répliquée, les données seront toujours accessibles même avec un disque manquant.
			md0 n’est pas encore utilisable. Il faut lui ajouter un système de fichier. Ici ext4 le système de  
			base sous Debian 9
			mkfs.ext4 /dev/md0
			![[Pasted image 20230114162838.png]]
			Un système de fichier a été ajouté pour md0. Il nous reste à « monter » ce système de fichier  
			dans un répertoire que vous allez créer.  
			Pour créer un répertoire sous Linux  
			mkdir /mnt/raid1  
			Pour monter le disque à cet emplacement  
			mount /dev/md0 /mnt/raid1/ (Attention de bien respecter les /)  
			On ajoute des fichiers pour tester sur le disque monté dans /mnt/raid1  
			touch /mnt/raid1/fichier1.txt  
			touch /mnt/raid1/fichier2.txt  
			echo « test » > /mnt/raid1/fichier1.txt  
			echo « test2 » > /mnt/raid1/fichier2.txt  
			Vérifiez le contenu du disque  
			cd /mnt/raid1/  
			ls
			![[Pasted image 20230114162902.png]]
			Afin de faciliter les tests nous allons faire en sorte que le disque md0 soit monté  
			automatiquement dans /mnt/raid1. Pour cela il faut modifier le fichier /etc/fstab  
			nano /etc/fstab  
			Et ajouter la ligne à la fin du fichier  
			/dev/md0 /mnt/raid1 ext4 defaults 0 2  
			Ctrl-X pour quitter. Sauvegardez le fichier.
			![[Pasted image 20230114162927.png]]
			Tapez la commande suivante afin de vérifier les erreurs éventuelles dans votre fichier  
			mount -av  
			Sauvegarde de votre configuration RAID  
			mdadm --detail --scan >> /etc/mdadm/mdadm.conf  
			Vérifiez le résultat
			![[Pasted image 20230114162951.png]]
	Test du raid miroir
		Nous allons maintenant tester notre RAID. Vérifiez une dernière fois l’état de votre RAID à  
		l’aide de la commande mdadm --detail /dev/md0  
		Lancez la commande avant de redémarrer  
		update-initramfs -u  
		Eteignez votre machine virtuelle et supprimez un des deux disques (Disque1 ou  
		Disque2). Ne supprimez pas le disque sur lequel se trouve votre OS !  
		Il est possible que vous redémarriez en mode « recovery ». Attendez la fin du décompte et  
		tapez votre accès root.  
		Vous pouvez relancer le disque /dev/md0 avec la commande suivante  
		mdadm --run /dev/md0  
		Vérifiez le statut avec la commande
		mdadm –-detail /dev/md0  
		Vous observez la panne
		![[Pasted image 20230114163047.png]]
		Vérifiez que votre fichier1.txt existe toujours bien dans /mnt/raid1
		![[Pasted image 20230114163109.png]]
	Réparation du RAID
		Eteignez de nouveau votre machine. Nous allons maintenant ajouter un nouveau disque  
		virtuel à votre machine (on simule de cette manière le remplacement de votre disque  
		défectueux).  
		Une fois le nouveau disque ajouté, relancez votre machine.  
		Vérifiez à l’aide de fdisk quel est le disque qui n’a pas de partition, et créez une partition sur  
		le disque que vous venez d’ajouter. (Voir manipulations précédentes).
		Une fois votre nouveau disque partitionné, vous pouvez l’ajouter au RAID existant  
		(/dev/md0).  
		mdadm --manage /dev/md0 --add /dev/sdb1  
		Il se peut que votre nouveau disque soit sdc et non sdb ! Adaptez votre commande au besoin  
		Vous pouvez suivre la resynchronisation avec mdadm –detail /dev/md0
		![[Pasted image 20230114163145.png]]
		Une fois terminée, vérifiez que tout est en ordre.
		![[Pasted image 20230114163205.png]]
		Et voilà, votre Raid est à nouveau mis en place et vous n'avez pas perdu vos fichiers !
	Création d'une image disque avec Clonezilla
		Le but de cette première manipulation est de réaliser un backup de notre machine Debian  
		précédemment utilisée. Nous allons donc créer un clone du disque dur principal de notre  
		machine (sda). Nous pourrons ensuite modifier notre Debian (simulation de fausse manœuvre  
		qui nous poussera à vouloir récupérer notre machine comme elle l'était avant) et restaurer  
		l'image sur le disque sda. Nous aurons donc récupéré notre machine comme elle l'était avant  
		de la modifier.  
		Les grandes étapes de ce premier test pratique sont donc :  
		1. Préparation d'un support pour recevoir le backup : ici un second disque dur  
		2. Réalisation du backup  
		3. Simulation d'un problème sur la vm  
		4. Restauration du système sur sda  
		Ajoutez un disque dur à votre machine debian. Démarrez la machine et créez une partition  
		que vous formaterez (voir plus haut).  
		Si votre nouveau disque est sdd :  
		fdisk /dev/sdd  
		Option n (création d'une partition)  laisser les paramètres par défaut  
		Option W pour enregistrer les modifications
		Formatez ensuite cette partition, par exemple :  
		mkfs.ext4 /dev/sdd1  Utilisation du système de fichiers ext4 sur notre partition.  
		Votre nouvelle partition devrait s'appeler sdd1. Nous allons sur cette partition créer un dossier  
		dans lequel on stockera l'image du disque dur qu'on fera ensuite avec Clonezilla.  
		Durant ces différentes étapes, je créé un dossier "dossierimage" dans lequel je monte notre  
		partition (pour que nous puissions accéder à notre partition, il est nécessaire de la monter)  
		Je me déplace dans ce dossier et je créé un nouveau dossier "partimag".  
		Grace à cela, nous pourrons stocker notre image disque dans ce dossier qui sera visible pour  
		Clonezilla
		![[Pasted image 20230114163351.png]]
		Eteignez la machine et démarrez sur l'image ISO de Clonezilla. C'est une image "live". Ce qui  
		signifie que le système d'exploitation Clonezilla n'a pas besoin d'être installé sur un disque  
		dur. Tous les fichiers nécessaires au bon fonctionnement de l'OS sont dans l'image.  
		Sur un PC physique, nous pourrions créer une clé USB bootable avec Clonezilla et démarrer  
		l'OS depuis la clé seulement par exemple.  
		Une fois démarré, Clonezilla est assez intuitif et simple d'utilisation (du moins dans le mode «  
		debutant »). Un assistant, dans la langue de votre choix, vous guide dans les étapes de création  
		de l'image. Réalisez un backup de votre premier DD et stockez l'image ainsi créée sur le  
		second DD !
	Réalisation du backup
		![[Pasted image 20230114163502.png]]
		Nous allons placer notre image sur un périphérique local (notre dernier disque dur)
		![[Pasted image 20230114163521.png]]
		Enter et puis Ctrl C  quitter la fenêtre
		Choisir de placer l'image sur notre disque dur prévu à cet effet (ici sdd1) :
		![[Pasted image 20230114163546.png]]
		Choisir le dossier partimag que nous avons créé
		![[Pasted image 20230114163602.png]]
		Tab  Done
		![[Pasted image 20230114163622.png]]
		Option "savedisk" pour créer une image du disque :
		![[Pasted image 20230114163636.png]]
		![[Pasted image 20230114163651.png]]
		Choisir de cloner sda (le disque sur lequel se trouve notre debian)
		![[Pasted image 20230114163709.png]]
		![[Pasted image 20230114163723.png]]
		Suivez ensuite les instructions et démarrez le clonage du disque.  
		Pour récapituler  
		Nous avons donc maintenant une image (clone exact du disque sda) à disposition sur notre  
		disque dur sdd ! Cela veut dire que s’il arrive un souci à notre machine Debian, nous pouvons  
		la restaurer via cette image !  
		Enlevez l'image de Clonezilla live et redémarrez normalement votre machine Debian.  
		En retournant dans le dossier "dossierimage" avec  
		Cd /dossierimage  
		Et en listant le contenu du dossier avec ls  
		On ne voit pas notre dossier partimag. Il faut remonter notre partition /dev/sdd1 dans le  
		dossier /dossierimage avec  
		Mount /dev/sdd1 /dossierimage/
		![[Pasted image 20230114163743.png]]
		Notre image a bien été créée !
	Modification du système
		Créez un dossier supplémentaire sur la machine ou modifiez quelque chose. Le but est  
		simplement de voir qu'après la restauration, le système sera tel qu'il l'était lors du backup.
	Restauration du système
		Redémarrez la machine sur Clonezilla et suivez les instructions pour restaurer notre image sur  
		le disque sda.  
		Il s'agit des mêmes options que pour la réalisation du clone jusqu’à cette étape :
		![[Pasted image 20230114163840.png]]
		Nous allons choisir de restaurer le disque, et notre image apparait normalement à l'écran.
		![[Pasted image 20230114163855.png]]
		Choisissez de restaurer l'image sur le disque sda (nous allons donc écraser notre machine  
		modifiée avec l'image)
		![[Pasted image 20230114163915.png]]
		Voici à quoi la restauration devrait ressembler :
		![[Pasted image 20230114163933.png]]
		Une fois la restauration terminée, vous pouvez démarrer votre Debian et constater que vos  
		modifications ne sont plus là. Vous avez récupéré votre Debian comme elle l'était quand vous  
		avez créé l'image !!

Séance 6: Initiation Red Hat - 3 ième partie
-----------------------------------------------------------------------------------------------------------------------------
!!! pas oublier chap récapitulatif
Chapitre 4 - Création, affichage et modification de fichiers texte
Objectifs
	-   De décrire les termes techniques que sont entrée standard, sortie standard et erreur standard.
	-   D'utiliser les caractères de redirection pour contrôler la sortie vers des fichiers.
	-   D'utiliser les pipelines pour diriger la sortie vers d'autres programmes.

Entrée standard, sortie standard et erreur standard
	Un programme d'exécution, ou _processus_, doit lire l'entrée depuis un emplacement et écrire la sortie sur l'écran ou dans des fichiers. Une commande exécutée depuis l'invite de shell lit habituellement son entrée depuis le clavier et envoie sa sortie vers sa fenêtre de terminal.
	-
	Un processus utilise des canaux numérotés appelés _descripteurs de fichiers_ pour obtenir une entrée et envoyer une sortie. Tous les processus disposent d'au moins trois descripteurs de fichiers pour commencer. L'_Entrée standard_ (canal 0) lit l'entrée depuis le clavier. La _Sortie standard_ (canal 1) envoie la sortie normale vers le terminal. L'_Erreur standard_ (canal 2) envoie les messages d'erreur vers le terminal. Si un programme ouvre des connexions séparées avec d'autres fichiers, il peut utiliser des descripteurs de fichiers portant des numéros plus élevés.

![[Pasted image 20230114152113.png]]
Tableau 4.1. Canaux (Descripteurs de fichiers)
![[Pasted image 20230114152239.png]]

Redirection de la sortie vers un fichier
	La _redirection_ d'E/S remplace les destinations de canal par défaut par les noms de fichiers qui représentent des fichiers de sortie ou des périphériques. En utilisant la redirection, les sorties de processus et les messages d'erreur normalement envoyés vers la fenêtre de terminal peuvent être capturés sous forme de contenu de fichier, envoyés vers un périphérique ou supprimés.
	-
	La redirection de `stdout` empêche l'affichage de la sortie du processus sur le terminal. Comme indiqué dans le tableau suivant, la redirection de _stdout_ `uniquement`n'empêche pas l'affichage des messages d'erreur `stderr` sur le terminal. Si le fichier n'existe pas, il sera créé. Si le fichier existe et que la redirection ne s'ajoute pas au fichier, le contenu du fichier sera écrasé. Le fichier spécial `/dev/null` élimine discrètement la sortie de canal redirigée vers ce fichier et est toujours un fichier vide.

Tableau 4.2. Opérateurs de redirection de sortie
![[Pasted image 20230114152435.png]]



">>fichier"
redirige stdout pour l'ajouter à un fichier
![[index 1.png]]

2>fichier
	redirige stderr pour écraser un fichier
![[index 2.png]]
2> /dev/null
	supprime les messages d'erreur stderr en les redirigeant vers /dev/null
![[index 3.png]]
">fichier"  2>&1 &>fichier
	redirige stdout et stderr pour écraser le même fichier
![[index 4.png]]

">>fichier"  2>&1 &>>fichier
	redirige stdout et stderr pour les ajouter au même fichier
![[index 5.png]]

1. Redirection de la sortie vers un fichier ou un programme
	Décrire comment afficher, contrôler et enregistrer efficacement la sortie des programmes.

Objectifs
	-   De décrire les termes techniques que sont entrée standard, sortie standard et erreur standard.
	-   D'utiliser les caractères de redirection pour contrôler la sortie vers des fichiers.
	-   D'utiliser les pipelines pour diriger la sortie vers d'autres programmes

Entrée standard, sortie standard et erreur standard
	Un programme d'exécution, ou _processus_, doit lire l'entrée depuis un emplacement et écrire la sortie sur l'écran ou dans des fichiers. Une commande exécutée depuis l'invite de shell lit habituellement son entrée depuis le clavier et envoie sa sortie vers sa fenêtre de terminal.
	Un processus utilise des canaux numérotés appelés _descripteurs de fichiers_ pour obtenir une entrée et envoyer une sortie. Tous les processus disposent d'au moins trois descripteurs de fichiers pour commencer. L'_Entrée standard_ (canal 0) lit l'entrée depuis le clavier. La _Sortie standard_ (canal 1) envoie la sortie normale vers le terminal. L'_Erreur standard_ (canal 2) envoie les messages d'erreur vers le terminal. Si un programme ouvre des connexions séparées avec d'autres fichiers, il peut utiliser des descripteurs de fichiers portant des numéros plus élevés.

![[index 6.png]]

Tableau 4.1. Canaux (Descripteurs de fichiers)
![[Pasted image 20230114153119.png]]

Redirection de la sortie vers un fichier
	La _redirection_ d'E/S remplace les destinations de canal par défaut par les noms de fichiers qui représentent des fichiers de sortie ou des périphériques. En utilisant la redirection, les sorties de processus et les messages d'erreur normalement envoyés vers la fenêtre de terminal peuvent être capturés sous forme de contenu de fichier, envoyés vers un périphérique ou supprimés.
	La redirection de `stdout` empêche l'affichage de la sortie du processus sur le terminal. Comme indiqué dans le tableau suivant, la redirection de _stdout_ `uniquement`n'empêche pas l'affichage des messages d'erreur `stderr` sur le terminal. Si le fichier n'existe pas, il sera créé. Si le fichier existe et que la redirection ne s'ajoute pas au fichier, le contenu du fichier sera écrasé. Le fichier spécial `/dev/null` élimine discrètement la sortie de canal redirigée vers ce fichier et est toujours un fichier vide

Tableau 4.2. Opérateurs de redirection de sortie
![[Pasted image 20230114153225.png]]

Important
	L'ordre des opérations de redirection est important La séquence suivante redirige la sortie standard vers le `fichier` et redirige l'erreur standard vers le même emplacement que la sortie standard (`fichier`).
 "> file 2" > &1 
	Toutefois, la séquence suivante exécute la redirection dans l'ordre inverse. Cette action redirige l'erreur standard vers l'emplacement par défaut pour la sortie standard (la fenêtre de terminal, donc aucune modification), _puis_ redirige uniquement la sortie standard ver le `fichier`.
	 2>&1 > file 
	Pour cette raison, certaines personnes préfèrent utiliser les opérateurs de redirection associés.

	![[Pasted image 20230114153351.png]]

	Toutefois, les autres administrateurs système et programmateurs qui utilisent également d'autres shells associés à **bash** (« shells compatibles Bourne ») pour créer des scripts de commande considèrent que les nouveaux opérateurs de redirection associés doivent être évités car ils ne sont pas standardisés ni mis en œuvre dans tous ces shells et sont soumis à d'autres limites.
	-
	Les auteurs de ce cours adoptent une position neutre sur ce sujet, et les deux syntaxes sont susceptibles de figurer dans le champ.

Exemples de redirection de sortie
	De nombreuses tâches d'administration de routine sont simplifiées grâce à la redirection. Utilisez le tableau précédent pour vous aider à déchiffrer les exemples suivants :
	-   Enregistrer un horodatage pour consultation ultérieure.
	![[index 7.png]]
	- Copier les 100 dernières lignes d'un fichier journal vers un autre fichier.
	![[index 8.png]]
	- Concaténer quatre fichiers en un
	![[index 9.png]]
	Répertorier le nom des fichiers masqués et standard du répertoire personnel dans un fichier.
	![[index 10.png]]
	Ajouter la sortie à un fichier existant.
	![[index 11.png]]
	- Dans les exemples suivants, des erreurs sont générées, étant donné que les utilisateurs standards n'ont pas accès aux répertoires système. Rediriger les erreurs vers un fichier tout en affichant la sortie de la commande normale sur le terminal.
	![[index 12.png]]
	- Enregistrer la sortie des processus et les messages d'erreur dans des fichiers distincts.
	![[index 13.png]]
	- Ignorer et éliminer les messages d'erreur.
	![[index 14.png]]
	- Stocker ensemble la sortie et les erreurs générées.
	![[index 15.png]]
	- Ajouter la sortie et les erreurs générées à un fichier existant.
	![[index 16.png]]

Construction de pipelines
	Un _pipeline_ est une séquence d'une ou plusieurs commandes séparées par **|**, le caractère _pipe_. Un pipe connecte la sortie standard de la première commande avec l'entrée standard de la commande suivante
	![[Pasted image 20230114154019.png]]
	Les pipelines permettent la manipulation et le formatage de la sortie d'un processus par d'autres processus avant sa transmission vers le terminal. Une image mentale utile consiste à imaginer que les données « circulent » dans le pipeline d'un processus à un autre, et sont légèrement modifiées par chaque commande du pipeline par lequel elles transitent.

Note
	Les pipelines et la redirection des E/S manipulent la sortie standard et l'entrée standard. La _redirection_ envoie la sortie standard vers ou obtient l'entrée standard depuis les _fichiers_. Les _pipes_ envoient la sortie standard vers ou obtiennent l'entrée standard depuis un autre _processus_.

Exemples de pipelines
	Dans cet exemple, la sortie de la commande **ls** est affichée sur un écran du terminal à la fois en utilisant **less**.
	![[index 17.png]]
	La sortie de la commande **ls** est transmise par le pipe à **wc -l**, qui compte le nombre de lignes reçues de **ls** et l'imprime sur le terminal.
	![[index 18.png]]
	Dans ce pipeline, **head** sort les 10 premières lignes de **ls -t**, avec le résultat final redirigé vers un fichier.
	![[index 19.png]]
	**Pipelines, redirection et tee.**  Lorsque la redirection est associée à un pipeline, le shell configure d'abord l'intégralité du pipeline, puis redirige l'entrée/la sortie. Cela signifie que si une redirection de sortie est utilisée au _milieu_ d'un pipeline, la sortie accède au fichier et non à la commande suivante du pipeline.
	-
	Dans cet exemple, la sortie de la commande **ls** accède au fichier et **less** n'affiche rien sur le terminal.
	![[index 20.png]]
	La commande **tee** est utilisée pour contourner cela. Dans un pipeline, **tee** copie son entrée standard vers sa sortie standard et redirige également sa sortie standard vers les fichiers nommés comme arguments de la commande. Si les données sont imaginées comme de l'eau circulant à travers un pipeline, **tee** peut être visualisé comme un raccord en « T » dans le tuyau qui dirige la sortie dans deux directions.
	![[Pasted image 20230114154437.png]]
	Exemples de pipeline utilisant la commande tee
	Cet exemple redirige la sortie de la commande **ls** vers le fichier et passe en **less** pour l'afficher sur un écran du terminal à la fois.
	![[index 21.png]]
	Si **tee** est utilisé à la fin d'un pipeline, la sortie finale d'une commande peut être enregistrée et envoyée vers le terminal en même temps.
	![[index 22.png]]
	Cet exemple plus sophistiqué tire avantage du fait qu'un _fichier de périphérique_ spécial existe et représente le terminal. Le nom du fichier de périphérique pour un terminal particulier peut être déterminé en exécutant la commande **tty** à l'invite de son shell. La commande **tee** peut être utilisée pour rediriger la sortie vers ce fichier afin de l'afficher sur la fenêtre de terminal, alors que la sortie standard peut être transmise à un autre programme via un pipe. Dans ce cas, **mail** envoie la sortie par courrier électronique à [mdp@henallux.be](mailto:mdp@henallux.be).
	![[index 23.png]]
	Ci-dessous est présentée la méthode appropriée pour rediriger la sortie standard et l'erreur standard via un pipe :
	![[index 24.png]]

Chapitre 5 - Gestion des utilisateurs et des groupes Linux locaux
1. Utilisateurs et groupes
	Dresser la liste des rôles des utilisateurs et groupes sur un système Linux et afficher les fichiers de configuration locaux.

Objectifs
	Après avoir terminé cette section, les participants devraient être en mesure d'expliquer le rôle des utilisateurs et groupes d'un système Linux, ainsi que la façon dont ils sont considérés par l'ordinateur.

Qu'est-ce qu'un utilisateur ?
	Chaque processus (programme en cours d'exécution) du système s'exécute avec le nom d'un utilisateur particulier. Chaque fichier est la propriété d'un utilisateur particulier. L'accès aux fichiers et aux répertoires est restreint par utilisateur. L'utilisateur auquel un processus en cours d'exécution est associé détermine à quels fichiers et répertoires ce processus peut accéder.
	-
	La commande **id** sert à afficher des informations sur l'utilisateur actuellement connecté. Il est également possible de demander des informations élémentaires sur un autre utilisateur, en passant son nom d'utilisateur comme premier argument de la commande **id**.
	![[index 25.png]]
	Pour afficher l'utilisateur associé à un fichier ou à un répertoire, utilisez la commande **ls -l**. La troisième colonne indique le nom de l'utilisateur :
	![[index 26.png]]
	Pour afficher les informations relatives au processus, utilisez la commande **ps**. Par défaut, seul les processus du shell courant sont affichés. Ajoutez l'option **a** pour afficher tous les processus liés à un terminal. Pour afficher l'utilisateur associé à un processus, ajoutez l'option **u**. La première colonne indique le nom de l'utilisateur :
	![[index 27.png]]
	Le résultat des commandes précédentes affiche les utilisateurs par nom, mais en interne, le système d'exploitation les repère à l'aide de leur _numéro UID_. La mise en correspondance des noms et des numéros est définie dans les bases de données des informations sur les comptes. Par défaut, les systèmes utilisent un simple « fichier plat », le fichier `/etc/passwd`, pour stocker les informations concernant les utilisateurs locaux. Le format de `/etc/passwd` (sept champs séparés par des deux-points) se présente comme suit :
	![[Pasted image 20230114155101.png]]

Qu'est-ce qu'un groupe ?
	Tout comme les utilisateurs, les groupes portent un nom et un numéro (GID). Les groupes locaux sont définis dans `/etc/group`.

Groupes principaux
	-   Chaque utilisateur a un seul _groupe principal_.
	-   Pour les utilisateurs locaux, le groupe principal est défini par le numéro GID du groupe mentionné dans le quatrième champ de `/etc/passwd`.
	-   Normalement, le groupe principal est propriétaire des fichiers créés par l’utilisateur.
	-   Normalement, le groupe principal d'un nouvel utilisateur est un nouveau groupe qui porte le même nom que l'utilisateur. L'utilisateur est le seul membre de ce _Groupe privé de l'utilisateur_ (User Private Group ou UPG).

Groupes supplémentaires
	-   Les utilisateurs peuvent être membres de zéro ou plusieurs _groupes supplémentaires_ _(secondaires)_.
	-   Les utilisateurs qui sont des membres supplémentaires de groupes locaux sont répertoriés dans le dernier champ de l’entrée du groupe dans `/etc/group`. Pour les groupes locaux, l’affiliation des utilisateurs est déterminée par une liste d’utilisateurs séparés par des virgules qui se trouvent dans le dernier champ de l’entrée du groupe dans `/etc/group` : groupname:password:GID:`list,of,users,in,this,group`
	-   L'appartenance à un groupe supplémentaire sert à garantir que les utilisateurs disposent des autorisations nécessaires pour accéder aux fichiers et autres ressources du système.




Séance 7: La ligne de commande sous Windows
-----------------------------------------------------------------------------------------------------------------------------
Introduction
	Les commandes de l'interpréteur de commande de Windows, parfois appelés "commandes  
	MSDOS (Microsoft Disk Operating System)" par référence au système duquel elles sont issues,  
	représentent parfois une dernière solution si le système Windows ne se lance pas correctement,  
	DOS étant un ancien OS de 16 bits où se trouvait un interpréteur de commandes appelé  
	command.com. Certaines commandes sont restées mais beaucoup sont nouvelles.  
	On distingue deux catégories de commandes :  
		• Les commandes internes (c’est-à-dire intégrées directement dans l’interpréteur de  
		commandes)  
		• Les commandes externes, (c’est-à-dire des fichiers exécutables devant être appelés  
		pour être exécutés).
	Le démarrage de l’interpréteur de commande s’effectue en tapant « cmd » dans la barre de  
	recherche. Un clic gauche permet de lancer l’interpréteur en mode utilisateur tandis qu’un clic  
	droit permet de démarrer en administrateur. Vous pouvez aussi procéder d’une autre manière,  
	après avoir tapé « cmd », vous trouvez sur votre droite, en dessous de « Ouvrir », « Exécutez  
	en tant qu’administrateur ».  
	L’invite ou prompt du DOS est un message d’attente qui signale que le système est prêt à  
	recevoir une commande.
	![[Pasted image 20230114164721.png]]
	L’invite indique la position du répertoire actif : le nom du disque (ici C:) suivi du chemin  
	complet depuis le répertoire racine représenté par le caractère « backslash » « \ » (le chemin  
	complet dans ce cas : \Users\user).  
	L’obtention d’une page d’aide peut s’effectuer de différentes manières, soit en tapant « nom de  
	la commande / ? » ou en tapant « help nom de la commande ». Par exemple, si je veux de l’aide  
	par rapport à la commande « ipconfig », je vais écrire « ipconfig / ? » ou « help ipconfig ». Les  
	informations peuvent également se trouver sur le site technique de Microsoft : Technet mais  
	également sur de nombreux sites internet et ouvrages traitant du sujet.

Les variables d’environnement
	Une variable d’environnement est une variable pouvant être lue ou modifiée par un programme.  
	C’est un moyen simple de centraliser une information et de configurer le système. Une variable  
	contient des donnes comme des chemins, un nom d’utilisateur, etc. C’est le même principe que  
	pour une variable lorsqu’on fait de la programmation.  
	Par exemple, la variable « TMP » va contenir le répertoire des fichiers temporaires. La variable  
	« COMPUTERNAME » va contenir le nom de l’ordinateur et « USERNAME » le nom de  
	l’utilisateur courant.  
	La variable d’environnement « PATH » est l’une des plus importante, elle comprend la liste des  
	répertoires contenant les programmes que le système peut exécuter.


EXERCICES :  
	• Affichez la liste des variables d’environnement avec la commande set  
	• Tapez echo TMP, puis echo %TMP%.  
	o Quelle est la différence entre les deux syntaxes ?  
	• Tapez echo %PATH%, puis path.  
	o Quelle est la différence entre les deux syntaxes ?  
	o Le PATH ou « chemin de recherche » définit la liste des répertoires où  
	l’interpréteur de commandes doit chercher les fichiers exécutables.  
	• Ajouter un répertoire dans PATH  
	o Dans l’explorateur de fichiers, créez le répertoire C:\my_bat  
	o Modifiez la variable d’environnement PATH en lui ajoutant le répertoire en  
	question
	![[Pasted image 20230114164847.png]]
	o Vérifiez en redémarrant l’invite de commande pour qu’elle recharge les  
	variables.

Commandes de base
	La commande « cd »  
		La commande « change directory » permet comme son nom l’indique de se déplacer dans  
		l’arborescence des dossiers.  
		La commande « cd C:\Windows\Fonts » permet de se déplacer dans le sous-répertoire du  
		répertoire Windows, appelé Fonts. Ainsi à l’écran le prompt de l’invite de commande  
		affichera :
		![[Pasted image 20230114164924.png]]
		• « cd .. » permet de se déplacer dans le répertoire parent.  
		• « cd \ » permet de se déplacer à la racine de l’arborescence.
	La commande « dir »  
		« Directory » permet d’afficher la liste des fichiers et des répertoires dans le répertoire courant.  
		Cette commande possède de nombreuses options, écrivez : « dir / ? » afin de les connaitre.  
		Parmi ces options certaines sont particulièrement intéressantes :  
		• L’option /a permet d’afficher les fichiers cachés.  
		• L’option /p permet d’interrompre l’affichage lorsque l’écran est plein.  
		• L’option /s permet l’affichage aussi dans les sous-répertoires.

Chemin relatif et absolu
	Le chemin absolu obéit à une règle basique : « Avec le chemin complet et on trouve le fichier  
	». Pour déclarer un chemin absolu, il faut donc décrire tout le chemin à parcourir en partant de  
	notre disque local (souvent C : ) jusqu’au fichier souhaité.
	![[Pasted image 20230114165019.png]]
	Le chemin relatif est bien plus subtil, son point de départ se situe dans l’endroit où l’on se  
	trouve.  
	Par exemple, dans le cas présent, le prompt indique qu’il se trouve dans le répertoire  
	C:\Windows\Web. Par ailleurs, on remarque qu’il n’y a pas de c:\ ou de \ au début du chemin  
	utilisé pour lister le fichier.
	![[Pasted image 20230114165040.png]]

Commandes de gestion de fichiers
	La commande « mkdir » ou « md »  
		« Make Directory » crée un répertoire. Faites bien attention au prompt, il vous indique à partir  
		de quel endroit de l’arborescence votre répertoire sera créé. Informez-vous grâce à l’aide «  
		mkdir /? ».
	La commande « rmdir » ou « rd »
		« Remove Directory » supprime un répertoire.

Jokers ou wildcards ou caractères génériques
	Le joker « ? » : remplace un seul caractère du nom ou de l'extension d’un fichier.
	Le joker « * » : remplace un ensemble de caractères indéfinis

La commande « copy »
	Copie d’un fichier source vers une autre destination ou sous un autre nom. Source est un nom  
	de fichier tandis que Destination est soit un nom de fichier (le nom de la copie), soit un nom de  
	répertoire où doit aboutir la copie qui aura le même nom que le fichier source.

La création de fichier
	Pour créer un fichier, nous allons utiliser la commande « copy con » suivi du nom du fichier  
	que l’on veut créer. Cette commande crée un seul fichier à la fois.  
	Par exemple : « copy con nom.txt »  
	On peut ensuite entrer le texte souhaité. Pour sauvegarder le texte, il faut appuyer sur la  
	touche F6 ou (touche fn + F6), cela affichera « ^Z » à la fin de votre texte, ce qui est tout à  
	fait normal. Pour terminer, appuyer sur la touche Enter.  
	Une fois votre fichier créé, vous pouvez ensuite le déplacer, le renommer...

Création et lecture de fichier et commande « more »
	Le signe > redirige ce qui devrait être indiqué à l’écran vers le fichier nom.txt en écrasant ce  
	qu’il contenait (ou en le créant s’il n’existait pas). On peut donc créer un fichier aussi avec le  
	signe >.
	Exemple : echo toto > nom.txt  
	Dans cet exemple, on place le texte toto dans le fichier nom.txt mais vu que le fichier nom.txt  
	n’existait pas encore, il l’a créé et a mis le texte toto dedans.  
	Le signe >> fait la même chose à part qu’il concatène/ajoute le contenu à la fin du fichier sans  
	l’écraser.  
	Exemple : echo tutu >> nom.txt  
	Dans cet exemple, on va ajouter le texte tutu à la fin du fichier nom.txt. Celui-ci contenait déjà  
	toto (voir exemple ci-dessus) donc il a mis tutu en dessous de toto.  
	La commande « more » suivi du nom du fichier indique à l’écran le contenu d’un fichier texte.  
	Exemple : « more nom.txt » affiche le contenu du fichier nom.txt

La commande « move »
	La commande « move » permet de déplacer ou de renommer un fichier ou un répertoire.

La commande « ren »
	La commande « ren » vient de « rename » et cette commande permet de renommer un fichier,  
	un répertoire, ou un groupe de fichiers/répertoires.

La commande « del »
	« del » vient de « delete » et comme son nom l’indique, cette commande permet de supprimer  
	un fichier ou un groupe de fichier.

La commande « xcopy »
	Cette commande vient de « extended copy » et elle permet entre-autre de copier des fichiers ou  
	répertoires ainsi que ce qu’ils contiennent. Lisez attentivement l’aide concernant xcopy, surtout  
	pour les options /E, /Q, /H, /T, /Y, /D.  
	Exemples :  
	xcopy C:\robert\*.* C:\sauvegarde  
	=> copie les fichiers du répertoire robert au répertoire sauvegarde  
	xcopy C:\robert\*.* C:\sauvegarde /p  
	=> idem, mais chaque copie est soumise à votre approbation  
	xcopy C:\robert\*.* C:\sauvegarde /D : 9-30-4  
	=> copie les fichiers modifiés depuis le 30/09/04

La commande « attrib »
	Cette commande affiche ou modifie des attributs de fichier. Comme attribut, on peut retrouver  
	par exemple : lecture seule, archive, système, masqué, etc.

La commande « subst »
	La commande « subst » vient du mot « subsituting » et cela permet d’assigner un chemin à un  
	disque/une lettre/une commande.  
	Exemple : subst W: C:\exercices\niv1  
	Dans cet exemple, la lettre/le disque/la commande W : correspondra au chemin  
	C:\exercices\niv1. La commande « W : » équivaut maintenant à cd C:\exercices\niv1

La commande « find »
	La commande « find » veut dire « trouver » en anglais et elle permet de rechercher/trouver  
	une chaîne de caractères dans un ou plusieurs fichiers. Sur Windows, on effectue bien une  
	recherche à l’intérieur du fichier et PAS dans le nom du fichier.  
	ATTENTION, cette commande sous linux fait une recherche sur les noms des fichiers ou  
	répertoires, pas à l’intérieur des fichiers !

Commandes de gestion d’utilisateurs et de groupes
	La commande « net user »
		Cette commande permet d’ajouter ou de gérer des utilisateurs.  
		« net user NomUtilisateur MotDePasse /add » permet d’ajouter (add = ajouter) un utilisateur en  
		spécifiant son mot de passe.  
		Utilisez / ? après la commande afin d’en vérifier la syntaxe et de découvrir diverses options.
	La commande « net localgroup »
		Cette commande permet d’ajouter ou de gérer les groupes.  
		« net localgroup nomDuGroupe /add » permet de créer un groupe.  
		Utilisez / ? après la commande afin d’en vérifier la syntaxe et de découvrir diverses options.  
		« net localgroup Administrateurs user /add »  
		Ici, nous avons placé un utilisateur appelé « user » dans un groupe appelé « Administrateurs ».

# Architecture des ordinateurs:
## Chapitre 1:
• transférer ..... :  
– quoi, où, et comment  
● 3 questions = 3 fonctions = 3 bus  
● où :  
– = adresses  
– bus d’adresses  
– espace adressable
● comment :  
– lecture / écriture  
– synchronisation  
– sélection du périhérique  
– bus de controle
● 3 questions = 3 bus  
● bus de données  
● bus d’adresses  
● bus de contrôle
### SCHÉMA-TYPE D’UN ORDINATEUR AVEC CPU
--> En fonction de ce que nous venons de voir, voici le schéma type d’un ordinateur (élémentaire)
![[Pasted image 20230121135105.png]]
### SCHÉMA-TYPE D’UN « ORDINATEUR » AVEC FPGA
![[Pasted image 20230121135150.png]]
### SCHÉMA-TYPE D’UN ORDINATEUR AVEC CPU
![[Pasted image 20230121135218.png]]
### • quoi faire :  
– lire  
● en mémoire  
● d’un registre  
– écrire  
● en mémoire  
● dans un registre  
– modifier  
● opérations + , - , * , /
### • où :  
– mémoire centrale  
● lecture/écriture de données  
● Lecture du programme  
– registres  
● mémoires internes au CPU (rapide)  
● datas / adresses / autres ...  
– périphériques E/S  
● clavier, écrans, réseau, ...
### • quand :  
– validité des données sur les bus  
● chgt d’adresse = beaucoup de bits en même tps,  
● signaux rapides  
● capacités parasites
### • comment :  
– lecture  
– écriture  
– gérer le temps
### LE PROGRAMMING MODEL
### La boite à outils du CPU :  
### – registres GPR  
● « General Purpose Register »  
● pour exécuter des opérations sur des  
nombres
### – registre PC  
● « Programm Counter »  
● où fait-on ce que l’on fait ?  
● où en est-on dans le programme ?
### – Status Register  (chatgpt)
● « PSW » Process Status Word  
● comment s’est déroulé la dernière  
opération ?  
● comment fonctionne le CPU  
● réglage du fonctionnement du CPU  
(interruptions)
### – Exécuter les opérations :  
● ALU  
– « Arithmetic and Logical Unit »  
– Unité arithmétique te logique  
● Load and Store unit  
– Lire ou écrire hors du CPU  
● BU  
– « Branch Unit »  
– Organise la discontinuité d’un PGM  
– sauts
![[Pasted image 20230121140436.png]]
### LE FONCTIONNEMENT DE L’ORDI
### • L’ordinateur démarre  
– Reset = allumage  
– première opération :  
	● RAZ de tout  
	● RAZ des registres  
	● RAZ du PC
– quoi faire = une instruction  
– PC = adresse « 0 »  
– lecture l’instruction pointée par le PC  
– exécution de l’instruction  
– incrément du PC  
– rebelotte
### • L’ordinateur exécute :  
– un programme en MR centrale  
– ROM (bios)  
	● « Read Only Memory »  
– RAM  
	● « Random Acces Memory »  
	● ce qui est « random » c’est le mode  
	d’accès (R/W)
– lecture / écriture (load/store) :  
	● par le load/store unit  
	● dans ou de la mémoire  
	● dans ou de les périph. E/S  
	● entre les registres
– sauts (jump) :  
	● par le branch unit  
	● modification du PC  
	● rupture dans la continuité du  
	programme
– opérations arithmétiques ou logiques  
	● par l’ALU  
	● sur des registres  
	● sur les CPU récents : <>  
	types de registres (ALU)
– autres opérations :  
	● en fonction du CPU  
	● interruptions  
	● reset = interruption « NMI »  
	● mise en veille
– écrire une donnée en MR ou dans un registre  
	● écraser  
	● effacer  
	● détruire  
	● = synonymes
– les premières opérations  
	● toujours les mêmes  
	● immuables  
	● fixées une fois pour toutes  
	● en ROM (bios)
– besoin de variables  
	● les registres  
		–limités en taille  
		–limités en nombre  
	● besoin de plus :  
		–la RAM
– exemple d’instruction  
	● A + 15 = C  
	● opération sur des registres  
	● « A » et « 15 » = sources  
	● « 15 » : « valeur immédiate »  
	● « C » = destination
	● A + 15 = C  
	● on lit « A »  
	● on envoie à l’ALU  
	● on réalise l’addition ( + 15 )  
	● on envoie le résultat ds. « C »
	● A + 15 = C  
	● le CPU lit l’instruction en MR  
	● le CPU lit la donnée immédiate
	● A + 15 = C  
	● il y a 2 choses en MR :  
		–les instructions  
		–les données
• Représentation du modèle :
![[Pasted image 20230121141113.png]]
– le code stream  
	● le code = l’ensemble des instructions  
	● pas seulement pour l’ALU  
		– ALU  
		– BU  
		– Load/Store
### • Codage des instructions :
– exemple de A + 15 = C  
– instruction :  
	● add A, 15, C  
		– Instruction source1, source2, destination  
	● en fonction de l’instruction :  
		– Load #12, A
### CPU théorique : AR1  
	– Programming model :  
		● 4 GPRs de 8 bits  
		● 8 bits d’adressage  
		● 1 PSW  
		● 1 ALU
### LE PREMIER PROGRAMME
### • Programme :  
	load #12, A  
	load #13, B  
	add A, B, C  
	store C, #14
	-
	1.  "load #12, A" : Cette instruction charge la valeur stockée à l'adresse mémoire 12 dans le registre A. Le symbole "#" indique qu'il s'agit d'une adresse mémoire plutôt qu'un registre. Cette instruction permet de charger une valeur stockée en mémoire dans un registre pour une utilisation ultérieure.
	2.  "load #13, B" : Cette instruction est similaire à la première instruction, mais elle charge la valeur stockée à l'adresse mémoire 13 dans le registre B.
	3.  "add A, B, C" : Cette instruction effectue une opération arithmétique en ajoutant les valeurs stockées dans les registres A et B, puis stockant le résultat dans le registre C. Cette instruction permet de faire des calculs avec les valeurs stockées dans les registres.
	4.  "store C, #14" : Cette instruction stocke la valeur stockée dans le registre C à l'adresse mémoire 14. Cette instruction permet de stocker des valeurs dans la mémoire pour une utilisation ultérieure. Le symbole "#" indique qu'il s'agit d'une adresse mémoire plutôt qu'un registre.
### • On utilise le contenu de MR => on  
doit connaître leur contenu
### Programme :  
load #12, A  
load #13, B  
add A, B, C  
store C, #14
Mémoire centrale:
![[Pasted image 20230121141656.png]]
### • Les mode d’adressage :  
	– Direct  
		● Load #12, A  
	– Indirect  
		● Load #D, A  
	– Indexé  
		● Load #(D+108), A
### • Intérêt :  
– chargement du PGM en RAM  
– L’emplacement parfois différent  
– Qui le sait ?  
– L’OS  
– Il fournit l’info (dans D p. exemple)
## Chapitre 2:
### Exécution d’un programme
• C’est ..... :  
	– une suite d’instructions  
	– chargées en mémoire (MR) centrale  
	– qui s’exécute instruction/instruction  
	– en se suivant les 1 après les autres  
	– sauf en cas de saut  
	– qui va lire/écrire des données en MR  
	– jusqu’à sa fin
• Une suite d’instructions :  
	– Codées en binaire dans la mémoire  
	– Exprimées en assembleur  
	– Résultat (le plus souvent) d’une compilation  
	– Suite d’instructions ≡ suite logique  
	– chaque instruction : séquence d’exécution  
	– Différents type d’instruction  
		● load/store (load /store unit)  
		● Jump (BU)  
		● Calculs (ALU)
• Chargées en mémoire (MR) :
	– Seule la MR est directement « sur » le CPU  
	– La mémoire de masse (HDD, SDD, USB, TAPEs)  
		● Interface de gestion (électronique)  
		● Système de fichier (géré par l’OS)
• Exécution instruction/instruction  
	– Quand il y a une seule ALU  
	– Dans les CPU modernes : plusieurs possibles  
	– Vu du programming model : peu importe
• En se suivant les unes les autres  
	– Dès que 1 instr. Exécutée  
	– On lit la suivante (en MR)  
	– (PC + « 1 »)  
	– Et rebelotte
• Sauf quand il y a un saut  
	– Toute la MR est « en ligne »  
	– Tests, conditions, appels de routines
• lire/écrire des données en MR  
	– Registres en nbre. limité  
	– Petites taille  
	– Mémorisation des résultats
• Jusqu’à l’arrêt  
	– Un programme fait un traitement  
	– Quand il est fini  
	– Retour à l’OS  
	– Libération de l’espace en MR (si c’est en RAM)
AR1
	• CPU théorique pour l’étude  
		– Simple  
		– Programming model :
![[Pasted image 20230121142351.png]]
		– GPRS : registres à usage général (4)  
		– PC : program counter  
		- PSW (Process Status Word) est un registre utilisé pour stocker des informations sur l'état d'un processus en cours d'exécution. Il peut contenir des informations telles que les codes d'erreur, les indicateurs de condition, les codes de privilèges, etc. Il est utilisé par le système d'exploitation pour gérer les processus et pour effectuer des opérations de commutation de contexte.
		- IR (Instruction Register) est un registre qui contient l'instruction en cours d'exécution. Il est utilisé pour stocker l'instruction qui est actuellement exécutée par le processeur. Il est utilisé pour décoder l'instruction et pour fournir les données nécessaires aux unités de traitement pour effectuer l'opération spécifiée par l'instruction. Lorsque l'instruction est exécutée, le contenu de l'IR est mis à jour avec la prochaine instruction à exécuter.
		– ALU : unité arithmétique et logique  
		– I/O unit : interfaces de bus
	• Codage des instructions  
		– Plusieurs groupes de bit  
		– Chacun a sa fonction  
		– En fonction du « mode » de l’instruction
		– Plusieurs groupes de bit  
		– Chacun a sa fonction  
		– En fonction du « mode » de l’instruction  
		– Forme générale :
		![[Pasted image 20230121142502.png]]
		– Forme générale :
		![[Pasted image 20230121142529.png]]
		– 16 bits = 2 bytes = 2 octets
		– Forme générale :
		![[Pasted image 20230121142554.png]]
		– 2 octets = 2 adresses MR pour une instruction
		– Pour des valeurs immédiates (8 bits) :
		![[Pasted image 20230121142626.png]]
		– Chargement d’un reg.avec une MR immédiate :
		![[Pasted image 20230121142649.png]]
		– Load relatif : source = base + offset
		![[Pasted image 20230121142713.png]]
		– Mode :  
			● = 0 si opération sur les registres  
			● = 1 si donnée immédiate
		– opcode :  
			● = 000 ... 111  
			● = opération exécutée  
			● Pas seulement par l’ALU
		– source/destination (registre) :  
			● = 00 : A  
			● = 01 : B  
			● = 10 : C  
			● = 11 : D
		– Donnée immédiate :  
			● Codée sur 8 bits  
			● Tous les bits sur le même octet (byte)
		- Ex:
			![[Pasted image 20230121142851.png]]
			-
			![[Pasted image 20230121142909.png]]
			-
			![[Pasted image 20230121142924.png]]
			– Plus de bits pour l’opcode et les registres : impact sur l’instruction set (jeu d’instructions)  
			– Si j’ai 5 bits pour l’opcode ?  
			– Si j’ai 18 registres ?
			– Codage binaire : lourd  
			– Premier langage : m’assembleur (cf plus haut)  
			– Besoin d’un traducteur = assembleur  
			– Assembleur = langage bas niveau (pas de variables, par  
			exemple)  
			– Possibilité de facilités (labels, etc ...)
			– Pour des aplication plus modernes : langage de haut niveau  
			– Langages compilés (p. ex. « C », « C++ », « pascal », ....)  
			– Plus facile, moins en prise directe avec le programming model  
			(plus portable d’un ordinateur à un autre)  
			– Plus économique dans la mise en œuvre
		• décodage des instructions  
			– Instructions lues => décodage  
			– Nouveau registre  
			– IR : instruction register
			![[Pasted image 20230121143057.png]]
			-
			![[Pasted image 20230121143116.png]]
		• Cycle d’exécution des instructions  
			– chercher les instruction en MR  
			– Décodage  
			– exécution
		• Cycle d’exécution des instructions  
			– chercher les instruction en MR  
			« Fetch »  
			– Décodage  
			« Decode »  
			– Exécution  
			« Execute »
			– « Fetch »  
				le CPU va lire l’instruction en MR  
			– « Decode »  
				Le « IR » branche les composants pour exécution  
			– « Execute »  
				Les opérations sont réalisées + « PC » = + 1
			– Note : dans l’AR1 :  
				● Datas = 1 octet  
				● Instruction = 2 octets  
				● « PC » + 1 = +2 sur ADRS
			– La vitesse d’exécution dépend du CLK (fréquence horloge CPU)  
			– Idéalement : 1 clk = 1 instruction  
			– Pas possible  
			– On augment CLK le + possible
			![[Pasted image 20230121143334.png]]
			-
			![[Pasted image 20230121143351.png]]
			• La BU  
				– Il y a plusieurs types de sauts  
					● Les sauts avec/sans retour  
					(jump/call/return)  
					● Les saut (in)conditionnels  
					(jump/jz/jnz)
			• L’ALU  
				– Tout ce qui se calcule  
				– Arithmétique  
				– Logique  
				– Sur des entier  
				– Sur combien de bits ?
			• Le load et store unit  
				– Le plus coûteux en temps  
				– Déroulement  
					● Mettre l’adresse sur l’add.bus  
					● Au clk suivant « lire/écrire »  
					● Remettre d’adresse sur le PC
## Chapitre 3:
Pipelined Execution:
Rappel sur l’exécution:
Rappel du cycle de base
	1.Fetch  
	2.Decode  
	3.Execute  
● Avec l’étape 3 divisée en (ex de  
l’addition):  
	a)Read  
	b)Add  
	c)Write
Remarque
	● La plupart des μc actuels traitent:  
		– Les sous-étapes 3a (read) et 3b (add)  
		comme un seul groupe,  
		– La sous-étape 3c (write) séparément.  
	● L’explication de ce point sera  
	abordée plus loin dans le cours.
Séquence à utiliser
● Fetch  
● Decode  
● Execute  
	– Read  
	– Add  
● Write  
	Quatre phases du cycle de vie d’une  
	instruction
![[Pasted image 20230121143709.png]]
-
![[Pasted image 20230121143730.png]]
-
![[Pasted image 20230121143745.png]]
-
![[Pasted image 20230121143801.png]]
-
![[Pasted image 20230121143838.png]]
-
![[Pasted image 20230121143852.png]]
-
![[Pasted image 20230121143907.png]]
-
![[Pasted image 20230121143924.png]]
-
![[Pasted image 20230121143937.png]]
-
![[Pasted image 20230121143951.png]]
-
![[Pasted image 20230121144003.png]]
-
![[Pasted image 20230121144017.png]]
-
![[Pasted image 20230121144029.png]]
-
![[Pasted image 20230121144042.png]]
Définition :
![[Pasted image 20230121144108.png]]
Attention
	• Le Completion Rate doit être défini comme le  
	nombre d’instructions terminées par unité de  
	temps  ex: en instr/ns  
	• A ne pas confondre avec le temps d’exécution  
	(program execution time) d’une instruction en  
	ns.  
	• Dans un processeur sans pipeline, le rapport  
	entre les deux est de type inversement  
	proportionnel.
	• Par contre, nous verrons que le  
	pipeline parvient à augmenter le  
	completion rate sans modifier le  
	temps d’exécution d’une instruction .  
	• Et même plus, avec des instructions  
	qui parfois, mettront un peu plus de  
	temps pour s’exécuter dans un  
	processeur avec pipeline que dans  
	un processeur sans pipeline !
Augmenter les performances
	• Deux pistes sont envisageables:  
	– Réduire le nombre d’instructions du  
	programme  
	– Augmenter le  
	completion rate.  
	• Nous considérerons d’abord que le nombre  
	d’instructions du programme est fixé.  
	• Nous allons donc étudier comment le  
	pipeline augmente le  
	completion rate
Analogie avec une fabrique de voiture
	1. Fabriquer le châssis  
	2. Mettre le moteur sur le châssis  
	3. Mettre les portes, les ailes et le capot  
	4. Attacher les roues  
	5. Peindre le véhicule  
	Pour cela, la chaine de production est  
	composée de 5 équipes distinctes  
	spécialisées dans un seule tâche.
Première approche
	• Les étapes se suivent et la production d’un  
	nouveau véhicule débute dès que le  
	précédent est fini,
	![[Pasted image 20230121144245.png]]
Deuxième approche
	• Une étape débute dès que la  
	précédente est terminée
	![[Pasted image 20230121144317.png]]
Gain
	• Dès la 6ème heure, on passe de 1  
	véhicule toutes les 5h à 1 véhicule  
	par heure.  
	• Sans changer le temps total pour  
	fabriquer un véhicule, on améliore  
	d’un facteur 5 les performances.  
	• Pour peu que la chaîne de fabrication  
	reste pleine...
Pour les processeurs single cycle
	• Single cycle = absence de pipeline  
	• 1 cycle de vie d’instruction = 1 cycle  
	d’horloge
	![[Pasted image 20230121144405.png]]
observations
	• Pour améliorer le  
	completion rate, il faut  
	cadencer l’horloge de + en + vite.  
	• Sans dépasser le temps maximum que  
	prend une instruction pour s’exécuter  
	complètement.  
	• Illustration précédente: un programme de  
	4 instructions prendra 16 ns, soit un  
	completion rate de 0,25 instr,/ns.
Pour les processeur avec pipeline
	• Ici une profondeur du pipeline de 4
	![[Pasted image 20230121144444.png]]
	• Dès le début de la 5ème ns, une  
	instruction est exécutée toutes les  
	ns.  
	• Les performances passent de 0,25  
	instr,/ns  
	à 1 instr,/ns  un gain de 4.
Incidence sur l’horloge
	• L’horloge ne cadence plus une instruction  
	complète mais les phases d’une  
	instructions.  
	• les pulsations sont bien plus courtes.  
	Dans l’exemple: 4ns  1ns  
	• Ceci implique qu’une instruction ne doit  
	plus nécessairement être finie à la fin de  
	chaque cycle d’horloge (ex: avant de  
	début de la 5ème ns dans l’illustration  
	précédente).
Incidence sur la durée d’exécution du programme
	• La durée d’exécution d’une instruction n’a  
	pas été modifiée mais la durée d’exécution  
	totale du programme entier (suite  
	d’instructions) a été fortement réduite.  
	• Cela a été réalisé en augmentant le nombre  
	d’instructions terminées par unité de temps.  
	• Le pipeline rend plus efficace l’utilisation  
	des ressources du CPU en faisant travailler  
	simultanément ses différentes sous-unités.
Améliorer encore les performances
	• En passant d’un processeur  
	single cycle à  
	un processeur ayant un profondeur de  
	pipeline de 4, on observe une amélioration  
	des performances d’un facteur 4.  
	• Que se passerait-il si la profondeur du  
	pipeline passait à 5, 6, 7,... avec des  
	durées d’étapes intermédiaires de + en +  
	courtes ?
Réponse
	![[Pasted image 20230121144607.png]]
	-
	![[Pasted image 20230121144625.png]]
Observations
	• Avec un découpage en 8 étapes, on  
	obtient 1 instruction terminée toutes  
	les 0,5 ns  
	•  completion rate : 2 instr./ns
Limites du Pipeline
Observation des 9ères ns  
	• En 8 ns, le pipeline a permis  
	d’exécuter 5 instructions  
	• Un processeur  
	single cycle en  
	aurait exécuté 2 dans le même  
	temps  
	• 5 au lieu de 2 ne représente  
	pas vraiment un gain de 4  
	comme annoncé !  
	• Et 5 instructions/8ns donne un  
	completion rate de 0,625  
	inst/ns ce qui ne représente  
	pas non plus le 1 inst/ns  
	annoncé !
	![[Pasted image 20230121144707.png]]
Analyse
	• Pour que le gain du au pipeline devienne  
	appréciable, il faudra que le nombre  
	d’instructions dans le programme soit  
	suffisant.  
	• Ex. Sur 1000 ns, un processeur à pipeline de  
	profondeur 4 aura exécuté 996 instructions  
	au lieu des 250 du processeur sans pipeline.  
	• Soit un gain de 3,984 ≈ 4  
	• 4 est en réalité un maximum théorique et  
	3,984 est la moyenne réelle.
Graphiquement
![[Pasted image 20230121144741.png]]
Décrochage du pipeline
	• Il peut arriver que des étapes du pipeline  
	nécessitent plus d’un cycle horloge !  
	• Des « bulles » apparaissent et voyagent  
	alors dans le pipeline, réduisant ainsi ses  
	performances.  
	• La  
	latence d’une instruction peut traduire  
	le temps réel qu’elle met pour traverser  
	le pipeline en prenant en compte les  
	bulles.
	![[Pasted image 20230121144810.png]]
	-
	![[Pasted image 20230121144822.png]]
	Idem mais avec 10 cycles bloqués sur 100
	![[Pasted image 20230121144847.png]]
Valeurs réelles
	• En pratique, un processeur cadencé à 3 GHz  
	peut facilement attendre 50 à 120 ns des  
	données en provenance de la mémoire  
	centrale.  
	• Une centaine de ns représentent, à ces  
	cadences, quelques milliers de cycles  
	d’horloge.  
	• Et cela pour un seul accès mémoire. Or il s’en  
	produit des millions lors du déroulement d’un  
	programme...
CCL sur le décrochage du pipeline
	• Les « bulles » » doivent absolument être  
	évitées au maximum.  
	• Or, elles sont généralement dues à des  
	accès trop lents à la mémoire centrale.  
	• Une des solutions envisageables est le  
	recourt à de la mémoire cache.  
	• D’autres causes et pistes de solutions  
	associées existent.
Limites du pipeline
	• Dans la pratique, il n’est pas toujours facile  
	de découper une instruction en autant  
	d’étapes équivalentes qu’on le voudrait.  
	• Toute la difficulté réside dans ce découpage  
	car certaines étapes finiront toujours par être  
	plus longues que d’autres (car indivisibles)  
	• Or, ce sont ces étapes plus longues qui  
	influencent le rythme de l’horloge et donc  
	finalement le temps d’exécution d’une  
	instruction.
	• En fait on peut même concevoir qu’une  
	instruction réalisée dans un pipeline peut  
	prendre plus de temps pour s ’exécuter  
	que dans un processeur sans pipeline !!!  
		– Ex: une instruction prend 4 ns pour se  
		réaliser sans pipeline.  
		– On la sépare en 4 étapes dont les durées  
		sont respectives sont w,x,y et z ns (proches  
		de 1 ns mais pas parfaitement identiques).  
		– Soit x, la plus longue qui impose le rythme  
		( x > 1 ns)  
		– On a un temps total de 4 fois x > 4 ns
	● L’horloge représente également une limite.  
	● On ne peut généralement pas atteindre  
	l’horloge théorique idéale:  
	horloge sans pipeline  
	/ profondeur du pipeline.  
	● L’horloge réelle est donc toujours limitée à une  
	cadence maximale.  
	● A une même cadence limite, un processeur  
	avec une profondeur plus élevée mettra alors  
	plus de temps pour se remplir.
	• Graphiquement
	![[Pasted image 20230121145038.png]]
	● Le coût financier du pipeline n’est pas  
	négligeable.  
	● Une architecture à pipeline est plus  
	complexe et requière des composants  
	supplémentaires.  
	● Ces composants ont évidement un  
	coût !