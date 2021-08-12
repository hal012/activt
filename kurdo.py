import os,sys,subprocess
subprocess.getoutput("pip install requests")
import requests,sys,os,time
#BY MOELSHAFEY
elshafey = '@bahamhex'
pss=input("\033[1;37m [~]\033[1;35mENTER PASSWORD :\033[1;33m")
if pss ==elshafey:
	pass
	print("\033[1;32m                    SUCCESS PASSWORD ")
	time.sleep(2)
	os.system('clear')
else:
	exit('\033[1;31m                    WORNG PASSWORD ')
import requests,time,random,os,sys
TOKEN=input('\033[1;33m BOT TOKEN :')
ID=input('\033[1;31m ID :')
os.system('clear')
MM=int(input('\033[1;31m [^]\033[1;36m AMOUNT OF USER :\033[1;37m'))
os.system('clear')
oip='qwertyuioplkjhgfdsazxcvbnm'
upper = 'ABCDEFGHIKLMNOPQSTVWSYZ'
number = '0987654321'
uu7='_'
all  = number + upper +oip
length = 1
for e in range(MM):
	u= ''.join(random.sample(all,length))
	s= ''.join(random.sample(all,length))
	r= ''.join(random.sample(all,length))
	kk=(u+'_'+s+'_'+r)
	ree = requests.get(f'https://t.me/{kk}').text
	if 'tgme_username_link' in ree:
		Account = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text=• Hi New UserName ✅⚠️\n ━━━━━━━━❪❂❫━━━━━━━━\n-❖UserName :- @{kk}✅\n-❖Valid :- Telegram✅\n-❖User Available :- True✅\n━━━━━━━━❪❂❫━━━━━━━━\n☬︙By : @barhamhex ↻︙ ••\n☬︙ch  : @barhamhex ↻ ︙••')
		print(f'\033[1;32m Available:{kk} ')
		
	else:
		print(f' \033[1;31mNOT Available:{kk}')
