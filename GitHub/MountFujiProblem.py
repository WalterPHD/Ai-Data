
paper_thickness=0.00008
Fuji_height=3776
i=0
k=0
j=0
l=0

#Question 1
while(True):
    paper_hight=paper_thickness* (2**i)
    if(paper_hight>=Fuji_height):
        print('the paper was folded {} times to reach or surpass mount fuji, having {:.1f} m'.format(i,paper_hight))
        break
    i+=1

#Problem 2
input_height=float(input("Insert the height you would like to know how many folds it takes: "))
while(True):
    paper_hight=paper_thickness* (2**j)
    if(paper_hight>=input_height):
        print('It took {} folds for the paper to reach {:.1f}m'.format(j,input_height))
        break
    j+=1
#Nearest star 4.0175*(10**16)m Proxima Centauri
Proxima_Centauri=4.0175*(10**16)
while(True):
    paper_hight=paper_thickness* (2**k)
    if(paper_hight>=Proxima_Centauri):
        print('It took {} folds for the paper to reach Proxima Centauri'.format(k))
        break
    k+=1

#Question 3 diffract a beam
#Length=((p*thickness)/6)*(2**n +4)*(2**n -1)
p=3.14
while(True):
    paper_hight1=paper_thickness* (2**l)
    if(paper_hight1>=Fuji_height):
        #print('the paper was folded {} times to reach or surpass mount fuji, having {:.1f} m'.format(l,paper_hight1))
        break
    l+=1
Length=((p*paper_thickness)/6)*(2**l +4)*(2**l -1)
print('The length of paper needed to reach mount fuji is {:.2f}m'.format(Length))


