# geoscan-tools
Some tools to process data from the GEOSCAN satellite. 
![output](https://user-images.githubusercontent.com/114111180/192885196-7b54cd63-fa24-4f51-977f-e8b944e0417c.jpg)


# Intro

GEOSCAN transmits in a 9600baud mode JPEG images of the Earth which can be received using a 70cm yagi, and subsequently decoded using this tool. A 6-element yagi antenna should work well. 

# How-to
While receiving the signal, set your SDR mode to WFM. A special version of SoundModem for GEOSCAN may be downloaded at http://uz7.ho.ua/geoscan.zip. To be successful, use a virtual audio cable!! Stereo Mix **does not work**! Soundmodem will decode the packets. Before starting to decode, click "Open Monitor Log file." When the dump is finished, click "Close Monitor Log file."

Next, use this tool to decode the image from the hex demodulated by SoundModem!

```
python geoscan_proc.py
``` 

The GEOSCAN raw option dictates whether or not to strip off the SoundModem header (see below). The cut option is used for denoting to cut a header. See the section below for some details

# Technical details

Essentially, first off we strip off a header issued by the decoding program. If GetKISS+ is used, a header of 47 is present. If SoundModem is used, set a length of 16 (in some rare cases, 10 might work too)!
```
2022-09-20 20:11:40.530 | len: 064 |
``` 
is present.
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
