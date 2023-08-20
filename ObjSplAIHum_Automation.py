import re

pattern = re.compile(r"vehicles\\\\")
import glob
import os
'''
刹那の誓い-Neko Hacker

 終わりを待つ刹那を今は
終わりは来るのだと知りながら
愛しき君となら永遠と呼ぼう

    等待終結到來的那一刻的現在
    既然知道終結是會到來的的話
    只要與珍愛的你在一起的話，我們的愛就能稱之為永遠

 
'''


path_of_map = './maps/project-HONGSHING/'
# Find all files with .txt extension in a directory
files = [file for file in os.listdir(path_of_map) if file.endswith(".map")]
#print(files)
line_before_spline = 9999
line_before_object = 9999
list_of_map_tiles = []
list_of_splines_used = []
list_of_objects_used = []
# Loop through each file and read its contents
for file in files:
    data = open(path_of_map+file, encoding='utf-16').read()
    for line in data.splitlines():
        line_before_spline += 1
        line_before_object += 1
        if line == '[spline]':
            line_before_spline = 1
        if line_before_spline == 3:
            x = line
            list_of_splines_used.append(x)
        if line == '[object]':
            line_before_object = 1
        if line_before_object == 3:
            x = line
            list_of_objects_used.append(x)
        

s = set()

# Define a new list to store the non-repeated strings
list_of_splines_used_2 = []

# Loop through each string in the list
for x in list_of_splines_used:
    # Check if the string is not in the set
    if x not in s:
        # Add the string to the set and the new list
        s.add(x)
        list_of_splines_used_2.append(x)

s2 = set()

# Define a new list to store the non-repeated strings
list_of_objects_used_2 = []

# Loop through each string in the list
for x in list_of_objects_used:
    # Check if the string is not in the set
    if x not in s2:
        # Add the string to the set and the new list
        s.add(x)
        list_of_objects_used_2.append(x)


write_to_spline_txt = open('./Splines.txt', 'w', encoding='utf-8')
for x in list_of_splines_used_2:
    write_to_spline_txt.write(x+'\n')

write_to_AICarandBus_txt = open('./AI_Vehicles.txt', 'w', encoding='utf-8')
open_ai_list = open('maps/project-HONGSHING/ailists.cfg', 'r', encoding='utf-8')
open_ai_list_2 = open_ai_list.readlines()
#print(open_ai_list_2)

for line in open_ai_list_2:
    if 'vehicles' in line:
        write_to_AICarandBus_txt.write(line)

write_to_object_txt = open('./Objects.txt', 'w', encoding='utf-8')
for x in list_of_objects_used_2:
    write_to_object_txt.write(x+'\n')

humans_text = open(f'./{path_of_map}Humans.txt', 'r', encoding='utf-8')
humans_text_2 = humans_text.readlines()
drivers_text = open(f'./{path_of_map}Drivers.txt', 'r', encoding='utf-8')
drivers_text_2 = drivers_text.readlines()
write_to_humans_txt = open('./Humans.txt', 'w', encoding='utf-8')
for i in humans_text_2 + drivers_text_2:
    if '\n' not in i:
        i += '\n'
    write_to_humans_txt.write(i)

