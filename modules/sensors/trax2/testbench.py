from trax_fxns import TRAX
import serial
import struct

"""
    Created by Ryan Sundermeyer
    https://github.com/rsunderr
    rwork@sundermeyer.com
"""

trax = TRAX()
trax.connect()
# datagram: [ byte count uint16 ] [ frame ID uint8 ] [ payload (opt) ] [ CRC uint16 ]

# check device version
frameID = 1
trax.send_packet(frameID)
resp = trax.recv_packet()
print(resp)
typ = TRAX.uint_to_str(resp[2], 32)
rev = TRAX.uint_to_str(resp[3], 32)
print(typ)
print(rev)
print()

# check if big endian
frameID = 7
payload = (6,)
trax.send_packet(frameID, payload)
resp = trax.recv_packet(payload)
print(resp)
print("Big Endian: ", resp[3])

trax.close()