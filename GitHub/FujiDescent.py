import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Problem 1
csv_path =r"C:\Users\HUAWEI\Downloads\mtfuji_data.csv"

np.set_printoptions(suppress=True) 
fuji = np.loadtxt(csv_path, delimiter=",", skiprows=1)

print(fuji[130:140])

df = pd.read_csv(csv_path) # i didn't undertsand how to source from numpy so i used pandas
x=df["x"]
elevation=df["elevation"]

plt.plot(x,elevation)
plt.xlabel("Position")
plt.ylabel("Elevation [m]")
plt.title("Mt. Fuji")
plt.grid()
plt.show()

#Problem 2
def slope(fuji, specific_point):
    specifiedpoint_location=fuji[specific_point,:]
    past_specifiedpoint_location=fuji[specific_point-1,:]
    d_x=past_specifiedpoint_location[0]-specifiedpoint_location[0]
    d_y=past_specifiedpoint_location[3]-specifiedpoint_location[3]
    gradient=d_y/d_x
    return gradient
print(slope(fuji,136)) 

def gradient_slope_all(fuji):
    d_x=np.gradient(fuji[:,0])
    d_y=np.gradient(fuji[:,3])
    gradient=d_y/d_x
    return gradient

#Problem 3
def destination_point(fuji,current_position,alpha=0.2):
    destination_point=fuji    
    if alpha>0:
        destination_point=fuji[current_position,0]-alpha*slope(fuji,current_position)
    else:
        return "Error, alpha not greater than 0"
    return np.round(destination_point).astype(int)
print("The next point to move to based on the information on the slope of the current point is: ",destination_point(fuji,136))


#Problem 4 testing
def descend_mountain(position,fuji):
    dest_point = destination_point(fuji,position)
    dest_point_list = [position]
    for i in range(position):
        current_point = dest_point 
        dest_point_list.append(dest_point)
        dest_point = destination_point(fuji,current_point)
        
        if current_point == dest_point:
            break
    return dest_point_list
path = descend_mountain(136,fuji)
path

#Problem 5
fuji_elevations = fuji[:, 3]
descended_elevations = fuji_elevations[path]
plt.title("mt. fuji")
plt.xlabel("position")
plt.ylabel("Elevation [m]")
plt.plot(fuji_elevations)
plt.scatter(path, descended_elevations, 20, color = "red")
plt.show()

plt.plot(path,fuji[path,3],color='red')
plt.title("mt. fuji")
plt.xlabel("number of iterations")
plt.ylabel("Elevation [m]")
plt.show()     

#Problem 6
descend_mountain(200,fuji)

#Problem 7
def descend_mountain(position,fuji):
    dest_point = destination_point(fuji,position) 
    dest_point_list = [position]
    for i in range(position):
        current_point = dest_point 
        dest_point_list.append(dest_point) 
        dest_point = destination_point(fuji,current_point)
        
        if current_point == dest_point:
            break
    
    plt.title("mt. fuji")
    plt.xlabel("position")
    plt.ylabel("Elevation [m]")
    plt.plot(fuji_elevations)
    plt.scatter(dest_point_list, fuji[dest_point_list,3], 20, color = "red")
    plt.show()
descend_mountain(142,fuji)

#Problem 8
def descend_mountain(position,fuji):
    dest_point = destination_point(fuji,position,0.5) 
    dest_point_list = [position]
    for i in range(position):
        current_point = dest_point 
        dest_point_list.append(dest_point) 
        dest_point = destination_point(fuji,current_point)
        
        if current_point == dest_point:
            break
    
    plt.title("mt. fuji")
    plt.xlabel("position")
    plt.ylabel("Elevation [m]")
    plt.plot(fuji_elevations)
    plt.scatter(dest_point_list, fuji[dest_point_list,3], 20, color = "red")
    plt.show()
descend_mountain(142,fuji)

# initialize destination point
# equate current point to destination point
# create a list of destination points