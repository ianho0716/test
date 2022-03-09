password = 'a123456'
i = 3 #3次機會
while True:
	psw = input('請輸入密碼：')
	if psw == password:
		print('登入成功！')
		break
	else:
		i = i - 1
		print('密碼錯誤！還有', i, '次機會')
		if i == 0:
			print('登入失敗！')
			break