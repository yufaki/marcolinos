import pyautogui,time,os
quantidade = int(input('\033[33mQuantidade de mensagens a serem enviadas: \033[0;0m'))
mensagem = str(input('\033[33mMensagem a ser enviada:\033[0;0m '))
for c in range(0,6):
	print(f'\033[31mIniciando programa em \033[34m{c}\033[31m...\033[0;0m')
	time.sleep(1)
	os.system('clear')
print(f'\033[33mQuantidade de mensagens a serem enviadas: \033[35m{quantidade}\033[0;0m')
print(f'\033[33mMensagem a ser enviada: \033[35m{mensagem}\033[0;0m')
for word in range(0,quantidade):
	pyautogui.typewrite(f'{mensagem}')
	pyautogui.press('enter')
	time.sleep(0.21)
print(f'\033[37mForam enviadas \033[36m{quantidade}\033[37m mensagens \033[0;0m'.capitalize())
