import random
r = random.randint(1, 100) #猜1~100範圍內的數字包含1跟100
count = 0
while True:
	count += 1 # count = count + 1 簡化版
	num = input('請猜數字： ')
	if int(num) == r:
		print('恭喜猜對了！')
		print('你總共猜了', count, '次才答對～')
		break
	elif int(num) > r:
		print('登愣～比答案大喔！')
	else:
		print('登愣～比答案小喔！')	
	print('這是你猜的第', count, '次～')