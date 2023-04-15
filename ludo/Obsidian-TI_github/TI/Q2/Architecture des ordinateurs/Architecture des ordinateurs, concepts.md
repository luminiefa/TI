 Grands types de virtualisation :  
	 Hardware  
	 SDS : Software Defined Storage  
	 SDN : Sofware Defined Network  
	 SDDC : Software Defined Data Center : combinaison des 3

 ISA + microcode  
 RISC  
	 Compilateur entre ISA et programmeur  
	 Augmentation performances

 2 familles de technologies :  
	 Virtualisation de systèmes d'exploitations  
	 Virtualisation d'applications

 Avantages :  
- Consolidation  
		* Meilleure utilisation de CPU (un serveur utilise typiquement 5-10%)  
		* Économie de surface et d’électricité en datacenter (argent + environnement)
- Load balancingtl
	- Une batterie de serveurs peut equilibrer la charge en déplaçant une machine virtuelle d'un système sur-utilisé à un système sous-utilisé  
- Tolérance de panne  
	- Si le matériel d'un serveur se dégrade, les machines virtuelles de ce serveur peuvent être transférées (en direct) vers d'autres serveurs. Le serveur d'origine peut ensuite être arrêté pour maintenance, sans interruption de service.  
- Isolation  
	- Les OS multi-utilisateurs ne suffisent pas toujours à isoler les utilisateurs les uns des autres  
		- Utilisateur demandant beaucoup de ressources  
		- Virus  
	- Un administrateur peut facilement isoler une VM pour des raisons de  
	performances et/ou de sécurité.
- Déboguer des programmes  
	 Si un bug bloque complètement l’OS et nécessite à chaque fois un  
	redémarrage pour pouvoir déboguer → plus rapide de redémarrer  
	une VM.  
- Développement logiciel (ex : android)  
	 Les développeurs utilisent également la virtualisation pour écrire  
	des programmes pour un OS ou un ISA bien spécifique et ce sur  
	n’importe quel OS hôte.  
- Compatibilité avec d'anciens systèmes (ex : win95/XP)  
- Virtualisation hétérogène  
	 Linux, Windows, AX, MAC, Android,...  
- Administration simplifiée  
	 Fini les problèmes hardware  
- HA, Migration, Clonage, affectation des ressources à chaud, Création de  
modèle...

- Contraintes :  
	 Pas de Self Service (Gestion par un admin)  
	 Surcharge de travail CPU  
		 logiciel « intermédiaire » en plus  
		 Un kernel /VM  
		 Solution : containers

Modèle de la Pile hard/Soft habituel
 Système d'exploitation au dessus du matériel  
 Logiciels au dessus de l'OS  
 L'OS  
	 a un accès exclusif avec tous les privilèges au matériel  
	 donne un accès sélectif aux ressources matérielles  
 Rôles de l'OS :  
	 Isoler les processus  
	 Gérer le partage des ressources entre les processus  
 → OS doit avoir accès complet au matériel  
 Virtualisation : Faire croire que l'OS a cet accès

![[Pasted image 20230212111221.png]]

![[Pasted image 20230212111251.png]]

Notions
 OS Hôte  
 OS Invité (Guest)  
 VMM : Moniteur de machine virtuelles  
	 Logiciel qui fait croire aux OS invités qu'ils tournent directement sur le matériel  
	avec tous les privilèges sans couche logiciel intermédiaire  
		 en exécutant un VMM au-dessus d'un système d'exploitation hôte qui  
		hébergera plusieurs machines virtuelles  
		 en installant un VMM entre le matériel et les OS invités, dans ce cas, le VMM  
		est appelé hyperviseur  
 ISA x86  
	 Pas prévue pour → compliqué  
	 Ajout des extensions à l'ISA pour la virtualisation (~ 2007)  
		 Intel Vanderpool : VT-x  
		 AMD : AMD-V  
	 Amélioré à chaque nouvelle génération de CPU par de nouvelles extensions  
 Machine virtuelle  
	 Image créée par un VMM d'un ordinateur "idéal" présentée à un OS

Méthode de virtualisation
 1. Hyperviseur  
	 Intermédiaire direct entre le matériel et les OS Virtualisés  
	 Tourne en espace kernel  
 2. Modèle hôte invité  
	 VMM exécuté en espace utilisateur → VM dans l'espace utilisateur  
		 Plus lent  
		 Plus facile à mettre en place  
 La VMM doit donner l'illusion à l'OS invité qu'il a l'accès exclusif à  
	 CPU  
	 Mémoire  
	 Stockage  
	 I/O

![[Pasted image 20230212111714.png]]

