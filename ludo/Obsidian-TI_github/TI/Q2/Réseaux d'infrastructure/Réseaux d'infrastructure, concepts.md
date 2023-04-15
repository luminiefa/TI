
![[reseaux_230306_164028.pdf]]

![[infra réseaux_230313_204333.pdf]]


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
![[Pasted image 20230316201727.png]]
• Qui établi et met à jour les standards pour la couche Physique ?
![[Pasted image 20230316202202.png]]
• Les signaux sur la couche Physique
![[Pasted image 20230316202221.png]]
## Signalisation
![[Pasted image 20230316202244.png]]
## Début de trame – Fin de trame
![[Pasted image 20230316202311.png]]
## NRZ
![[Pasted image 20230316202332.png]]
## Manchester
![[Pasted image 20230316202351.png]]
## Encodage
![[Pasted image 20230316202407.png]]
## 4B/5B
![[Pasted image 20230316202424.png]]
## Signalisation et encodage
• Définition en terme de bande passante, débit et données utilisables
![[Pasted image 20230316202452.png]]
## Caractéristiques et utilisation d’un média réseau
• Média Ethernet
![[Pasted image 20230316202523.png]]
• Sans fil
![[Pasted image 20230316202543.png]]
• Caractéristiques d’un câble UTP
![[Pasted image 20230316202616.png]]
• Sources d’interférences
![[Pasted image 20230316202634.png]]
• Câble STP et coaxial
![[Pasted image 20230316202651.png]]
• Caractéristiques de cablâge fibre optique
![[Pasted image 20230316202708.png]]
• Sans fil
![[Pasted image 20230316202726.png]]
# IpV6
## Encapsulating IPv6
![[Pasted image 20230414153154.png]]
## IPv6 Packet Header
![[Pasted image 20230414153213.png]]
## Sample IPv6 Header
![[Pasted image 20230414153227.png]]
## The Need for IPv6
- IPv6 is designed to be the successor to IPv4.
- Depletion of IPv4 address space has been the motivating factor for
moving to IPv6.
- Projections show that all five RIRs will run out of IPv4 addresses
between 2015 and 2020.
- With an increasing Internet population, a limited IPv4 address space,
issues with NAT and an Internet of things, the time has come to begin
the transition to IPv6!
- IPv4 has a theoretical maximum of 4.3 billion addresses, plus private
addresses in combination with NAT.
- IPv6 larger 128-bit address space provides for 340 undecillion
addresses.
- IPv6 fixes the limitations of IPv4 and includes additional
enhancements, such as ICMPv6.
## IPv4 and IPv6 Coexistence
### Dual-stack
The migration techniques can be divided into three categories:
Dual-stack, Tunnelling, and Translation.
![[Pasted image 20230414154458.png]]
Dual-stack: Allows IPv4 and IPv6 to coexist on the same network.
Devices run both IPv4 and IPv6 protocol stacks simultaneously. It's
the best solution !
### Tunnelling
![[Pasted image 20230414154516.png]]
Tunnelling: A method of transporting an IPv6 packet over an IPv4
network. The IPv6 packet is encapsulated inside an IPv4 packet.
Usefull to interconnect IPv6 network trough an only IPv4 network
### Translation
![[Pasted image 20230414154552.png]]
Translation: The Network Address Translation 64 (NAT64) allows
IPv6-enabled devices to communicate with IPv4-enabled devices
using a translation technique similar to NAT for IPv4. An IPv6 packet
is translated to an IPv4 packet, and vice versa.
## Hexadecimal Number System
- Hexadecimal is a base
sixteen system.
- Base 16 numbering
system uses the
numbers 0 to 9 and the
letters A to F.
- Four bits (half of a byte)
can be represented with
a single hexadecimal
value.
![[Pasted image 20230414154647.png]]
Look at the binary bit
patterns that match the
decimal and hexadecimal
values
![[Pasted image 20230414154724.png]]
## IPv6 Address Representation
- 128 bits in length and written as a string of hexadecimal values
- In IPv6, 4 bits represents a single hexadecimal digit, 32 hexadecimal value = IPv6 address
2001:0DB8:0000:1111:0000:0000:0000:0200
FE80:0000:0000:0000:0123:4567:89AB:CDEF
- Hextet used to refer to a segment of 16 bits or four hexadecimals
- Can be written in either lowercase or uppercase
![[Pasted image 20230414154858.png]]
## Rule 1- Omitting Leading 0s
- The first rule to help reduce the notation of IPv6 addresses is any
leading 0s (zeros) in any 16-bit section or hextet can be omitted.
- 01AB can be represented as 1AB.
- 09F0 can be represented as 9F0.
- 0A00 can be represented as A00.
- 00AB can be represented as AB.
![[Pasted image 20230414155852.png]]
## Rule 2 - Omitting All 0 Segments
- A double colon (::) can replace any single, contiguous string of one or more 16-bit segments (hextets) consisting of all 0’s.
- Double colon (::) can only be used once within an address otherwise the address will be ambiguous.
- Known as the compressed format.
- Incorrect address - 2001:0DB8::ABCD::1234.
![[Pasted image 20230414160008.png]]
Training
Convert to hex
1010001111100110 ->
0011000011110100 ->
Find the full adress
2001::10:20AE:1021:AC45 ->
FE80::1                                 -> 
Find the compressed format
0000:0000:0000:0000:0000:0000:0000:0001 ->
## IPv6 Prefix Length
- IPv6 does not use the dotted-decimal subnet mask notation
- Prefix length indicates the network portion of an IPv6 address using the following format:
	–IPv6 address/prefix length
	–Prefix length can range from 0 to 128
	–Typical prefix length is /64
