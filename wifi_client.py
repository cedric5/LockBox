import pexpect
import subprocess


def connect(ssid, password):
    child = pexpect.spawn('comitup-cli')
    child.expect('\r\n')
    child.sendline('m')
    child.sendline(ssid)
    child.sendline(password)


def disconnect():
    print()


def ssid_list():
    p = subprocess.Popen("iwlist wlan0 scan | grep 'ESSID'", stdout=subprocess.PIPE, shell=True)

    (output, err) = p.communicate()
    ssid_arr = output.splitlines()
    for index, id in enumerate(ssid_arr):
        id = id.decode().split(':')
        id = id[1].replace('"', '')
        ssid_arr[index] = id.rstrip()  # remove the newline\
    return ssid_arr


