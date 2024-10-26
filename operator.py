operatorpy = "menghitung nilai"
print (operatorpy)

uts = float(input("78:"))
uas = float(input("77:"))
nilai_akhir = (uts*0.4) + (uas*0.6)
if nilai_akhir >= 70:
    print("Selamat, Anda LULUS!")
else:
     print("Maaf, Anda TIDAK LULUS!")

if nilai_akhir >= 80:
     predikat = "A" 
elif nilai_akhir >= 70:
     predikat = "C"
elif nilai_akhir >= 60:
     predikat = "C"
else:
     predikat = "D"

print ("nilai_akhir")
print ("predikat")