![[Pasted image 20230414160243.png]]
## IPv6 Address Types
There are three types of IPv6 addresses:
- Unicast
- Multicast
- Anycast.
Note: IPv6 does not have broadcast addresses.
## IPv6 Unicast Addresses
–Uniquely
identifies an
interface on an
IPv6-enabled
device.
–A packet sent
to a unicast
address is
received by
the interface
that is
assigned that
address.
![[Pasted image 20230414160422.png]]
![[Pasted image 20230414160752.png]]
Global Unicast
	–Similar to a public IPv4 address
	–Globally unique
	–Internet routable addresses
	–Can be configured statically or assigned dynamically
	–Prefix: 2000::/3
Link-local
	–Used to communicate with other devices on the same local link
	–Confined to a single link; not routable beyond the link
	–FE80::/10
Loopback
	–Used by a host to send a packet to itself and cannot be
	assigned to a physical interface.
	–Ping an IPv6 loopback address to test the configuration of
	TCP/IP on the local host.
	–All-0s except for the last bit, represented as ::1/128 or just ::1.
Unspecified Address
	–All-0’s address represented as ::/128 or just ::
	–Cannot be assigned to an interface and is only used as a
	source address.
	–An unspecified address is used as a source address when the
	device does not yet have a permanent IPv6 address or when
	the source of the packet is irrelevant to the destination.
Unique Local
	–Similar to private addresses for IPv4.
	–Used for local addressing within a site or between a limited number of sites.
	–In the range of FC00::/7 to FDFF::/7.
IPv4 Embedded (not covered in this course)
	–Used to help transition from IPv4 to IPv6.
## IPv6 Link-Local Unicast Addresses
- Every IPv6-enabled network interface is REQUIRED to have a link-
local address
- Enables a device to communicate with other IPv6-enabled devices
on the same link and only on that link (subnet)
- FE80::/10 range, first 10 bits are 1111 1110 10xx xxxx
- 1111 1110 1000 0000 (FE80) - 1111 1110 1011 1111 (FEBF)
![[Pasted image 20230414161206.png]]
Packets with a source or destination link-local address cannot be routed beyond the link from where the packet originated.
![[Pasted image 20230414161246.png]]
## Structure of an IPv6 Global Unicast Address
- IPv6 global unicast addresses are globally unique and routable on the IPv6 Internet
- Equivalent to public IPv4 addresses
- ICANN allocates IPv6 address blocks to the five RIRs
Currently, only global unicast addresses with the first three bits of 001 or 2000::/3 are being assigned
![[Pasted image 20230414161340.png]]
A global unicast address has three parts: Global Routing Prefix, Subnet ID, and Interface ID.
- Global Routing Prefix is the prefix or network portion of the address assigned by the provider, such as an ISP, to a customer or site, currently, RIR’s assign a /48 global routing prefix to customers.
- 2001:0DB8:ACAD::/48 has a prefix that indicates that the first 48 bits (2001:0DB8:ACAD) is the prefix or network portion.
![[Pasted image 20230414161435.png]]
- Subnet ID is used by an organization to identify subnets within its site
- Interface ID
	–Equivalent to the host portion of an IPv4 address.
	–Used because a single host may have multiple interfaces, each
	having one or more IPv6 addresses.
