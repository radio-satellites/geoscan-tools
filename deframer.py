import binascii
import io
import os

header = "4F 4F 4F 4F 4F 4F 4F 4F 4F 4F 4F 4F 4F 4F 4F 4F 4F 4F 4F 4F 4F 4F 4F 4F FF C4 01 A2 00 00 01 05".replace(" ","")
#Above: header for each new file that is downlinkeds

def mult_files(in_file):
    if header in in_file:
        return True
    else:
        return False
def deframe(in_file):
    output = in_file.split(header)
    return output
