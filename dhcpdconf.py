nets = [
        {'ip': '10.1.1.', 'name': 'core01-', 'ports': 32},
        {'ip': '10.1.2.', 'name': 'strand01-', 'ports': 24},
        {'ip': '10.1.3.', 'name': 'brynas01-', 'ports': 24},
        {'ip': '10.1.4.', 'name': 'bomhus01-', 'ports': 24},
        {'ip': '10.1.5.', 'name': 'andersberg01-', 'ports': 24},
        {'ip': '10.1.6.', 'name': 'villastaden01-', 'ports': 48},
        {'ip': '10.1.7.', 'name': 'satra01-', 'ports': 24},
]

for i, net in enumerate(nets):
    print("""subnet {ip}0 netmask 255.255.255.0 {{
    option routers {ip}254;""".format(ip=net['ip']))
    for j in range(1,net['ports']+1):
        name = "{name}{j}".format(name=net['name'], j=j)
        hexlen =  ('\\x%02X' % (len(name)))
        print(('    host {name} {{\n' + 
              '        fixed-address {ip}{j};\n' + 
              '        host-identifier option agent.circuit-id "\\x01{hexlen}{name}";\n' + 
              '    }}\n').format(name=name, ip=net['ip'], j=j, hexlen=hexlen))
    print("}\n")
