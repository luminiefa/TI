
![[reseaux_230306_164028.pdf]]

# Couche network partie 2
## Adresses particulières
• 2 adresses non affectables à une machine  
• Host-Id composé uniquement de 0 = l’adresse  
du réseau (ou du sous réseau lui-même)  
• Host-Id composé uniquement de 1 = l’adresse  
de broadcast (de diffusion)
## Exercices
• Exercice 1  
• Pour les adresses IP suivantes,  
–Identifiez leur classe  
–Identifiez leur masque de réseau (SM) initial (par  
défaut)  
–Déterminez si l’adresse IP est une adresse publique ou  
un adresse privée  
• 198.54.32.5,  
• 9.54.21.38,  
• 192.168.54.28,  
• 23.25.68.2,  
• 110.0.0.0.

• Exercice 2  
• Pour les adresses de l’exercice précédent,  
donnez l’adresse du réseau obtenu en  
appliquant le masque par défaut.

• Exercice 3  
• A partir des adresses suivantes et du nombre  
voulu de sous-réseaux, calculez le masque et  
le nombre d’hôtes par sous-réseau.  
1. 148.25.0.0 et 37 sous-réseaux,  
2. 198.63.24.0 et 2 sous-réseaux,  
3. 110.0.0.0 et 1000 sous-réseaux,  
4. 209.206.202.0 et 60 sous-réseaux.

• Exercice 4  
• Dans cet exercice, le nombre maximal  
d’hôtes par sous-réseau est donné.  
Calculez le masque de sous-réseau et le  
nombre de sous-réseaux possibles.  
1. Réseau 63.0.0.0 et un maximum de 100 hôtes par  
sous-réseau,  
2. Réseau 198.53.25.0 et un maximum de 100 hôtes par  
sous-réseau,  
3. Réseau 154.25.0.0 et un maximum de 1500 hôtes par  
sous-réseau,  
4. Réseau 121.0.0.0 et un maximum de 2000 hôtes par  
sous-réseau,  
5. Réseau 223.21.25.0 et un maximum de 14 hôtes par  
sous-réseau
## Unicast – Broadcast - Multicast
![[Pasted image 20230316193847.png]]
## Adresses publiques et privées
![[Pasted image 20230316193922.png]]
## Planification – “classic” → VLSM
• Allouer les plus grands blocs en premier
![[Pasted image 20230316193946.png]]
# Couche liaison de données
• La couche Liaison de données prépare la communication pour la  
transmission sur un média spécifique = gérer l’accès au média
• Gérer l’accès au media = s’adapater au support
![[Pasted image 20230316194844.png]]
• Gérer l’accès au media = mettre en oeuvre des stratégies d’accès au  
média
![[Pasted image 20230316194909.png]]
1. Une machine gère le droit de parole sur le réseau → environnement maître-esclaves.  
2. Les machines ont la parole chacune à leur tour → passage du jeton.  
3. Les machines accèdent au réseau quand elles veulent. Lorsque des collisions se produisent, les  
machines doivent réémettre.
• Gérer l accès au media = mise en oeuvre d un connecteurConnexion  
au media
![[Pasted image 20230316195017.png]]
• Celà se traduit par différents standards
![[Pasted image 20230316195135.png]]
## Un exemple concret:  ETHERNET
Petit historique // Topologies physiques et logiques
![[Pasted image 20230316195244.png]]
• Emergence des switchs dans le LAN
![[Pasted image 20230316195309.png]]
## Caractéristiques d’un média utilisé par Ethernet
• Ethernet au-delà du LAN
![[Pasted image 20230316195400.png]]
## Ethernet VS Modèle OSI
![[Pasted image 20230316195507.png]]
## Trame Ethernet
![[Pasted image 20230316195531.png]]
## Format des adresses MAC
![[Pasted image 20230316195602.png]]
## Construction de la table de commutation
![[Pasted image 20230316195622.png]]
![[Pasted image 20230316195636.png]]
![[Pasted image 20230316195648.png]]
![[Pasted image 20230316195701.png]]
![[Pasted image 20230316195717.png]]
![[Pasted image 20230316195728.png]]
![[Pasted image 20230316195742.png]]
![[Pasted image 20230316195753.png]]
## Ethernet: types de communications possibles
• UNICAST: un à un  
• MULTICAST: un à plusieurs  
• BROADCAST: un à tous
## Domaine de broadcast
![[Pasted image 20230316195843.png]]
Et si une (ou plusieurs) autre  
technologie existait ?  
Dans ce cas, comment connecter des  
technologies différentes ?
# Couche physique
# IpV6