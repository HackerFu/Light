dy = 0.000001
def newton(f,start):
	print("=>",start)
	return start if abs(f(start)) < 0.000000000001 else newton(f,start-f(start)/((f(start+dy)-f(start))/dy))
def myequart(coeflist):
	expr,length ="" if int(coeflist[0]) >= 0 else "-",len(coeflist)
	for i in range(length):
		expr+=str(abs(int(coeflist[i])))+"*y**"+str(length-1-i)+(("+" if int(coeflist[i+1]) >= 0 else "-") if i != length-1 else "")
	print("\n你要求解的方程是：",(" "+expr).replace("**","^").replace("*","").replace("+"," + ")\
		.replace("-"," - ").replace("y^0","").replace(" 1y"," y").replace("^1 "," "),"= 0")
	try:
		nearby = int(input("\n从哪个数开始迭代？(默认：0) ").strip())
	except Exception:
		print("\n使用默认值0")
		nearby = 0
	print("\n<运功>  \\_o_/")
	return newton(lambda y:eval(expr),nearby)
def funconce():
	while True:
		coeflist=input("输入方程降幂系数：").split()
		if len(coeflist)>= 2:
			break
		else:
			print("请输入至少两个系数！")
	try:
		print("<收功>  _/o\\_\n\n方程解估计值为：y =",myequart(coeflist))
	except RecursionError:
		print(">.< 不小心走火入魔，可能要闭关修炼了 ...")
if __name__ == '__main__':
	print("这是一个用牛顿法解多项式方程的程序\n")
	while True:
		funconce()
		if input("\n是否继续(y/n 默认:y)? ").strip() == "n":
			print("\n告辞")
			break
		print("\n又是美好的开始！\n")
		
