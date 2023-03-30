Manip TrueNAS:

Création des datasets (plus d'infos sur  gestion des permissions --> [[Systèmes d'exploitation, labo]] )


TFTP :  
TFTP (pour Trivial File Transfer Protocol ou protocole simplifié de transfert de fichiers)
- Il fonctionne en UDP sur le port 69
- On réserve généralement l'usage du TFTP à un réseau local.
- Les principales simplifications visibles du TFTP par rapport au FTP sont qu'il ne gère pas le listage de fichiers, et ne dispose pas de mécanismes d'authentification, ni de chiffrement. Il faut connaître à l'avance le nom du fichier que l'on veut récupérer. De même, aucune notion de droits de lecture/écriture n'est disponible en standard.
- TFTP est un protocole lent, car il nécessite un paquet ACK (accusé de réception) pour chaque bloc de données qui sont envoyées. Le serveur n'envoie pas le bloc suivant dans la séquence jusqu'à ce que le paquet ACK pour le bloc précédent soit reçu. En conséquence, le cycle complet, sur un réseau lent, peut être extrêmement long.
PXE : (sigle de Pre-boot eXecution Environment)




	Manipulation 3 - Récupération des mots de passe et planification de tâches
	Pour réaliser cette opération, on va devoir entrer une suite de  
	commandes qui ont chacune un sens, et il est important de bien  
	comprendre ce que l'on fait pour ne pas se contenter d'une recette de  
	cuisine :  
	1. mkdir /linux  
	Pourquoi linux ?
	car ce dossier contiendras le linux en question au final
	où va se placer le répertoire en question ?  
	sur la racine
	2. mount /dev/sda1 /linux (parce que c'est comme cela pour ma VM 
	
		Que fait la fonction ntfs-3g ?
	
		Que représentent les paramètres "/dev/sda2" et "/sda2"  ?  
	1. cd /linux  
	2. ls -l
		nous voyons que le dossier linux a été bind sur sda3 ( la partition qui contiens le linux)
	
	chroot /linux
	
	
	
	4. Lister les partitions (nous sommes sous Linux) et repérer la partition contenant  
	Linux
	
	pour trouver le bon numéro de la bonne partition (/dev/sda) suffit de regarder la plus grande partition.(dans la colonne Size il faut voir le plus grand nombre en Giga) dans mon cas /sda2
	
	5. Réglage du système pour accéder à la partition contenant Windows :  
	Pour réaliser cette opération, on va devoir entrer une suite de  
	commandes qui ont chacune un sens, et il est important de bien  
	comprendre ce que l'on fait pour ne pas se contenter d'une recette de  
	cuisine :  
	1. mkdir /sda2
	vous pouvez créer un nouveau répertoire avec n'importe quel nom que vous souhaitez, à condition qu'il n'existe pas déjà dans le système de fichiers.
	Pourquoi sda2 ?
	moi c'est sda4 car j'ai déjà le 1 2 3 occupé !
	où va se placer le répertoire en question ?
	le dossier crée par la commande mkdir se trouvera dans à la racine
	2. ntfs-3g /dev/sda2 /sda2  
	Que fait la fonction ntfs-3g ?
	La fonction "ntfs-3g" est un pilote qui permet de monter et d'accéder aux partitions formatées en NTFS (New Technology File System) sous Linux. NTFS est le système de fichiers utilisé par les versions récentes de Windows, et il n'est pas nativement pris en charge par Linux.
	
	En utilisant la fonction "ntfs-3g", vous pouvez monter une partition NTFS en lecture et en écriture sous Linux. Cela signifie que vous pouvez accéder aux fichiers et aux dossiers de la partition, les modifier et en ajouter de nouveaux. Sans "ntfs-3g", vous ne pourriez accéder à une partition NTFS qu'en lecture seule sous Linux.
	
	La commande "ntfs-3g" est utilisée pour monter une partition NTFS. Les paramètres "/dev/sda2" et "/sda2" dans la commande "ntfs-3g /dev/sda2 /sda2" indiquent que la partition que vous voulez monter se trouve sur le périphérique de stockage "/dev/sda2" et sera montée dans le point de montage "/sda2".
	Que représentent les paramètres "/dev/sda2" et "/sda2"  ?
	/dev/sda2 est la partition où se trouve le windows tandis que /sda2 et le dossier que on a cré à la racine
	3. cd /sda2  
	4. ls -l
	
	6. Repérer le fichier "SAM"  
	on vois que une fois le montage de partition terminé une fois dans le dossier /sda2 que on a crée à la racine tous les fichiers de notre windows sont accesible en lecture et écriture.
	Sur le screenshot nous voyons que nous devons aller dans le dossier /sda2/Windows/System32/config
	7. Entrez, dans le bon répertoire, la commande "chntpw -l SAM"
	Lecture des infos de la console.
	8. Déverrouillage du compte "Administrateur"
	chntpw -u Administrateur SAM
	9. Sélection de l'option "2" pour déverrouiller le compte:
	
	6.2. Utilisation de la commande schtasks  
	1. Listez les options de la commande schtasks.
	schtasks /query /?
	2. Planifiez une tache avec schtasks qui fera une copie des fichiers et répertoires de  
	votre bureau dans « C:\desktop_bkp\ ». Cette copie devra se passer tous les jours à  
	23 h, excepté le WE.
	
	schtasks /CREATE /TN "Mon test" /SC WEEKLY /D MON,TUF,WED,THU,FRI /ST 23:00 /TR "xcopy /E /Y /R c:\Users\ludo\desktop c:\desktop_bkp"
	
	Cela créera une tâche planifiée nommée "Mon test" qui sera exécutée toutes les semaines les lundis, mardis, mercredis, jeudis et vendredis à 23 heures. La commande xcopy sera alors exécutée pour copier tous les fichiers et les sous-dossiers du dossier "c:\Users\ludo\desktop" vers le dossier "c:\desktop_bkp", en incluant les fichiers vides, les fichiers cachés et en écrasant les fichiers existants sans demander de confirmation.
	
	3. Vérifiez que la tâche est bien présente dans la liste schtasks.
	schtasks /QUERY | findstr "Mon test"
	
	6.3. Exécution d'un script
	(oublié pas faire le backup avant)
	
	
	@echo -----------------------------------------
	@echo ------- Ceci est mon script de backup
	@echo -----------------------------------------
	@echo .
	xcopy /E /Y /R c:\Users\ludo\Desktop c:\Users\ludo\desktop_bkp
	@echo .
	@echo -----------------------------------------
	@echo -------- Backup Termine
	@echo -----------------------------------------
	@echo .
	@timeout 15
	
	schtasks /CREATE /TN "Mon test" /SC WEEKLY /D MON,TUE,WED,THU,FRI /ST 23:00 /TR c:\Users\ludo\script.bat
	
	6. Atelier Linux  
	6.1. Utilisation des commandes « at » et « batch »
	
	c. Utiliser ces commandes pour planifier l’arrêt de votre machine demain à 22h30
	at 22:30
	
	at 22:30
	shutdown -h now
	<EOT>
	ctrl+d
	
	
	d. Programmez la même commande « shutdown », cette fois en utilisant un script  
	qui sera exécuté par « at ». Utilisez « nano » pour créer le script.
	echo "shutdown -h now" > script.bat
	
	f. Annuler la tâche planifiée.
	at -r <numéro de la commande>
	
	6.2. Utilisation de la commande « crontab »
	*/10       *   *     *     *  shutdown -r now



# Manip live cd
## Extraction du LiveCD
![[Pasted image 20230330114430.png]]
dans mon cas:
mkdir /home/ludo/livecdtmp
solution récup iso:
dd if=/dev/cdrom of=/home/ludo/livecdtmp/mint.iso
!!! une erreur peut être produit si dans les cdrom connecté à la VM il n'y a pas que le iso mint.

![[Pasted image 20230330115251.png]]
dans mon cas:
mkdir mnt dans livecdtmp
mount -o loop mint.iso mnt

![[Pasted image 20230330115510.png]]
dans mon cas:
mkdir extract-cd
sudo rsync --exclude=/casper/filesystem.squashfs -a mnt/ extract-cd

![[Pasted image 20230330115900.png]]
dans mon cas:
unsquashfs mnt/casper/filesystem.squashfs
mv squashfs-root edit

![[Pasted image 20230330124545.png]]
dans mon cas:
sudo cp /etc/resolv.conf edit/etc/
sudo cp /etc/hosts edit/etc/

sudo mount --bind /dev/ edit/dev
sudo chroot edit
mount -t proc none /proc
mount -t sysfs none /sys
mount -t devpts none /dev/pts

![[Pasted image 20230330125104.png]]
dans mon cas:
export HOME=/root
export LC_ALL=C

## INSTALLATION DE LOGICIELS
dans mon cas:
add-apt-repository ppa:wireshark-dev/stable
apt install wireshark
apt install language-pack-fr
apt install ubiquity-frontend-gtk
dpkg-reconfigure keyboard-configuration
dpkg-reconfigure tzdata

apt clean

![[Pasted image 20230330130525.png]]
dans mon cas:
umount /proc || umount -lf /proc  
umount /sys  
umount /dev/pts
exit  
sudo umount edit/dev

![[Pasted image 20230330130734.png]]
dans mon cas:
!!! attention à l'endroit du dossier que vous vous trouvez quand vous tapez une commande
sudo chmod +w extract-cd/casper/filesystem.manifest
chroot edit dpkg-query -W --showformat='${Package} ${Version}\n' > extract-cd/casper/filesystem.manifest
exit
sudo cp extract-cd/casper/filesystem.manifest extract-cd/casper/filesystem.manifest-desktop
sudo sed -i '/ubiquity/d' extract-cd/casper/filesystem.manifest-desktop  
sudo sed -i '/casper/d' extract-cd/casper/filesystem.manifest-desktop

![[Pasted image 20230330132355.png]]
dans mon cas:
cd extract-cd  
sudo rm MD5SUMS
find -type f -print0 | sudo xargs -0 md5sum | grep -v isolinux/boot.cat | sudo tee MD5SUMS

![[Pasted image 20230330132726.png]]
dans mon cas:
sudo mksquashfs edit extract-cd/casper/filesystem.squashfs -comp xz
printf $(du -sx --block-size=1 edit | cut -f1) > extract-cd/casper/filesystem.size
exit
cd /home/ludo/livecdtmp
sudo nano extract-cd/README.diskdefines
(changer le nom dans la variable DISKNAME)

![[Pasted image 20230330133835.png]]
dans mon cas:
cd extract-cd
sudo mkisofs -D -r -V "$IMAGE_NAME" -cache-inodes -J -l -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -o ../mint-custom.iso .

![[Pasted image 20230330134230.png]]
dans mon cas:

j'ai upload l'iso sur onedrive depuis la vm

## Réponse aux questions
Question I: Les deux logiciels sont squashfs-tools et genisoimage. Squashfs-tools est un outil qui permet de créer et manipuler des systèmes de fichiers compressés en lecture seule, appelés squashfs. Genisoimage est un outil qui permet de créer une image ISO à partir d'un système de fichiers. Pour les installer, vous pouvez utiliser la commande suivante dans un terminal :

`sudo apt-get install squashfs-tools genisoimage`

Question II: L'option -o loop de la commande permet de monter le fichier ISO comme un périphérique de boucle. Cela permet de monter le fichier ISO comme s'il était un lecteur de CD ou de DVD. Cette option est nécessaire pour pouvoir monter des images ISO sous Linux.

Question III: L'outil rsync est utilisé pour synchroniser des fichiers entre deux répertoires. L'option -a englobe plusieurs autres options, notamment -r (pour copier des répertoires récursivement), -l (pour copier des liens symboliques en tant que liens symboliques), -p (pour préserver les permissions des fichiers) et -t (pour préserver les horodatages des fichiers).

Question IV: La commande chroot permet de changer la racine du système de fichiers en utilisant un autre répertoire comme racine. Dans ce contexte, elle est utilisée pour changer la racine du système de fichiers de la machine virtuelle vers le répertoire /extract-cd, qui contient les fichiers extraits de l'image ISO.

Question V: L'option --bind de la commande mount permet de monter un répertoire à un emplacement spécifique sans remplacer le répertoire existant à cet emplacement. Cette option est utilisée pour monter les répertoires /dev, /sys et /proc du système hôte dans le système de fichiers de la machine virtuelle. L'option -t indique le type de système de fichiers utilisé pour le montage. Dans ce cas, il s'agit de systèmes de fichiers spéciaux utilisés par Linux pour fournir des informations sur les périphériques, les processus et le système.