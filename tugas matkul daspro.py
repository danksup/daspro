set_mhs = []

def Konso(e,L):
    return [e] + L

def FirstElmt(lst):
    return lst[0]

def Tail(lst):
    return lst[1:] 

def IsEmpty(lst):
    return lst == []

def get_nim(mhs):
    return FirstElmt(mhs)

def get_nama(mhs):
    return FirstElmt(Tail(mhs))

def get_kelas(mhs):
    return FirstElmt(Tail(Tail(mhs)))

def get_nilai(mhs):
    return FirstElmt(Tail(Tail(Tail(mhs))))

def AvgElmt(L):
    if L == []:
        return 1 
    else:
        return FirstElmt(L) / AvgElmt(Tail(L))
    
def MaxElmt(L):
    if OneElmt(L):
        return (FirstElmt(L))
    else:
        return MaxElmt(Tail(L))

def OneElmt(L):
    return NbElmt(L) == 1

def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))

def MakeMhs(nim, nama, kelas, nilai):
    return (nim, nama, kelas, nilai)

mhs1 = MakeMhs('234', 'Andi', 'C', [])
mhs2 = MakeMhs('123', 'Caca', 'C', [90, 80, 100])
mhs3 = MakeMhs('123', 'Budi', 'B', [85, 75, 95]) 

set_mhs = []

# MakeMhs: <string, string, character, list of integer> -> Mhs 

#   {MakeMhs(nim, nama, kelas, nilai) membentuk sebuah mahasiswa 
#   dengan dengan nim, nama, kelas dan nilai berbentuk list of integer. 

#   Contoh: 
#   MakeMhs(‘234’, ‘Andi’, ‘C’, []) membentuk mahasiswa dengan nim ‘234’,nama ‘Andi’ dari kelas C, 
#   dan belum pernah mengerjakan kuis (nilainya berupa list kosong).

#   MakeMhs(‘123’, ‘Caca’, ‘C’, [90,80,100]) membentuk mahasiswa dengan 
#   nim ‘123’, nama ‘CC’ dari kelas C, dan telah mengerjakan kuis sebanyak tiga kali 
#   dengan nilai masing-masing adalah 90, 80, dan 100. }

def SetMhs(set_mhs, new_mhs):
    if IsEmpty(set_mhs):
        return [new_mhs]  
    elif get_nim(FirstElmt(set_mhs)) == get_nim(new_mhs):
        return set_mhs  
    else:
        return Konso(FirstElmt(set_mhs), SetMhs(Tail(set_mhs), new_mhs))

def SiswaLolos(set_mhs):
    if IsEmpty(set_mhs):
        return []
    if AvgElmt(get_nilai(FirstElmt(set_mhs))) >= 70:
        return Konso(FirstElmt(set_mhs), SiswaLolos(Tail(set_mhs)))
    else:
        return SiswaLolos(Tail(set_mhs))
    
def TidakMengerjakanQuiz(set_mhs, kelas):
    if IsEmpty(set_mhs):
        return []
    if get_kelas( FirstElmt(set_mhs)) == kelas and IsEmpty(get_nilai( FirstElmt(set_mhs))):
        return Konso( FirstElmt(set_mhs), TidakMengerjakanQuiz(Tail(set_mhs), kelas))
    else:
        return TidakMengerjakanQuiz(Tail(set_mhs), kelas)
    
def NilaiTertinggi(set_mhs):
    if IsEmpty(set_mhs):
        return 0
    else:
        if IsEmpty(get_nilai(FirstElmt(set_mhs))):
            return max(0, NilaiTertinggi(Tail(set_mhs)))
        else:
            return max(MaxElmt(get_nilai(FirstElmt(set_mhs))), NilaiTertinggi(Tail(set_mhs)))

def SiswaNilaiTertinggi(set_mhs, kelas):
    if IsEmpty(set_mhs):
        return None
    else:
        if get_kelas(FirstElmt(set_mhs)) == kelas:
            if SiswaNilaiTertinggi(Tail(set_mhs), kelas) is None or MaxElmt(get_nilai(FirstElmt(set_mhs))) > MaxElmt(get_nilai(SiswaNilaiTertinggi(Tail(set_mhs), kelas))):
                return FirstElmt(set_mhs)
            else:
                return SiswaNilaiTertinggi(Tail(set_mhs), kelas)
        else:
            return SiswaNilaiTertinggi(Tail(set_mhs), kelas)

def JumlahLulus(set_mhs):
    if IsEmpty(set_mhs):
        return 0
    else:
        if AvgElmt(get_nilai(FirstElmt(set_mhs))) >= 70:
            return 1 + JumlahLulus(Tail(set_mhs))
        else:
            return JumlahLulus(Tail(set_mhs))

def JumlahTidakMengerjakan(set_mhs):
    if IsEmpty(set_mhs):
        return 0
    else:
        if IsEmpty(get_nilai(FirstElmt(set_mhs))):
            return 1 + JumlahTidakMengerjakan(Tail(set_mhs))
        else:
            return JumlahTidakMengerjakan(Tail(set_mhs))

set_mhs = SetMhs(set_mhs, MakeMhs('234', 'Andi', 'C', [])) 
set_mhs = SetMhs(set_mhs, MakeMhs('123', 'Caca', 'C', [90, 80, 100]))  
set_mhs = SetMhs(set_mhs, MakeMhs('225', 'Budi', 'B', [85, 75, 95]) )  

print(SiswaLolos(set_mhs))
print(TidakMengerjakanQuiz(set_mhs,'C'))
print(SiswaNilaiTertinggi(set_mhs, 'A'))
print(NilaiTertinggi(set_mhs))
print(JumlahTidakMengerjakan(set_mhs))
print(JumlahLulus(set_mhs))
