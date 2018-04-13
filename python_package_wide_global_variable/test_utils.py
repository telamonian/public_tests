__all__ = ['flags', 'summation']



class Flags(object):
    def __init__(self, *items):
        for key,val in zip(items[:-1], items[1:]):
            setattr(self,key,val)

flags = Flags('debug', True)

def summation(x, y, z):
    if flags.debug:
        print 'I am going to add %s %s and %s' % (x, y, z)
    return x + y + z
