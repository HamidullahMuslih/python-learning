import os

#read first sector of the disk 1
disk_fd = os.open( r"\\.\PhysicalDrive0", os.O_RDONLY | os.O_BINARY) 
data = os.read(disk_fd, 512)
os.close(disk_fd)

file = open('TrueCryptmbr.bin', 'w+b') # opens/create the MBR bin file 
binary = bytearray(data) #convert it to bytearry
file.write(binary)
file.close()

