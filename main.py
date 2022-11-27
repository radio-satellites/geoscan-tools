import process_image
import deframer

#characters_to_remove = 16 #For raw soundmodem data
#characters_to_remove = 10 #For raw soundmodem data that has been processed by GetKISS+
#characters_to_remove = 47 #For data output from GetKISS+

in_file = input("Input file:")
out_file = input("Output file:")
characters_to_remove = int(input("Characters to remove (0 raw soundmodem, 31 for GetKISS+):"))

"""
def process_from_hex(in_hex,output):
    if raw_j == "y" or raw_j == "Y" or raw_j == "Yes" or raw_j == "yes":
        process_image.process_RAW(in_hex,output)
    else:
        process_image.process_image(in_hex,output)

"""
f_joined = process_image.process(in_file,characters_to_remove)


if deframer.mult_files(f_joined)[0] == True:
    print("Detected multiple files downlinked...")
    no_files = deframer.mult_files(f_joined)[1]
    print(str(no_files)+" files have been detected.")
    process_image.process_multiple(f_joined,out_file)
    
else:
    print("Single JPEG file only")
    #process_from_hex(f_joined,out_file)
    process_image.process_multiple(f_joined,out_file)

print("Done.")