![[Pasted image 20230414161523.png]]
## Static Configuration of a Global Unicast Address
![[Pasted image 20230414161537.png]]
Windows IPv6 Setup
![[Pasted image 20230414161721.png]]
CLI :
ip -6 addr add 2002:c000:203::1/64 dev eth0
Linux IPv6 Setup
	/etc/network/interfaces :
	iface eth0 inet6 static
	address 2607:f0d0:2001:000a:0000:0000:0000:0002
	netmask 64
	gateway 2607:f0d0:2001:000a:0000:0000:0000:0001
## Dynamic Configuration of a Global Unicast Address using SLAAC
Stateless Address Autoconfiguraton (SLAAC)
- A method that allows a device to obtain its prefix, prefix length and
default gateway from an IPv6 router
- No DHCPv6 server needed
- Rely on ICMPv6 Router Advertisement (RA) messages
IPv6 routers
- Forwards IPv6 packets between networks
- Can be configured with static routes or a dynamic IPv6 routing protocol
- Sends ICMPv6 RA messages
- The IPv6 unicast-routing command enables IPv6 routing.
- RA message can contain one of the following three options:
	 - SLAAC Only – Uses the information contained in the RA message.
	- SLAAC and DHCPv6 – Uses the information contained in the RA message and get other information from the DHCPv6 server, stateless DHCPv6 (for example, DNS).
	- DHCPv6 only – The device should not use the information in the RA, stateful DHCPv6.
- Routers send ICMPv6 RA messages using the link-local address as the source IPv6 address
![[Pasted image 20230414162143.png]]
## Dynamic Configuration of a Global Unicast Address using DHCPv6 (cont.)
Dynamic Host Configuration Protocol for IPv6 (DHCPv6)
- Similar to IPv4
- Automatically receives addressing information, including a global unicast address, prefix length, default gateway address and the addresses of DNS servers using the services of a DHCPv6 server.
- Device may receive all or some of its IPv6 addressing information from a DHCPv6 server depending upon whether option 2 (SLAAC and DHCPv6) or option 3 (DHCPv6 only) is specified in the ICMPv6 RA message.
- Host may choose to ignore whatever is in the router’s RA message and obtain its IPv6 address and other information directly from a DHCPv6 server.
![[Pasted image 20230414162249.png]]
## EUI-64 Process or Randomly Generated
EUI-64 Process
	- Uses a client’s 48-bit Ethernet MAC address and inserts another 16 bits in the middle of the 46-bit MAC address to create a 64-bit Interface ID.
	- Advantage is that the Ethernet MAC address can be used to determine the interface; is easily tracked.
	- Default on most hosts !
EUI-64 Interface ID is represented in binary and comprises three parts:
	- 24-bit OUI from the client MAC address, but the 7th bit (the Universally/Locally bit) is reversed (0 becomes a 1).
	- Inserted as a 16-bit value FFFE.
	- 24-bit device identifier from the client MAC address.
![[Pasted image 20230414162425.png]]
![[Pasted image 20230414162441.png]]
Randomly Generated Interface IDs
- Depending upon the operating system, a device can use a randomly generated Interface ID instead of using the MAC address and the EUI-64 process.
- Beginning with Windows Vista, Windows uses a randomly generated Interface ID instead of one created with EUI-64.
- Windows XP (and previous Windows operating systems) used EUI-64.
- Usefull to protect private life.
## Dynamic Link-local Addresses
Link-Local Address
	- After a global unicast address is assigned to an interface, an IPv6-enabled device automatically generates its link-local address.
	- Must have a link-local address that enables a device to communicate with other IPv6-enabled devices on the same subnet.
	- Uses the link-local address of the local router for its default gateway IPv6 address.
	- Routers exchange dynamic routing protocol messages using link-local addresses.
	- Routers’ routing tables use the link-local address to identify the next-hop router when forwarding IPv6 packets.
