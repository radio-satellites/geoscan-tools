import process_image
import deframer

#characters_to_remove = 16 #For raw soundmodem data
#characters_to_remove = 10 #For raw soundmodem data that has been processed by GetKISS+
#characters_to_remove = 47 #For data output from GetKISS+

in_file = input("Input file:")
out_file = input("Output file:")
raw_j = input("Write raw JPEG (for corrupt/incomplete images, or for multiple files)?")
characters_to_remove = int(input("Characters to remove (16 raw soundmodem, 47 for GetKISS+):"))

def process_from_hex(in_hex,output):
    if raw_j == "y" or raw_j == "Y" or raw_j == "Yes" or raw_j == "yes":
        process_image.process_RAW(in_hex,output)
    else:
        process_image.process_image(in_hex,output)


f_joined = process_image.process(in_file,characters_to_remove)

if deframer.mult_files(f_joined) == True:
    print("Detected multiple files downlinked...")
    proc_im = input("Process the images into JPEG (and binary)?")
    
    deframed = deframer.deframe(f_joined)
    no_files = len(deframed)
    print(str(no_files)+" files have been detected")
    out_file = input("outfile: ")
    for i in range(len(deframed)):
        #process_from_hex(deframed[i],out_file+str(i)+".jpg")
        f = open(out_file+str(i)+".txt",'w')
        f.write(deframed[i])
        f.close()
        if proc_im == "y" or proc_im == "Y" or proc_im == "Yes" or proc_im == "yes":
            try:
                process_from_hex(deframed[i],out_file+str(i)+".jpg")
            except:
                print("This is not an image.")
        print("Processed "+str(i+1)+" out of "+str(no_files))
else:
    print("Single JPEG file only")
    process_from_hex(f_joined,out_file)

