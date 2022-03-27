# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 12:56:17 2021

@author: Jothy Natarajan
"""

from statistics import mean
print("\n************************************************************")
print("\n ANNA UNIVERSITY-2017 Regulation")
print("\n GPA and CGPA calculator for COMPUTER SCIENCE AND ENGG.")
print("\n************************************************************")
print("1.CGPA CALCULATOR")
print("2.GPA CALCULATOR")
print("\n************************************************************")
ch=int(input("ENTER YOUR CHOICE= "))
grade={'O':10,'A+':9,'A':8,'B+':7,'B':6,'U':0}
if(ch==1):
    sem=int(input("Enter number of Semesters = "))
    listA=[]
    for i in range(0,sem,1):
        gpa=float(input("GPA for Semester %s =" %str(i+1)))
        listA.append(gpa)
    print("\nYour CGPA upto",i+1,"Semester  =",mean(listA))
if(ch==2):
    print("1.Semester 1\n2.Semester 2\n3.Semester 3\n4.Semester 4\n5.Semester 5\n6.Semester 6\n7.Semester 7\n8.Semester 8")
    ch1=int(input("choose a Semester="))
    if(ch1==1):
        s1=input("ENGINEERING MATHEMATICS I=")
        s2=input("ENGINEERING PHYSICS=")
        s3=input("ENGINEERING CHEMISTRY=")
        s4=input("PYTHON PROGRAMMING=")
        s5=input("ENGINEERING GRAPHICS=")
        s6=input("COMMUNICATIVE ENGLISH=")
        s7=input("PHYSICS & CHEMISTRY LAB=")
        s8=input("PYTHON PROGRAMMUNG LAB=")
        gpa1=((4*grade[s1])+(3*grade[s2])+(3*grade[s3])+(3*grade[s4])+(4*grade[s5])
     +(4*grade[s6])+(2*grade[s7])+(2*grade[s8]))/25 
        print("\nYour GPA for sem 1=",gpa1)
        print("-------------------------------------------")
    if(ch1==2):
        s21=input("TECHNICAL ENGLISH=")
        s22=input("ENGINEERING MATHEMATICS II=")
        s23=input("PHYSICS FOR INFORMATION=")
        s24=input("ENVIRONMENTAL STUDIES=")
        s25=input(" BASIC ELECTRICAL AND ELECTRONICS=")
        s26= input("PROGRAMMING IN C=")
        s27= input("C LABORATORY=")
        s28= input("ENGINEERING PRACTICES LAB=")
        gpa2=((4*grade[s21])+(4*grade[s22])+(3*grade[s23])+(3*grade[s24])
        +(3*grade[s25])+(3*grade[s26])+(2*grade[s27])+(2*grade[s28]))/24
        print("\nYour GPA for Semester =",gpa2)
        print("-------------------------------------------")
    if(ch1==3):
        s31=input("Discrete Mathematics - MA8351=")
        s32=input("Digital Principles & System Design - CS8351=")
        s33=input("Data Structures - CS8391=")
        s34=input("Object Oriented Programming - CS8392=")
        s35=input("Communication Engineering - EC8395=")
        s36= input("Data Structures Lab - CS8381=")
        s37= input("Object Oriented programming Lab - CS8383=")
        s38= input("Digital Systems Lab - CS8382=")
        s39= input("Interpersonal Skills Listening &Speaking - HS8381=")
        gpa3=((4*grade[s31])+(4*grade[s32])+(3*grade[s33])+(3*grade[s34])
        +(3*grade[s35])+(2*grade[s36])+(2*grade[s37])+(2*grade[s38])+(1*grade[s39]))/24
        print("\nYour GPA for Semester =",gpa3)
        print("-------------------------------------------")
    if(ch1==5):
        s51=input("Algebra & Number theory - MA8551=")
        s52=input("Computer Networks - CS8591=")
        s53=input("Microprocessors and Microcontrollers - EC8691=")
        s54=input("Theory of Computation - CS8501=")
        s55=input("Object Oriented Analysis & Design - CS8592=")
        s56= input("Product Design and Development - OMF551=")
        s57= input("Microprocessors and Microcontrollers Lab - EC8681=")
        s58= input("Object Oriented Analysis & Design Lab - CS8582=")
        s59= input("Networks Lab - CS8581=")
        gpa5=((4*grade[s51])+(3*grade[s52])+(3*grade[s53])+(3*grade[s54])
        +(3*grade[s55])+(3*grade[s56])+(2*grade[s57])+(2*grade[s58])+(2*grade[s59]))/25
        print("\nYour GPA for Semester =",gpa5)
        print("-------------------------------------------")
    if(ch1==6):
        s61=input("Internet Programming - CS8651=")
        s62=input("Artificial Intelligence - CS8691=")
        s63=input("Mobile Computing - CS8601=")
        s64=input("Compiler Design - CS8602=")
        s65=input(" Distributed Systems - CS8603=")
        s66= input("Software Testing - IT8076 =")
        s67= input("Internet Programming Lab - CS8661=")
        s68= input("Mobile Application Development Lab - CS8662=")
        s69= input("Mini Project - CS8611=")
        s60= input(" Professional Communication - HS8581=")
        gpa6=((3*grade[s61])+(3*grade[s62])+(3*grade[s63])+(4*grade[s64])
        +(3*grade[s65])+(3*grade[s66])+(2*grade[s67])+(2*grade[s68])+(1*grade[s69])+(1*grade[s60]))/24
        print("\nYour GPA for Semester =",gpa6)
        print("-------------------------------------------")
    if(ch1==7):
        s71=input("Principles of Management - MG8591=")
        s72=input("Cryptography & Network Security - CS8792=")
        s73=input("Cloud Computing - CS8791=")
        s74=input("Open Elective II=")
        s75=input(" Professional Elective II=")
        s76= input(" Professional Elective III =")
        s77= input("Cloud Computing Lab - CS8711+")
        s78= input("Security Lab - IT8761+")
        gpa7=((3*grade[s71])+(3*grade[s72])+(3*grade[s73])+(3*grade[s74])
        +(3*grade[s75])+(3*grade[s76])+(2*grade[s77])+(2*grade[s78]))/22
        print("\nYour GPA for Semester =",gpa7)
        print("-------------------------------------------")
    if(ch1==8):
        s81=input("Professional Elective IV - CS6801=")
        s82=input(" Professional Elective V =")
        s83=input("Project Work - CS8811=")
        gpa8=((3*grade[s71])+(3*grade[s72])+(10*grade[s73]))/16
        print("\nYour GPA for Semester =",gpa8)
        print("-------------------------------------------")
        
        
   