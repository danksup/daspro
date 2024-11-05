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


def MakeMhs(nim, nama, kelas, nilai):
    return (nim, nama, kelas, nilai)

mhs1 = MakeMhs('234', 'Andi', 'C', [])
mhs2 = MakeMhs('123', 'Caca', 'C', [90, 80, 100])
mhs3 = MakeMhs('123', 'Budi', 'B', [85, 75, 95]) 

set_mhs = []


def SetMhs(set_mhs, new_mhs):
    if IsEmpty(set_mhs):
        return [new_mhs]  
    elif get_nim(FirstElmt(set_mhs)) == get_nim(new_mhs):
        return set_mhs  
    else:
        return Konso(FirstElmt(set_mhs), SetMhs(Tail(set_mhs), new_mhs))


set_mhs = SetMhs(set_mhs, mhs1) 
set_mhs = SetMhs(set_mhs, mhs2)  
set_mhs = SetMhs(set_mhs, mhs3)  

print(set_mhs)

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

    
print(TidakMengerjakanQuiz(set_mhs, 'C'))
#test rayyan