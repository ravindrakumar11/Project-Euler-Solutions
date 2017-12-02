#MIT License
#Copyright (c) 2017 Ravindra Kumar

#This one look cool to me!
def answer0003():
    ans, div  = 600851475143, 1
    while(div < ans**(1/2.0)):
        if ans % div == 0:
            ans /= div
        div += 1	
    return ans

if __name__ == "__main__":
	print answer0003() 
