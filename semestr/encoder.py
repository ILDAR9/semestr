def divide(nodes_dict, l_index, r_index):
    if ((r_index - l_index) == 1):
    #        add_prefix(nodes_dict,l_index,l_index+1,'1')
        return
    elif (r_index <= l_index):
        return
    spl_index = l_index + (r_index - l_index) / 2
    #    print "split index = %d" % spl_index
    l_sum = sum([x._freak for x in nodes_dict[l_index: spl_index]])
    r_sum = sum([x._freak for x in nodes_dict[spl_index:r_index]])
    while True:
        delta = l_sum - r_sum
        #        print "delta = %d" % delta
        if (delta < 0):
            l_sum = l_sum + nodes_dict[spl_index]._freak
            r_sum = r_sum - nodes_dict[spl_index]._freak
            spl_index_temp = spl_index + 1
        elif (delta > 0):
            spl_index_temp = spl_index - 1
            l_sum = l_sum - nodes_dict[spl_index_temp]._freak
            r_sum = r_sum + nodes_dict[spl_index_temp]._freak
        if (abs(delta) > abs(l_sum - r_sum)):
            spl_index = spl_index_temp
        else:
            add_state(nodes_dict, l_index, spl_index, '1')
            #            print "left: %s" % nodes_dict[l_index: spl_index]
            divide(nodes_dict, l_index, spl_index)
            add_state(nodes_dict, spl_index, r_index, '0')
            #            print "right: %s" % nodes_dict[spl_index:r_index]
            divide(nodes_dict, spl_index, r_index)
            return

#            return {"left":[x for x in srt_dict[l_index:spl_index]],"right":[x for x in srt_dict[spl_index:r_index]]}

def add_state(nodes_dict, start, end, bin_state):
    for index in range(start, end):
        temp = nodes_dict[index]
        temp.addCode(bin_state)


def sort(dict):
    return sorted(list(dict.items()), key=lambda item: item[1], reverse=True)


class Node:
    _code = ""
    _signal = 0
    _freak = 0

    def __init__(self, item):
        self._signal = item[0]
        self._freak = item[1]

    def __repr__(self):
        return "Node(%d)-%s" % (self._signal, self._code)

    def addCode(self, bin_state):
        self._code = self._code + bin_state


def get_encoded_dict(dict):
    srt_dict = sort(dict)
    nodes_dict = [Node(x) for x in srt_dict]
    divide(nodes_dict, 0, len(nodes_dict))
    return {node._signal: node._code for node in nodes_dict}


def encode(signals, map):
    dec_code = get_encoded_dict(map)
    return (''.join([str(dec_code[x]) for x in signals]) if len(dec_code) > 1 else '1' * len(signals),
            dict((v, k) for k, v in dec_code.iteritems()))


def size_list_to_str(temp):
    return sum(map(lambda x: len(str(x)), temp)) + len(temp)


