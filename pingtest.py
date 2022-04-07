import os

ggdnsaccess = "google.com"
gg8access = "8.8.8.8"
gateway = "172.19.4.1"
awsdev1 = "8.0.0.202"

host_to_ping = [gg8access, gg8access, gateway, awsdev1]

for host in host_to_ping:
    response = os.system("ping -c 4 " + host)

    #and then check the response...
    if response == 0:
        print (f'{host} is up!')
    else:
        print (f'{host} is down!')