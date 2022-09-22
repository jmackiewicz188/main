import paramiko
#from getpass import getpass
import time

# host = "10.191.192.12"
username = "admin"
password = "admin"
# command = "show rssi"

cmd1 = ["show rssi",
        "show rssi",
        "show rssi",]
cmd2 = ["show rssi",
        "show rssi"]
# priv_key_pass = getpass("Enter Private Key Password : ")
# key_file = '/home/evolve/.ssh/01_id'
# key_pass = paramiko.RSAKey.from_private_key_file(key_file, priv_key_pass)
# session = paramiko.SSHClient()
# session.load_system_host_keys()
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
def ssh_connector(host, commands):
    try:
        client.connect( host,
                        username=username, 
                        password=password,
                        # pkey=key_file,
                        # allow_agent=False,
                        # look_for_keys=False
                        )
        #wypluwa bez prompta
        # _stdin, _stdout,_stderr = client.exec_command(command)
        # print(_stdout.read().decode())
        # err = _stderr.read().decode()
        # if err:
        #     print(err)
        # client.close()

        #wypluwa z promptem
        for command in commands:
            DEVICE_ACCESS = client.invoke_shell()
            DEVICE_ACCESS.send(f'{command}\n')
            time.sleep(1)
            output = DEVICE_ACCESS.recv(65000)
            print (output.decode('ascii'))
        client.close()
    except:
         print("Unable to connect to the Device")

ssh_connector('10.191.192.12', cmd1)