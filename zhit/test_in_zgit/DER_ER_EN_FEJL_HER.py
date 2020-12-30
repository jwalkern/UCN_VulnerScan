# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:04:16 2020

@author: JaMiBiCh
"""
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError



IPaddress = "192.168.1.111"
    
    
with open("test.xml", "r") as f:
    scan_result = f.read()

try:
    xml_str = str(scan_result)
    root = ET.fromstring(xml_str)

except ParseError as e:
    print(e)
tag = root.tag
hosts = []

for host in root.findall('host'):

    details = {'address':host.find('address').attrib.get('addr')}
    port_list = []
    ports=host.find("ports")
    
    #Fjerner host ip addressen
    if details['address'] == IPaddress:
        print("virker")
        continue
    
    for port in ports:
        
        port_details={'port':port.attrib.get('portid'),
                      'protocol':port.attrib.get('protocol')}
        service = port.find('service')
        state = port.find('state')
        script = port.find('script')
        if service is not None:
            port_details.update({'service':service.attrib.get('name'), 
                                 'product':service.attrib.get('product',''),
                                 'version':service.attrib.get('version',''),
                                 'extrainfo':service.attrib.get('extrainfo',''),
                                 'ostype':service.attrib.get('ostype','')})
        if state is not None:
            port_details.update({'state':state.attrib.get('state'),
                                 'reason':state.attrib.get('reason', '')})
        
        
        """
        OBS!
           
        PÅ NOGLE PORT FINDER DEN 2 SCRIPTS. DEN TJEKKER KUN ÉT.
           
        EVT. FOR ITEM IN SCRIPT?
           
        
        """       
        if script is not None:
            port_details.update({'id':script.attrib.get('id', '')})
 
            exploits = []
            active_exploits = []
            vulners = script.attrib.get('id')
       
            if vulners == 'vulners':
                for elem in script.iter('elem'):
                    is_exploit = elem.text
                    if is_exploit == 'true':
                        active_exploits.append(1)
                    if is_exploit == 'false':
                        exploits.append(1)
                        
                        
            elif vulners != 'vulners':
                elem = script.findall('elem')
                table = script.findall('table')
                for item in elem:
                    exploits.append(1)
                for item in table:
                    exploits.append(1)
                    
            port_details.update({'exploits:': sum(exploits),
                                 'active exploits:': sum(active_exploits)})
         
        """           
        OBS! FÆRDIG
        
        """
    
        
        
        if port_details['port'] is not None:
            port_list.append(port_details)
            
    details['ports']=port_list
    hosts.append(details)


for host in hosts:
    print('---------------------------------------------------------')
    print('Name:', str(host.get('name','')))
    print('IP:', str(host.get('address', '')))
    print('Services: ')
    for port in host['ports']:
        print('\t Service: ')
        print('\t-----------------------------------')
        for k,v in port.items():
            print('\t\t',str(k),':',str(v))
    print('---------------------------------------------------------')      
 


