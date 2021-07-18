import optparse
import scapy.all as scapy
from scapy_http import http

def listen_packets(interface):
# store = False -> aldığım paketleri hafızaya kaydetme demek
# prn bir callback function , paketleri belirtilen fonksiyona input olarak yolluyor
    scapy.sniff(iface=interface,store=False,prn=analyze_packets)

def analyze_packets(packet):

    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):

            print(packet[scapy.Raw].load)



def listen_all_packets(interface):
    scapy.sniff(iface=interface, store=False, prn=analyze_all_packets)

def analyze_all_packets(packet):
    packet.show()


if __name__ == "__main__":
    parse_object = optparse.OptionParser()
    parse_object.add_option("--all", dest="allpackets")
    parse_object.add_option("--userinfos", dest="userinfos")
    (inputs, arguments) = parse_object.parse_args()

    if inputs.userinfos:
        listen_packets(inputs.userinfos)

    if inputs.allpackets:
        listen_all_packets(inputs.allpackets)
