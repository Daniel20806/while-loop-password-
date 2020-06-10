password = 'a123456'
G = 3
while True:
	pd = input('請輸入密碼: ')
	if pd == password:
		print('登入成功!')
		break
	else:
		G = G - 1
		if G == 0:
			print('登入失敗,無法再次登入喔!')
			break
		print('登入失敗!剩餘', G,'次機會')
		


		