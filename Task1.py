import os
import subprocess
while True:
	print("what is your requirements: " , end='')
	p=input()
	if ("run" in p) or ("launch" in p) or ("execute" in p) or ("open" in p):
		if ("chrome" in p) or ("browser" in p):
			os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
		elif ("firefox" in p):
			os.system("start firefox.exe")
		elif ("edge" in p) or ("microsoft edge" in p):
			os.system('"C:\Program Files (x86)\microsoft\Edge\Application\msedge.exe"')

		elif ("picasa" in p) or ("photos" in p):
			os.system('"C:\Program Files (x86)\Google\Picasa3\Picasa3.exe"')

		elif ("adobe reader" in p) or ("pdf reader" in p):
			os.system('"C:\Program Files (x86)\Adobe\Reader 11.0\Reader\AcroRd32.exe"')

		elif ("buildbox" in p):
			os.system('"C:\Program Files (x86)\Buildbox3\Buildbox.exe"')

		elif ("Assassian Creed" in p):
			os.system('"C:\Program Files (x86)\GOG.com\Assassins Creed\AssassinsCreed_Game.exe"')
		elif ("x-men wolverine" in p) or ("x men" in p) or ("wolverine" in p):
			os.system('"D:\external drive copy\Games\X-Men Wolverine\Autorun.exe"')

		elif ("dreamweaver" in p):
			os.system('"C:\Program Files (x86)\Macromedia\Dreamweaver 8\Dreamweaver.exe"')
		elif ("my sql" in p) or (("database" in p) and ("tool" in p)):
			os.system('"C:\Program Files\MySQL\MySQL Workbench 8.0 CE\MySQLWorkbench.exe"')		
		elif ("visual studio" in p):
			os.system("start devenv.exe")
		elif ("nodejs" in p):
			 subprocess.call(r'C:\Program Files\nodejs\node.exe')
		elif("python" in p):
			os.system("start python")

		elif ("virtual machine" in p) or ("linux" in p):
			os.system("start vmware.exe")

		elif ("km player" in p):
			os.system('"C:\Program Files (x86)\The KMPlayer\KMPlayer.exe"') 

		elif ("wordpad" in p):
			os.system('"C:\Program Files (x86)\Windows NT\Accessories\wordpad.exe"')
		elif ("winrar" in p) or ("rar" in p):
			os.system('"C:\Program Files (x86)\WinRAR\WinRAR.exe"')
		elif ("windows firewall defender" in p) or ("firewall" in p):
			os.system("wf.msc")
		elif("camera" in p):
			os.system("start microsoft.windows.camera:")
		elif("music" in p):
			os.system("start mswindowsmusic:")
		elif("settings" in p):
			os.system("start ms-settings:")
		elif("voice recorder" in p):
			os.system("explorer.exe shell:appsFolder\Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe!App") 
		elif("calculator" in p):
			os.system("calc")
		elif("notepad" in p):
			os.system("notepad")
		elif("cmd" in p) or ("terminal" in p):
			os.system("start cmd")

		elif("excel" in p):
			os.system("excel.exe")		
		elif("outlook" in p):
			os.system("outlook")
		elif("ms word" in p):
			os.system("winword")
		elif("ms access" in p):
			os.system("msaccess")
		elif("ms powerpoint" in p):
			os.system("powerpnt")

		elif("app store" in p) or ("ms store" in p) or ("play store" in p):
			os.system("start ms-windows-store:")

		else:
			print("dont support")
			print(' try "list all" for more acceptable programs')
	elif ("list all" in p) or ("what can be done" in p) or ("options" in p):
		print("availabe options are:")
		print("		chrome")
		print("		firefox")
		print("		microsoft edge")
		print("		picasa")
		print("		camera")
		print("		km player")
		print("		music")
		print("		voice recorder \n")
		print(" supported games are:")
		print("		x men")
		print("		Assassian Creed \n")
		print("	some windows application are:")
		print("		wordpad")
		print("		winrar")
		print("		settings")
		print("		notepad")
		print("		cmd")
		print("		calculator")
		print("		windows firewall defender \n")
		print("	some programming required applications are:")
		print("		dreamweaver")
		print("		my sql")
		print("		visual studio")
		print("		nodejs")
		print("		python \n")
		print("	other environment:")
		print("		linux \n")
		print("	some office tools:")
		print("		ms word")
		print("		ms excel")
		print("		ms powerpoint")
		print("		access")
		print("		outlook")
		print("		app store")
	elif ("exit" in p):
		break
	else:
		print("sorry i couldn't understand!")
		print("Hint:")
		print(" can you run chrome for me")