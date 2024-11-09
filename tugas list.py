#type Mhs
def MakeMhs(nim, nama, kelas, nilai):
    return [nim, nama, kelas, nilai]

# konso: List -> List
# Konso(e, L) menambahkan elemen e di depan list L
# Realisasi
def Konso(e, L):
    return [e] + L

# konslo: List -> List
# Konslo(L2, L1) menambahkan list L2 di depan list L1
# Realisasi
def Konslo(L2, L1):
    return [L2] + L1

# konsi: List, Elemen -> List
# Konsi(L, e) menambahkan elemen e di akhir list L
# Realisasi
def Konsi(L, e):
    return L + [e]

# konsli: List, List -> List
# Konsli(L1, L2) menggabungkan dua list L1 dan L2 dengan L2 di akhir L1
# Realisasi
def Konsli(L1, L2):
    return L1 + [L2]

# FirstElmt: List -> Elemen
# FirstElmt(L) mengembalikan elemen pertama dari list L
# Realisasi
def FirstElmt(L):
    return L[0]

# LastElmt: List -> Elemen
# LastElmt(L) mengembalikan elemen terakhir dari list L
# Realisasi
def LastElmt(L):
    return L[-1]

# Tail: List -> List
# Tail(L) mengembalikan list tanpa elemen pertama
# Realisasi
def Tail(L):
    return L[1:]

# Head: List -> List
# Head(L) mengembalikan list tanpa elemen terakhir
# Realisasi
def Head(L):
    return L[:-1]

# get_nim: List -> String
# get_nim(mhs) mengembalikan nim (ID mahasiswa) dari list data mahasiswa
# Realisasi
def get_nim(mhs):
    return mhs[0]

# get_nama: List -> String
# get_nama(mhs) mengembalikan nama mahasiswa dari list data mahasiswa
# Realisasi
def get_nama(mhs):
    return mhs[1]

# get_kelas: List -> String
# get_kelas(mhs) mengembalikan kelas mahasiswa dari list data mahasiswa
# Realisasi
def get_kelas(mhs):
    return mhs[2]

# get_nilai: List -> List of integers
# get_nilai(mhs) mengembalikan nilai mahasiswa dari list data mahasiswa
# Realisasi
def get_nilai(mhs):
    return mhs[3]

# IsEmpty: List -> Boolean
# IsEmpty(L) mengembalikan True jika list kosong, False jika tidak
# Realisasi
def IsEmpty(L):
    return L == []

# NbElmt: List -> Integer
# NbElmt(L) mengembalikan jumlah elemen dalam list L
# Realisasi
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))

# SumElmt: List of integers -> Integer
# SumElmt(L) mengembalikan jumlah semua elemen dalam list L
# Realisasi
def SumElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))

# AvgElmt: List of integers -> Float
# AvgElmt(L) mengembalikan rata-rata elemen dalam list L
# Realisasi
def AvgElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return SumElmt(L) / NbElmt(L)

# RataRataMhs: List of list -> Float
# RataRataMhs(L) menghitung rata-rata nilai mahasiswa
# Realisasi
def RataRataMhs(L):
    return AvgElmt(get_nilai(L))

# MaxElmt: List of integers -> Integer
# MaxElmt(L) mengembalikan elemen terbesar dalam list L
# Realisasi
def MaxElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return max(FirstElmt(L), MaxElmt(Tail(L)))

# MahasiswaLulus: List of list -> List of list
# MahasiswaLulus(SetL) mengembalikan list mahasiswa yang lulus (rata-rata >= 70)
# Realisasi
def MahasiswaLulus(SetL):
    if IsEmpty(SetL):
        return []
    elif RataRataMhs(FirstElmt(SetL)) >= 70:
        return Konso(FirstElmt(SetL), MahasiswaLulus(Tail(SetL)))
    else:
        return MahasiswaLulus(Tail(SetL))

# MahasiswaTIdakMengerjakan: List of list, String -> List of list
# MahasiswaTidakMengerjakan(SetL, kelas) mengembalikan list mahasiswa yang tidak mengerjakan tugas di kelas tertentu
# Realisasi
def MahasiswaTidakMengerjakan(SetL, kelas):
    if IsEmpty(SetL):
        return []
    elif get_kelas(FirstElmt(SetL)) == kelas:
        if IsEmpty(get_nilai(FirstElmt(SetL))):
            return Konso(FirstElmt(SetL), MahasiswaTidakMengerjakan(Tail(SetL), kelas))
        else:
            return MahasiswaTidakMengerjakan(Tail(SetL), kelas)
    else:
        return MahasiswaTidakMengerjakan(Tail(SetL), kelas)

