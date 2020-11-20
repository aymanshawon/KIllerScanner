'''
Author : Luci madmax

KillerScanner is a PortScanner .. 
KillerScanner can scan 65k ports in few seconds
'''
from os         import system     as __sys__
from os         import getuid     as __uid__
from os         import cpu_count  as __cpuc__
from sys        import platform   as __osname__
from re         import findall    as __find__
from time       import time       as __time__
from time       import sleep      as __sleep__
from threading  import Thread     as __thread__
from subprocess import check_output as __check__
from pwd        import getpwuid
from colorama   import init
from socket     import AF_INET , SOCK_STREAM ,socket
from optparse   import OptionParser
init()
CG,CY,CC,CW,CR,RR,GR = '\033[32;1m','\033[33;1m','\033[36;1m','\033[37;1m','\033[31;1m','\033[00;1m','\033[30;1m'

def Banner():
    print(f"""{CR}
       ╦╔═┬┬  ┬  ┌─┐┬─┐╔═╗┌─┐┌─┐┌┐┌┌─┐┬─┐
       ╠╩╗││  │  ├┤ ├┬┘╚═╗│  ├─┤│││├┤ ├┬┘
       ╩ ╩┴┴─┘┴─┘└─┘┴└─╚═╝└─┘┴ ┴┘└┘└─┘┴└─{CW}
({CC} LUC1 M4DM4X {CW},{CC} KN0T CH7P3R {CW},{CC} M_Duff7 {CW},{CC} Ly_C0d3R{CW} )
                  [ {CG}L7!MC{CW} ] 
""")

class Scan:
    def __init__(self,ip_address='',Range=65000,Delay=''):
        self.__ip    = ip_address
        self.__range = int(Range)
        self.__delay = self.cpu() if Delay=='' else float(Delay)
        if self.__check():
            self.__finaly()

    def cpu(self):
        self.__cup = __cpuc__()
        if self.__cup == 2:
            return 0.0001
        elif 2 < self.__cup < 6:
            return 0.00001
        elif 4 < self.__cup <= 8:
            return 0.00000011

    def __check(self):
        try:
            self.__check_ip  = __find__(r"(.\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})",self.__ip)
            if self.__check_ip:
                if __osname__ not in ['nt','win32','win','dos','xp']:
                    self.__output = __check__(['ping','-c','1',self.__ip]).decode()
                    self.__output = __find__(r"64 bytes from \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}: icmp_seq=\d{1,4} ttl=\d{1,4}", self.__output)
                    if self.__output:
                        return True
                else:
                    self.__output = __check__(['ping','-n','1',self.__ip],shell=True).decode()
                    self.__output = __find__(r'Reply from \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}: bytes=\d{1,3} time<\d{1,4}ms TTL=\d{1,4}',self.__output)
                    if self.__output:
                        return True
            else:
                print(f"\n{CW}*{CR} Invalid IP address {CY}Mr.Hoker !")
                exit()
        except:
            print(f"\n{CW}*{CR} Death IP Address\n")
            exit()

    def __Scan(self,port):
        text = "Port is Open"
        try:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect((self.__ip,port))
            sock.close()
            if len(str(port)) == 2:
                text = "\bPort is Open"
            elif len(str(port)) == 3:
                text = "\b\bPort is Open"
            elif len(str(port)) == 4:
                text = "\b\b\bPort is Open"
            elif len(str(port)) == 5:
                text = "\b\b\b\bPort is Open"
            print(f"{CY}........................")
            print(f"{CW}|{CG} {port}      {CW}{text}  |")
            print(f"{CY}........................")
        except:
            print(f'{CW} * {CR}{port}',end='\r')

    def __finaly(self):
        try:
            Count_time = __time__()
            print(f"\n{CW}*{CG} Starting.......")
            print(f"{CW}*{CG} Your Target IP:{CY} {self.__ip}")
            for key in range(self.__range+1):
                Thread1 = __thread__(target=self.__Scan, args=(key,))
                Thread1.daemon = True
                Thread1.start()
                __sleep__(self.__delay)
            print(f"{CW}*{CY} {int(__time__() - Count_time)} secound"+8*' ')
            print(f"{CW}*{CG} Finish.......")
        except:
            print(f"{CW}*{CR} Stoped......."+4*' ')

def main():
    parser = OptionParser()
    parser.add_option('-i',type='str',  dest='ip_add',  help="IP address for scaning...")
    parser.add_option('-r',type='int',  dest='range',   help="Port range for scaning...")
    parser.add_option('-d',type='float',dest='delay',   help="Time delay for scaning...")
    args=parser.parse_args()[0]
    if args.ip_add:
        Banner()
        if args.range == None and args.delay == None:
            Scan(ip_address=args.ip_add)
        elif args.delay == None:
            Scan(ip_address=args.ip_add,Range=args.range)
        elif args.range == None:
            Scan(ip_address=args.ip_add,Delay=args.delay)
        else:
            Scan(ip_address=args.ip_add,Range=args.range,Delay=args.delay)
    else:
        __sys__('clear||cls')
        Banner()
        _login_ = getpwuid(__uid__())[0]
        try:
            print(f"{CG}┌──({CY}{_login_}{CC}@{CR}DadyScanner{CG})-[{CW}IP{CG}]\n└─{CW}$ ",end='')
            ip = input()
            if ip:
                try:
                    print(f"{CG}┌──({CY}{_login_}{CC}@{CR}DadyScanner{CG})-[{CW}Range{CG}]\n└─{CW}$ ",end='')
                    Range = input()
                    print(f"{CG}┌──({CY}{_login_}{CC}@{CR}DadyScanner{CG})-[{CW}Delay{CG}]\n└─{CW}$ ",end='')
                    delay = input()
                    if delay.strip() == '' and Range.strip() == '':
                        Scan(ip_address=ip)
                    elif delay.strip() == '' and int(Range) >= 0:
                        Scan(ip_address=ip,Range=Range)
                    elif Range.strip() == '':
                        Scan(ip_address=ip,Delay=delay)
                    elif float(delay) >= 0 <= int(Range):
                        Scan(ip_address=ip,Range=Range,Delay=delay)
                    else:
                        print(f"{CR}[-] Worng Value !\n")
                except:
                    print(f"\n{CW}* {CR}Plz Enter Number and Float Number !\n{RR}")
            else:
                print(f"\n{CW}*{CR} Invalid input !\n{RR}")
        except:
            pass
        input("\nEnter  To Exit ")
        print('\n')

if __name__ == "__main__":
    main()