## Requirements :
1. Windows system
2. Bluetooth adapter and Driver
3. python (version > 3.9)

## NOTE: 
-> You must change the MAC address in the code and set it to your server MAC. Follow the steps to do this:

## Steps to find bluetooth address of your computer.
1. Open cmd
2. type : getmac /v
3. Look for the entry 'Bluetooth', next to it you will find the MAC address.

OR, if commandline scares you enough to make you choose a longer path

1. Go to Search bar located at the bottom on the taskbar and type 'device manager' and press enter
2. In the Devices , locate bluetooth and expand it.
3. Click on the option matches the name of your bluetooth adapter. (eg. intel , amd, realtek or something else)
4. Double click to open settings.
5. Click on 'Advanced' tab and locate the address field. (it looks like - ab:12:ef:45:3e:5t , this is just an example)

## Make the changes
1. in server.py, write your own MAC address at line 4
2. in client.py, write your own MAC address at line 4
   
## How to setup :
1. Download the server.py on the server system
2. Go to the folder where server.py is stored and open terminal
3. type and enter : py server.py
4. Download the client.py on the client system
5. Go to the folder where client.py is stored and open terminal
6. type and enter : py client.py
7. The connection will now be established and you can start texting.
