#MIT License
#Copyright (c) 2017 Ravindra Kumar

#This one look cool to me!
from fractions import gcd 
def answer0005():
    num, lcm  = 20, 1
    while(num):
	lcm = num * lcm / gcd(num, lcm)
    	num -= 1
    return lcm
	
if __name__ == "__main__":
	print answer0005() 
