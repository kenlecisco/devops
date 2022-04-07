import subprocess


ggdnsaccess = "google.com"
gg8access = "8.8.8.8"
gateway = "172.19.4.1"
awsdev1 = "8.0.0.202"

list_of_host =[ggdnsaccess, gg8access, gateway, awsdev1]
pingresult = subprocess.run(['ping', 'google.com'], capture_output=True)
print(pingresult.stdout.decode())


