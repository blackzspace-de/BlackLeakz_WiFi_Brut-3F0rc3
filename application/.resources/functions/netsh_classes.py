import os
import sys
import subprocess 



class Connect:
    def connect():
        print("Blackz-Brut3 > ")
        
        os.system("netsh wlan show networks")
        print("Blackz-Brut3 > Enter SSID to connect to:")
        connect_to = input("SSID: ")
        os.system(f"netsh wlan connect name={connect_to}")
        
        
        



class AddProfile:
    def add():
        print("Console > Adding Profile")
        
    def delete():
        print("Console > Deleting profile")