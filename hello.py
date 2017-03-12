mena = []


def pozdrav():
	meno = input('Ako sa volas? ')
	mena.append(meno)
	print('Ahoj,', meno)
	if meno == 'Lucia':
		print('To si ty,', meno)
	else: 
		print('Teba nepoznam!') 


dalsi = True

while dalsi:
	pozdrav()
	odpoved = input('Este raz?')
	if odpoved.lower() in ['ano','hej','yes']:
		dalsi = True
	else:
		dalsi = False
		for meno in mena:
			print('Dakujem a prajem pekny den, {}!'.format(meno))	
