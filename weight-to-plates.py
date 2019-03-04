p45 = 0
p35 = 0
p25=0
p10=0
p5=0
pmin=0
tmp=0.0
cont=''

def convert():
	global p45,p35,p25,p10,p5,pmin,tmp,cont
	tmp=int(input("\n Type the weight that you want to convert to plates: "))
	bar=int(input("\n Type the bar/default weight: "))
	tmp=tmp-bar
	while tmp >= 90:
		p45=p45+2
		tmp=tmp-90
	while tmp >= 70:
		p35=p35+2
		tmp=tmp-70
	while tmp >= 50:
	 	p25=p25+2
	 	tmp=tmp-50
	while tmp >= 20:
		p10=p10+2
		tmp=tmp-20
	while tmp >= 10:
		p5=p5+2
		tmp=tmp-10
	while tmp >= 5:
		pmin=pmin+2
		tmp=tmp-5
	print("\n45 lb plates: "+str(p45))
	print("\n35 lb plates: "+str(p35))
	print("\n25 lb plates: "+str(p25))
	print("\n10 lb plates: "+str(p10))
	print("\n5 lb plates: "+str(p5))
	print("\n2.5 lb plates: "+str(pmin))
	print("\nRemaining weight: "+str(tmp)+" lbs")
	cont = input("\nContinue? Y/n ")
		
while cont != 'n' and cont != 'N':
	msg = ''
	emsg = ''
	tmp = ''
	cont = ''
	convert()
if cont == 'n' or cont == 'N':
	print("\nClosing...")