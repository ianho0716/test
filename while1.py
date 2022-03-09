while True: #無限迴圈練習
	driving = input('請問你有開過車嗎？')
	if driving == '有':
		age = input('請問你幾歲呢？')
		if int(age) >= 18:
			print('有駕照才能上路喔～開車小心')
			break
		else:
			print('未成年請勿開車')
			break
	elif driving == '沒有':
		age = input('請問你幾歲呢？')
		if int(age) >= 18:
			print('先去考駕照')
			break
		else:
			print('滿18歲就能考駕照了～考過才能開喔')
			break
	else:	
		print('請輸入 有/沒有')	