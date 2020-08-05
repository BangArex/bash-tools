# Didecrypt pada: 05-08-2020  17:03:15
# Python bytecode 2.7 (62211)
# Didecrypt dengan: python 2.7.18 di platform linux2
# Decrypt by: AnonyMass AKA Zhu Bai Lee
# Embedded file name: <Sanz>

N = '\x1b[0m'
D = '\x1b[90m'
W = '\x1b[1;37m'
C = '\x1b[94m'
R = '\x1b[91m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
B = '\x1b[1;36m'
import os, sys, fileinput, time, socket, random, time, sys, platform, os

#texylt mengetik
def wr(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./15)


def bn(h):
	for d in h + '\n':
                sys.stdout.write(d)
                sys.stdout.flush()
                time.sleep(1./30)

wr( G + 'Install bahan dulu...')
wr( B + 'Loading...')
os.system('pkg install nodejs &> /dev/null;')
os.system('npm install -g bash-obfuscate &> /dev/null;')
os.system('termux-wake-lock;')
os.system('clear')

def tampil(x):
    w = {'m': 31, 'h': 32, 'k': 33, 'b': 34, 'p': 35, 'c': 36}
    for i in w:
        x = x.replace('\r%s' % i, '\x1b[%s;1m' % w[i])

    x += '\x1b[0m'
    x = x.replace('\r0', '\x1b[0m')
    print x


ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '\xe2\x88\x9a' + G + '] '
eror = R + '[' + W + '!' + R + ']'
print
os.system('figlet "Bash Tools"')
bn(C +'===================== '+ R +'====================='+ B)
print
bn('             #\x1b[92mAuthor   :\x1b[36;1mMRROBO28')
bn('             #\x1b[92mYoutube  :\x1b[36;1mTEKTRIKBOT CN')
bn('             #\x1b[92mgithub   :\x1b[36;1mhttps://github.com/MRROBO28')
bn('             #\x1b[92mInstagram:\x1b[36;1m@irshad_faqih')
print
bn('\x1b[92m===================== \x1b[95m=====================')
time.sleep(2)
print
print '\x1b[91m[1]\x1b[97mEncript'
print '\x1b[91m[2]\x1b[97mDecrypt'
print '\x1b[91m[0]\x1b[97mKeluar'

def keluar():
    tampil('\rm[!]Thanks for used my script')
    os.sys.exit()


def dekrip():
    try:
        sc = raw_input(ask + W + 'Masukan Alamat Input ' + G + '> ' + W)
        f = open(sc, 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace('eval', 'echo')
        out = raw_input(ask + W + 'Masukan Alamat Output' + G + ' > ' + W)
        f = open(out, 'w')
        f.write(newdata)
        f.close()
        os.system('touch decript.sh')
        os.system('bash ' + out + ' > decript.sh')
        os.remove(out)
        os.rename('decript.sh', out)
        print sukses + 'Berhasil..'
    except KeyboardInterrupt:
        print eror + ' Berhenti!'
    except IOError:
        print eror + ' File Tidak Terdeteksi!'


def enkrip():
    try:
        script = raw_input(ask + W + 'Masukan Alamat Script ' + G + '|> ' + W)
        output = raw_input(ask + W + 'Masukan Alamat Output ' + G + '|> ' + W)
        os.system('bash-obfuscate ' + script + ' -o ' + output)
        print sukses + 'Berhasil..'
    except KeyboardInterrupt:
        print eror + ' Berhenti!'
    except IOError:
        print eror + ' File Tidak Terdeteksi!'


takok = raw_input(W + 'Encript' + G + ' |> ')
if takok == '1' or takok == '01':
    enkrip()
elif takok == '2' or takok == '02':
    dekrip()
elif takok == '0' or tatok == '00':
    keluar()
else:
    print eror + ' Wrong input'
    keluar()