Technologies de Virtualisation
 Supportées au moins en partie par la majorités des VMM's actuels  
 Matérielles (assistée par le « hardware »)  
	 le matériel fournit un support architectural qui facilite la construction d’un  
	VMM et permet aux systèmes d'exploitation invités de fonctionner de  
	manière isolée  
		 CPU  
			 VT-x / AMD-V  
		 Mémoire (MMU)  
			 Nested paging : Intel EPT et AMD RVI  
		 Mémoire de masse (HD)  
		 I/O (carte réseau etc.)  
			 Chipset I/O MMU intel VT-d / AMD-Vi  
		 Périphériques  
			 GPU : intel GVT (Graphics Virtualization Technology)

Logicielles  
 Full Virtualisation  
	 L’hyperviseur crée un environnement virtuel  
	complet en simulant du « faux » matériel.  
	L’OS invité n’a accès qu’à ces ressources  
	simulées, et non aux ressources matérielles  
	réelles. Ce type de virtualisation est limité  
	aux systèmes d’exploitation prévus pour la  
	même architecture matérielle (x86, x64,  
	ARM, ...) que le processeur physique de la  
	machine hôte.  
 Émulation  
	 Pour dépasser les limites ci-dessus,  
	l’hyperviseur créé un environnement virtuel  
	complet. Il simule un microprocesseur qui  
	peut avoir une architecture matérielle  
	différente de celle du CPU hôte. Le  
	principal inconvénient est le niveau de  
	performances, souvent assez bas. (Vmware  
	Server, Virtualbox, Microsoft Virtual PC, ...)

