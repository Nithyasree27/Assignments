# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 14:58:07 2021

@author: Jothy Natarajan
"""

import statistics as s
num1=float(input("Enter MEAN ="))
num2=float(input("Enter STANDARD DEVIATION="))
nd=s.NormalDist(mu=num1,sigma=num2)
con=1
while(con==1):
    print("\n1.Probability lesser than or equal\n2.Probability greater than or equal \n3.Probability between 2 ranges \n4.Probability of particular value")
    ch=int(input("Enter your choice ="))
    if(ch==1):
        val1=float(input("Enter the value="))
        n=nd.cdf(val1)
        print("Probability greater than or equal to",val1,"is =",n)
        print("Probability in % =",n*100)
    if(ch==2):
        val1=float(input("Enter the value="))
        n=nd.cdf(val1)
        print("Probability greater than or equal to",val1,"is =",1-n)
        print("Probability in % =",(1-n)*100)
    if(ch==3):
        val1=float(input("Enter the first value="))
        val2=float(input("Enter the second value="))
        n=nd.cdf(val2)-nd.cdf(val1)
        print("Probability between",val1,"and ",val2,"is =",n)
        print("Probability in % =",n*100)
    if(ch==4):
        val1=float(input("Enter the value="))
        print("Probability greater than or equal to",val1,"is =0")
        print("Probability in % =0")

    con=int(input("Do you want to continue yes-1/no-0 ="))
    print("-------------------------------------------------------------")
        

