#MatthewLaneP2M5Final

import os

os.system ("curl  https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o ""elements1_20.txt")

def get_names() :
    while True :
        if(len(ele_list) < 5):
            ele_input = input("Enter the name of an element: ").strip().lower()
            if not ele_input :
                continue
            elif (ele_input not in ele_list) :
                ele_list.append(ele_input)
            elif(ele_input in ele_list) :
                print(ele_input,"that was already entered; do not enter duplicates")
        else :
            break
    return ele_list

ele = open('elements1_20.txt','r')
ele_list =[]
index = 0
fl_list =[]
found_list =[]
not_found_list =[]
fl_string = ele.readline().strip("\n").upper().lower()
get_names()
while fl_string :
    if fl_string is None :
        break
    else :
        fl_list.append(fl_string)
        fl_string = ele.readline().strip("\n").upper().lower()

ele.close()

for ele_line in range(len(ele_list)) :
    temp_comp=ele_list[ele_line]
    if  temp_comp in fl_list :
        found_list.append(ele_list[ele_line])
    else :
        not_found_list.append(ele_list[ele_line])
correct_ans = int(len(found_list))*20
print (correct_ans," %"," correct")
print("Elements found : ",' '.join(found_list).title())
print("Elements not found: ",' '.join(not_found_list).title())