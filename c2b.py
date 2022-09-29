import io
import binascii

in_file = input("Input:")
out_file = input("Output:")
f = open(in_file)
f_raw = f.read()
f.close()
o = open(out_file,'wb')
o.write(binascii.unhexlify(f_raw))
o.close()
