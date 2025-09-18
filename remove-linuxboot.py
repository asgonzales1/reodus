### Remove Linux in a windows partition boot

# Go to disk mgt and delete partition w/ no drive letter
# Open command prompt as admin 

# Type and press enter
diskpart

# then and enter the below command to check fo the list of disks
list disk

# Type and enter the number of the disk listed
select disk 0

#Type and enter, to list the partitions
list partition     # then look for partition type system, mostly 100MB

# Type and run - if 100MB is in partition 1
select partition 1, 
# then run command 
assign letter=z
# then run,
exit


###Go and mount the drive letter
z:
dir
cd efi
dir

# Look for ay linux names listed, then run below
rd ubuntu /s   # then type y when prompted for YES

dir            # to check if it really has been removed
exit           # then restart
