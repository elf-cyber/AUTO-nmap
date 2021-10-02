########################
#Creator : @e_l_f_6_6_6#
########################

import os
import time
from colorama import Fore ,  Back ,Style 
print(Fore.BLACK+Back.WHITE+'''
┌─┐┬  ┌─┐  ┌─┐┌─┐┌─┐┬ ┬┬─┐┬┌┬┐┬ ┬   ┌─┐┬ ┬┌┐ ┌─┐┬─┐
├┤ │  ├┤   └─┐├┤ │  │ │├┬┘│ │ └┬┘   │  └┬┘├┴┐├┤ ├┬┘
└─┘┴─┘└────└─┘└─┘└─┘└─┘┴└─┴ ┴  ┴────└─┘ ┴ └─┘└─┘┴└─


''')
print("my channel : @elf_security_cyber")

if os.name == 'nt':
    print(f'{Fore.RED+Back.BLACK}[{Fore.YELLOW+Back.BLACK}+{Fore.RED+Back.BLACK}]{Fore.GREEN+Style.DIM} no windows!')
    
else:
    os.system('pkg install nmap')
    os.system('pkg install nmap')
    
result = input(f'{Fore.RED}[{Fore.YELLOW}+{Fore.RED}]{Fore.GREEN+Style.BRIGHT}enter the ip: ')
    

res = 'nmap -F '
res2 = 'nmap -v '
res3 = 'nmap -V '
res4 = 'nmap -r '

output = res+result
output2 = res2+result
output3 = res3+result
output4 = res4+result


a = os.system(output)

printed = f'''{Fore.RED}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$${Fore.YELLOW}%{Fore.GREEN+Style.BRIGHT}ELF_666{Fore.YELLOW}%{Fore.RED}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''
time.sleep(3)

b = os.system(output2)


print(printed)
time.sleep(3)

c = os.system(output3)

print(printed)
time.sleep(3)
    
d = os.system(output4)

while True:
    os.chdir("/sdcard")
    f = open("look_at_me.txt","w+")
    c = 50
    for i in range(c):
        f.write("[-]thank you for follow me "+printed+" \n\nmy channel telgram:@elf_security_cyber "+printed+"\n\n pelese sub me!")
        f.close()
    if c == 50:
        break

if os.name =='nt':
    print("channel : @elf_security_cyber")
else:    

    os.system('termux-open-url https://t.me/elf_security_cyber')