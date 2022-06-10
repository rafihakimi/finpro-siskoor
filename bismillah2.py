
import numpy as np
from numpy import degrees, radians

class olahdata:
    def __init__(self, asal, tujuan, koordinat):
        self.asal = asal
        self.tujuan = tujuan
        self.koordinat = koordinat

    def kartesiketujuan(self):                                      #mengubah dari koordinat kartesi ke tujuan
        global koordinat
        if self.tujuan == 1 or self.tujuan == 3:
            print('koordinat',koordinat)
        else:
            if self.tujuan == 5:
                for i in range(len(koordinat)):
                    koordinat[i][0] = np.linalg.norm(a[i])
                    koordinat[i][1] = (degrees(np.arctan(radians((np.hypot(a[i, 0], a[i, 1])) / (a[i, 2] ** 2)))) if a[i,2] != 0 else 'tak hingga')
                    koordinat[i][2] = (degrees(np.arctan(radians(a[i, 1] / a[i, 0]))) if a[i,0] != 0 else 'tak hingga')
            elif self.tujuan == 4 or self.tujuan == 3:
                for i in range(len(koordinat)):
                    koordinat[i][0] = np.hypot(a[i, 0], a[i, 1])
                    koordinat[i][1] = (degrees(np.arctan(radians(a[i, 1] / a[i, 0]))) if a[i,0] != 0 else 'tak hingga')
                    if self.tujuan == 4:
                        koordinat[i][2] = a[i, 2]


    def hitung(self):                                               #mengubah data yang di input ke kartesian 3 dimensi
        global a
        a = np.array(self.koordinat)
        if self.asal != 1 or self.asal != 3:
            for i in range(len(a)):
                if self.asal == 2:
                    koordinat[i][0] = a[i, 0] * np.cos(radians(a[i, 1]))
                    koordinat[i][1] = a[i, 0] * np.sin(radians(a[i, 1]))
                elif self.asal == 1:
                    koordinat[i][0] = a[i, 0]
                    koordinat[i][1] = a[i, 1]
                elif self.asal == 4:
                    koordinat[i][0] = a[i, 0] * np.cos(radians(a[i, 1]))
                    koordinat[i][1] = a[i, 0] * np.sin(radians(a[i, 1]))
                elif self.asal == 5:
                    koordinat[i][0] = a[i, 0] * np.sin(radians(a[i, 1])) * np.cos(radians(a[i, 2]))
                    koordinat[i][1] = a[i, 0] * np.sin(radians(a[i, 1])) * np.sin(radians(a[i, 2]))
                    koordinat[i][2] = a[i, 0] * np.cos(radians(a[i, 2]))
            if self.tujuan == 3 or self.tujuan == 1:
                pass
            else:
                olahdata.kartesiketujuan(self)
        else:
            if self.tujuan == 3 or self.tujuan == 1:
                pass
            else:
                olahdata.kartesiketujuan(self)
        return '\nJika koordinat {koorawal} pada sistem koordinat {asalsiskoor} \ndiubah menjadi sistem koordinat {t} maka akan koordinatnya akan menjadi \n' \
               '{n}'.format(n=koordinat, asalsiskoor=nama[asal-1], t=nama[tujuan-1], koorawal=a.tolist())

def inputdata():
    global asal, tujuan, koor, nama, koordinat
    print('Daftar jenis koordinat yang dapat dipilih')
    print('1. kartesi 2D')
    print('2. polar 2D')
    print('3. kartesi 3D')

    print('4. 3D silindrical')
    print('5. 3D sperical')

    asal = int(input('Masukkan nomor dari sistem koordinat yang ingin diubah : '))
    jumlahtitik = int(input('Berapa banyak titik yang ingin diubah : '))
    tujuan = int(input('Masukkan nomor ke sistem koordinat yang ingin didefinisikan : '))

    if asal > 5 or asal < 1 or tujuan > 5 or tujuan < 1:
        print('Nomor yang anda masukkan tidak ada di dalam pilihan')

    elif asal == tujuan:
        print('Koordinat awal dan koordinat akhir anda sama')

    else:
        koor = [['x', 'y'], ['r', 'θ'], ['x', 'y', 'z'], ['r', 'θ', 'z'], ['r', 'θ', 'phi']]
        nama = ['Kartesi 2 Dimensi', 'Polar 2 Dimensi', 'Kartesi 3 Dimensi', 'Silindrikal 3 Dimensi',
                'Spherical 3 Dimensi']

        koordinat = []
        for i in range(jumlahtitik):
            koordinat.append([0])
        for i in range(jumlahtitik):
            for j in range(1 if tujuan == 1 or tujuan == 2 else 2):
                koordinat[i].append(0)

        for n in range(jumlahtitik):
            for i, j in (enumerate(koor[asal - 1])):
                titikasal = (input('Masukkan titik ke {no} {k} dari sistem koordinat {siskoorasal} : '.format(k=j, no=n+1, siskoorasal=nama[asal - 1])))

                try:
                    koordinat[n][i] = float(titikasal)
                except ValueError:
                    print('Data yang anda masukkan bukan angka\nMengulang Program\n')
                    inputdata()

        coba1 = olahdata(asal, tujuan, koordinat)
        print(coba1.hitung())

    opsi = int(input('\nApakah masih ada yang ingin ada ubah\n1 untuk Ya, selain 1 untuk Mengakhiri Program\nMasukkan angka : '))
    if opsi == 1:
        print()
        inputdata()
    else:
        print('Program Berakhir\nTerimakasih')
        exit()
inputdata()