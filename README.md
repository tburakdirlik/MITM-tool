# MITM-tool
MITM is known as one of the most common attack and this tool do this attack. This repo include arp poisoner and packet listener python files. This is educational repository so don't try this tool over other users. Firstly run arp_poisoner.py then packet_listener.py also you can use wireshark instead of packet_listener.py
![Image of Yaktocat](https://i0.wp.com/hackonology.com/wp-content/uploads/2019/10/man-in-the-middle-attack.png?w=893&ssl=1)

# Requirements

Operating system: Linux

Libraries: 
```bash
> pip install scapy 
> pip install sslstrip
```
# Arp poisoner usage
```bash
> python3 arp_poisoner.py -t <target ip> -g <gateway ip>
```

# Packet listener usage
if you want to see all packets by sent target user you should use option 1  
```bash
Option 1 ->  python3 packetlistener.py --all <interface>
```
if you want to see just user infos like username and password when a user go into http sites you should use option 2 
```bash    
Option 2 -> python3 packetlistener.py --userinfos <interface>
```
