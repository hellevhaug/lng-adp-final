import json

"""
This file is for printing out the saved optimal values
"""


file1 = open('solution/x.json')
data1 = json.load(file1)

print('------------------------------------------')
print('                                          ')
print('1. The routes of the vessels in the fleet')
print('                                          ')
print('------------------------------------------')
print('\n')
for vessel in data1:
    if len(data1[vessel])==1:
        print('Vessel '+ vessel + ' is not used in the planning period.')
    else:
        print('Vessel '+ vessel + ' route:')
        route = data1[vessel][0][2] + ' (day ' + str(data1[vessel][0][0]) +') '
        for arc in data1[vessel]:
            route += '------ ' + arc[3] + ' (day ' + str(arc[1]) +') '
        print(route)
    print('\n')


print('\n')


file2 = open('solution/s.json')
data2 = json.load(file2)

print('-------------------------------------------')
print('                                           ')
print('2. The inventory level for each loading port')
print('                                           ')
print('-------------------------------------------')

for loading_port in data2:
    print('-----------------------------------------')
    print('Loading port name: ' + loading_port)
    for day in data2[loading_port]:
        print('On day ' + str(day[0]) +' : ' + str(day[1]))
    print('-----------------------------------------')
    print('\n')

print('\n')

file3 = open('solution/g.json')
data3 = json.load(file3)

print('--------------------------------------------------')
print('                                                  ')
print('3. Number of cargoes charted for each loading port')
print('                                                  ')
print('--------------------------------------------------')

for loading_port in data3:
    print('---------------------------------------------------')
    print('Loading port name: ' + loading_port)
    for cargo in data3[loading_port]:
        print('Day: ' + str(cargo[0]) +', Contract: ' + str(cargo[1])+', Amount: ' + str(cargo[2]))
    print('---------------------------------------------------')
    print('\n')

file4 = open('solution/z.json')
data4 = json.load(file4)

print('------------------------------')
print('                              ')
print('4. The fulfilled FOB-contracts')
print('                              ')
print('------------------------------')
print('\n')
for fob_contract in data4:
    print('-------------------------')
    print('Fob contract ID: ' + fob_contract)
    if fob_contract=='ART_FIC':
        if len(data4[fob_contract])==0:
            print('No artificial FOB in ADP.')
        else:
            for cargo in data4[fob_contract]:
                print('Day: ' + str(cargo[0]) + ', Amount: ' + str(cargo[2]))
    else:
        print('Day: ' + str(data4[fob_contract][0]) +', Amount: ' + str(data4[fob_contract][1]))
        
    print('-------------------------')
    print('\n')