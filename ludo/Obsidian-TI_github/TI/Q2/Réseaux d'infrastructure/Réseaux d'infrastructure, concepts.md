# reseaux_230306_164028
![image](https://user-images.githubusercontent.com/19058019/236684410-980bd10a-fdc7-444a-9119-f6d23fad4157.png)


# infra réseaux_230313_204333
![image](https://user-images.githubusercontent.com/19058019/236684446-fbfb3387-34ab-4a89-8f30-e8abbfe9b069.png)
![image](https://user-images.githubusercontent.com/19058019/236684461-8a106a9a-6282-4e44-84c4-2e5bb31be669.png)

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
![image](https://user-images.githubusercontent.com/19058019/236684477-f34c5bcd-db32-488c-b967-b7678526e2dc.png)
## Adresses publiques et privées
![image](https://user-images.githubusercontent.com/19058019/236684490-7dae0826-0aa5-4cbf-8809-174c5f3fb8fc.png)
## Planification – “classic” → VLSM
• Allouer les plus grands blocs en premier
![image](https://user-images.githubusercontent.com/19058019/236684499-15dfc6e9-795b-47c9-be2a-424d7c1e23f0.png)
# Couche liaison de données
• La couche Liaison de données prépare la communication pour la  
transmission sur un média spécifique = gérer l’accès au média
• Gérer l’accès au media = s’adapater au support
![image](https://user-images.githubusercontent.com/19058019/236684513-e885bb2e-3f5b-421d-8d9b-7dfc8ca313ce.png)
• Gérer l’accès au media = mettre en oeuvre des stratégies d’accès au  
média
![image](https://user-images.githubusercontent.com/19058019/236684530-5c4a4ff5-1018-41ba-839f-881920e3b837.png)
1. Une machine gère le droit de parole sur le réseau → environnement maître-esclaves.  
2. Les machines ont la parole chacune à leur tour → passage du jeton.  
3. Les machines accèdent au réseau quand elles veulent. Lorsque des collisions se produisent, les  
machines doivent réémettre.
• Gérer l accès au media = mise en oeuvre d un connecteurConnexion  
au media
![image](https://user-images.githubusercontent.com/19058019/236684540-650c544c-76ab-4ec9-bd27-e564c51ab0a5.png)
• Celà se traduit par différents standards
![image](https://user-images.githubusercontent.com/19058019/236684553-79975b03-25d2-4c45-9987-662869fb6718.png)
## Un exemple concret:  ETHERNET
Petit historique // Topologies physiques et logiques
![image](https://user-images.githubusercontent.com/19058019/236684563-49fe5aa8-80aa-4a3f-9126-940c8486202d.png)
• Emergence des switchs dans le LAN
![image](https://user-images.githubusercontent.com/19058019/236684575-743a1504-b899-453a-968e-b5a65c4f70e4.png)
## Caractéristiques d’un média utilisé par Ethernet
• Ethernet au-delà du LAN
![image](https://user-images.githubusercontent.com/19058019/236684584-b148de3d-187b-47be-a8e9-39c258360de2.png)
## Ethernet VS Modèle OSI
![image](https://user-images.githubusercontent.com/19058019/236684598-73f3044c-9b94-4330-991e-784f96338a3c.png)
## Trame Ethernet
![image](https://user-images.githubusercontent.com/19058019/236684613-bdb35486-7cb7-4fda-ad3d-ac9606e83f93.png)
## Format des adresses MAC
![image](https://user-images.githubusercontent.com/19058019/236684624-7a255d19-36fe-47b4-9c9f-5bdcdccb5c7c.png)
## Construction de la table de commutation
![image](https://user-images.githubusercontent.com/19058019/236684631-4558c2f7-1d43-4b21-88c7-6af92544c665.png)
![image](https://user-images.githubusercontent.com/19058019/236684650-00cd3759-33cb-4797-9b27-0c25c2415a05.png)
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
![image](https://user-images.githubusercontent.com/19058019/236690870-8ffd80b2-4178-4faf-aede-009c82f6eb8a.png)
Et si une (ou plusieurs) autre  
technologie existait ?  
Dans ce cas, comment connecter des  
technologies différentes ?
# Couche physique
![image](https://user-images.githubusercontent.com/19058019/236690880-7fff8e97-f235-4702-bdfd-2cbc8d500b0d.png)
• Qui établi et met à jour les standards pour la couche Physique ?
![image](https://user-images.githubusercontent.com/19058019/236690888-2f2ae6de-56e3-47a2-9a38-439e3125988c.png)
• Les signaux sur la couche Physique
![image](https://user-images.githubusercontent.com/19058019/236690897-0f0096b0-f467-479d-ac18-ae8c6b66a7fa.png)
## Signalisation
![image](https://user-images.githubusercontent.com/19058019/236690906-185b3355-c298-4866-a517-d0477f65443c.png)
## Début de trame – Fin de trame
![image](https://user-images.githubusercontent.com/19058019/236690912-222a8624-ec57-471e-99ef-7fdf9d3212e5.png)
## NRZ
![image](https://user-images.githubusercontent.com/19058019/236690918-9be1ea96-8f7f-429d-aa81-9616fb14d107.png)
## Manchester
![image](https://user-images.githubusercontent.com/19058019/236690929-b8a9c896-271e-42d4-a62c-e2bdbf0ff7da.png)
## Encodage
![image](https://user-images.githubusercontent.com/19058019/236690942-81c26277-9af3-4e42-99bb-8809963b8359.png)
## 4B/5B
![image](https://user-images.githubusercontent.com/19058019/236690953-4262ba61-7078-4b8d-b1c5-5511400a3ee6.png)
## Signalisation et encodage
• Définition en terme de bande passante, débit et données utilisables
![image](https://user-images.githubusercontent.com/19058019/236690961-731e64f8-f49d-45f4-a232-86ad2075ddb3.png)
## Caractéristiques et utilisation d’un média réseau
• Média Ethernet
![image](https://user-images.githubusercontent.com/19058019/236690976-a473e094-a794-49e2-8192-5340a4695d85.png)
• Sans fil
![image](https://user-images.githubusercontent.com/19058019/236690984-a744f36f-e0d0-4454-9cf8-2655b3f0393f.png)
• Caractéristiques d’un câble UTP
![image](https://user-images.githubusercontent.com/19058019/236690992-04632224-32a6-4c3f-9df5-af123d01fd08.png)
• Sources d’interférences
![image](https://user-images.githubusercontent.com/19058019/236690998-765d2903-2c7c-463d-829a-3b5337b14e52.png)
• Câble STP et coaxial
![image](https://user-images.githubusercontent.com/19058019/236691003-2d1b4cce-56e9-4d9b-a7ec-1cae8d06663e.png)
• Caractéristiques de cablâge fibre optique
![image](https://user-images.githubusercontent.com/19058019/236691013-16fc3323-e363-4aee-86c4-8477ec26072d.png)
• Sans fil
![image](https://user-images.githubusercontent.com/19058019/236691020-4cb68159-3431-4ef5-80fd-1e3c664b5b79.png)
# IpV6
## Encapsulating IPv6
![image](https://user-images.githubusercontent.com/19058019/236691025-816db6dc-798f-46ee-b072-65c260aa4a82.png)
## IPv6 Packet Header
![image](https://user-images.githubusercontent.com/19058019/236691035-a40f4c83-3592-4936-91ce-41858b44685b.png)
## Sample IPv6 Header
![image](https://user-images.githubusercontent.com/19058019/236691044-15436e4c-883b-40d7-9357-b6694173e8e1.png)
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
![image](https://user-images.githubusercontent.com/19058019/236691053-41a77574-c223-48bf-a967-22958530c432.png)
Dual-stack: Allows IPv4 and IPv6 to coexist on the same network.
Devices run both IPv4 and IPv6 protocol stacks simultaneously. It's
the best solution !
### Tunnelling
![image](https://user-images.githubusercontent.com/19058019/236691058-b4311d3d-2bd9-4880-bb9f-5bd6ed7b41ae.png)
Tunnelling: A method of transporting an IPv6 packet over an IPv4
network. The IPv6 packet is encapsulated inside an IPv4 packet.
Usefull to interconnect IPv6 network trough an only IPv4 network
### Translation
![image](https://user-images.githubusercontent.com/19058019/236691064-dce2c2a9-5bf2-49e1-8232-2231c454d33d.png)
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
![image](https://user-images.githubusercontent.com/19058019/236691072-751e2aba-e736-4cf7-a815-a3cdfaf24e2b.png)
Look at the binary bit
patterns that match the
decimal and hexadecimal
values
![image](https://user-images.githubusercontent.com/19058019/236691080-6cafe89d-e99d-46f8-be6e-012a970d4f72.png)
## IPv6 Address Representation
- 128 bits in length and written as a string of hexadecimal values
- In IPv6, 4 bits represents a single hexadecimal digit, 32 hexadecimal value = IPv6 address
2001:0DB8:0000:1111:0000:0000:0000:0200
FE80:0000:0000:0000:0123:4567:89AB:CDEF
- Hextet used to refer to a segment of 16 bits or four hexadecimals
- Can be written in either lowercase or uppercase
![image](https://user-images.githubusercontent.com/19058019/236691086-2f9e30f9-59c9-4fa5-bb13-810b481c08d8.png)
## Rule 1- Omitting Leading 0s
- The first rule to help reduce the notation of IPv6 addresses is any
leading 0s (zeros) in any 16-bit section or hextet can be omitted.
- 01AB can be represented as 1AB.
- 09F0 can be represented as 9F0.
- 0A00 can be represented as A00.
- 00AB can be represented as AB.
![image](https://user-images.githubusercontent.com/19058019/236691096-5a4e0858-ee44-4d7a-9278-a91d32b0beb1.png)
## Rule 2 - Omitting All 0 Segments
- A double colon (::) can replace any single, contiguous string of one or more 16-bit segments (hextets) consisting of all 0’s.
- Double colon (::) can only be used once within an address otherwise the address will be ambiguous.
- Known as the compressed format.
- Incorrect address - 2001:0DB8::ABCD::1234.
![image](https://user-images.githubusercontent.com/19058019/236691102-bb94ac54-933b-455b-a6d3-2a485040a8c6.png)
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
![image](https://user-images.githubusercontent.com/19058019/236691109-4f64718e-d4b6-4739-925a-53772b3708a1.png)
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
![image](https://user-images.githubusercontent.com/19058019/236691116-15fe3281-da67-4309-a64e-0037f86ef773.png)
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
![image](https://user-images.githubusercontent.com/19058019/236691131-0ae49926-ebab-4e74-96aa-b7bf4e574826.png)
Packets with a source or destination link-local address cannot be routed beyond the link from where the packet originated.
![image](https://user-images.githubusercontent.com/19058019/236691140-c167084e-cfbd-4388-8733-de60005c0f8c.png)
## Structure of an IPv6 Global Unicast Address
- IPv6 global unicast addresses are globally unique and routable on the IPv6 Internet
- Equivalent to public IPv4 addresses
- ICANN allocates IPv6 address blocks to the five RIRs
Currently, only global unicast addresses with the first three bits of 001 or 2000::/3 are being assigned
![image](https://user-images.githubusercontent.com/19058019/236691149-1fb0d740-1629-40c8-af01-c574a12cc99a.png)
A global unicast address has three parts: Global Routing Prefix, Subnet ID, and Interface ID.
- Global Routing Prefix is the prefix or network portion of the address assigned by the provider, such as an ISP, to a customer or site, currently, RIR’s assign a /48 global routing prefix to customers.
- 2001:0DB8:ACAD::/48 has a prefix that indicates that the first 48 bits (2001:0DB8:ACAD) is the prefix or network portion.
![image](https://user-images.githubusercontent.com/19058019/236691157-f7c079ee-f975-4399-b904-cfab67fc2736.png)
- Subnet ID is used by an organization to identify subnets within its site
- Interface ID
	–Equivalent to the host portion of an IPv4 address.
	–Used because a single host may have multiple interfaces, each
	having one or more IPv6 addresses.
![image](https://user-images.githubusercontent.com/19058019/236691160-f00aecfe-50d8-4a4d-a6a7-dffa44e38165.png)
## Static Configuration of a Global Unicast Address
![image](https://user-images.githubusercontent.com/19058019/236691166-f91888fe-2949-4fb6-8889-b08c37fdbefb.png)
Windows IPv6 Setup
![image](https://user-images.githubusercontent.com/19058019/236691176-3dc9036b-169f-4182-a508-569b18508886.png)
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
![image](https://user-images.githubusercontent.com/19058019/236691185-7e5edcb3-76a8-409c-85db-c919c123fcce.png)
## Dynamic Configuration of a Global Unicast Address using DHCPv6 (cont.)
Dynamic Host Configuration Protocol for IPv6 (DHCPv6)
- Similar to IPv4
- Automatically receives addressing information, including a global unicast address, prefix length, default gateway address and the addresses of DNS servers using the services of a DHCPv6 server.
- Device may receive all or some of its IPv6 addressing information from a DHCPv6 server depending upon whether option 2 (SLAAC and DHCPv6) or option 3 (DHCPv6 only) is specified in the ICMPv6 RA message.
- Host may choose to ignore whatever is in the router’s RA message and obtain its IPv6 address and other information directly from a DHCPv6 server.
![image](https://user-images.githubusercontent.com/19058019/236691196-f8e262ec-70f1-46f9-bd84-a379dcd1416b.png)
## EUI-64 Process or Randomly Generated
EUI-64 Process
	- Uses a client’s 48-bit Ethernet MAC address and inserts another 16 bits in the middle of the 46-bit MAC address to create a 64-bit Interface ID.
	- Advantage is that the Ethernet MAC address can be used to determine the interface; is easily tracked.
	- Default on most hosts !
EUI-64 Interface ID is represented in binary and comprises three parts:
	- 24-bit OUI from the client MAC address, but the 7th bit (the Universally/Locally bit) is reversed (0 becomes a 1).
	- Inserted as a 16-bit value FFFE.
	- 24-bit device identifier from the client MAC address.
![image](https://user-images.githubusercontent.com/19058019/236691210-7d4ed3b4-b44d-4333-94a9-35d072dc4301.png)
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
![image](https://user-images.githubusercontent.com/19058019/236691225-2f13268a-fab3-41ca-9d96-9ac4d8e191df.png)
## Static Link-local Addresses
![image](https://user-images.githubusercontent.com/19058019/236691230-4efbdaa9-1d01-484a-b964-e6547de88990.png)
## Exercise
Calculate the local link address (l’adresse lien-local) for MAC adress : 00-11-5B-69-C1-D4.
![image](https://user-images.githubusercontent.com/19058019/236691243-4590ae4d-6bed-4ff7-ad69-b1917f00d900.png)
What is your host Loopback adress ?
::1
![image](https://user-images.githubusercontent.com/19058019/236691249-51e30deb-0038-4d74-8abc-e8120f6f421e.png)
## Verifying IPv6 Address Configuration
Each interface has two IPv6 addresses -
1. global unicast address that was configured
2. one that begins with FE80 is automatically added as a link-local unicast address
![image](https://user-images.githubusercontent.com/19058019/236691259-604ede47-d9f9-46ee-9b69-58efeb571f85.png)
## Assigned IPv6 Multicast Addresses
Two common IPv6 assigned multicast groups include:
-FF02::1 All-nodes multicast group –
	- All IPv6-enabled devices join
	- Same effect as an IPv4 broadcast address
-FF02::2 All-routers multicast group
	- All IPv6 routers join
	- A router becomes a member of this group when it is enabled as an IPv6 router with the ipv6 unicast-routing global configuration mode command.
	- A packet sent to this group is received and processed by all IPv6 routers on the link or network.
![image](https://user-images.githubusercontent.com/19058019/236691281-0905b11c-3535-4a52-9ad4-6b77158b44c4.png)
## Solicited Node IPv6 Multicast Addresses
- Similar to the all-nodes multicast address, matches only the last 24 bits of the IPv6 global unicast address of a device
- Automatically created when the global unicast or link-local unicast addresses are assigned
- Created by combining a special FF02:0:0:0:0:0:FF00::/104 prefix with the right-most 24 bits of its unicast address
![image](https://user-images.githubusercontent.com/19058019/236691289-dee80205-8f5c-43a3-9b53-dcb38951a9e9.png)
The solicited node multicast address consists of two parts:
- FF02:0:0:0:0:0:FF00::/104 multicast prefix – First 104 bits of the all solicited node multicast address
- Least significant 24-bits – Copied from the right-most 24 bits of the global unicast or link-local unicast address of the device
![image](https://user-images.githubusercontent.com/19058019/236691296-2225ce65-a341-4384-883d-754195607596.png)
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
![image](https://user-images.githubusercontent.com/19058019/236691329-3a9f0bac-4009-4979-aa33-a9db6ba99fdc.png)
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
![image](https://user-images.githubusercontent.com/19058019/236691335-0aeb7811-20a8-41b3-83c0-fd0d10d62ce1.png)
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
![image](https://user-images.githubusercontent.com/19058019/236691347-cb2f4dfc-061f-49b3-8bd8-0f9273417116.png)
## IPV6 Subnet Allocation
![image](https://user-images.githubusercontent.com/19058019/236691349-98eeb2a6-f5d1-4874-8b0a-f58a044bc2b7.png)
## Subnetting into the Interface ID
IPv6 bits can be borrowed from the interface ID to create additional
IPv6 subnets.
![image](https://user-images.githubusercontent.com/19058019/236691356-2afffa1d-d000-4b13-a3ca-199512653b9e.png)


