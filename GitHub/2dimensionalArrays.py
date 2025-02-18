import matplotlib.pyplot as plt
import numpy as np

#Problem 1
x = np.arange(-50, 50.1, 0.1)
y = ((1/2)*x)+1

# Print first 10 values as an example
print("First 10 values of x:", x[:10])
print("First 10 values of y:", y[:10])

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("f(x)= (1/2)x + 1")
plt.legend()
plt.grid()
plt.show()

#Problem 2
x_array=[]
y_array=[]

value=-50
while value<=50:
    x_array.append(value)
    y_value=((1/2)*value)+1
    y_array.append(y_value)
    value=value+0.1

#reshape
x_array=np.array(x_array).reshape(-1,1)
y_array=np.array(y_array).reshape(-1,1)

concatenate=np.concatenate((x_array,y_array), axis=1)
print(concatenate[:20])

#Problem 3
x_changes = np.diff(x_array.flatten())  
y_changes = np.diff(y_array.flatten())

print("X changes:", x_changes[:10])  
print("Y changes:", y_changes[:10])  

gradient=y_changes/x_changes
print("Gradiente", gradient[:10])


#problem 4
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("f(x)= (1/2)x + 1")
plt.legend()
plt.grid()
plt.show()


plt.plot(x[:-2],gradient)
#x and y must have same first dimension, but "
#ValueError: x and y must have same first dimension, but have shapes (1001,) and (999,) which is why i subtracted it
plt.xlabel("x")
plt.ylabel("gradient")
plt.title("Gradient")
plt.legend()
plt.grid()
plt.show()

#Question 5
# Function to compute function values and gradients
def compute_function_and_gradient(func, x_range=(-50, 50.1, 0.1)):
    x_values = np.arange(*x_range) 
    y_values = func(x_values)       
    
    # Compute gradient using np.diff()
    delta_y = np.diff(y_values)
    delta_x = np.diff(x_values)
    gradient = delta_y / delta_x  # Numerical differentiation
    
    return x_values, y_values, gradient

# dieferente functions
def function1(x):  
    return x**2  # f1(x) = x²

def function2(x):  
    return 2*x**2 + 2*x  # f2(x) = 2x² + 2x

def function3(x):  
    return np.sin(np.sqrt(x))  # f3(x) = sin(sqrt(x))

# Compute results for each function
x1, y1, grad1 = compute_function_and_gradient(function1)
x2, y2, grad2 = compute_function_and_gradient(function2)
x3, y3, grad3 = compute_function_and_gradient(function3, x_range=(0, 50.1, 0.1))  # f3 is only for x >= 0 so we dont get imaginary numbers like 2i

# Plot the functions
plt.figure(figsize=(10, 5))
plt.plot(x1, y1, label="f(x) = x²")
plt.plot(x2, y2, label="f(x) = 2x² + 2x")
plt.plot(x3, y3, label="f(x) = sin(Vx)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function Plots")
plt.legend()
plt.grid()
plt.show()

# Plot the gradients
plt.figure(figsize=(10, 5))
plt.plot(x1[:-1], grad1, label="Gradient of x²")
plt.plot(x2[:-1], grad2, label="Gradient of 2x² + 2x")
plt.plot(x3[:-1], grad3, label="Gradient of sin(Vx)")
plt.xlabel("x")
plt.ylabel("Gradient")
plt.title("Gradient Plots")
plt.legend()
plt.grid()
plt.show()

#Problem 6
min_y1, min_idx1 = np.min(y1), np.argmin(y1)
min_y2, min_idx2 = np.min(y2), np.argmin(y2)
min_y3, min_idx3 = np.min(y3), np.argmin(y3)

#gradients before and after min
grad_before_1 = grad1[min_idx1 - 1] if min_idx1 > 0 else None
grad_after_1 = grad1[min_idx1] if min_idx1 < len(grad1) else None

grad_before_2 = grad2[min_idx2 - 1] if min_idx2 > 0 else None
grad_after_2 = grad2[min_idx2] if min_idx2 < len(grad2) else None

grad_before_3 = grad3[min_idx3 - 1] if min_idx3 > 0 else None
grad_after_3 = grad3[min_idx3] if min_idx3 < len(grad3) else None


print(f"Function 1 (x²): Minimum y = {min_y1} at x = {x1[min_idx1]}")
print(f"Gradient before: {grad_before_1}, Gradient after: {grad_after_1}\n")

print(f"Function 2 (2x² + 2x): Minimum y = {min_y2} at x = {x2[min_idx2]}")
print(f"Gradient before: {grad_before_2}, Gradient after: {grad_after_2}\n")

print(f"Function 3 (sin(Vx)): Minimum y = {min_y3} at x = {x3[min_idx3]}")
print(f"Gradient before: {grad_before_3}, Gradient after: {grad_after_3}\n")

# Plot the functions
plt.figure(figsize=(10, 5))
plt.plot(x1, y1, label="f(x) = x²")
plt.plot(x2, y2, label="f(x) = 2x² + 2x")
plt.plot(x3, y3, label="f(x) = sin(Vx)")
plt.scatter(x1[min_idx1], min_y1, color='red', label="min of x²")
plt.scatter(x2[min_idx2], min_y2, color='blue', label="min of 2x² + 2x")
plt.scatter(x3[min_idx3], min_y3, color='green', label="min of sin(Vx)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function Plots with minimum Points")
plt.legend()
plt.grid()
plt.show()
