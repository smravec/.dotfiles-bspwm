# Arch Linux install guide

### Before install
1. download arch iso and flash it onto usb stick with BalenaEtcher
2. plug usb stick into the machine
3. enter bios by pressing f2 when booting and put the usb stick to the top of the boot order
4. save changes, exit and reboot

## Connect to internet (wifi)
start iwctl
```
iwctl 
```
scan for networks
```
station wlan0 scan
```
show all available networks
```
station wlan0 get-networks
```
connect to network
```
station wlan0 connect NAME_OF_NETWORK
```

## Set up system clock and timezones
list all timezones (exit with q)
```
timedatectl list-timezones
```
set timezone
```
ln -sf /usr/share/zoneinfo/Europe/Bratislava /etc/localtime
```
sync clock
```
timedatectl set-ntp true
```
```
hwclock --systohc
```
## Partition your disk
list all available disks
```
fdisk -l
```
start partitioning your disk (could be named /dev/sda, /dev/nvme0n1 or /dev/mmcblk0, I will use /dev/nvme0n1)
```
fdisk /dev/nvme0n1
```
view all the commands for fdisk
```
m
```
create a new gpt table
```
g
```
create 4 partitions (EFI, SWAP, ROOT and HOME)
### EFI (create partition, assign the number 1 to it, select how big it should be, change the type to EFI partition)
```
n
1
(just press enter)
+350M
t
1
1
```
### SWAP (create partition, assing the number 2 to it, select how big it should be, change the type to Linux swap)
```
n
2
(just press enter)
```
if using laptop this should be your ram size + few gb (my ram is 32gb so +34G)
```
+34G
```
change the type to Linux swap
```
t
2
```
to get this number type L which prints all available partition types
```
19
```
### Linux root filesystem (create new partition, assign the number 3 to it, select how big it should be, dont have to change the type)
```
n
3
(just press enter)
+140G
```

### Linux home filesystem (create new partition, assign the number 4 to it, select how big it should be, dont have to change the type)
```
n
4
(just press enter)
(just press enter)
```
to save all changes press w
```
w
```
# Format partitions
format the EFI, SWAP, ROOT and HOME partitions (and enable swap)
```
mkfs.fat -F32 /dev/nvme0n1p1
mkswap /dev/nvme0n1p2
swapon /dev/nvme0n1p2
mkfs.ext4 /dev/nvme0n1p3
mkfs.ext4 /dev/nvme0n1p4
```
## Install base
mount all partitions except swap on /mnt
```
mount /dev/nvme0n1p3 /mnt
mkdir /mnt/boot
mount /dev/nvme0n1p1 /mnt/boot
mkdir /mnt/home
mount /dev/nvme0n1p4 /mnt/home
```
install linux
```
pacstrap /mnt base linux linux-firmware
```
generate fstab (save partition mount points)
```
genfstab -U /mnt >> /mnt/etc/fstab
```
## Chroot
change root into the new arch install
```
arch-chroot /mnt
```
setup clock and timezone again
```
ln -sf /usr/share/zoneinfo/REGION/CITY /etc/localtime
hwclock --systohc 
```
download vim (basic vim commands: I to enter insert mode, Esc to exit insert mode, to exit and save :wq (also you have to be out of insert mode), to just exit without saving :q! (also you have to be out of insert mode))
```
pacman -S vim
```
### Localisation
setup keyboard layout
```
vim /etc/locale.gen
```
find this line
```
#en_US.UTF-8 UTF-8 
```
uncomment it e.g.
```
en_US.UTF-8 UTF-8
```
generate locale
```
locale-gen
```
setup en_US.UTF-8 as default fallback
```
echo "LANG=en_US.UTF-8" >> /etc/locale.conf
```
### Networking
setup hostname (replace framework for your hostname)
```
echo "framework" >> /etc/hostname
```
setup hosts (ip lookup table)
```
vim /etc/hosts
```
copy this into /etc/hosts (replace framework for your hostname)
```
127.0.0.1   localhost
::1         localhost
127.0.1.1   framework.localdomain  framework
```
### Permissions
setup root password
```
passwd 
```
add user, set password and give permissions (replace simon with your username)
```
useradd -m simon
passwd simon
usermod -aG wheel,audio,video,optical,storage simon
```
download sudo with pacman
```
pacman -S sudo
```
setup sudo
```
EDITOR=vim visudo
```
find this line
```
#%wheel ALL=(ALL:ALL) ALL
```
uncomment it e.g.
```
%wheel ALL=(ALL:ALL) ALL
```
save and exit by pressing Ecs and :wq

## Bootloader (EFISTUB)
NOT FNISHED
```
bootctl install
```
```
vim /boot/loader/loader.conf
```
```
default  arch.conf
timeout  0
console-mode max
editor   no
```
```
touch /boot/loader/entries/arch.conf
vim /boot/loader/entries/arch.conf
```
```
title   Arch Linux
linux   /vmlinuz-linux
initrd  /intel-ucode.img
initrd  /initramfs-linux.img
options root=/dev/nvme0n1p3 rw
```
## Other packages install and setup
install base packages 
```
pacman -S base-devel networkmanager wpa_supplicant intel-ucode linux-headers
```
setup network manager
```
systemctl enable NetworkManager
```
## Reboot
exit chroot
```
exit
```
unmount file system
```
umount -R /mnt
```
reboot pc and remove usb stick
```
reboot
```
## OTHER

## Silent boot
remove last login message on boot
```
touch ~/.hushlogin
```
remove kernel messages on boot
```
sudo vim /etc/sysctl.d/20-quiet-printk.conf
```
add this line
```
kernel.printk = 3 3 3 3
```
remove agetty messages
```
sudo mkdir /etc/systemd/system/getty@tty1.service.d
sudo vim /etc/systemd/system/getty@tty1.service.d/autologin.conf
```
make this file look like this (replace simon with your user)
```
[Service]
ExecStart=
ExecStart=-/usr/bin/agetty --skip-login --nonewline --noissue --autologin simon --noclear %I $TERM
```
remove fsck messages
```
sudo vim /etc/mkinitcpio.conf
```
make the line that starts with HOOKS look like this
```
HOOKS=(base systemd autodetect modconf block filesystems keyboard fsck)
```
regenerate initramfs
```
sudo mkinitcpio -P
```