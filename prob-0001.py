#MIT License
#Copyright (c) 2017 Ravindra Kumar

#Starting it after a longtime and seems like mathematical genes are not activated yet. The problem 
#deserves better mathematical solution!   
def answer0001():
    ans  = 1000*(1000-1)/2
    for i in range(1000):
        if ((i+1)%3 != 0) & ((i+1)%5 !=0) :
            ans -= (i+1)
    return ans

if __name__== "__main__":
    print answer0001()
