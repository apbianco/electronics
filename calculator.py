import math;

###############################################################################

def Mili(x):
    return x/1000.0

def Micro(x):
    return Mili(x)/1000.0

def Nano(x):
    return Micro(x)/1000.0

def ToMili(x):
    return x/Mili(x)

def ToMicro(x):
    return x/Micro(1)

def ToNano(x):
    return x/Nano(1)

###############################################################################

def Kilo(x):
    return x*1000.0

def Mega(x):
    return Kilo(x)*1000.0

def ToKilo(x):
    return x/Kilo(1)

def ToMega(x):
    return x/Mega(1)

###############################################################################

def ToKiloOhm(x):
    return '{:.2f} KOhm'.format(ToKilo(x))

def ToMicroF(x):
    return '{:.2f} uF'.format(ToMicro(x))

def ToMiliV(x):
    return '{:.2f} mV'.format(ToMili(x))

def ToKHz(x):
    return '{:.2f} KHz'.format(ToKilo(x))

###############################################################################

def RValueToColors(R, Bands=5):
    stripes = str(int(R));
    values = {'0': 'Black',  '1': 'Brown',  '2': 'Red',
              '3': 'Orange', '4': 'Yellow', '5': 'Green',
              '6': 'Blue',   '7': 'Violet', '8': 'Grey', '9': 'White'}
    multipliers = {1: 'Black',      10: 'Brown',     100: 'Red',
                   1000: 'Orange',  10000: 'Yellow', 100000: 'Green',
                   1000000: 'Blue', 10000000: 'Violet'}
    if Bands == 5:
        last = 3
    if Bands == 4:
        last = 2
    else:
       print('Can not handle bands=', Bands)

    colors = []
    for stripe in stripes[0:last]:
        colors.append(values[stripe])
    colors.append('|')
    value = int(stripes[0:last])
    mult = int(R/value)
    colors.append(multipliers[mult])
    print(' '.join(colors))

###############################################################################

def FC(R, C, Conv=None):
    f = 1/(2*math.pi*R*C);
    return Conv(f) if Conv else f

def Bridge(Vin, R1, R2, Conv=None):
    Vo = Vin*R2/(R1+R2)
    return Conv(Vo) if Conv else Vo

###############################################################################
#
# Transistor polarization for a NPN transistor of gain Beta
#
#     Vcc -+--------+-
#          |        |        
#          R1       RC
#          |      |/   C
#          +----B-|     
#          |      |\   E
#          |        v 
#          |        |
#          R2       RE
#          |        |
#    Gnd  -+--------+-

def Q():
    R1 = 300.0*1000
    R2 = 500.9
    RC = 4,7*1000
    RE = 2.0*1000
    Beta = 200
    K = Beta+1
    Vcc = 10.0

    N = (0.7/R1) + (0.7/R2) - (Vcc/R1)
    D = 1 + ((RE * K)/R1) + ((RE * K)/R2)

    IB = -N/D
    VE = RE*IB*(Beta+1)
    VB = VE+0.7
    print(VB*1000)
    print(IB*1000000)
    print(VE*1000)
    
# print (ToMiliV(1))
# print (Bridge(5, Kilo(16), Kilo(16), ToMiliV))
# print (FC(Kilo(16), Micro(0.01), ToKHz))
# print (ToMicroF(Nano(48)))
# print (ToKiloOhm(470*100))
print(RValueToColors(Kilo(100), Bands=5))

