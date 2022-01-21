import subprocess
import sys

try:
    p = subprocess.Popen(['powershell.exe', 'C:\\Users\\v\\Desktop\\python_automation\\a.ps1',"knname"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s=p.communicate()
    print(s)
except Exception as e:
    print("Exception occured",e)
