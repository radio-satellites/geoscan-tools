import io
import os
from PIL import Image
import binascii

def process(in_file,characters_to_remove):
    no_header = []
    bad_words = ["1: [GEOSCAN]"]
    with open(in_file) as dumpfile:
        for line in dumpfile:
            if not any(bad_word in line for bad_word in bad_words):
                no_header.append(line)



    f_lines = no_header
    f_lines_joined = []
    f_joined = ""

    for i in range(len(f_lines)):
        if f_lines[i] == "":
            pass
        else:
            f_lines_joined.append(f_lines[i].replace(" ","")[characters_to_remove:len(f_lines[i].replace(" ",""))])

     
    for i in range(len(f_lines_joined)):
        f_joined = f_joined+f_lines_joined[i]

    f_joined = f_joined.replace("\n","").replace("\r","")
    return f_joined
def process_RAW(f_joined,out_file):
    o = open(out_file,'wb')
    o.write(binascii.unhexlify(f_joined))
    o.close()
    print("Wrote raw JPEG!")

def process_image(f_joined,out_file):
    print("Writing complete JPEG...")
    image_data = bytearray.fromhex(f_joined)
    image_geoscan = Image.open(io.BytesIO(image_data))
    image_geoscan.save(out_file)
    print("Done!")
    
