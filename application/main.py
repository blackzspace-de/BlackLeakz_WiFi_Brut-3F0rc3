import os   
import sys 
import subprocess
import platform as p
import logging
import re 
import shlex
import cmd
import colorama


from colorama import Fore, Back

from subprocess import PIPE, Popen, STDOUT

from os.path import *
from pathlib import *



from cmd import Cmd










################################################################  KONSTANTEN WIE DIE PLANK-KONSTANTE ###############################################################


psk_known1 = "hailey"   # ZU 25%* die ersten 6 bestandteile des WPA2-PSKeys !
psk_known1_big = "Hailey" # Zu 25%* 

psk_known2 = "harley" # zu 25%*
psk_known2 = "Harley" # zu 25%*



psk_addnr1 = 80

psk_add0 = 0

psk_addnr2 = 20

psk_addnr3 = 60


psk_known1 + psk_addnr1 + psk_add0 + psk_addnr3
psk_known1 + psk_addnr1 + psk_add0 + psk_add0 + psk_addnr3
psk_known1 + psk_addnr1 + psk_add0 + psk_add0 + psk_addnr3 + psk_add0
psk_known1 + psk_addnr1 + psk_add0 + psk_add0 + psk_addnr3 + psk_add0 + psk_add0

psk_known1 + psk_addnr1 + psk_add0 + psk_addnr3 + psk_add0 + psk_add0


psk_known1 + psk_addnr1 + psk_add0 + psk_addnr3 + psk_add0
psk_known1 + psk_addnr1 + psk_add0 + psk_addnr3 + psk_add0 + psk_add0





###################################################################################################################################################################










### Init App... Creating enviroment !


print(Fore.LIGHTCYAN_EX + Back.BLACK + "blackz-brute > " + Fore.RESET + Back.RESET + "Creating application enviroment! (Folders & Logs)")



# create .logs folder
if os.path.isdir(".logs"):
    print("blackz-brute > .logs directory exists!")
    logging.debug("blackz-brute > .logs directory exists!")
else:
    os.mkdir(".logs")
    
    
# create .profiles folder
if os.path.isdir(".profiles"):
    print("blackz-brute > .profiles directory exists!")
    logging.debug("blackz-brute > .profiles directory exists!")
else:
    os.mkdir(".profiles")








os.chdir(".logs")



logging.basicConfig(filemode="w", filename="blackzbrute.log", level="DEBUG")









class Main(cmd.Cmd):
    """ This is the commadlines main-class"""
    
    
    
    prompt = "bru1e<3f0rc3 >> "
    
    
    
    
    
    def do_run(self, line):
        print("Starting whole attk.")
        
        
    
    
    def do_get(self, line):
        self.get_ssid()
       
        
    
    def do_read(self, line):
        logging.info("Reading following files: ")
        with open("log.log", "r") as f:
            vars = f.readlines()
            f.close()
            for readline in vars:
                print(readline)        
        
        
        
        
    
    def get_ssid(self):
        print("Scanning networks ! ... .. .")
        print("Logs can be found in main-log file & \n      \r in single-function logfiles in folder: '.logs'")
        self.exec(command_line="", argx="netsh wlan show networks")
        target_network = input("SSID: ")
        self.exec(command_line="", argx=f"netsh wlan connect name={target_network}")
        
    
 
 
            
        
                
    def exec(self, command_line, argx):
        command_line_args = shlex.split(argx)
        process = subprocess.Popen(command_line_args, shell=True, stdout=PIPE, stderr=STDOUT)
        with process.stdout:
            for line in iter(process.stdout.readline, b''):
                logging.debug(line.decode("latin1").strip())
                logging.debug(command_line + '"')
        try:
                command_line_process = subprocess.Popen(
                command_line_args,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            # process_output, _ =  command_line_process.communicate()
            # self.log_subprocess_output(process_output)
        except (OSError, subprocess.CalledProcessError) as exception:
            logging.debug('Exception occured: ' + str(exception))
            logging.debug('Subprocess failed')
            return False
        else:
            logging.debug('Subprocess finished')
            return True
                
            





    
    
def loop():
    try:
        Main().cmdloop()
    except KeyboardInterrupt:
        print("Exiting")
        sys.exit()
        
        
        
        
        
        
if __name__ == '__main__':
    loop()