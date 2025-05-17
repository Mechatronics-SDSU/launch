from trax_fxns import TRAX
import serial
import struct
import time

"""
    Created by Ryan Sundermeyer
    https://github.com/rsunderr
    rwork@sundermeyer.com
"""

trax = TRAX()
trax.connect()

# kSetAcqParams
frameID = "kSetAcqParams" # OR =24
payload = (False, False, 0.0, 0.001)
trax.send_packet(frameID, payload)
# kSetAcqParamsDone
data = trax.recv_packet()
print(data[1] == 26)

# kSetDataComponents
frameID = "kSetDataComponents" # OR =3
payload = (4, 0x5, 0x18, 0x19, 0x4f)
trax.send_packet(frameID, payload)

# kStartContinuousMode
frameID = "kStartContinuousMode" # OR =21
trax.send_packet(frameID)

data = trax.recv_packet()

# kStopContinuousMode
#frameID = "kStopContinuousMode" # OR =22
#trax.send_packet(frameID)


trax.close()