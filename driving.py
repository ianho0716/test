driving = input('請問你有開過車嗎？')
if driving != '有' and driving != '沒有' and driving != 'yes' and driving != 'no':
	print('請輸入 有/沒有/yes/no')
	raise SystemExit #非限定答案直接終止

age = input('你幾歲呢?')
if driving == '有':
	if int(age) >= 18:
		print('開車小心')
	else:
		print('無照駕駛')
elif driving == 'yes':
	if int(age) >= 18:
		print('safe driving')
	else:
	    print('fku')	
else:
    if int(age) >= 18:
        print('去上駕訓班')
    else:
        print('乖寶寶')