#! / usr / bin / python

# ---------------- BACA AKU ------------------------------- --------------
# Script Ini Dibuat Hanya Untuk Praktek Dan Tujuan Pendidikan Saja
# Script Ini Dibuat Untuk Anda Sok Pro
# Script Ini Ditulis Oleh
#
#
###############################################
######## Harap Jangan Hapus Nama Penulis #########
############### Terima kasih #########################
###############################################
#
#
__author __ = '' '

############################################### ####
              Anonymousid          
############################################### ####


    Catatan: Kami Merasa Bangga Menjadi Orang Indonesia
############################################### ####
'' '
impor soket, struct, binascii, os
import pye

print pye .__ author__

jika os.name == "nt":
    s = socket.socket (socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind ((("YOUR_INTERFACE_IP", 0))
    s.setsockopt (socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.ioctl (soket.SIO_RCVALL, soket.RCVALL_ON)
lain:
    s = socket.socket (socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs (0x0800))

sementara Benar:
    pkt = s.recvfrom (65565)
    unpack = pye.unpack ()
    cetak "\ n \ n === >> [+] ------------ Header Ethernet ----- [+]"
    untuk saya di unpack.eth_header (pkt [0] [0:14]). iteritems ():
        a, b = i
        cetak "{}: {} |" .format (a, b),
    cetak "\ n === >> [+] ------------ Header IP ------------ [+]"
    untuk saya di unpack.ip_header (pkt [0] [14:34]). iteritems ():
        a, b = i
        cetak "{}: {} |" .format (a, b),
    cetak "\ n === >> [+] ------------ Tcp Header ----------- [+]"
    untuk saya di unpack.tcp_header (pkt [0] [34:54]). iteritems ():
        a, b = i
        cetak "{}: {} |" .format (a, b),

    
