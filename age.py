driving = input('請問您有開過車嗎？')
if driving != '有' and driving != '沒有':
	print('只能輸入有或沒有')
	raise SystemExit

age = int(input('請問您的年齡為？'))
if driving == '有':
	if age >= 18:
		print('通過測驗')
	else:
		print('奇怪 你有駕照嗎？！')
elif driving == '沒有':
	if age >= 18:
		print('快快去把駕照考起來！')
	else:
		print('再過幾年久可以考駕照囉！')