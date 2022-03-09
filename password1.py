password = 'a123456'
i = 3
while i > 0:
	psw = input('請輸入密碼：')
	if psw == password:
		print('登入成功！')
		break
	else:
		i = i - 1
		print('登入錯誤，還有', i, '次機會')