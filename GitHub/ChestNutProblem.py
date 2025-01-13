# Determining the exact volume of the solar system is challenging due to its vast and diffuse boundaries.
# A common method is to consider the region encompassing the Sun and the orbits of its planets.
# trough extensive research and hyphotethical calculations, and theories found across the internet
# the solar system is aproximately 3.82 x 10^44 cm^3
# the volume of a chest nut bun is 523.6 cm^3
import matplotlib.pyplot as plt

solar_system=3.82*(10**44)
chest_nut_bun=523.6
minutes=0
i=0
while(True):
    size_growth=chest_nut_bun*(2**i)
    if(size_growth>=solar_system):
        print('It took {} minutes for the chest nut bun to grow the size of our solar system'.format(minutes))
        break
    minutes+=5
    i+=1

#Tokyo Dome problem
Tokyo_Stadium=float(input('insert tokyos stadium size '))#stadium size is 1.57x10^6 m^3 or 1570796327000.000
ball=float(input('insert the balls size '))#avg size is 5.58x10^-3 m^3  or 5575.280
           # Note that you need to use the same measurments for the best resulta (cm/cm km/km ...etc)
minutes=0
i=0
list_sizes=[]
while(True):
    size_growth=ball*(2**i)
    list_sizes.append(size_growth)
    if(size_growth>=Tokyo_Stadium):
        print('It took {} minutes for the ball to grow the size of the Tokyo Stadium'.format(minutes))
        break
    minutes+=5
    i+=1

#graph for visual representation
plt.title('Size of ball')
plt.xlabel('growth')
plt.ylabel('minutes')
plt.plot(list_sizes)
plt.show()