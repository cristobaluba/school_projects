#! /usr/bin/env python
# -*- coding: utf8 -*-

import os

def check1(file):
    try : p = open("eredmeny.txt", "r")
    except : 
        print "Nem volt eredmeny.txt!\n"
        return 0
    else:
        f = open(file, "r")
        pline = p.readline()
        fline = f.readline()
        while fline :
            if not(fline.isspace() or pline.split() == fline.split()) :
                p.close()
                f.close()
                return 1
            pline = p.readline()
            fline = f.readline()
        while pline.isspace() : pline = p.readline();    
        if pline :
            p.close()
            f.close() 
            return 1    
        p.close()
        f.close()
        return 2


def checkFile(str):
    try : p = open("tmpkk.txt", "r")
    except: return False
    else:
        pline = p.readline()
        while pline.isspace() : pline = p.readline();
        if pline :
            if pline.strip() == str : 
                p.close()
                return True
        p.close()    
        return False

try :      
   f=open("bead1.py", 'r')
except IOError: print "Nincs bead1.py file!\n"
else:
   f.close()
   
   i = 1
   os.system("python bead1.py kakukkkk > tmpkk.txt")
   if not checkFile("Nincs ilyen file!"): 
      print "Rossz hibakezelés nem létező adatfájl esetén!\n"
      i = 0

   os.system("python bead1.py > tmpkk.txt")
   if not checkFile("Nincs argumentum!"): 
      print "Rossz hibakezelés hiányzó argumentum esetén!\n"
      i = 0
   
   if i :
      try: 
         f = open("adatok2.txt", 'r')
      except IOError: print "Nincs adatok2.txt file!\n"
      else:
         os.system("python bead1.py adatok2.txt")
         l = check1("eredmeny2.txt")
         if l==2 : print "Jó eredmény!\n"
         elif l == 1: print "Hibás eredmény!\n"    