![[Pasted image 20230212111836.png]]

 Paravirtualisation (PVM)  
	 Le système d’exploitation invité est  
	conscient de s’exécuter dans un  
	environnement virtualisé → modifications  
	logicielles (par exemple l'installation de  
	pilotes ou d'une surcouche logicielle). En  
	contrepartie, il devient capable d’interagir  
	avec l’hyperviseur et de lui demander de  
	transmettre directement les appels  
	systèmes au matériel du serveur hôte.  
	Les performances « virtuelles » sont  
	alors théoriquement proches de celles  
	qu’il serait possible d’atteindre avec le  
	matériel réel. (Xen, KVM, ...)  
	 PCI PassThrough / DirectPass I/O

![[Pasted image 20230212111919.png]]
 
 Virtualisation assistée par le matériel (HVM)  
	 Ajout d’extension de virtualisation au  
	processeur  
		 Intel-VT et AMD-V  
 Les VM’s gèrent leurs propres  
interruptions et leurs changement de  
contexte  
 Plus d’émulations de zone mémoire  
 Accès direct au processeur

![[Pasted image 20230212112356.png]]

![[Pasted image 20230212112421.png]]

 Isolation  
	 L’isolateur est une spécificité des systèmes Unix. Cette technique  
	permet d’isoler une application du reste du monde. (VServer, chroot, bsd  
	jail, ...)

![[Pasted image 20230212112452.png]]

 Container  
	 Pas de noyau dans les containers  
	 Un répertoire = un OS  
	 Pas d’émulation matériel  
	 Accès direct au matériel

![[Pasted image 20230212112557.png]]

 Pour mettre en place ces techniques, il faut donc du « matériel virtuel »  
implémenté logiciellement ou dans le matériel:  
	 CPU virtuel  
		 Virtual Instruction Set  
		 Virtual Memory Management Unit MMU  
		 Virtual Programmable Interrupt Controller (PIC)  
	 Mémoire virtuelle  
	 Périphériques d'E/S virtuels  
	 Timers virtuels  
	 Autres périphériques

![[Pasted image 20230212112655.png]]

Rappel sur les privilèges d'accès
 CPU n'accepte pas « d'office » d'exécuter toutes les instructions  
	 L'OS peut accéder directement au matériel  
	 Un processus normal ne peut pas  
 Niveau de privilège  
	 Mécanisme intégré au processeur qui empêche une application  
	d'usurper l'accès hardware de l'OS  
	 "Ring levels"  
		 0 le plus privilégié : accès complet (OS)  
		 Nombre dépend de l'ISA  
			 X86 : 4  
			 2 seulement utilisés par les OS : 0 et 3

Virtualisation et privilèges
 Code user level (ring3)  
	 Le code est exécuté directement sur le CPU  
	 Le code d'exécution ne peut accéder directement au matériel ou à la mémoire  
 Code kernel level (ring 0):  
	 Seul un processus en ring 0 peut accéder aux données et instructions de  
	l'état privilégié  
		 L'état = Les variables et tableaux liés à un processus stockés en RAM et  
		dans le CPU  
		 Données à sauvegarder si l'on arrête le processus pour le relancer plus tard  
		 Ex : Pages mémoires et flags associés  
		 L'état privilégié : les données privées de l'OS à propos des processus  
		 Hyperviseur gère l'accès à ces données  
			 Lecture → ok  
			 Ecriture / modification → interdits  
	 → Virtualiser le jeux d'instructions ring0 pour cacher à la VM qu'elle  
		 n'est pas dans le ring 0  
		 Partage le matériel avec d'autres OS

 Mécanismes pour cacher à la VM qu'elle n'est pas dans le ring 0 et gérer l'accès aux  
instructions privilégiées (Full Virtualization) : virtualisation du jeux d'instructions  
	 Trap & emulate  
		 Un programme veut exécuter une instruction pour laquelle il n'a pas de privilège  
		suffisant (pas le bon ring)  
			 → une exception (trap) est générée  
		 L'hyperviseur écoute les exceptions provoquées par l'OS virtualisé. Il  
			 Intercepte (traps) l’exception: il reprend la main sur le CPU  
			 Exécute l’instruction pour émuler le comportement attendu  
			→ Os invité ne voit voit pas qu'il est n'est pas en ring 0  
 Mécanismes pour cacher et gérer l'accès aux informations privilégiées  
	 Shadow structure  
		 Un OS doit accéder et modifier certaines donnés liée au hardware, stockées  
		dans  
			 RAM  
			 registres CPU  
		 Un CPU ne supporte qu'un seul exemplaire de ces données → un seul OS  
		 Shadow structure = une copie privée propre à une VM gérée par l'hyperviseur

Problèmes de l'ISA x86
 L'ISA x86 permet l'accès au mode privilégié sans provoquer d’exception  
	 Certaines instructions sont <> en ring 3 & 0 → L’hyperviseur n'est pas prévenu  
	par manque de traps → trap & emulate impossible  
	 Techniques de virtualisation "classique" du jeux d'instruction impossible  
 Solutions possibles :  
	 1998 :Just in time Binary translation  
		 « traduction » à la volée du code kernel non virtualisable (émulation)  
			 Translation lors du 1er appel du code  
			 Ensuite, stocké dans un cache pour accès plus rapide  
		 Trap & emulate pour les instruction qui provoquent des traps  
	 Paravirtualisation  
	 Extension de l'ISA x86 → VT-x, AMD-V  
		 Ajout « root mode » pour le VMM

![[Pasted image 20230212113619.png]]

Virtualisation de la mémoire
 VMM  
	 Partage de la mémoire physique entre VM's  
	 Allocation dynamique de la mémoire aux VM's  
 Même principe que la présentation de la mémoire au processus par un OS  
	 L’application voit un espace mémoire présenté par l'OS qui n'est pas lié à mémoire physique  
	 L’OS gère une table de correspondance en RAM  
	entre les pages de mémoire virtuelle et les pages  
	physiques de la table des pages physiques  
	 Le but est d’améliorer les performances de la  
	mémoire virtuelle  
		 MMU :Memory Management Unit assure la gestion  
		matérielle de  
			 Adresse virtuelle (VA) → adresse linéaire (LA) (table des segments)  
			 Adresse linéaire (LA) → adresse physique (PA) (table des pages)  
		 TLB  
			 Mémoire cache du CPU dédiée à la translation  
			d'adresse virtuelle (+ rapide que la RAM)

![[Pasted image 20230212113751.png]]
![[Pasted image 20230212113803.png]]

 Virtualisation de la MMU  
	 Shadow page table  
		 Une shadow page table associée à chaque table de mémoire virtuelle  
		 2 associations dans une shadow page table :  
			 Crée par le guest : LA VM → PA VM  
			 Crée par le VMM : PA VM → adresse machine (MA)  
		 une seule table pour associer la mémoire virtuelle de la VM à la MMU de la  
		machine → presque aussi rapide qu'en « natif », sauf dans certains  
		situations

![[Pasted image 20230212113942.png]]

 Hardware  
	 2ème génération extensions x86 pour virtualisation  
		 AMD RVI et Intel EPT  
		 MMU table avec 2ème table :  
			 LA → PA modifiable par la VM  
			 PA → MA modifiable par le VMM  
		 TLB rempli avec correspondances LA → MA  
		 VMM ne doit plus intervenir lors d'une modification  
		 Parcours hardware des tables  
	 Gain de performance : de rien ou légère perte à +- 40 %

Solutions
 Émulateurs  
	 MAME (borne arcade)  
	 BOCHS  
	 Android ARM : intégré à Android  
	Studio et MS Visual Studio  
	 Consoles : emu pour NES, PS, etc.
 Simulateurs
 Isolateurs / containeurs  
	 Chroot  
	 Docker  
	 LXD  
	 BSD Jail  
	 Linux Vserver  
	 OpenVz  
	 Solaris container
 Hyperviseurs Type I
	 VmWare ESXi  
	 Xen  
	 HyperV  
	 KVM
 Hyperviseurs Type II
	 VirtualBox  
	 VmWare player/Workstation  
	 HyperV server (sur base de  
	Windows Core)  
	 Qemu  
	 Parallels (mac)

Cloud
 Définition : Mise à disposition à la demande de ressources informatiques partagées (CPU, mémoire, stockage, réseau) via un réseau  
ou Internet. Ressources en général situées dans un datacenter.  
 Types  
	 Iaas  
		 Infrastuture as a service  
		 Fourniture de VM's  
		 Stockage  
		 Réseau  
		 Load balancers  
		 Ex : OpenStack  
	 Paas  
		 Platform as a service  
		 Hébergement d’application  
		 Environnement de développement (Middelware) avec DB, réseaux, etc.  
		 Ex : Azure, Google Engine  
	 Saas  
		 Software as a service  
		 Ex : Google Docs, Office 365  
	 Publique  
		 Via un fournisseur Cloud  
		 !!sécurité !!!  
		 Ex : Amazon, Rackspace, SalesForce  
	 Privé  
		 Cloud interne  
		 Vsphère, OpenStack, Citrix  
 Hybride  
	 Mix de privé et publique

Containers
 Virtualisation au niveau de l’OS  
	 Plusieurs instances du même OS qui tournent avec le même Kernel  
 Chaque container contient tout ce qui est nécessaire pour tourner:  
	 Application  
	 Dépendances de l’espace utilisateur (JVM, shell, etc.)  
	 Librairies  
 Éléments de l’espace kernel fournis par l’OS hôte  
 OS hote  
	 Isole les ressources des containers  
	 Alloue les ressource CPU et RAM  
 → Container doit être prévu pour un OS  
 Avantage  
	 Déploiement facile de plusieurs instances d’un application  
	 Isolation  
	 Performance ÷ Machine Virtuelle  
 Inconvénient  
	 Dépendant de l’OS → pas Cross platform  
	 Isolation moins forte que avec une VM


# Chapitre 5 - 64 bits
## Introduction
● ISA x86 était peu pratique d'utilisation :  
– Mode d'adressage complexe  
– Instructions obscures  
– Instructions de longueur variable  
– ...  
● Et pourtant, l'ISA x86 continue à avoir du succès  
grâce à l'inertie du marché.  
● Le coût pour passer à l'ISA RISC serait trop élevé.
## Pourquoi passer au 64 bits ?
En fait, cette question en englobe deux :  
– Comment les serveurs 64-bit et le marché du  
PC utilise l'informatique 64-bit ?  
– Quelle est l'utilité de l'informatique 64-bit pour  
le marché du consommateur ?
## Qu'est-ce que l'informatique 64-bit ?
● De manière simple, lorsque l'on parle de  
microprocesseur, les étiquettes 16, 32 et 64  
bits correspondent au flux de données du  
processeur.  
● Plus spécifiquement, cela correspond au  
nombre de bits que peuvent contenir  
chacun des GPRs du processeur.
● Processeur 64-bit : processeur avec des  
GPRs pouvant stocker des nombres 64-bit.  
● Instruction 64-bit : instruction travaillant sur  
des nombres 64-bit stockés dans des  
GPRs 64-bit.
## Ordinateur 32-bit vs 64-bit
![[Pasted image 20230411105004.png]]
● D'autre part, la largeur du flux données et  
résultats a lui doublé.  
● Pour pouvoir gérer ce flux plus large, la  
taille des registres et la taille des bus  
alimentant ces registres ont aussi du  
doublé.
![[Pasted image 20230411105035.png]]
## Pourquoi l'informatique 64-bit
● On commence à répondre à la question de  
manière simple:  
– Les données et les registres sont plus grands  
● La réponse peut en fait être un peu plus  
complexe si on prend en compte les autres  
types de données.
## Types de données en 32-bit et 64-bit
![[Pasted image 20230411105104.png]]
## Avantages du 64-bit
● Dynamic Range (DR)  
– Des entiers plus larges permettent de  
représenter plus de nombres...  
– Le passage du 32 bit au 64 bit permet de  
multiplier la DR par 4.3 milliards  
– Un entier 64 bits permet de représenter  
beaucoup plus de nombres qu'un entier 32  
bits.
● Certaines applications (monde scientifique  
– simulations) ont besoin des entiers 64-  
bits car ils travaillent avec des nombres  
sortant de la DR des entiers 32 bits.  
● Quand le résultat d'un calcul dépasse la  
fourchette de valeurs d'entiers  
représentables, on entre en situation  
d'Overflow ou d'Underflow.
● Quand ces situations arrivent, le nombre  
se trouvant dans le registre de résultat  
n'est pas la réponse correcte.  
● Un bit dans le PSW signale si le résultat a  
dépassé le DR, prévenant ainsi de l'erreur.
● Des GPRs plus grands permettent de  
représenter des entiers plus grands, mais  
surtout, de travailler sur des adresses plus  
grandes !  
● Les adresses plus grandes sont le principal  
avantage de l'architecture 64-bit sur la 32-bit.
● Tous les composants d'un PC avec lequel  
on communique dispose d'une adresse.  
● Sans adresse, on ne pourrait pas  
communiquer directement avec lui.  
● Toutes les adresses sont représentées par  
un nombre (un entier)...
● Or, le nombre de bits composant une  
adresse va affecter la fourchette  
d'adresses pouvant être représentées.  
● Une fourchette d'adresse se nomme  
espace d'adressage.
● Le processeur et l'OS travaillent ensemble  
pour fournir à chaque programme l'illusion  
qu'il a accès à un espace d'adressage de 4 Go  
● Rappelez-vous : 232 nombres. Ces 4,3  
milliard d'octets, soit 4 Go, sont le nombre  
d'octets qu'un PC 32 bit peut représenter.
● En 64 bits, l'espace d'adressage est bien  
plus important.  
● En théorie : 264 nombres possibles soit 18  
millions de To d'espace d'adressage.  
● Dans les faits : 248 nombres soit 282 To de  
mémoire virtuelle (pouvant supporter 1 To  
de RAM).
# Chapitre 6 - Superscalar Execution
## Introduction
•Durant les décennies ayant suivi la sortie de  
l’Intel 8080, le nombre de transistors pouvant  
être embarqués sur une seule puce ont  
augmenté considérablement.  
•Les concepteurs ont cherché de nouvelles  
manières d’exploiter ces transistors.
•Ils se sont rendus compte qu’ils pouvaient  
placer plus d’une ALU sur une puce, les faisant  
alors travailler en parallèle pour traiter le code  
plus rapidement.  
•Les ordinateurs exploitant ce concept furent  
appelés les ordinateurs superscalaires.
## L’architecture AR2
•Version améliorée du AR1 disposant de 2 ALUs.  
•Capable d’exécuter 2 instructions arithmétiques  
en parallèle.  
•Les 2 ALUs partagent les mêmes registres.
![[Pasted image 20230411105859.png]]
## Pipeline du AR2
![[Pasted image 20230411105913.png]]
## Decode/Dispatch
•Un petit circuit de « dispatch » vient se placer à  
la fin de l’étage.  
•Son rôle est de déterminer si oui ou non, deux  
instructions peuvent être réalisées en parallèle,  
c.à.d. sur la même pulsation d’horloge.
•Si elles peuvent être exécutées en parallèle,  
l’unité de dispatch en envoie une à la première  
ALU et l’autre à la deuxième ALU.  
•Si elles ne peuvent pas être exécutées en  
parallèle, l’unité de dispatch les envoie dans  
l’ordre du programme vers la première des deux  
ALUs.
## Programming Model
Le « programming model » ne change pas.  
Bien que le CPU exécute des instructions en  
parallèle, l’illusion d’une exécution séquentielle  
doit être maintenue pour le bien du  
programmeur.  
La mémoire centrale continue de voir un flux  
d’instructions, un flux de données et un flux de  
résultats.
## Cycle d’exécution
•AR2 est capable de « fetch » deux instructions à  
la fois depuis la mémoire en une pulsation  
d’horloge.  
•Il peut également « decode » et « dispatch »  
deux instructions à chaque pulsation d’horloge.
![[Pasted image 20230411110022.png]]
## Architecture superscalaire
•Permet à un microprocesseur de dépasser le  
seuil théorique d’une instruction par pulsation  
d’horloge fixée par l’architecture pipeline  
simple.  
•Dans l’exemple précédent, deux instructions  
sont terminées à chaque pulsation d’horloge,  
une fois le pipeline chargé.
Plus un microprocesseur disposera d’ALUs en  
parallèle, plus le nombre d’instructions  
terminées par pulsation d’horloge pourra être  
élevé.  
Il y a cependant des limites pratiques à ce  
concept qui seront abordées plus tard.
Nous nous sommes limités à l’exécution en  
parallèle d’instructions en ajoutant de nouveaux  
ALUs.  
Dans les processeurs modernes, cette mise en  
parallèle se fait également entre les différentes  
unités d’exécution et pas seulement à celles  
propres aux instructions arithmétiques et  
logiques.
## Différents types de nombres
![[Pasted image 20230411110101.png]]
## Opérations arithmétiques et logiques
•Opérations arithmétiques: Addition,  
soustraction, division et multiplication.  
Compatibles avec tous les types de nombres  
•Opérations logiques: Opérations booléennes  
telles que le AND, OR, NOT, XOR, les shifts et les  
rotations de bits.  
•Compatibles avec les entiers scalaires et  
vectoriels.
![[Pasted image 20230411110126.png]]
## Processeur Intel Pentium
![[Pasted image 20230411110140.png]]
## Distinction entre les ALUs
Jusqu’ici, nous avons considéré les ALUs comme  
étant des unités d’exécutions dédiées aux  
entiers.  
Dorénavant, ALU sera un terme générique pour  
les unités d’exécution faisant des opérations  
arithmétiques ou logiques.
•IU: integer execution unit. ALU dédié aux  
entiers.  
•FPU: floating-point unit. ALU dédié aux  
nombres à virgules flottantes.
## Memory-Access Units
•LSU: Load-Store Unit. Unité responsable des  
instructions load et store ainsi que du calcul des  
adresses.  
•BEU: Branch Execution Unit. Unité responsable  
de l’exécution des instructions de sauts  
conditionnels et non conditionnels.
## Problèmes posés par l’architecture superscalaire
Certaines conditions peuvent empêcher la mise  
en parallèle de deux instructions arithmétiques.  
En plus de perturber l’aspect superscalaire, elles  
peuvent également créer des bulles dans le  
pipeline, comme vu lors de la séance  
précédente.
## Problèmes liés aux données
![[Pasted image 20230411110226.png]]
## Conséquences
Il faudra attendre que l’instruction 1 soit  
terminée et fournisse son résultat pour que  
l’instruction 2 puisse se réaliser.  
C’est un problème tant pour l’exécution  
superscalaire que pour l’exécution en pipeline.
## Conséquences en superscalaire
Si le programme tourne sur un processeur  
superscalaire embarquant 2 integer ALUs, les  
deux instructions ne pourront être exécutées  
simultanément par les deux ALUs.  
De fait, l’ALU exécutant la première instruction  
devra terminer son addition et seulement, l’ALU  
exécutant la deuxième instruction pourra  
réaliser son addition.
## Conséquences en pipeline
La deuxième instruction add devra attendre que  
la première instruction ait terminé son étape  
d’écriture (write) avant de pouvoir entrer dans  
son étape d’exécution (execute).
•Le circuit de dispatch devra donc être capable  
de reconnaître la dépendance entre les deux  
instructions et devra empêcher l’instruction 2  
d’entrer dans sa phase d’exécution avant que le  
résultat de la première ne soit disponible dans le  
registre C.
## Techniques employées par les processeurs
Pour contourner le problème, la plupart des  
processeurs en pipeline disposent d’une  
technique appelée forwarding.  
Le processeur prend le résultat du premier add  
depuis le port de sortie du premier ALU et le  
renvoie directement vers le port d’entrée du  
deuxième ALU, contournant ainsi l’étape  
d’écriture dans le registre.
Etant donné qu’un microprocesseur dispose  
généralement de plus de registres que ceux  
énoncés dans le programming model, une  
technique consiste à réattribuer les registres du  
programming model vers des registres physiques  
pour éviter les conflits.
![[Pasted image 20230411110332.png]]
![[Pasted image 20230411110352.png]]
Il est cependant impératif que le premier add  
soit réalisé avant l’écriture du résultat du second  
add.  
Le problème est réglé à l’aide de ces registres  
temporaires: le deuxième add écrit son résultat  
dans son registre temporaire personnel; une fois  
que les deux add ont terminé leur exécution en  
parallèle, le résultat du deuxième add sera placé  
dans le registre A du programming model après  
que la première instruction ait elle aussi écrit ses résultats.
## Problèmes liés à la structure du CPU
![[Pasted image 20230411110429.png]]
Cependant, il a été nécessaire de faire quelques  
modifications dans la structure du processeur.  
En effet, pour pouvoir permettre l’accès  
simultané aux registres depuis les 2 ALUs, il a  
fallu modifier légèrement la méthode de  
fonctionnement de ces registres pour que 2  
opérations d’écriture simultanées puissent se  
faire.
## Le fichier de registres
Dans un design superscalaire avec de nombreux  
ALUs, il aurait fallu une quantité importante de  
fils connectant chaque registre à chaque ALU.  
La solution a été de regrouper tous ces registres  
en une unité spéciale, le fichier de registres.  
L’unité est un tableau mémoire accessible par le  
biais d’un bus de données et de 2 ports: un port  
de lecture et un port d’écriture.
Au final, chaque ALU est connecté à cette unité à  
l’aide de 2 ports de lecture, permettant la  
lecture simultanée de 2 registres, et d’un port  
d’écriture, lui permettant d’écrire dans les  
registres indépendamment des autres ALUs.  
Une interface spéciale permet à l’ALU de lire ou  
d’écrire dans une registre spécifique de cette  
zone mémoire.
•Par exemple si 2 ALU se partagent une fichier  
de registre, ce dernier aura besoin de 4 ports de  
lecture et de 2 ports d’écriture.  
•Evidement, le nombre de ports sur un fichier de  
registre n’est pas indéfiniment extensible.  
•Une solution est d’utiliser des fichiers de  
registres différents pour des types d’opérations  
différents.  
•De plus, des registres plus petits (qu’un seul  
gros) permettent des accès plus rapides.
## Problèmes liés aux instructions de saut
Lorsque le processeur arrive à un saut  
conditionnel, il doit décider de la prochaine  
instruction à fetch.  
Dans les anciens processeurs, on devait attendre  
pendant que l’instruction de saut était évaluée  
et que l’adresse cible était calculée.  
 création de bulles dans le pipeline.
## Techniques employées par les processeurs
Dans les processeurs modernes, on utilise une  
technique appelée la prédiction de branchement  
pour contourner le blocage dû aux instructions  
de sauts.
Une fois l’adresse de la prochaine instruction  
connue, charger l’instruction depuis la mémoire  
prend également beaucoup de temps (cfr.  
séance 3), ce qui là aussi, génère un effet de  
« bulles » important dans le pipeline.  
Une technique appelée instruction caching  
permet de réduire cet effet négatif.

# Chapitre 7 - RISC-CISC
## ISA
• Soit AR1 et son programming model ainsi que  
son instruction set déjà rencontrés.  
• Cet ensemble programing model et instruction  
set forme l’ISA  
• L’ISA est l’Instruction Set Architecture
• Nous avons ensuite introduit un deuxième  
ordinateur fictif: AR2, rencontré dans le  
chapitre superscalar.  
• AR2 avait une architecture matérielle bien  
distincte de AR1: plusieurs ALU.  
• Pourtant, pour le programmeur, la logique de  
fonctionnement restait inchangée: un  
déroulement séquentiel de son programme
•  malgré des architectures matérielles  
différentes, l’ISA de ces deux machines restait  
inchangé !  
• En effet, le programming model et l’instruction  
set de AR1 et AR2 sont identiques malgré des  
implémentations hardware différentes (des  
microarchitectures différentes)!
## Application: les améliorations du Pentium
• Le pentium est un processeur Intel qui a  
connu plusieurs versions au cours de son  
existence.  
• Ces différentes versions ont été  
accompagnées de nombreuses améliorations  
et nouvelles fonctionnalités: MMX  
(multimedia extensions), SSE (streaming SIMD  
extensions),SSE2.
• Ces « nouveautés » nécessitaient:  
– Des extensions du programming model,  
– Des extensions de l’instruction set.  
• Des extensions de l’ISA mais pas de profondes  
modifications  on conserve ainsi une  
compatibilité avec l’existant.  
• Mais au fait, d’où viennent ces idées ?  
• De chez IBM...
## Petit historique de l’ISA
• A l’origine des premiers ordinateurs , les  
programmes étaient écrits directement pour  
le hardware unique d’une machine.  
• Les programmes étaient intimement liés au  
hardware
![[Pasted image 20230411112510.png]]
• Conséquence: un programme écrit pour une  
machine A n’avait aucune chance de  
s’exécuter sur une machine B.  
• Et ce même au sein d’une même marque telle  
que IBM...  
• Pour chaque nouvelle génération de  
machines, il fallait réécrire tous les  
programmes...  nécessitait beaucoup de  
temps et d’argent !
• La solution proposée par IBM pour assurer la  
portabilité des programmes entre des  
machines distinctes fut le concept d’ISA (IBM  
system/360)  
• L’ISA permet une abstraction par rapport au  
matériel. Les programmes sont écrits pour  
une ISA donnée et non plus pour une  
architecture matérielle précise.
• Si la microarchitecture du processeur évolue,  
la compatibilité restera assurée si l’ISA reste  
inchangée (du moins la partie orientée  
utilisateur).
![[Pasted image 20230411112547.png]]
## Le microcode
• La première solution pour assurer cette  
abstraction (IBM system/360) reposait sur un  
microcode engine.  
• Composition: une mémoire ROM stockant des  
microcodes programs et une unité d’exécution  
qui exécute ces programmes.
• Fonctionnement:  
– L’unité microcode lit l’instruction à exécuter.  
– Elle exécute alors la portion de mémoire ROM qui  
contient le code correspondant à l’instruction lue.  
– Cette exécution produit alors une séquence  
d’instructions machine au format interne du  
processeur.  
• Ce mode de fonctionnent est appelé  
émulation (comparable à un CPU dans un CPU.
• Lors de l’apparition d’une nouvelle génération de  
processeurs, les fabricants n’ont qu’à réécrire un  
microcode adapté de telle sorte que l’ISA proposé à  
l’utilisateur ne change pas.  
• Au début, le mode émulé fonctionnait moins vite  
qu’une exécution directe par le hardware.  
• Néanmoins, l’avantage lié à la compatibilité entre les  
versions de CPU a vite fait oublier ce désagrément.  
• De plus, cette différence de vitesse a été fortement  
réduite avec le temps.  
• A la fin des années 60, c’était devenu le mode normal  
de fonctionnement d’une machine
## RISC vs CISC
• A la fin des années 60, les instructions  
supportées par l’émulation étaient devenues  
de plus en plus nombreuses et de plus en plus  
complexes.  
• Les designers avaient conçu des instructions  
spécialisées basées sur des microcodes de  
plus en plus complexes.
• Ces instructions complexes devaient  
normalement faciliter la vie des développeurs  
mais dans la pratique, elles n’étaient pas  
toujours utilisées.  
• De plus, plus d’instructions signifie plus de  
ROM pour le microcode, des CPU de plus en  
plus volumineux et de plus en plus d’énergie  
consommée...
• Certaines personnes ont remis cette tendance  
en doute, créant ainsi un nouveau  
mouvement autour du concept de RISC  
(Reduced instruction set computing).  
• L’idée était de se débarrasser de tout ce qui  
était superflu.  
• Le principe est  
– de diminuer le nombre d’instructions,  
– De diminuer la complexité des instructions.
• Le but recherché:  
– Obtenir un instruction set plus léger et plus rapide  
qui peut plus facilement être implémenté dans le  
hardware sans microcode engine.  
• Malgré ce retour vers une exécution directe  
par le hardware, les concepteurs du RISC n’ont  
pas oublié l’énorme avantage lié à l’ISA (la  
compatibilité avec les versions précédentes).  
• Cet avantage et donc l’abstraction vis-à-vis du  
matériel doit absolument être conservé.
## Migrer la complexité du hardware vers le software
• Pour se libérer du microcode tout en gardant les  
bénéfices liés à l’ISA, les machines RISC ont pu  
s’appuyer sur les progrès des compilateurs des  
langages de haut niveau (peu performants  
auparavant).  
• Exemple: le langage C  
• La complexité des instructions a ainsi pu migrer  
du hardware vers des fonctions software plus  
complexes proposées par ces langages.
## CISC
• CISC (Complex Instruction Set Computing) est  
un terme créé à postériori pour distinguer les  
anciennes méthodes des « nouvelles »  
pensées RISC.
# Les composants de ma carte mère
## Les composants sur la carte mère
- Au début de l’informatique : pas de standard
- Succès de l’informatique = besoin de rationalisation de :
	– Fabrication des ordinateurs
	– Des logiciels (cf ISA, et autres architectures)
	– De l’ergonomie (Ctrl-C, Ctrl-V, etc ...)
- Définition d’une architecture (hwd)
- Apparition des premiers PC (« personal computers ») construits par IBM.
- Apparition d’une game de PC compatibles

- Aujourd’hui, c’est pareil
- Il y a des fabricants de CPU
- Il y a des fabricants de cartes diverses
- Et tout doit fonctionner « pareil »

- Aujourd’hui, c’est pareil
- Il y a des fabricants de CPU
- Il y a des fabricants de cartes diverses
- Et tout doit fonctionner « pareil »

- Évolution des performances => évolution de la consommation
- Technologie actuelle : CMOS
- Dissipation = puissance dynamique
- Dépend de la charge capacitive
- P = Ccharge x U2 x f

- Exemple :
- Un CPU plus simple de 15 % (ex : RISC)
- Qui travaille à une tension 15 % + faible
- À une fréquence 15 % + faible (mode eco)
- Alors :
	– Ratio = (0,85) x (0,85)2 x 0,85 = 0,52 = 52%

![[Pasted image 20230414134230.png]]
- NB, un VAX, c’est ça !
![[Pasted image 20230414134253.png]]
●Exemple d’architecture de serveur :
●Sun Fire x4150 1U
●(le livre de référence date un peu)
![[Pasted image 20230414134329.png]]
![[Pasted image 20230414134349.png]]

●Explication des éléments :
●Intel Xeon, ce sont les CPU (2)
●MCH : contrôleur de mémoire
●DIMMs banques de mémoire
	– 2 canaux / CPU
●Slots PCi + controleur RAID
●IOH ESB-2 : chipset sud
●AST2000 : chipset nord

- Sur les cartes mères récentes : plus de chipset, mais un PCH (Platform Controler Hub)
- Le « north chipset » connectait la RAM, le CPU et le port de la carte graphique.
- Le « south bridge » connectait les périphériques « lents » (HDD, USB, PCi slots, …)
- Il y a une connexion rapide entre les 2

- Avec le PCH, une grande part des fonctions du north bridge => dans le CPU
- North bridge éliminé
- Les fonctions du south bridge => PCH

- Pour les cartes mères, il existe plusieurs formes.
Il y a des formes pour les boitiers de PC
- ATX (advance technology extended)
	- Standard
	- 1995
	- 12’’ x 9,6’’
- AT (advance technology)
	- 1990 par IBM
	- 12’’ x 13,8’’
	- abandonné

- Il y a des formes pour les boitiers de PC
	– Micro ATX
		- 9,6’’ x 9,6’’
		- Pour les petits boitiers


- Quid du CMOS et du BIOS
	– BIOS
		- Contient le programme de démarrage du PC
	– CMOS
		- Est une mémoire qui comprend les réglages de la carte mères