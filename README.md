# gadgetstuff
Playground for gadget automation

Here is a run of the raw device, not using the sample fine, but should be very similar temperatures, etc as was roughly the same time. I did play with the CP3800 to test the Desired Temperature is correct (well, believable considering there's rounding issues), so I believe it's a decent start.

```
root@home:/opt/gadgetstuff# ls
compool_lx3400_sample.bin  decodecompool.py  LICENSE  compool_lx3400_sample_2.bin  sampledata.py
root@home:/opt/gadgetstuff# ./decodecompool.py
Synchronization byte found: 0f1b02101316020802670000007693380000700004325ada5affaa
Remaining bytes: 0f1b02101316020802670000007693380000700004325ada5affaa
Byte: 0x0F, Destination Address: 15
Byte: 0x1B, Source Address: 27
Byte: 0x02, OpCode: 2
Byte: 0x10, Info Field Length: 16
Byte: 0x13, Minutes: 19
Byte: 0x16, Hours: 22
Byte: 0x02, Primary Equipment: 2
Byte: 0x08, Secondary Equipment: 8
Byte: 0x02, Delay/Heat Source: 2
Byte: 0x67, Water Temp: 78.35
Byte: 0x00, Solar Temp: 32.0
Byte: 0x00, Spa Water Temp: 32.0
Byte: 0x00, Spa Solar Temp: 32.0
Byte: 0x76, Desired Pool Temp: 85.1
Byte: 0x93, Desired Spa Temp: 98.15
Byte: 0x38, Air Temp: 57.2
Byte: 0x00, UNK 1: 0
Byte: 0x00, UNK 2: 0
Byte: 0x70, Equip Status: 112
Byte: 0x00, Product Type: 0
Byte: 0x04, Hi Byte of Checksum: 4
Byte: 0x32, Lo Byte of Checksum: 50
Synchronization byte found: 0f1b02101316020802670000007693380000700004325ada5affaa
Remaining bytes: 0f1b02101316020802670000007693380000700004325ada5affaa
Byte: 0x0F, Destination Address: 15
Byte: 0x1B, Source Address: 27
Byte: 0x02, OpCode: 2
Byte: 0x10, Info Field Length: 16
Byte: 0x13, Minutes: 19
Byte: 0x16, Hours: 22
Byte: 0x02, Primary Equipment: 2
Byte: 0x08, Secondary Equipment: 8
Byte: 0x02, Delay/Heat Source: 2
Byte: 0x67, Water Temp: 78.35
Byte: 0x00, Solar Temp: 32.0
Byte: 0x00, Spa Water Temp: 32.0
Byte: 0x00, Spa Solar Temp: 32.0
Byte: 0x76, Desired Pool Temp: 85.1
Byte: 0x93, Desired Spa Temp: 98.15
Byte: 0x38, Air Temp: 57.2
Byte: 0x00, UNK 1: 0
Byte: 0x00, UNK 2: 0
Byte: 0x70, Equip Status: 112
Byte: 0x00, Product Type: 0
Byte: 0x04, Hi Byte of Checksum: 4
Byte: 0x32, Lo Byte of Checksum: 50
```
