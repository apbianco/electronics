import math;

###############################################################################
# Self explanatory: return scaled input, convert input to scale.
###############################################################################

def Nano(x):
    return Micro(x)/1000.0

def Micro(x):
    return Mili(x)/1000.0

def Mili(x):
    return x/1000.0

def Kilo(x):
    return x*1000.0

def Mega(x):
    return Kilo(x)*1000.0

def ToNano(x):
    return x/Nano(1)

def ToMicro(x):
    return x/Micro(1)

def ToMili(x):
    return x/Mili(x)

def ToKilo(x):
    return x/Kilo(1)

def ToMega(x):
    return x/Mega(1)

def ToKiloOhm(x):
    return '{:.3g} KOhm'.format(ToKilo(x))

def ToMicroF(x):
    return '{:.3g} uF'.format(ToMicro(x))

def ToMiliV(x):
    return '{:.3g} mV'.format(ToMili(x))

def ToKHz(x):
    return '{:.3g} KHz'.format(ToKilo(x))

###############################################################################
# Convert X into its most convenient unit, return the value of X in
# that discovered unit and the letter designating the unit.
###############################################################################

def Unit(x):
    units = {Nano(1):  'n',
             Micro(1): 'u',
             Mili(1):  'm',
             1:        '',
             Kilo(1):  'K',
             Mega(1):  'M'}
    unit = Nano(1)
    done = False
    while not done:
        if x/unit < 1000:
            return ('{:.3g}'.format(x/unit), units[unit])
            done = True
        unit *= 1000

###############################################################################
# Print the 2 or 3 color bands and the color of the multiplier ring for the
# value of R. 
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
    elif Bands == 4:
        last = 2
    else:
       print('Can not handle bands=', Bands)
       return None

    colors = []
    for stripe in stripes[0:last]:
        colors.append(values[stripe])
    colors.append('|')
    value = int(stripes[0:last])
    mult = int(R/value)
    colors.append(multipliers[mult])
    return ' '.join(colors)

# Print the colors corresponding to R, also print R in the most
# convenient unit. Usage:
#
#   PrintRColor(2200000))
#   PrintRColor(Mega(2.2))
# 
#   2.2M Ohms: Red Red Black | Yellow
#
#
# A 2.2M Ohms resistor with 5 bands is labled Red/Red/Back and the
# multiplier ring is Yellow.

def PrintRColor(R, Bands=5):
    v, u = Unit(R)
    f = float(v)
    if f - int(f) == 0:
        v = int(f)
    c = RValueToColors(R)
    if not c:
        print('Can not convert {:} to color bands!'.format(R))
    print('{:}{:} Ohms: {:}'.format(v, u, c))

###############################################################################
# Cut off frequency for a RC circuit
###############################################################################
def FC(R, C, Conv=None):
    f = 1/(2*math.pi*R*C)
    return Conv(f) if Conv else f

###############################################################################
# Simple resistor divider bridge
###############################################################################
def Bridge(Vin, R1, R2, Conv=None):
    Vo = Vin*R2/(R1+R2)
    return Conv(Vo) if Conv else Vo

###############################################################################
# Polarization for a NPN transistor of gain Beta
#
# TODO: Use parameters, compute regime once Ib and Vce are known
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
# print (ToMicroF(Nano(55)))
# print (ToKiloOhm(470*100))
PrintRColor(Mega(2.2))
