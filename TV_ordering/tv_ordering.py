import os
import pandas as pd
import time
import xml.etree.ElementTree as ET
import sys


"""
Erstinstallation
-> keine bevorzugte empfangsart
automatischer Senderdurchlauf
Kabel Digital
106-8XX
mit 1000 



"""




def medion(cmd, sleep=1.0):
    output = os.popen('medion {}'.format(cmd))
    time.sleep(sleep)
    return output

def get_active():
    print('try to get active channel list')
    output = medion('activechannellist')
    channel_list = output.read()
    channel_list = channel_list.split('\n')[1]
    channel_list = channel_list.replace('&', '')
    tree = ET.fromstring(channel_list)
    channel_list = []
    number_list = []
    for child in tree:
        channel_list.append(child.attrib['name'])
        number_list.append(int(child.attrib['rsn']))
    f_active = open('active.txt', 'w')
    f_active.write('\n'.join(channel_list))
    f_active.close()
    print('got list of current channels')
    return channel_list, number_list



def sorting(channel_list, number_list):

    f_setup = open('setup.txt', 'r')
    setup = f_setup.readlines()
    f_setup.close()
    setup = [i.replace('\n', '') for i in setup]
    print('got setup list')


    print('start with ordering')
    medion('1', 1)
    medion('return', 1)


    """
    - wenn channel nicht in activer liste, also nicht verfuegbar
        dann wird der platz uebersprungen und es 
    """

    set_position = 1
    for channel in setup:

        if channel not in channel_list:
            print(channel, 'not in list')
            continue

        name_pos = channel_list.index(channel)
        pos = number_list[name_pos]

        if set_position == pos:
            print(channel, 'already at', str(pos))
            set_position += 1
            continue


        # move to the channel
        for d in list(str(pos)):
            medion(d, 0.8)
            
        time.sleep(2)
        medion('return')
        medion('ok')
        medion('green')
        medion('ok')
        medion('down')
        medion('ok')

        for d in list(str(set_position)):
            medion(d, 0.8)

        medion('ok')
        medion('ok')
        medion('return')
        medion('return')

        
        print('{} moved to {}'.format(channel, set_position))


        # print('before')
        # print(channel_list)
        # print(number_list)
        # update number and list
        ch_to_switch = channel_list.pop(name_pos)
        number_list.pop(name_pos)
        
        for i in range(len(number_list)):
            if set_position <= number_list[i]:
                number_list.insert(i, set_position)
                channel_list.insert(i, ch_to_switch)
                break
        # print('between')
        # print(channel_list)
        # print(number_list)

        for j in range(i+1, len(number_list)):
            if number_list[j-1] == number_list[j]:
                number_list[j] = number_list[j] + 1
            else:
                break

        # print('after')
        # print(channel_list)
        # print(number_list)


        set_position += 1
        # michi = input('weiter:')


    medion('1')


if __name__ == '__main__':

    # c_list, n_list = get_active()
    if len(sys.argv) < 2:
        c_list, n_list = get_active()
        sorting(c_list, n_list)

    else:
        if sys.argv[1] == 'active':
            c_list, n_list = get_active()




# #
#
# for i in range(len(setup)):
#     channel = setup[i]
#
#     print('now',channel)
#     input('continue?')
#
#     if channel in channel_list:
#         name_pos = channel_list.index(channel)
#         pos = number_list[name_pos]
#         
#         
#     else:
#         print(channel, 'not in list')
#         continue
#
#     if str(i+1) == str(pos):
#         print(channel, 'already at', str(pos))
#         continue
#     # change to pos
#     # move pos to i+1
#     for d in list(str(pos)):
#         medion(d)
#
#     time.sleep(2)
#     medion('return')
#     medion('ok')
#     medion('green')
#     medion('ok')
#     medion('down')
#     medion('ok')
#
#     for d in list(str(i+1)):
#         medion(d)
#
#     medion('ok')
#     medion('ok')
#     medion('return')
#     medion('return')
#     
#     print('{} moved to {}'.format(channel, i+1))
#
#     
#     ch_to_switch = channel_list.pop(name_pos)
#     channel_list.insert(i, ch_to_switch)
#     number_list.pop(name_pos)
#     number_list.insert(i, i+1)
#     for k in range(i+1,name_pos+1):
#         # these two lines are added
#         if (number_list[k-1] + 1) != number_list[k]:
#             break
#
#         number_list[k] += 1
#
#     print('finished ',channel)
#     input('continue?')
#
#
# medion('1')
