def permutations(route, ports):
    if len(ports) > 0:
        for port in ports:
            temp_route = route.copy()
            temp_route.append(port)
            temp_port = ports.copy()
            temp_port.remove(port)
            permutations(temp_route, temp_port)
    else:
        print(' '.join([portnames[x] for x in route]))
        return


portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

permutations([0], list(range(1, len(portnames))))



# def permutations(route, ports):
#     if len(ports) < 1:
#         print(' '.join([portnames[i] for i in route]))
#     else:
#         for i in range(len(ports)):
#             permutations(route+[ports[i]], ports[:i]+ports[i+1:])
#
# permutations([0], list(range(1, len(portnames))))

