import math

#tupple
tupple_rumus = (
    'L = S^2',
    'L = p x l',
    'L = (a x t) /2',
    'L = 2 x r x phi'

)

#list
rumus = ["1. persegi","2. Persegi Panjang","3. segitiga","4. lingkaran"]

while True :

    print("Pilih bangun datar untuk menghitung luas :")

    for i in rumus :
      print(i)

    r = input("\npilih bangun datar (1/2/3/4): ")

    #dictionary
    lrumus = {'1': 'persegi', '2': 'persegi panjang', '3': 'segitiga', '4': 'lingkaran'}

    if r in lrumus :
      keyr =lrumus[r]


      #boolean
      if keyr == 'persegi' :
        try :
          print("rumurs persegi = ", tupple_rumus[0])

          p = float(input("\nmasukkan panjang sisi : "))

          #integer
          L = float(p)**2
          print(f"\nLuas Persegi = {L}\n")
        
        # ni benda buat mastiin input user tu nomor
        except ValueError:
          print("Invalid input. masukkan input berupa angka.\n")


      elif keyr == 'persegi panjang' :
        try :
          print("rumurs persegi = ", tupple_rumus[1])

          p = float(input("\nmasukkan panjang : "))
          l = float(input("masukkan lebar : "))

          #integer
          L = float(p)*float(l)
          print(f"\nLuas Persegi = {L}\n")

        except ValueError:
          print("Invalid input. masukkan input berupa angka.\n")


      #boolean
      elif keyr == "segitiga" :
        try :
          print("rumurs segitiga = ", tupple_rumus[2])

          a = float(input("\nmasukkan alas : "))
          t = float(input("masukkan tinggi : "))

          #integer
          L = (float(a)*float(t))/2

          print(f"\nLuas segitiga = {L}\n")

        except ValueError:
          print("Invalid input. masukkan input berupa angka.\n")


      #boolean
      elif keyr == "lingkaran" :
        try :
          print("rumurs lingkaran = ", tupple_rumus[3])

          ra = float(input("\nmasukkan jari-jari : "))

          #integer
          L = (math.pi)*(float(ra)**2)
          print(f"\nLuas lingkaran = {L}\n")

        except ValueError:
          print("Invalid input. masukkan input berupa angka.\n")

    else :
      print("\ninvalid\n")