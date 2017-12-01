#MIT License
#Copyright (c) 2017 Ravindra Kumar

#I took help of the loop but there might be a better solution, not sure though.    
def answer0002():
    a1, a2 = 1, 2
    num = [2]
    while(a2 < 4000000):
	temp = a1+a2
	a1 = a2
	a2 = temp
	if a2 % 2 == 0:
	   num.append(a2)
    return sum(num)

if __name__== "__main__":
    print answer0002()
