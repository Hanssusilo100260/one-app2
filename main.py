#[import]
import tkinter as tk
from tkinter import messagebox
import qrcode
import calendar
import os
import random

#[def system]
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clean')

#[def color system]
def color_text1():
    if os.name == 'nt':
        _ = os.system('color 1') #[color text BLUE]
def color_text2():
    if os.name == 'nt':
        _ = os.system('color 2') #[color text GREEN]
def color_text3():
    if os.name == 'nt':
        _ = os.system('color 3') #[color text AQUA]
def color_text4():
    if os.name == 'nt':
        _ = os.system('color 4') #[color text RED]
def color_text5():
    if os.name == 'nt':
        _ = os.system('color 5') #[color text PURPLE]
def color_text6():
    if os.name == 'nt':
        _ = os.system('color 6') #[color text YELLOW]
def color_text7():
    if os.name == 'nt':
        _ = os.system('color 7') #[color text WHITE]
def color_text8():
    if os.name == 'nt':
        _ = os.system('color 8') #[color text GRAY]

#[def app]
def kalkulator():
    while True:
        try:
            print("========== Kalkulator ===========")
            a = int(input("Masukan angka pertama: "))
            b = int(input("Masukan angka kedua: "))
            print("========= Pilih Operasi =========")
            print("=> Perkalian                 (a)")
            print("=> Perkurangan               (b)")
            print("=> Pembagian                 (c)")
            print("=> Pertambahan               (d)")
            print("=================================")
            input_op = input("=> ")
            print("============ Jawaban ============")

            #[IF]
            if input_op == 'a' or input_op == 'A':
                print(f"{a} x {b} = {a * b}")
            elif input_op == 'b' or input_op == 'b':
                print(f"{a} - {b} = {a - b}")
            elif input_op == 'c' or input_op == 'C':
                print(f"{a} : {b} = {a / b}")
            elif input_op == 'd' or input_op == 'D':
                print(f"{a} + {b} = {a + b}")
            else:
                print("Input Op Is Error")

            print("=================================")
            end = input("Lanjut?(y/n): ")
            print("=================================")

            if end.lower() != 'y':
                clear()
                break
            else:
                clear()

        except ValueError:
            print("Input Error")
            clear()
def password():
    while True:
        try:
            print("========== Password ==========")
            jumlah = int(input("Masukan jumlah: "))
            print("==============================")

            #[index random]
            huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
            angka = "0123456789"
            karater = "!@#%$&*.,"

            semua = huruf_besar + huruf_kecil + angka + karater

            password = ''.join(random.sample(semua,jumlah))

            #[Output]
            print(f"Result: {password}")

            print("==============================")
            end = input("Lanjut?(y/n): ")
            print("==============================")

            if end.lower() != 'y':
                clear()
                break
            else:
                clear()

        except ValueError:
            print("Input Error")
            clear()
def word_loop():
    while True:
        try:
            print("========== Word Loop ==========")
            print("=> Satu Kata                (a)")
            print("=> Dua Kata                 (b)")
            print("=> Tiga Kata                (c)")
            print("=> Empat Kata               (d)")
            print("=> lima Kata                (e)")
            print("===============================")
            opsi = input("=> ")
            print("===============================")
            clear()

            #[IF]
            if opsi == 'a' or opsi == 'A':
                print("========== Word Loop ==========")
                word_a_1 = input("Masukan kata: ")
                loop_a_1 = int(input("Masukan jumlah pengulangan: "))
                print("===============================")

                #[generate loop]
                for a in range(loop_a_1):
                    print(word_a_1)
            elif opsi == 'b' or opsi == 'B':
                print("========== Word Loop ==========")
                word_b_1 = input("Masukan kata pertama: ")
                loop_b_1 = int(input("Masukan jumlah pengulangan: "))
                word_b_2 = input("Masukan kata kedua: ")
                loop_b_2 = int(input("Masukan jumlah pengulangan: "))
                print("===============================")

                #[generate loop]
                for b in range(loop_b_1):
                    print(word_b_1)
                for b in range(loop_b_2):
                    print(word_b_2)
            elif opsi == 'c' or opsi == 'C':
                print("========== Word Loop ==========")
                word_c_1 = input("Masukan kata pertama: ")
                loop_c_1 = int(input("Masukan jumlah pengulangan: "))
                word_c_2 = input("Masukan kata kedua: ")
                loop_c_2 = int(input("Masukan jumlah pengulangan: "))
                word_c_3 = input("Masukan kata ketiga: ")
                loop_c_3 = int(input("Masukan jumlah pengulangan: "))
                print("===============================")

                #[generate loop]
                for c in range(loop_c_1):
                    print(word_c_1)
                for c in range(loop_c_2):
                    print(word_c_2)
                for c in range(loop_c_3):
                    print(word_c_3)
            elif opsi == 'd' or opsi == 'D':
                print("========== Word Loop ==========")
                word_d_1 = input("Masukan kata pertama: ")
                loop_d_1 = int(input("Masukan jumlah pengulangan: "))
                word_d_2 = input("Masukan kata kedua: ")
                loop_d_2 = int(input("Masukan jumlah pengulangan: "))
                word_d_3 = input("Masukan kata ketiga: ")
                loop_d_3 = int(input("Masukan jumlah pengulangan: "))
                word_d_4 = input("Masukan kata keempat: ")
                loop_d_4 = int(input("Masukan jumlah pengulangan: "))
                print("===============================")
                
                #[generate loop]
                for d in range(loop_d_1):
                    print(word_d_1)
                for d in range(loop_d_2):
                    print(word_d_2)
                for d in range(loop_d_3):
                    print(word_d_3)
                for d in range(loop_d_4):
                    print(word_d_4)
            elif opsi == 'e' or opsi == 'E':
                print("========== Word Loop ==========")
                word_e_1 = input("Masukan kata pertama: ")
                loop_e_1 = int(input("Masukan jumlah pengulangan: "))
                word_e_2 = input("Masukan kata kedua: ")
                loop_e_2 = int(input("Masukan jumlah pengulangan: "))
                word_e_3 = input("Masukan kata ketiga: ")
                loop_e_3 = int(input("Masukan jumlah pengulangan: "))
                word_e_4 = input("Masukan kata keempat: ")
                loop_e_4 = int(input("Masukan jumlah pengulangan: "))
                word_e_5 = input("Masukan kata kelima: ")
                loop_e_5 = int(input("Masukan jumlah pengulangan: "))
                print("===============================")

                #[generate loop]
                for d in range(loop_e_1):
                    print(word_e_1)
                for d in range(loop_e_2):
                    print(word_e_2)
                for d in range(loop_e_3):
                    print(word_e_3)
                for d in range(loop_e_4):
                    print(word_e_4)
                for d in range(loop_e_5):
                    print(word_e_5)
            
            print("===============================")
            end = input("Lanjut?(y/n): ")
            print("===============================")

            if end.lower() != 'y':
                clear()
                break
            else:
                clear()

        except ValueError:
            print("Input Error")
            clear()
