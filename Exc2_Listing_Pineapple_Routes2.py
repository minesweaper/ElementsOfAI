def permutation(route, ports):
    if len(ports) > 1:
        perm_list = [] # resulting list
        for a in ports:
            remaining_elements = [x for x in ports if x != a]
            z = permutation(route, remaining_elements) # permutations of sublist
            for t in z:
                perm_list.append([a] + t)
        print(perm_list)
        return perm_list
    else:
        return [ports + route]


portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]


for b in permutation([0], list(range(1, len(portnames)))):
    print(' '.join([portnames[x] for x in b[::-1]]))
