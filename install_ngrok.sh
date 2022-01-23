termux-setup-storage
pkg update -y
pkg upgrade -y
apt update && apt upgrade -y
pkg install python -y
pip install pyfiglet
clear
python .logo.py
echo "Put the activation code you got from the site 👇"
read url
cd /sdcard/Download
mv ngrok-stable-linux-arm.tgz $HOME
cd
tar zxvf ngrok-stable-linux-arm.tgz
rm -rf ngrok-stable-linux-arm.tgz
clear
python .logo.py
$url
./ngrok tcp 4444