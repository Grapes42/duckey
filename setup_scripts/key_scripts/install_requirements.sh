if [ "$EUID" -ne 0 ]; then
	echo "Please run this program as root by typing \"sudo ./install_requirements.sh\""
	exit
else
    apt update
    apt install python3 python3-pip
    pip install rsa pysftp
fi
