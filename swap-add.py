#!/usr/bin/env python3

# Author: Arvin Gonzales
# Author ID: reodus.x
# Date Created: 2025/09/19
# Purpose: Add a swap file to the current one and make it a prioroty
# Use case: My old swap file (3G) is not enough to run 2 or more VMs smoothly

# Check current swap
swapon --show
free -h

# Create the swap file
sudo fallocate -l 10G /swapfile

# If fallocate fails, use:
sudo dd if=/dev/zero of=/swapfile bs=1M count=10240 status=progress

# Secure the file
sudo chmod 600 /swapfile

# Firmat it as a swap file
sudo mkswap /swapfile

# Enable it immediately
sudo swapon /swapfile

# Make it permanent with priority
sudo nano /etc/fstab
# Add this command below at the very bottom
/swapfile none swap sw,pri=100 0 0

# Reload swap configuration
sudo swapoff /swapfile
sudo swapon -a

# Verify
swapon --show
free -h

# It should show something like below:
# PRIO=100 → this means the kernel will always try to use it first, highest in priority
NAME           TYPE      SIZE   USED PRIO
/swapfile      file       10G     0B  100
/dev/nvme0n1p4 partition 977M     0B   -2
/dev/nvme0n1p7 partition 2.3G     0B   -3
