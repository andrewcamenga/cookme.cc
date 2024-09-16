import time
import os
import subprocess

def gitpull():
    return subprocess.run(['git','pull'], capture_output = True)

def hugo_build():
    timestamp = time.strftime('%Y%m%d%H%M%S')
    results = subprocess.run(['hugo','--config','config-web.toml','--destination', f'builds/{timestamp}'], capture_output=True)
    return timestamp, results

def mklink(timestamp):
    return subprocess.run(['ln','-s',f'builds/{timestamp}','tmp'], capture_output = True)

def mvlink():
    return subprocess.run(['mv','-T','tmp','public'],capture_output = True)

os.chdir('/var/www/cookme.cc')

result = gitpull()
print(result.stdout.decode())
assert(result.returncode == 0)

timecode, result = hugo_build()
print(result.stdout.decode())
assert(result.returncode == 0)

result = mklink(timecode)
print(result.stdout.decode())
assert(result.returncode == 0)

result = mvlink()
print(result.stdout.decode())
assert(result.returncode == 0)

