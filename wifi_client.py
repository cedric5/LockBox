import pexpect

def connect(ssid, password):
    child = pexpect.spawn('comitup-cli')
    child.expect('\r\n')
    child.sendline('1')
    child.sendline('EC5225259929')
    print (child.before)
    child.interact()


def disconnect():
    print()


def show_networks():
    return []


