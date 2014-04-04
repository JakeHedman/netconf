name = input("Name? (e.g strand) ")
ports = int(input("Number of ports? "))
vlan = input("Vlan? ")

print("""no ip domain-lookup
hostname sw-{name}01
enable secret 123
ip dhcp snooping vlan 51-57
ip dhcp snooping

interface range FastEthernet0/1-{ports}
switchport access vlan {vlan}
switchport mode access
""".format(ports=ports, vlan=vlan, name=name))

for i in range(1, ports+1):
    print (("interface FastEthernet0/{i}\n" +
            "ip dhcp snooping vlan {vlan} information option format-type circuit-id string {name}01-{i}"
           ).format(name=name, vlan=vlan, i=i))

print("""
interface range GigabitEthernet0/1-2
switchport trunk encapsulation dot1q
switchport trunk allowed vlan 10,51-57
switchport mode trunk
ip dhcp snooping limit rate 10
ip dhcp snooping trust

exit

vlan 10
name management

vlan 51
name core

vlan 52
name strand

vlan 53
name brynas

vlan 54
name bomhus

vlan 55
name andersberg

vlan 56
name villastaden

vlan 57
name satra

interface vlan 10
ip address 10.10.10.{ip} 255.255.255.0

interface vlan 51
no ip address

interface vlan 52
no ip address

interface vlan 53
no ip address

interface vlan 54
no ip address

interface vlan 55
no ip address

interface vlan 56
no ip address

interface vlan 57
no ip address

line con 0
line vty 0 4
password telnetpass
login
""".format(ip=int(vlan)-50))
