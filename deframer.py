import binascii
import io
import os
import process_image

headers = ['01003E01', '01003E05', '01002605']
headerlength = 16
#Above: header for each new file that is downlinked

def mult_files(in_file):
    file_counter = 0
    for row in in_file:
        header = row[:headerlength]
        cmd = row[:headerlength//2]
        addr = int((row[12:14] + row[10:12]), 16) % 32768
        payload = row[headerlength:]
        #the above was SHAMELESSLY taken from the OTHER geoscan-tools =D
        if cmd in headers:
            if cmd == headers[0]:
                file_counter = file_counter + 1
        if file_counter == 1:
            return False, 1
        else:
            return True, file_counter
        
def deframe(in_file,outputfile):
    outfile = io.BufferedWriter
    file_counter = 0
    for row in in_file:
        header = row[:headerlength]
        cmd = row[:headerlength//2]
        addr = int((row[12:14] + row[10:12]), 16) % 32768
        payload = row[headerlength:]
        #the above was SHAMELESSLY taken from the OTHER geoscan-tools =D
        if cmd in headers:
            if cmd == headers[0] and not outfile.closed:
                file_counter = file_counter + 1
                outfile.close()
                if process_image.check_valid(outfile.name) == True:
                    print("Finished processing file "+str(file_counter - 1)) #voodoo!
                else:
                    print("Writing INVALID JPEG "+str(outfile.name))

            if outfile.closed:
                filetype = 'bin'
                if payload.startswith("FFD8"):
                    filetype = 'jpg'
                    outfile = open(outputfile+"_"+str(file_counter)+"."+str(filetype),'wb')
                else:
                    outfile = open(outputfile+"_"+str(file_counter)+"."+str(filetype),'wb')
                    
            outfile.write(bytes.fromhex(payload))
            
            if cmd == headers[2]:
                outfile.close()
    if not outfile.closed:
        outfile.close()
            
