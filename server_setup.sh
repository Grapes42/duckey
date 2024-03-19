#!/bin/bash

# Script that creates a sftp only group and adds the user pass_man to it

# Check if run as root, else exit
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

groupadd sftponly
useradd -g sftponly -s /bin/false -m -d /home/pass_man pass_man

passwd pass_man

chown root: /home/pass_man
chmod 755 /home/pass_man

mkdir /home/pass_man/passwords
chmod 755 /home/pass_man/passwords
chown pass_man:sftponly /home/pass_man/passwords

cat >> /etc/ssh/sshd_config<< EOF
Subsystem sftp internal-sftp
Match Group sftponly
  ChrootDirectory %h
  ForceCommand internal-sftp
  AllowTcpForwarding no
  X11Forwarding no
EOF

systemctl restart ssh
