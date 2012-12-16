from semestr.settings import STATIC_ROOT

def savetofile(code, name):
    file = open(STATIC_ROOT + '//%s.txt' % name,'w')
    file.write(str(code))
    file.close()
def savedict(binary_dict, name):
    file = open(STATIC_ROOT + '//%s.txt' % name,'w')
    temp = ''.join([str(k) + ':' + str(v) + ';' for k,v in binary_dict.iteritems()])
    file.write(temp)
    file.close()