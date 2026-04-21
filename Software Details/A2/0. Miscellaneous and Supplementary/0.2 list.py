import time

i = 0
my_list = [1, 2, 3, 4]

while True:
    for i in range(4):
        shifted = my_list[-i:] + my_list[:-i]  # Output: [4, 1, 2, 3]
        i = i+1
        print(shifted)
        time.sleep(0.5)
