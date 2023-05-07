1.  Préparation matérielle et logicielle :

-   Insérez la clé USB contenant Kali Linux dans le PC.
-   Redémarrez le PC et accédez au menu de démarrage pour sélectionner le mode "live CD" de Kali Linux.
-   Fixez l'antenne sur le HackRF One à l'endroit prévu.
-   Une fois Kali Linux démarré, connectez le HackRF One au PC via le câble USB.

2.  Recherche de la fréquence d'émission :

-   Ouvrez un terminal et tapez `gqrx` pour lancer le programme.
-   Configurez les paramètres d'acquisition selon les instructions fournies si une boîte de dialogue apparaît. Sinon, accédez à Files → Configure I/O devices.
-   Réglez la fréquence centrale d'acquisition sur 93 MHz.
-   Cliquez sur le bouton "Play" pour démarrer l'acquisition et observez les changements de densité spectrale sur le graphique pour identifier les fréquences de transmission des programmes radio FM.

3.  Ecoute d'une chaîne radio FM :

-   Arrêtez l'acquisition en cliquant sur le bouton "Stop".
-   Modifiez la fréquence vers celle d'une des stations radio identifiées précédemment.
-   Choisissez le mode de modulation WFM (mono) à la place de WFM (stéréo) pour un meilleur son.
-   Augmentez le gain Audio (en bas à droite) pour permettre d'entendre la station radio.
-   Essayez d'écouter d'autres stations radio en modifiant la fréquence.

4.  Réception des données RDS (dans Gqrx) :

-   Activez la réception des messages RDS dans Gnuradio en suivant les images fournies dans la manipulation.
-   Testez la réception des messages RDS sur plusieurs stations radio pour vous assurer qu'elle fonctionne correctement.

5.  Envoyer une musique sur une station FM :

-   Copiez un fichier MP3 sur Kali Linux et convertissez-le en WAV à l'aide d'Audacity.
-   Ouvrez un terminal et tapez `gnuradio-companion` pour lancer le programme.
-   Configurez gnuradio en suivant le schéma et les instructions fournies dans la manipulation. Assurez-vous d'utiliser les bonnes valeurs pour chaque composant.
-   Réglez la radio sur la 108FM, modifiez la valeur de la variable freq de votre projet pour qu'elle corresponde à la fréquence d'émission (108 MHz).
-   Modifiez le composant Wav File Source pour sélectionner votre fichier WAV.
-   Démarrez le projet en cliquant sur le bouton "Play". La radio devrait recevoir votre musique.
-   Essayez d'envoyer un son personnalisé sur une station radio que vous avez identifiée précédemment.

6.  Rédaction du rapport :

-   Répondez aux questions posées dans la partie réception et émission.
-   Utilisez le canevas habituel pour la constitution d'un rapport, en incluant une introduction, un développement, une conclusion et des références si nécessaire.
-   N'hésitez pas à ajouter d'autres découvertes ou observations que vous auriez pu faire lors de la manipulation.

En suivant ces étapes détaillées, vous devriez être