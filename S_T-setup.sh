#this is the installer of the needed packages
#S_T-setup v1
#!/bin/bash
#colors
red="\e[0;91m"
blue="\e[0;94m"
expand_bg="\e[K"
blue_bg="\e[0;104m${expand_bg}"
red_bg="\e[0;101m${expand_bg}"
green_bg="\e[0;102m${expand_bg}"
green="\e[0;92m"
white="\e[0;97m"
bold="\e[1m"
uline="\e[4m"
reset="\e[0m"
#the installation
printf"$blue[$green + $blue] $green updating and ugrading"
sudo apt-get update && apt-get upgrade > cache/intall.txt
printf"$blue[$green + $blue] $green installing python3"
sudo apt-get install python3 -y > cache/intall.txt
printf"$blue[$green + $blue] $green installing ssh"
sudo apt-get install ssh -y > cache/intall.txt
printf"$blue[$green + $blue] $green installing modules"
sudo pip3 install -r requerements.txt > cache/intall.txt
printf"$blue[$green + $blue] $green installing ngrok"
sudo curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.zip > cache/install.txt
sudo install unzip -y > cache/install.txt
sudo unzip ngrok-stable-linux-arm64.zip > cache/install.txt
printf"$green Done"