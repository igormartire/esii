def peaoBranco(source):
	movimentos=[]
	y= source[0]
	x = str(source[1]+1)
	z= y+x
	movimentos.append(z)
	return movimentos

def peaoPreto(source):
	movimentos=[]
	y= source[0]
	x= str(source[1]-1)
	z=y+x
	movimentos.append(z)
	return movimentos

def torre(source):
	movimentos=[]
	for i in range(8):
		y = str(i+1)
		x= source[0]
		z=x+y	
		movimentos.append(z) 
	
	l=['A','B','C', 'D', 'E', 'F', 'G', 'H']
	
	for i in l:
		x= str(source[1])
		z= i+x
		movimentos.append(z)
	
	rpt= source[0]+str(source[1])
	movimentos.remove(rpt)	
	movimentos.remove(rpt)	
	
	return movimentos

def bispo(source):
	movimentos=[]

	j=source[0]
	i=source[1]

	#diagonal direita superior

	while ((i!=8) & (j!='H')):
		j=chr(ord(j) + 1)
		i=str(i+1)
		z=j+i 
		movimentos.append(z)
		i=int(i)
		j=str(j)

	j=source[0]
	i=source[1]
		
	#diagonal esquerda superior
	while ((i!=8) & (j!='A')):
		j=chr(ord(j) - 1)
		i=str(i+1)
		z=j+i 
		movimentos.append(z)
		i=int(i)
		j=str(j)			

	j=source[0]
	i=source[1]

	#diagonal esquerda inferior

	while ((i!=1) & (j!='A')):
		j=chr(ord(j) - 1)
		i=str(i-1)
		z=j+i 
		movimentos.append(z)
		i=int(i)
		j=str(j)			

	j=source[0]
	i=source[1]

	#diagonal direita inferior
	while((i!=1) & (j!='H')):
		j=chr(ord(j) + 1)
		i=str(i-1)
		z=j+i 
		movimentos.append(z)
		i=int(i)
		j=str(j)	

	return movimentos

def cavalo(source):
	movimentos=[]
	j=source[0]
	i=source[1]

	#1 possibilidade 

	i= i+2
	j= chr(ord(j) + 1)

	if((i<=8) & (j<=chr(ord('H')))):
		i= str(i)
		z=j+i
		movimentos.append(z)
	
	#2 possibilidade

	j=source[0]
	i=source[1]

	i=i+2
	j= chr(ord(j) - 1)

	if ((i<=8) & (j>=chr(ord('A')))):
		i= str(i)
		z=j+i
		movimentos.append(z)

	#3 possibilidade 

	j=source[0]
	i=source[1]

	i=i+1
	j= chr(ord(j) - 2)	

	if((i<=8) & (j>=chr(ord('A')))):
		i= str(i)
		z=j+i
		movimentos.append(z)

	#4 possibilidade

	j=source[0]
	i=source[1]

	i=i-1
	j= chr(ord(j) - 2)	

	if((i>=1) & (j>=chr(ord('A')))):
		i= str(i)
		z=j+i
		movimentos.append(z)

	#5 possibilidade

	j=source[0]
	i=source[1]
	
	i=i+1
	j= chr(ord(j) + 2)	

	if((i<=8) & (j<=chr(ord('H')))):
		i= str(i)
		z=j+i
		movimentos.append(z)

	#6 possibilidade

	j=source[0]
	i=source[1]
	
	i=i-1
	j= chr(ord(j) + 2)	
	
	if((i>=1) & (j<=chr(ord('H')))):
		i= str(i)
		z=j+i
		movimentos.append(z)
	
	#7 possibilidade

	j=source[0]
	i=source[1]

	i=i-2
	j= chr(ord(j) + 1)	

	if((i>=1) & (j<=chr(ord('H')))):
		i= str(i)
		z=j+i
		movimentos.append(z)	

	#8 possibilidade
	
	j=source[0]
	i=source[1]

	i=i-2
	j= chr(ord(j) - 1)	

	if((i>=1) & (j>=chr(ord('A')))):
		i= str(i)
		z=j+i
		movimentos.append(z)		


	return movimentos

