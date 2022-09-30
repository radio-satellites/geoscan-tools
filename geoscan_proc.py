import io
from PIL import Image
import os
import binascii
#characters_to_remove = 16 #For raw soundmodem data
#characters_to_remove = 10 #For raw soundmodem data that has been processed by GetKISS+
#characters_to_remove = 47 #For data output from GetKISS+

in_file = input("Input file:")
out_file = input("Output file:")
raw_j = input("Write raw JPEG (for corrupt/incomplete images)?")
characters_to_remove = int(input("Characters to remove (16 raw soundmodem, 47 for GetKISS+):"))

bad_words = ["1: [GEOSCAN]"]
with open(in_file) as dumpfile, open('dump_noheader.txt', 'w') as cleanfile:
    for line in dumpfile:
        if not any(bad_word in line for bad_word in bad_words):
            cleanfile.write(line)
    cleanfile.close()



f = open("dump_noheader.txt")
f_raw = f.read()
f_lines = f_raw.split("\n")
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

if raw_j == "y" or raw_j == "Y" or raw_j == "Yes" or raw_j == "yes":
    o = open(out_file,'wb')
    o.write(binascii.unhexlify(f_joined))
    o.close()
    print("Wrote raw JPEG!")
else:
    print("Writing complete JPEG...")
    image_data = bytearray.fromhex(f_joined)
    image_geoscan = Image.open(io.BytesIO(image_data))
    image_geoscan.save(out_file)
    print("Done!")

f.close()
os.remove("dump_noheader.txt")
