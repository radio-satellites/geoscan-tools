# geoscan-tools
Some tools to process data from the GEOSCAN satellite (wip). 
![output](https://user-images.githubusercontent.com/114111180/192885196-7b54cd63-fa24-4f51-977f-e8b944e0417c.jpg)

***NOTE: There is news that GEOSCAN now sometimes transmits multiple images per file. The program cannot handle this right now! I'm working on it :)***
***UPDATE: Yes it can now =D***
# Intro

GEOSCAN transmits in a 9600baud mode JPEG images of the Earth which can be received using a 70cm yagi and subsequently decoded using this tool. A 6-element yagi antenna should work rather well as a budget receiving antenna. 

# How-to
While receiving the signal, set your SDR mode to WFM. A special version of SoundModem for GEOSCAN may be downloaded at http://uz7.ho.ua/geoscan.zip. To be successful, use a virtual audio cable!! Stereo Mix **does not work**! Soundmodem will decode the packets. Before starting to decode, click "Open Monitor Log file." When the dump is finished, click "Close Monitor Log file."

Next, use this tool to decode the image from the hex demodulated by SoundModem!

```
python geoscan_proc.py
``` 

Use case example: GetKISS+

```
Input file:geoscan-edelveis.txt
Output file:output.jpg
Write raw JPEG (for corrupt/incomplete images)?y
Characters to remove (16 raw soundmodem, 47 for GetKISS+):47
Wrote raw JPEG!
``` 

For soundmodem, the same options can be used with a small modification. "Characters to remove" should be set to 16. 

A NOTE ON RAW JPEGs:

If you have a corrupt image (e.g missing packets), writing a raw JPEG might help remedy this problem a bit and allow the program to not crash when processing!

# Technical details

Essentially, first off we strip off a header issued by the decoding program. If GetKISS+ is used, a header of 47 is present. If SoundModem is used, set a length of 16 (in some rare cases, 10 might work too)!

A GetKISS+ file has a header
```
2022-09-20 20:11:40.530 | len: 064 |
``` 

Otherwise (if using the "monitor log file" function in SoundModem), a header of 
```
1: [GEOSCAN] [18:03:49R]
``` 
is attached to each packet. 

Note that there are extra newlines that need to be removed as well. 

Then, I noticed a fixed almost always repeating sequence 

```
01003E050970800B
``` 
This could be telemetry or something unknown right now. Rather, we need to cut the sequence out, because with it the JPEG will not decode correctly. 

After this, we just convert everything to hexadecimal, and then write it to a JPEG. 

# C2B

This super-simple script converts the hexadecimal to binary to be analyzed with different tools. 

# Note for UNIX-like systems
When running on a UNIX system, [PE0SAT](https://community.libre.space/u/PE0SAT) found that it is necessary to run 
```
dos2unix geoscan_proc.py
```
in order to run without errors. 

73!
