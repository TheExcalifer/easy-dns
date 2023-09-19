import os
import json

dns_list_json =  json.load(open('dns.json'))

print("Insert number of DNS: ")
# Print available DNS
for (key) in dns_list_json:
    print(f"{key}.{dns_list_json[key][0]}")

# Select dns & interface by user
selected_dns = input('Insert number of DNS: ')
entered_interface = input('Insert Interface: ')

def set_primary_DNS(selected_dns):
    os.system(
        f'netsh interface ipv4 set dnsservers {entered_interface} static {selected_dns}')
def set_secondary_DNS(selected_dns):
    os.system(
        f'netsh interface ipv4 add dnsservers {entered_interface} {selected_dns} index=2')
    
try:
    set_primary_DNS(dns_list_json[selected_dns][1])
    set_secondary_DNS(dns_list_json[selected_dns][2])
    print('DNS has been set')
except:
    print('Error occured')
