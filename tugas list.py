#type Mhs
def MakeMhs(nim, nama, kelas, nilai):
    return [nim, nama, kelas, nilai]

#set mhs

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso: elemen, List -> List
# Konso(e, L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama # Realisasi
def Konso(e,L):
    return [e] + L

def Konslo(L2,L1):
    return [L2] + L1
# Konsi: List, elemen -> List
# Konsi(L,e) -> menghasilkan sebah list dari L dan e dengan e sebagai elemen terakhir # Realisasi
def Konsi(L,e):
    return L + [e]

def Konsli(L1,L2):
    return L1 + [L2]


# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: List tidak kosong -> elemen
# FirstElmt(L) Menghasilkan elemen pertama list L
# Realisasi
def FirstElmt(L):
    return L[0]

# LastElmt: List tidak kosong -> elemen
# LastElmt(L): mengembalikan elemen terakhir list L
# Realisasi
def LastElmt(L):
    return L[-1]

# Tail: List tidak kosong -> List
# Tail(L) : Menghasilkan list tanpa elemen pertama list L, mungkin kosong
# Realisasi
def Tail(L):
    return L[1:]

# Head: List tidak kosong -> List
# Head(L) : Menghasilkan list tanpa elemen terakhir list L, mungkin kosong
# Realisasi
def Head(L):
    return L[:-1]

def get_nim(mhs):
    return mhs[0]

def get_nama(mhs):
    return mhs[1]

def get_kelas(mhs):
    return mhs[2]

def get_nilai(mhs):
    return mhs[3]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty: List -> boolean
# IsEmpty(L) benar jika list kosong
# Realisasi
def IsEmpty(L):
    return L == []

# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
# NbElmt: List -> integer
# NbElmt(L): Menghasilkan banyaknya elemen list, nol jika kosong
# Realisasi
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))

# SumElmt: List of integer -> integer
# SumElmt(L) menghasilkan jumlahan dari setiap elemen di list L
def SumElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))

# AvgElmt: List of integer -> integer 
# AvgEmlt(L) menghasilkan nilai rata-rata
def AvgElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return SumElmt(L) / NbElmt(L)

def SetMhs(L):
    return [L]

def NewSetMhs(NewL, L):
    return Konslo(NewL, L)

def RataRataMhs(L):
    return AvgElmt(get_nilai(L))

def MahasiswaLulus(SetL):
    if IsEmpty(SetL):
        return []
    elif RataRataMhs(FirstElmt(SetL)) >= 70:
        return Konso(FirstElmt(SetL), MahasiswaLulus(Tail(SetL))) 
    else:
        return MahasiswaLulus(Tail(SetL))

def MahasiswaTidakMengerjakan(SetL, kelas):
    if IsEmpty(SetL):
        return []
    elif get_kelas(FirstElmt(SetL)) == kelas:
        if get_nilai(FirstElmt(SetL)) == []:
            return Konso(FirstElmt(SetL), MahasiswaTidakMengerjakan(Tail(SetL), kelas))
        else:
            return MahasiswaTidakMengerjakan(Tail(SetL), kelas)
    else:
        return MahasiswaTidakMengerjakan(Tail(SetL), kelas)

def MaxElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return max(FirstElmt(L),MaxElmt(Tail(L)))
    
def NilaiTertinggi(SetL):
    if IsEmpty(SetL):
        return 0
    else:
        return max(MaxElmt(get_nilai(FirstElmt(SetL))), NilaiTertinggi(Tail(SetL)))

def MahasiswaTertinggi(SetL, kelas):
    if IsEmpty(SetL):
        return []
    elif get_kelas(FirstElmt(SetL)) == kelas:
        if MaxElmt(get_nilai(FirstElmt(SetL))) >= MaxElmt(get_nilai(FirstElmt(Tail(SetL)))):
            return FirstElmt(SetL)
        else:
            return MahasiswaTertinggi(Tail(SetL), kelas)
    else:
        return MahasiswaTertinggi(Tail(SetL), kelas)
    
def JumlahMahasiswaTidakMengerjakan(SetL):
    if IsEmpty(SetL):
        return 0
    elif get_nilai(FirstElmt(SetL)) == []:
        return 1 + JumlahMahasiswaTidakMengerjakan(Tail(SetL))
    else:
        return JumlahMahasiswaTidakMengerjakan(Tail(SetL))

def JumlahMahasiswaLulus(SetL):
    if IsEmpty(SetL):
        return 0
    elif RataRataMhs(FirstElmt(SetL)) >= 70:
        return 1 + JumlahMahasiswaLulus(Tail(SetL))
    else:
        return JumlahMahasiswaLulus(Tail(SetL))


a = MakeMhs('234', 'Andi', 'C', [])
b = MakeMhs('123', 'Caca', 'C', [90, 80, 70])
c = MakeMhs('225', 'Budi', 'B', [85, 75, 0])
g = MakeMhs('124', 'Thoriq', 'C', [90, 80, 100])

#print(a)
d = SetMhs(a)
#print(d)
e = NewSetMhs(b,d)
#print(e)
f = NewSetMhs(c, e)
h = NewSetMhs(g,f)

print(f"Himpunan mahasiswa : {h}")

print(f"MahasiswaLulus(h) = {MahasiswaLulus(h)}")

print(f"MahasiswaTidakMengerjakan(h, 'C') = {MahasiswaTidakMengerjakan(h, 'C')}")

print(f"NilaiTertinggi(h) = {NilaiTertinggi(h)}")

print(f"MahasiswaTertinggi(h,'C') = {MahasiswaTertinggi(h,'C')}")

print(f"JumlahMahasiswaTidakMengerjakan(h) = {JumlahMahasiswaTidakMengerjakan(h)}")

print(f"JumlahMahasiswaLulus(h) = {JumlahMahasiswaLulus(h)}")