# func: List of list -> Integer
# NilaiTertinggi(SetL) mengembalikan nilai tertinggi dari semua mahasiswa dalam list
# Realisasi
def NilaiTertinggi(SetL):
    if IsEmpty(SetL):
        return 0
    else:
        return max(MaxElmt(get_nilai(FirstElmt(SetL))), NilaiTertinggi(Tail(SetL)))

# MahasiswaTertinggi: List of list-> Student record
# MahasiswaTertinggi(SetL, kelas) mengembalikan mahasiswa dengan nilai tertinggi di kelas tertentu
# Realisasi
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

# JumlahMahasisawaTidakMengerjakan: List of list -> Integer
# JumlahMahasiswaTidakMengerjakan(SetL) menghitung jumlah mahasiswa yang tidak mengerjakan tugas
# Realisasi
def JumlahMahasiswaTidakMengerjakan(SetL):
    if IsEmpty(SetL):
        return 0
    elif get_nilai(FirstElmt(SetL)) == []:
        return 1 + JumlahMahasiswaTidakMengerjakan(Tail(SetL))
    else:
        return JumlahMahasiswaTidakMengerjakan(Tail(SetL))

# JumlahMahasiswaLulus: List of lists -> Integer
# JumlahMahasiswaLulus(SetL) menghitung jumlah mahasiswa yang lulus
# Realisasi
def JumlahMahasiswaLulus(SetL):
    if IsEmpty(SetL):
        return 0
    elif RataRataMhs(FirstElmt(SetL)) >= 70:
        return 1 + JumlahMahasiswaLulus(Tail(SetL))
    else:
        return JumlahMahasiswaLulus(Tail(SetL))
        
def SetMhs(L):
    return [L]

# NewSetMhs: List of list -> List of list
# NewSetMhs(NewL, L) menambahkan mahasiswa baru ke dalam set mahasiswa
# Realisasi
def NewSetMhs(NewL, L):
    return Konslo(NewL, L)

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
print(f"Himpunan mahasiswa : {e}")

print(f"MahasiswaLulus(h) = {MahasiswaLulus(h)}")
print(f"MahasiswaLulus(h) = {MahasiswaLulus(e)}")

print(f"MahasiswaTidakMengerjakan(h, 'C') = {MahasiswaTidakMengerjakan(h, 'C')}")
print(f"MahasiswaTidakMengerjakan(h, 'C') = {MahasiswaTidakMengerjakan(e, 'C')}")

print(f"NilaiTertinggi(h) = {NilaiTertinggi(h)}")
print(f"NilaiTertinggi(h) = {NilaiTertinggi(e)}")

print(f"MahasiswaTertinggi(h,'C') = {MahasiswaTertinggi(h,'C')}")
print(f"MahasiswaTertinggi(h,'C') = {MahasiswaTertinggi(e,'C')}")

print(f"JumlahMahasiswaTidakMengerjakan(h) = {JumlahMahasiswaTidakMengerjakan(h)}")
print(f"JumlahMahasiswaTidakMengerjakan(h) = {JumlahMahasiswaTidakMengerjakan(e)}")

print(f"JumlahMahasiswaLulus(h) = {JumlahMahasiswaLulus(h)}")
print(f"JumlahMahasiswaLulus(h) = {JumlahMahasiswaLulus(e)}")

# a = SetMhs([], MakeMhs('225', 'Budi', 'B', [85, 75, 0]))
# b = SetMhs(a, MakeMhs('123', 'Caca', 'C', [90, 80, 70]))
# c = SetMhs(b, MakeMhs('234', 'Andi', 'C', []))
# e = SetMhs(c,MakeMhs('124', 'Thoriq', 'C', [90, 80, 100]))

# """
# SetMhs(SetMhs(SetMhs(SetMhs([], MakeMhs('225', 'Budi', 'B', [85, 75, 0])), 
#                      MakeMhs('123', 'Caca', 'C', [90, 80, 70])), 
#               MakeMhs('234', 'Andi', 'C', [])), 
#        MakeMhs('124', 'Thoriq', 'C', [90, 80, 33]))
# """
# #kalau mau pemanggilan tanpa variable
# print(f"Himpunan mahasiswa : {e}")

# print(f"MahasiswaLulus(h) = {MahasiswaLulus(e)}")

# print(f"MahasiswaTidakMengerjakan(h, 'C') = {MahasiswaTidakMengerjakan(e, 'C')}")

# print(f"NilaiTertinggi(h) = {NilaiTertinggi(e)}")

# print(f"MahasiswaTertinggi(h,'C') = {MahasiswaTertinggi(e,'C')}")

# print(f"JumlahMahasiswaTidakMengerjakan(h) = {JumlahMahasiswaTidakMengerjakan(e)}")

# print(f"JumlahMahasiswaLulus(h) = {JumlahMahasiswaLulus(e)}")