def rainha(source):

	movimentos=[]

	#juncao dos movimentos da torre com os movimentos do bispo

	#torre
	for i in range(8):
		y = str(i+1)
		x= source[0]
		z=x+y	
		movimentos.append(z) 
	
	l=['A','B','C', 'D', 'E', 'F', 'G', 'H']
	
	for i in l:
		x= str(source[1])
		z= i+x
		movimentos.append(z)
	
	rpt= source[0]+str(source[1])
	movimentos.remove(rpt)	
	movimentos.remove(rpt)	
	
	#bispo

	j=source[0]
	i=source[1]

	#diagonal direita superior

	while ((i!=8) & (j!='H')):
		j=chr(ord(j) + 1)
		i=str(i+1)
		z=j+i 
		movimentos.append(z)
		i=int(i)
		j=str(j)

	j=source[0]
	i=source[1]
		
	#diagonal esquerda superior
	while ((i!=8) & (j!='A')):
		j=chr(ord(j) - 1)
		i=str(i+1)
		z=j+i 
		movimentos.append(z)
		i=int(i)
		j=str(j)			

	j=source[0]
	i=source[1]

	#diagonal esquerda inferior

	while ((i!=1) & (j!='A')):
		j=chr(ord(j) - 1)
		i=str(i-1)
		z=j+i 
		movimentos.append(z)
		i=int(i)
		j=str(j)			

	j=source[0]
	i=source[1]

	#diagonal direita inferior
	while((i!=1) & (j!='H')):
		j=chr(ord(j) + 1)
		i=str(i-1)
		z=j+i 
		movimentos.append(z)
		i=int(i)
		j=str(j)	


	return movimentos


def rei(source):
	
	movimentos=[]

	j=source[0]
	i=source[1]

	#1 possibilidade
	i=i+1

	if (i<=8):
		i= str(i)
		z=j+i
		movimentos.append(z)

	#2 possibilidade

	j=source[0]
	i=source[1]

	i=i-1

	if (i>=1):
		i= str(i)
		z=j+i
		movimentos.append(z)

	#3 possibilidade

	j=source[0]
	i=source[1]

	j= chr(ord(j) + 1)	

	if(j<=chr(ord('H'))):
		i= str(i)
		z=j+i
		movimentos.append(z)

	#4 possibilidade
	
	j=source[0]
	i=source[1]

	j= chr(ord(j) - 1)

	if(j>=chr(ord('A'))):
		i= str(i)
		z=j+i
		movimentos.append(z)

	#5 possibilidade

	j=source[0]
	i=source[1]

	i=i+1
	j= chr(ord(j) - 1)

	if((i<=8) & (j>=chr(ord('A')))):
		i= str(i)
		z=j+i
		movimentos.append(z)

	#6 possibilidade

	j=source[0]
	i=source[1]

	i=i+1
	j= chr(ord(j) + 1)

	if((i<=8) & (j<=chr(ord('H')))):
		i= str(i)
		z=j+i
		movimentos.append(z)

	#7 possibilidade

	j=source[0]
	i=source[1]	

	i=i-1
	j= chr(ord(j) + 1)

	if((i>=1) & (j<=chr(ord('H')))):
		i= str(i)
		z=j+i
		movimentos.append(z)

	#8 possibilidade

	j=source[0]
	i=source[1]	

	i=i-1
	j= chr(ord(j) - 1)

	if((i>=1) & (j>=chr(ord('A')))):
		i= str(i)
		z=j+i
		movimentos.append(z)


	return movimentos


def destinations(piece, source):
	movimentos=[]
	
	if(piece=='p'):
		movimentos = peaoPreto(source)

	if(piece=='P'):
		movimentos = peaoBranco(source)

	if((piece=='r')| (piece=='R')):
		movimentos = torre(source)

	if((piece=='n')|(piece=='N')):
		movimentos= cavalo(source)

	if((piece=='b')|(piece=='B')):
		movimentos= bispo(source)

	if((piece=='q')|(piece=='Q')):
		movimentos=rainha(source)

	if((piece=='k')|(piece=='K')):
		movimentos=rei(source)

	return movimentos


		













