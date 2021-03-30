def remove_elt(para):
    len_list = len(para)
    i = 0
    while True:
        len_list = len(para)
        if i > len_list-1:
            break
        else:
            if para.count(para[i]) > 1:
                li.pop(i)
                i -= 1
        i += 1

    para.sort()

    return para

li = ['a', 'a', 'b', 'c', 'd', 'b']

print(remove_elt(li))