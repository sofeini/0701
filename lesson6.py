#提醒本檔案for python第幾版
#!/usr/bin/python3.10.2

"""py檔要執行要進入terminal，輸入 python lesson6.py
要重複執行就按上下鍵"""


import random

min = 1
max = 10
count = 0
random_number = random.randint(min , max)
print(random_number)

while True:
    keyin_number = int(input(f"猜數字範圍{min}~{max}:"))
    count += 1
    if (keyin_number == random_number):
        print(f"已經猜了{count}次，恭喜猜對答案是{random_number}")
        break
    else: 
        print(f"已經猜錯{count}次") 
print("遊戲結束") 