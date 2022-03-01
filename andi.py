nama = "Andi"
hobi = ["makan", "sepeda", "coding"]

def sepeda():
    print("Andi pergi bersepeda")

def cekTiketPesawat(umur, saldo, harga):
    if (umur >= 17):
        print("boleh beli tiket karena umur", umur)
        if (saldo >= harga):
            print("bisa beli tiket karena saldo", saldo, "dan harga", harga)
        else:
            print("saldo tidak cukup")
    else:
        print("umur tidak cukup")
        
class Foo:
    pass


if(__name__ == "__main__"):
    import sys
    print(sys.argv)
    if (sys.argv[1]):
        if (sys.argv[1] == 'hobi'):
            print(hobi)
            
        if (sys.argv[1] == 'sepeda'):
            sepeda()
            
        if (sys.argv[1] == 'cek'):
            if (len(sys.argv)>4):
                a, b, c = [sys.argv[2], sys.argv[3], sys.argv[4]]
                cekTiketPesawat(int(a), int(b), int(c))
            else:
                print("fungsi cek memerlukan 3 required argumen: umur, saldo, harga_tiket")