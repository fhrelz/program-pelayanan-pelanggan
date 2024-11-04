def main():
    while True:
        print("==========TOKO GAWAT DARURAT==========")
        Pembeli = input("Nama Pembeli : ")
        print("Nama Pembeli : ", Pembeli)

        def paket():
            global paket_makanan
            global porsi_paket
            global paket_menu
            print("\n==========MENU PAKET MAKANAN==========")
            print(''' ✿ PAKET 1                           - Rp.15000.00
                        (Nasi + Ayam Goreng + Es Teh)''')
            print(''' ✿ PAKET 2                           - Rp.17000.00
                        (Nasi + Ayam Geprek + Es Jeruk)''')
            print(''' ✿ PAKET 3                           - Rp.15000.00
                        (Nasi + Tumis Usus  + Es Lemon Tea)''')
            print(''' ✿ PAKET 4                           - Rp.10000.00
                        (Nasi + Sayur Bungga Pepaya + Es Teh)''')
            print(''' ✿ PAKET 5                           - Rp.13000.00
                        (Nasi + Mie Goreng Premium + Es Kopyor)''')
            print(''' ✿ PAKET 6                           - Rp.17000.00
                        (Mie Goreng + Ayam Geprek + Es Buah)''')


        def makanan():
            global totalmakanan
            global porsi
            global menu
            print("\n==========MENU MAKANAN==========")
            print(" ● Nasi               - Rp.3000.00")
            print(" ● Gorengan           - Rp.1000.00")
            print(" ● Sambal Pete        - Rp.2000.00")
            print(" ● Perkedel           - Rp.2000.00")
            print(" ● Pecel Gendar       - Rp.5000.00")
            print(" ● Aneka Tusukan      - Rp.2000.00")
            print(" ● Tempe Tahu Bacem   - Rp.1000.00")
            print(" ● Telur Goreng       - Rp.3000.00")
            print(" ● Nasi Liwet         - Rp.5000.00")
            print(" ● Nasi Uduk          - Rp.5000.00")
            print(" ● Nasi Pecel         - Rp.7000.00")
            print(" ● Nasi Padang        - Rp.10000.00")
            print(" ● Nasi Goreng        - Rp.10000.00")
            print(" ● Nasi Kucing        - Rp.3000.00")
            print(" ● Nasi Campur        - Rp.8000.00" )
            print(" ● Nasi Urap          - Rp.5000.00")
            print(" ● Ayam Bakar         - Rp.10000.00")
            print(" ● Mie Tante          - Rp.7000.00")
            print(" ● Sayur Sop          - Rp.5000.00")
            print(" ● Sayur Bayam        - Rp.5000.00")
            print(" ● Oseng Kangkung     - Rp.5000.00")
            print(" ● Terik Tahu         - Rp.5000.00")
            print(" ● Ikan Kakap         - Rp.13000.00")
            print(" ● Telur Balado       - Rp.8000.00")
            print(" ● Kentang Balado     - Rp.5000.00")
            print(" ● Sayur Asem         - Rp.5000.00")
            print(" ● Semur Jengkol      - Rp.5000.00")
            print(" ● Sambel Krecek      - Rp.5000.00")
            print(" ● Tumis Usus Ayam    - Rp.8000.00")
            print(" ● Tempe Orek         - Rp.5000.00")
            print(" ● Kering Tempe       - Rp.5000.00")
            print(" ● Garang Asem        - Rp.5000.00")
            print(" ● Terong Balado      - Rp.5000.00")
            print(" ● Ati Ampela         - Rp.7000.00")
            print(" ● Capcay             - Rp.6000.00")
            print(" ● Oseng Cumi         - Rp.10000.00")
            print(" ● Tumis Buncis       - Rp.5000.00")
            print(" ● Pindang Bandeng    - Rp.8000.00")
            print(" ● Sayur Tahu Santan  - Rp.5000.00")
            print(" ● Sayur Lombok Tahu  - Rp.5000.00")
            print(" ● Gulai Nangka       - Rp.5000.00")
            print(" ● Tumis Pare         - Rp.5000.00")
            print(" ● Pepes              - Rp.6000.00")
            print(" ● Ayam Rica-Rica     - Rp.6000.00")
            print(" ● Tumis Kikil        - Rp.8000.00")
            print(" ● Mangut Lele        - Rp.12000.00")
            print(" ● Gulai Ayam         - Rp.8000.00")
            print(" ● Rendang Sapi       - Rp.10000.00")
            print(" ● Mie Goreng Premium - Rp.8000.00")
            print(" ● Bihun Goreng       - Rp.5000.00")
            print(" ● Sayur Orak-Arik    - Rp.5000.00")
            print(" ● Sayur Bunga Pepaya - Rp.5000.00")
            print(" ● Tumis Terong Teri  - Rp.5000.00")
            print(" ● Tumis Sawi Putih   - Rp.5000.00")
            print(" ● Cah Brokoli        - Rp.5000.00")
            print(" ● Bakmi Goreng       - Rp.3000.00")
            print(" ● Bakmi Rebus        - Rp.3000.00")
            print(" ● Gudeg              - Rp.10000.00")
            print(" ● Mie Jumbo          - Rp.8000.00")
            print(" ● Mie Rebus          - Rp.6000.00")
            print(" ● Soto Tegal         - Rp.7000.00")
            print(" ● Nasi Ikan          - Rp.12000.00")
            print(" ● Ayam Geprek        - Rp.8000.00")
            print(" ● Ayam Goreng        - Rp.6000.00")
            print(" ● Ayam Ungkep        - Rp.15000.00")
            print(" ● Ayam Penyet        - Rp.8000.00")
            print(" ● Ayam Bakar         - Rp.9000.00")
            
            menu = input("Masukkan Pilihan Menu Yang Anda inginkan : ")
            porsi = int(input("Porsi Yang Ingin Dipesan : "))
            
            if menu == "Nasi Uduk":
                totalmakanan = porsi * 5000
                print(porsi, ' Nasi Uduk : Rp.', totalmakanan)
                menu=("Nasi Uduk")
            elif menu == "Nasi Pecel":
                totalmakanan = porsi * 7000
                print(porsi, ' Nasi Pecel : Rp.', totalmakanan)
                menu=("Nasi Pecel")
            elif menu == "Nasi Padang":
                totalmakanan = porsi * 10000
                print(porsi, ' Nasi Padang : Rp.', totalmakanan)
                menu=("Nasi Padang")
            elif menu == "Nasi Goreng":
                totalmakanan = porsi * 10000
                print(porsi, ' Nasi Goreng : Rp.', totalmakanan)
                menu=("Nasi Goreng")
            elif menu == "Nasi Kucing":
                totalmakanan = porsi * 3000
                print(porsi, ' Nasi Kucing : Rp.', totalmakanan)
                menu=("Nasi Kucing")
            elif menu == "Nasi Kuning":
                totalmakanan = porsi * 7000
                print(porsi, ' Nasi Kuning : Rp.', totalmakanan)
                menu=("Nasi kuning")
            elif menu == "Mie Goreng":
                totalmakanan = porsi * 6000
                print(porsi, ' Mie Goreng : Rp.', totalmakanan)
                menu=("Mie Goreng")
            elif menu == "Mie Goreng Premium":
                totalmakanan = porsi * 8000
                print(porsi, ' Mie Goreng Premium : Rp.', totalmakanan)
                menu=("Mie Goreng Premium")
            elif menu == "Mie Jumbo":
                totalmakanan = porsi * 8000
                print(porsi, ' Mie Jumbo : Rp.', totalmakanan)
                menu=("Mie Jumbo")
            elif menu == "Mie Rebus":
                totalmakanan = porsi * 6000
                print(porsi, ' Mie Rebus : Rp.', totalmakanan)
                menu=("Mie Rebus")
            elif menu == "Soto Tegal":
                totalmakanan = porsi * 10000
                print(porsi, ' Soto Tegal : Rp.', totalmakanan)
                menu=("Soto Tegal")
            elif menu == "NasiIkan":
                totalmakanan = porsi * 12000
                print(porsi, ' Nasi Ikan : Rp.', totalmakanan)
                menu=("Nasi Ikan")
            elif menu == "Ayam Geprek":
                totalmakanan = porsi * 15000
                print(porsi, ' Ayam Geprek : Rp.', totalmakanan)
                menu=("Ayam Geprek")
            elif menu == "Ayam Ungkep":
                totalmakanan = porsi * 15000
                print(porsi, ' Ayam Ungkep : Rp.', totalmakanan)
                menu=("Ayam Ungkep")
            elif menu == "Nasi Campur":
                totalmakanan = porsi * 9000
                print(porsi, ' Nasi Campur : Rp.', totalmakanan)
                menu=("Nasi Campur")
            else:
                print("Menu Tidak Tersedia.. \nMohon Masukkan Nama Menu Dengan Benar!")
                makanan()
                
        def minuman():
            global totalminuman
            global gelas
            global minum
            print("\n==========MENU MINUMAN==========")
            print(" ● Air Putih          - Rp.2000.00")
            print(" ● Es Teh             - Rp.3000.00")
            print(" ● Es Nutrisari       - Rp.4000.00")
            print(" ● Es Pop Ice         - Rp.5000.00")
            print(" ● Es Jeruk           - Rp.3000.00")
            print(" ● Es Nipis           - Rp.5000.00")
            print(" ● Es Doger           - Rp.7000.00")
            print(" ● Es Buah            - Rp.8000.00")
            print(" ● Thai Tea           - Rp.6000.00")
            print(" ● Jus Buah           - Rp.8000.00")
            print(" ● Sogem              - Rp.12000.00")
            print(" ● Capcin             - Rp.5000.00")
            print(" ● Pandan Latte       - Rp.7000.00")
            print(" ● Cappuchhino        - Rp.5000.00")
            print(" ● Es Sirup Kampul    - Rp.4000.00")
            print(" ● Susu               - Rp.4000.00")
            print(" ● Es Tarro           - Rp.3000.00")
            print(" ● Huzzlenut Latte    - Rp.7000.00")
            print(" ● Smootise           - Rp.10000.00")
            print(" ● Alpukat Float      - Rp.11000.00")
            print(" ● Es Banana Ijo      - Rp.5000.00")
            print(" ● Es Beng-Beng       - Rp.4000.00")
            print(" ● Es Milkshake       - Rp.7000.00")
            print(" ● Strawberry Kiss    - Rp.7000.00")
            print(" ● Es Kuwut           - Rp.7000.00")
            print(" ● Es Dawed           - Rp.5000.00")
            print(" ● Es Sirup           - Rp.3000.00")
            print(" ● Es Teh Tarik       - Rp.5000.00")
            print(" ● Es Choko Banana    - Rp.7000.00")
            print(" ● Es Rhom Regal      - Rp.7000.00")
            print(" ● Es Millo           - Rp.5000.00")
            print(" ● Es Kacang Ijo      - Rp.5000.00")
            print(" ● Es LemonTea        - Rp.4000.00")
            print(" ● Es Coklat          - Rp.5000.00")
            print(" ● Es Matcha          - Rp.6000.00")
            print(" ● Es Kopyor          - Rp.4000.00")
            print(" ● Es Campur          - Rp.5000.00")
            
            menu = input("Masukkan Pilihan Minuman Yang Anda inginkan : ")
            gelas = int(input("Berapa Gelas Yang Ingin Dipesan : "))
            
            if menu == "Es Teh":
                totalminuman = gelas * 3000
                print(gelas, ' Es Teh : Rp.', totalminuman)
                minum=("Es Teh")
            elif menu == "Es Jeruk":
                totalminuman = porsi * 3000
                print(gelas, ' Es Jeruk : Rp.', totalminuman)
                minum=("Es Jeruk")
            elif menu == "Es Doger":
                totalminuman = porsi * 5000
                print(gelas, ' Es Doger : Rp.', totalminuman)
                minum=("Es Doger")
            elif menu == "Es Buah":
                totalminuman = porsi * 7000
                print(gelas, ' Es Buah : Rp.', totalminuman)
                minum=("Es Buah")
            elif menu == "Es LemonTea":
                totalminuman = porsi * 5000
                print(gelas, ' Es LemonTea : Rp.', totalminuman)
                minum=("Es LemonTea")
            elif menu == "Es Coklat":
                totalminuman = porsi * 5000
                print(gelas, ' Es Coklat : Rp.', totalminuman)
                minum=("Es Coklat")
            elif menu == "Es Matcha":
                totalminuman = porsi * 5000
                print(gelas, ' Es Matcha : Rp.', totalminuman)
                minum=("Es Matcha")
            elif menu == "Es Kopyor":
                totalminuman = porsi * 3000
                print(gelas, ' Es Kopyor : Rp.', totalminuman)
                minum=("Es Kopyor")
            elif menu == "Es Campur":
                totalminuman = porsi * 5000
                print(gelas, ' Es Campur : Rp.', totalminuman)
                minum=("Es Campur")
            elif menu == "Jus Buah":
                totalminuman = porsi * 7000
                print(gelas, ' Jus Buah : Rp.', totalminuman)
                minum = ("Jus Buah")
            else:
                print("Miinuman Tidak Tersedia.. \nMohon Masukkan Nama Menu Dengan Benar!")
                minuman()
                
        makanan()
        minuman()
        total_harga = totalmakanan + totalminuman

        print("\nTotal Harga Yang Harus Dibayar : ", total_harga)
        uang = int(input("Jumlah Uang Yang Dibayarkan :"))
        kembalian = int(uang - total_harga)
        print("Jumlah Kembalian : ", kembalian)

        print("\n●●●●●●●●●●●● STRUK PEMBELIAN ●●●●●●●●●●●●\n")
        print("Nama\t\t\t\t:", Pembeli)
        print("Pembelian\t\t\t:", porsi, menu, "\nHarga Yang Harus Dibayar\t: Rp.", totalmakanan)
        print("\t\t\t\t:", gelas, minum, "\nHarga Yang Harus Dibayar\t: Rp.", totalminuman)
        print("Total Harga\t\t\t: Rp.", total_harga)
        print("Dibayar\t\t\t\t: Rp.", uang)
        print("Uang Kembali\t\t\t: Rp.", kembalian)

        print("\n●●●●●●●●●●●● TERIMAKASIH! ●●●●●●●●●●●●")
        print("●●●●●●●●● SELAMAT MENIKMATI😋 ●●●●●●●●●")
        
        while True:
            lanjut = input("\nApakah ingin memesan lagi? (y/n): ")
            if lanjut.lower() == 'y':
                print("\n")
                break
            elif lanjut.lower() == 'n':
                print("\n●●●●●●●●●●●● PROGRAM SELESAI ●●●●●●●●●●●●")
                return  # Keluar dari fungsi main()
            else:
                print("Input tidak valid! Mohon masukkan 'y' atau 'n'")

# Menjalankan program
main()