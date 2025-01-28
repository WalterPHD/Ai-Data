import numpy as np
import matplotlib.pyplot as plt
import time

n_squares = 4
small_board_list = [1]
for _ in range(n_squares - 1):
    small_board_list.append(2*small_board_list[-1])
print("4マスの板に小麦を並べる（リスト）：{}".format(small_board_list))

small_board_ndarray = np.array(small_board_list)
print("4マスの板に小麦を並べる（ndarray）：{}".format(small_board_ndarray))

#Question 1

TwobyTwo=[1]
squares = 4
for i in range(squares-1):
    TwobyTwo.append(2*TwobyTwo[-1])

board_2x2=np.array(TwobyTwo)
new_board_2x2=board_2x2.reshape(2,2)

print(new_board_2x2)

#Problem 2
x=int(input("insert the chessboard rows :"))
y=int(input("insert the chessboard columns :"))

xy_board=[1]
sqquares = x*y
for i in range(sqquares-1):
    xy_board.append(2*xy_board[-1])

board_8x8=np.array(xy_board)
new_board_8x8=board_8x8.reshape(x,y)

print(new_board_8x8)

#Question 3
sum=0
for i in range(len(new_board_8x8)):
    sum=sum+new_board_8x8[i]
print('The total number of grains is {} '.format(sum))

plt.xlabel("column")
plt.ylabel("number")
plt.title("quantity in each column")
plt.bar(np.arange(board_8x8.size), board_8x8)
plt.show()

#Question 4
#heatmap
plt.xlabel("column")
plt.ylabel("number")
plt.title("heatmap")
plt.pcolor(np.array(board_8x8).reshape(x, y))
plt.show()

#Question 5
#number os grains in the 2nd half multiplied by the first half
# Question 5
first_half = new_board_8x8[:4, :].sum()

second_half = new_board_8x8[4:, :].sum()

# How many times larger the second half is than the first half
ratio = second_half / first_half

multiplication = second_half * first_half

print("The sum of grains in the first half (rows 0–3):", first_half)
print("The sum of grains in the second half (rows 4–7):", second_half)
print("The second half is {:.2f} times larger than the first half.".format(ratio))
print("The product of grains in the second half and the first half is:", multiplication)

#Problem 6 and Problem 7 of comparison

# Function using np.append()
def chessboard_append(n, m):
    grains = np.array([1], dtype=object) 
    for _ in range(n * m - 1):
        grains = np.append(grains, 2 * grains[-1])
    return grains.reshape(n, m)


# Function using broadcasting
def chessboard_broadcast(n, m):
    return (2 ** np.arange(n * m, dtype=object)).reshape(n, m)


# 8x8 chessboard using both methods
n=8
m=8
board_append = chessboard_append(n, m)
board_broadcast = chessboard_broadcast(n, m)

start=time.time()
print("Chessboard using np.append():\n", board_append)
elapsed_time = time.time() - start
print('Time : {:.5f}[s]'.format(elapsed_time))

start=time.time()
print("\nChessboard using broadcasting:\n", board_broadcast)
elapsed_time = time.time() - start
print('Time : {:.5f}[s]'.format(elapsed_time))

print("\nTotal number of grains on the 8x8 chessboard:", board_broadcast.sum())

# elapsed_time = time.time() - start
# print('Time : {:.5f}[s]'.format(elapsed_time))