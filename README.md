# Duckey 

![](images/logo_transparent_small.png)

A project designed to make a secure USB password key.

Duckey is a device you plug into your computer or phone when you want to enter a password. It name comes from a cross between a USB Rubber Ducky (which is a USB sized device for injecting keystrokes) and a key.

You plug Duckey in just like a key, then it will type in the appropriate password for you.

## Functions
- Get and enter password
- Add password
- Generate new keys
- Backup passwords
- Rollback to old ID
- Merge IDs

(IDs are what attributes a password to a user, only a user with the ID of a password is able to use it.)

## Software
Duckey will borrow the internet connection from host device it is connected to, it will then connect to the server, retrieve the appropriate RSA encrypted password, decrypt it locally, and enter the keystrokes of the password for you. 

This way, there is no need to install any program on the host, which means it would be useful in cases where you need to sign in on a friends computer, or other.

## Hardware
Duckey currently runs on a Raspberry Pi Zero with a custom PCB, in the future I would like to design a more specialised device to decrease price.

It features 3 buttons: up, down and select, to navigate the menu on its LCD display, which will allow you to intuitively use 
 
