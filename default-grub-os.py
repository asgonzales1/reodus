#!/usr/bin/env python3

# Author: Arvin Gonzales
# Author ID: reodus.x
# Date Created: 2025/09/18
# Purpose: Change default boot OS in grub

### open grub file
sudo vim /etc/default/grub			

GRUB_DEFAULT=#				### change the default value to the order# in boot

### to update the /boot/grub/grub.cfg file
sudo update-grub 				