def kalender():
    while True:
        try:
            print("========== Kalender ==========")
            year = int(input("Tahun: "))
            print("==============================")

            #[generate year]
            x = calendar.TextCalendar()
            print(x.pryear(year))

            print("===============================")
            end = input("Lanjut?(y/n): ")
            print("===============================")

            if end.lower() != 'y':
                clear()
                break
            else:
                clear()
        
        except ValueError:
            print("Input Error")
            clear()
def acak_dadu():
    while True:
        try:
            print("========== Acak Dadu ==========")
            name = input("Nama pemain: ")
            print("===============================")

            #[index dadu]
            angka_dadu = '1','2','3','4','5','6','7','8','9','10','11','12'

            #[random dadu]
            result = ''.join(random.sample(angka_dadu,1))

            #[hasil]
            print(f"Nama Pemain: {name}")
            print(f"Angka dadu : {result}")

            print("===============================")
            end = input("Lanjut?(y/n): ")
            print("===============================")

            if end.lower() != 'y':
                clear()
                break
            else:
                clear()
        
        except ValueError:
            print("Input Error")
            clear()
def generate_QRcode():
    while True:
        try:
            print("========== Generate QRcode ==========")
            data = input("Masukan isian QRcode: ")
            print("=====================================")
            name_qrcode = input("Masukan Nama: ")
            print("=====================================")

            #[generate qrcode]
            img = qrcode.make(data)

            #[save qrcode]
            img.save(f"{name_qrcode}.png")

            #[result]
            print(f"QRcode anda telah berhasil dibuat. nama file: {name_qrcode}.png")

            print("=====================================")
            end = input("Lanjut?(y/n): ")

            if end.lower() != 'y':
                clear()
                break
            else:
                clear()

        except ValueError:
            print("Input Error")
            clear()

#[def setting]
def color_pick_text():
    while True:
        try:
            print("========== Pilih Warna ==========")
            print("Biru                          (1)")
            print("Hijau                         (2)")
            print("Aqua                          (3)")
            print("Merah                         (4)")
            print("Ungu                          (5)")
            print("Kuning                        (6)")
            print("Putih                         (7)")
            print("Abu abu                       (8)")
            print("=================================")
            pick = input("=> ")
            
            #[change color]
            if pick == '1':
                color_text1()
            elif pick == '2':
                color_text2()
            elif pick == '3':
                color_text3()
            elif pick == '4':
                color_text4()
            elif pick == '5':
                color_text5()
            elif pick == '6':
                color_text6()
            elif pick == '7':
                color_text7()
            elif pick == '8':
                color_text8()

            print("=================================")
            end = input("Apakah anda mau ganti lagi(y/n): ")
            print("=================================")

            if end.lower() != 'y':
                clear()
                break
            else:
                clear()
        
        except ValueError:
            print("Input Error")
            clear()

while True:
    print("========== One For All ==========")
    print(" Fitur app:")
    print(" => Kalkulator                (a)")
    print(" => Password                  (b)")
    print(" => Word Loop                 (c)")
    print(" => Kalender                  (d)")
    print(" => Acak Dadu                 (e)")
    print(" => Generate QRcode           (f)")
    print()
    print(" Pengaturan:")
    print(" => Pick Color Text           (0)")
    print("=================================")
    print(" Ketik exit untuk keluar program")
    print("=================================")
    option = input(" => ")
    print("=================================")
    clear()

    #[IF (fitur)]
    if option == 'a' or option == 'A':
        kalkulator()
    elif option == 'b' or option == 'B':
        password()
    elif option == 'c' or option == 'C':
        word_loop()
    elif option == 'd' or option == 'D':
        kalender()
    elif option == 'e' or option == 'E':
        acak_dadu()
    elif option == 'f' or option == 'F':
        generate_QRcode()
    
    #[IF (pengaturan)]
    if option == '0':
        color_pick_text()

    #[IF (lain)]
    if option == 'exit':
        print("apakah anda yakin untuk keluar dari program ini (y/n)?")
        end = input("=> ")

        if end.lower() != 'n':
            clear()
            break
        else:
            clear()