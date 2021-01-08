import os
from pathlib import Path


#read first sector of the disk 1
disk_fd = os.open( r"\\.\PhysicalDrive0", os.O_RDONLY | os.O_BINARY)
data = os.read(disk_fd, 512)
os.close(disk_fd)


binary = bytearray(data) #convert it to bytearry
after = open('Current-mbr.bin', 'w+b') # opens/create the MBR bin file 

after.write(binary) # writing to file 
after.close()

beforeenc = Path('TrueCryptmbr.bin').read_bytes() #open the MBR bin before the enc
afterenc = Path('Current-mbr.bin').read_bytes() #open the MBR bin after the enc

if beforeenc == afterenc:
    print("MBR code integrity check has been succesfull")

else:
    print("MBR code has been modified")
