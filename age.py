driving = input("請問你有沒有開過車?")
if driving != "有" and driving != '沒有':
	print('只能輸入 有/沒有')
	raise systemExit
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('騙人 怎麼可能開過車，乖乖回去讀書')
elif driving == "沒有" :
	if age >= 18:
		print('為什麼不考駕照呢?')
	else:
		print('很好,再',18-int(age),'年就可以考駕照了')
else:
	print('只能輸入 有/沒有')