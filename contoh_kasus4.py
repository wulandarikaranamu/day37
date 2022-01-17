nama = input("masukkan nama anda :")
nim = int(input("masukkan nim anda :"))
jumlah_matkul = int(input("masukkan jumlah mata kuliah :"))

for i in range(0,jumlah_matkul):
    nama_matkul = input("masukkan nama mata kuliah :")
    sks = int(input("masukkan jumlah sks permata kuliah :"))
    nilai = int(input("masukkan nilai mata kuliah :"))

if nilai >= 80 and nilai < 100 :
    bobot_angka = 4
    print(f"nilai anda dimata kuliah {nama_matkul} adalah A")
else:
    if nilai >= 65 and nilai < 79 :
        bobot_angka = 3
        print(f"nilai anda dimata kuliah {nama_matkul} adalah B")
    else:
        if nilai >= 55 and nilai < 64 :
            bobot_angka = 2
            print(f"nilai anda dimata kuliah {nama_matkul} adalah C")
        else:
            if nilai < 55 :
                bobot_angka = 0
                print(f"nilai anda dimata kuliah {nama_matkul} adalah D")

total_bobot = bobot_angka*sks
total_sks = sks + jumlah_matkul
ipk = total_bobot/total_sks
print(total_sks)

if ipk >= 35 and ipk <= 4 :
    print("PREDIKAT DENGAN PUJIAN")
elif ipk >= 3 and ipk <= 3.49 :
    print("PREDIKAT SANGAT MEMUASKAN")
elif ipk >= 2.5 and ipk <= 2.99 :
    print("PREDIKAT MEMUASKAN")
else:
    print("PREDIKAT LULUS")

print(f"total ipk anda adalah {ipk}")

   
        
    
