import time
import matplotlib.pyplot as plt

#How i would resolve it 
paper_thick=0.00008
folds=0

print('insert the amount of folds')
folds=int(input())#input 43 times for the problem

hight= paper_thick *(2**folds)

print('The hight the paper would reach is {} meters'.format(hight))

#problem 1
thickness= 0.00008
folded_thickness= thickness * (2**43)

print('thickness {:.3f} meters'.format(folded_thickness))
#convertions
print('thickness {:.2f} kilometers'.format(folded_thickness/1000))

#Using for statement
Moon_distance=384400

for i in range(50):
    paper_hight=thickness* (2**i)
    if(paper_hight/1000>Moon_distance):
        print('the paper was folded {} times to reach the moon'.format(i))
        break

#Comparison Calculation
start=time.time()

for i in range(100):
    paper_hight=thickness* (2**i)
    if(paper_hight/1000>Moon_distance):
        print('the paper was folded {} times to reach the moon'.format(i))
        break

elapsed_time = time.time() - start
print('Time : {:.5f}[s]'.format(elapsed_time))

#Graph visualization
paper_thickness=0.00008
thickness_list=[]
for i in range(44):
    reach=paper_thickness* (2**i)
    thickness_list.append(reach)

print(f'The values in the list have a lenght of: {len(thickness_list)}')

plt.title('thickness of paper')
plt.xlabel('number of folds')
plt.ylabel('thickness [m]')
plt.plot(thickness_list)
plt.show()

#customizing the graph
plt.title('thickness of paper')
plt.xlabel('number of folds')
plt.ylabel('thickness [m]')
plt.plot(thickness_list,marker='o',color='red')
plt.show()

plt.title('thickness of paper')
plt.xlabel('number of folds')
plt.ylabel('thickness [m]')
plt.tick_params(labelsize=20)
plt.plot(thickness_list)
plt.show()