Dynamically Assigned
The link-local address is dynamically created using the FE80::/10 prefix and the Interface ID.
![[Pasted image 20230414162725.png]]
## Static Link-local Addresses
![[Pasted image 20230414162749.png]]
![[Pasted image 20230414162815.png]]
## Exercise
Calculate the local link address (l’adresse lien-local) for MAC adress : 00-11-5B-69-C1-D4.
![[Pasted image 20230414162849.png]]
What is your host Loopback adress ?
::1
![[Pasted image 20230414162912.png]]
## Verifying IPv6 Address Configuration
Each interface has two IPv6 addresses -
1. global unicast address that was configured
2. one that begins with FE80 is automatically added as a link-local unicast address
![[Pasted image 20230414163012.png]]
![[Pasted image 20230414163033.png]]
## Assigned IPv6 Multicast Addresses
Two common IPv6 assigned multicast groups include:
-FF02::1 All-nodes multicast group –
	- All IPv6-enabled devices join
	- Same effect as an IPv4 broadcast address
-FF02::2 All-routers multicast group
	- All IPv6 routers join
	- A router becomes a member of this group when it is enabled as an IPv6 router with the ipv6 unicast-routing global configuration mode command.
	- A packet sent to this group is received and processed by all IPv6 routers on the link or network.
![[Pasted image 20230414163213.png]]
## Solicited Node IPv6 Multicast Addresses
- Similar to the all-nodes multicast address, matches only the last 24 bits of the IPv6 global unicast address of a device
- Automatically created when the global unicast or link-local unicast addresses are assigned
- Created by combining a special FF02:0:0:0:0:0:FF00::/104 prefix with the right-most 24 bits of its unicast address
![[Pasted image 20230414163335.png]]
The solicited node multicast address consists of two parts:
- FF02:0:0:0:0:0:FF00::/104 multicast prefix – First 104 bits of the all solicited node multicast address
- Least significant 24-bits – Copied from the right-most 24 bits of the global unicast or link-local unicast address of the device
![[Pasted image 20230414163444.png]]
## ICMPv4 and ICMPv6 Messages
- ICMP messages common to both ICMPv4 and ICMPv6 include:
	–Host confirmation
	–Destination or Service Unreachable
	–Time exceeded
	–Route redirection
- Although IP is not a reliable protocol, the TCP/IP suite does provide for messages to be sent in the event of certain errors, sent using the services of ICMP.
## ICMPv6 Router Solicitation and Router Advertisement Messages
- ICMPv6 includes four new protocols as part of the Neighbor Discovery Protocol (ND or NDP):
	–Router Solicitation message
	–Router Advertisement message
	–Neighbor Solicitation message
	–Neighbor Advertisement message
- Router Solicitation and Router Advertisement Message – Sent between hosts and routers.
- Router Solicitation (RS) message – RS messages are sent as an IPv6 all-routers multicast message.
- Router Advertisement (RA) message – RA messages are sent by routers to provide addressing information.
![[Pasted image 20230414163643.png]]
## ICMPv6 Neighbor Solicitation and Neighbor Advertisement Messages
- Two additional message types:
	- Neighbor Solicitation (NS)
	- Neighbor Advertisement (NA) messages
- Used for address resolution is used when a device on the
	LAN knows the IPv6 unicast address of a destination, but does
	not know its Ethernet MAC address.
- Also used for Duplicate Address Detection (DAD)
	- Performed on the address to ensure that it is unique.
	- The device sends an NS message with its own IPv6
	address as the targeted IPv6 address.
![[Pasted image 20230414163834.png]]
## Summary (cont.)
- IPv4 hosts can communicate one of three different ways: unicast, broadcast, and multicast.
- The private IPv4 address blocks are: 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16.
- The depletion of IPv4 address space is the motivating factor for moving to IPv6.
- Each IPv6 address has 128 bits verses the 32 bits in an IPv4 address.
- The prefix length is used to indicate the network portion of an IPv6 address using the following format: IPv6 address/prefix length.
- There are three types of IPv6 addresses: unicast, multicast, and anycast.
- An IPv6 link-local address enables a device to communicate with other IPv6-enabled devices on the same link and only on that link (subnet).
- Packets with a source or destination link-local address cannot be routed beyond the link from where the packet originated.
- IPv6 link-local addresses are in the FE80::/10 range.
- ICMP is available for both IPv4 and IPv6.
## Subnetting Using the Subnet ID
An IPv6 Network Space is subnetted to support hierarchical, logical
design of the network
![[Pasted image 20230414164026.png]]
## IPV6 Subnet Allocation
![[Pasted image 20230414164042.png]]
## Subnetting into the Interface ID
IPv6 bits can be borrowed from the interface ID to create additional
IPv6 subnets.
![[Pasted image 20230414164110.png]]


