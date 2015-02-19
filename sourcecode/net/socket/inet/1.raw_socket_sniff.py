import socket
import struct
import binascii

ETH_P_ALL = 0x0003

rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW,
                          socket.htons(ETH_P_ALL))

while True:

    packet = rawSocket.recvfrom(2048)

    ethernet_header = packet[0][0:14]
    ethernet_detailed = struct.unpack("!6s6s2s", ethernet_header)

    arp_header = packet[0][14:42]
    arp_detailed = struct.unpack("2s2s1s1s2s6s4s6s4s", arp_header)

    # skip non-ARP packets
    ethertype = ethernet_detailed[2]
    if ethertype != '\x08\x06':
        continue

    print "****************_ETHERNET_FRAME_****************"
    print "Dest MAC:        ", binascii.hexlify(ethernet_detailed[0])
    print "Source MAC:      ", binascii.hexlify(ethernet_detailed[1])
    print "Type:            ", binascii.hexlify(ethertype)
    print "************************************************"
    print "******************_ARP_HEADER_******************"
    print "Hardware type:   ", binascii.hexlify(arp_detailed[0])
    print "Protocol type:   ", binascii.hexlify(arp_detailed[1])
    print "Hardware size:   ", binascii.hexlify(arp_detailed[2])
    print "Protocol size:   ", binascii.hexlify(arp_detailed[3])
    print "Opcode:          ", binascii.hexlify(arp_detailed[4])
    print "Source MAC:      ", binascii.hexlify(arp_detailed[5])
    print "Source IP:       ", socket.inet_ntoa(arp_detailed[6])
    print "Dest MAC:        ", binascii.hexlify(arp_detailed[7])
    print "Dest IP:         ", socket.inet_ntoa(arp_detailed[8])
    print "*************************************************\n"
