#!/bin/bash
dnsNames=("Google" "Shecan" "Cloudflare" "403.ir")
dnsPrimaryAddress=("8.8.8.8" "178.22.122.100" "1.1.1.1" "10.202.10.202")
dnsSecondaryAddress=( "8.8.4.4" "185.51.200.2" "1.0.0.1" "10.202.10.102")

index=1
for dnsName in ${dnsNames[@]}; do
  echo ${index}.${dnsName}
((++index))
done

echo

read -p "Enter DNS Number: " enteredDNS

((enteredDNS--))

echo "nameserver ${dnsPrimaryAddress[enteredDNS]}" > /etc/resolv.conf
echo "nameserver ${dnsSecondaryAddress[enteredDNS]}" >> /etc/resolv.conf