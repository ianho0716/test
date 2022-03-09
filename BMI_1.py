name = input('請輸入你的名字：')
print('Hi', name)
height = input('請問你的身高幾公分呢？')
weight = input('請問你體重幾公斤呢？')
height_1 = float(height) / 100
height_2 = float(height_1) ** 2
bmi = float(weight) / float(height_2)
if bmi < 18.5:
	print(name, '你的BMI為', bmi, '，體重過輕～宵夜吃太少')
elif 18.5 <= bmi < 24:  #else if 另外如果 也可以寫成 elif bmi>= 18.5 and bmi < 24
	print(name, '你的BMI為', bmi, '，正常範圍喔～羨慕死了馬的')
elif 24 <= bmi < 27:
	print(name, '你的BMI為', bmi, '，過重～趕快減肥')
elif 27 <= bmi < 30:
	print(name, '你的BMI為', bmi, '，輕度肥胖～歡迎加入胖子家族')
elif 30 <= bmi < 35:
	print(name, '你的BMI為', bmi, '，中度肥胖～要瘦很難ㄌ')
else:
    print(name, '你的BMI為', bmi, '，重度肥胖～我們花那麼多錢，吃那麼多吃那麼好，幹麻減肥＾_＾')