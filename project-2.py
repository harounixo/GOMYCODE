def remove_match_char(list1, list2):
 
    for i in range(len(list1)) :
        for j in range(len(list2)) :

            if list1[i] == list2[j] :
                c = list1[i] 

                list1.remove(c)
                list2.remove(c)

                list3 = list1 + [""] + list2
 
                return [list3, True]
 
    list3 = list1 + [""] + list2
    return [list1, list2]
