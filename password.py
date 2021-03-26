password = 'a123456'
i = 2
while i >= 0:
	word = input('請輸入密碼：')
	if word == password:
	    print('登入成功')
	    break
	else:
		print('密碼錯誤！ 還有', i, '次機會')
		i = i - 1
	        