# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from xml_driver import xml_reader

hosts = xml_reader('test.xml')
ipaddr = []
port = []
exploit = []
active_exploit = []
counter = 0

for host in hosts:
    
    ipaddresse = host['address']
    if len(host['ports']) > 1:
        for ports in host['ports']:

            port.append(ports['port'])
            exploit.append(ports['port']['exploit:'])
            active_exploit.append((ports['port']['active exploits:']))



    
    labels = port
    men_means = exploit
    women_means = active_exploit
    
    width = 0.35       # the width of the bars: can also be len(x) sequence
    
    # fig, ax = plt.subplots()
    
    # ax.bar(labels, men_means, width, label='Exploit')
    # ax.bar(labels, women_means, width, bottom=men_means,
    #         label='Active')
    
    # ax.set_ylabel('Scores')
    # ax.set_title(str(ipaddresse))
    # ax.legend()
    
    # plt.savefig('/static/images/name'+str(counter)+'.png')
    # counter = counter + 1