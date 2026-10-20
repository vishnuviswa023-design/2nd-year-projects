from scapy.all import *

for port in range(20,101):
        pkt=IP(dst="127.0.0.1")/TCP(dport=port,flags="S")
        reply=sr1(pkt,timeout=1,verbose=0)
        if reply is None:
                print(f"port is {port}: filtered")
        elif reply.haslayer(TCP):
                if reply[TCP].flags == 0x12:
                        print(f"port is open :{port}")
                elif reply[TCP].flags == 0x14:
                        print(f"port is closed {port}")
