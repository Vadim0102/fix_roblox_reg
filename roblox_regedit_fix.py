import glob
import os
b = '\\'

def get_roblox_exe(base_dir=r'C:/Program Files (x86)/Roblox/Versions/'):
    return glob.glob(base_dir + '/**/RobloxPlayerBeta.exe', recursive=True)[0]

try:
    path = get_roblox_exe()
except IndexError:
    path = get_roblox_exe(f'{os.getenv("LOCALAPPDATA")}/Roblox/Versions/')
except:
    print('Where your roblox dir??? ("??/Roblox/Versions/")')
    path = get_roblox_exe(input())

os.system(r'reg add HKEY_CURRENT_USER\SOFTWARE\Classes\roblox-player\shell\open\command /f /d "\"' + f'{path.replace("/", b)}' + r'\" %1"')

