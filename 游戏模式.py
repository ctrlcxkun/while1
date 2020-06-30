while True:
	mode = input('请输入游戏模式')
	if mode == 'q': # quit
	    break
	elif mode == '1':
	    print('游戏模式一')
	elif mode == '2':
	     print('游戏模式二')
	else:
	    print('只能输入 q / 1 / 2')