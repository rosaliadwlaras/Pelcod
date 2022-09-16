print('Program menghitung luas, keliling, volume balok dan kubus ')

print('BALOK')
p = int(input('masukkan panjang balok: '))
l = int(input('masukkan lebar balok: '))
t = int(input('masukkan tinggi balok: '))

def luas_permukaan(p,l,t):
    L = 2 * ( (p*l) + (p*t) + (l*t) )
    return L

def volume(p,l,t):
    V = p*l*t
    return V

def keliling(p,l,t):
    K = 4 * (p+l+t)
    return K

print('jadi balok dengan panjang: {}, lebar: {}, tinggi: {}, \nMempunyai luas: {}, volume: {}, keliling: {}' .format(p,l,t, luas_permukaan(p,l,t), volume(p,l,t),  keliling(p,l,t)))

print('KUBUS')
s = int(input('masukkan sisi kubus: '))

def Luas_permukaan(s):
    L= 6 * ( s*s )
    return L

def Volume(s):
    V = s*s*s
    return V

def Keliling(s):
    K = 4 * s
    return K

print('jadi balok dengan sisi:{}, \nMempunyai luas: {}, volume: {}, keliling: {} ' .format(s, Luas_permukaan(s), Volume(s),  Keliling(s)))