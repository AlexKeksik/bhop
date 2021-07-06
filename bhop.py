import pymem # pip install pymem
import requests # pip install requests
import keyboard # pip install keyboard
from threading import Thread 
import pymem.process
import time

!!!
#Создано в науных целях и для веселья, читы это плохо!
!!!
# < Подключаемся к игре >

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

print ('')

# < Получаем оффсеты >
print ('>>> Получение оффсетов...')

offsets = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
response = requests.get(offsets).json()

dwLocalPlayer = int(response["signatures"]["dwLocalPlayer"])
dwForceJump = int(response["signatures"]["dwForceJump"])
m_fFlags = int(response["netvars"]["m_fFlags"])

print ('>>> Запуск BunnyHop...')

# < Запускаем функцию >

def BunnyHop():
    flag = True
    while True:
        try:
        # if keyboard.is_pressed( 'p' ):
        #     print("Программа закрылась")
        #     break

            if pm.read_int(client + dwLocalPlayer):
                player = pm.read_int(client + dwLocalPlayer)
                force_jump = client + dwForceJump
                on_ground = pm.read_int(player + m_fFlags)

                if keyboard.is_pressed('space')& flag:
                # print (flag)
                    if on_ground == 257 or on_ground == 263:# 257 стоит на земле 263 в присяде 
                        pm.write_int(force_jump, 6)
                        # time.sleep(0.15)
                        # pm.write_int(force_jump, 4)

                if keyboard.is_pressed( 'v' ) & flag:
                    flag = False
                    print ('>>> Bunny Hop остановлен.')
                    # print (flag)
                    time.sleep(0.5)
                
                if keyboard.is_pressed( 'v' ) & (flag==False):
                    flag = True
                    print ('>>> Bunny Hop включен.')
                    # print (flag)
                    time.sleep(0.5)

        except:
            print("Ошибка в получении данных !!! ")
            time.sleep(5)
			
# < Запускаем функцию в мультипоток >
Thread(target = BunnyHop).start()

print ('')
print ('>>> BunnyHop запущен.')