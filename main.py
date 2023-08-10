import os
import settings
import random

os.system("cls")

# pemilihan random (antara 0-2) buat computer
computer_choise = random.randint(0, 2)

while True:
    player_name = input("Masukan Nama Anda: ")
    player_choise = int(
        input("Masukan Pilihan anda: (0: Batu, 1: Gunting, 2: Kertas)\n")
    )

    # Validasi pilihan user
    if settings.validate(player_choise):
        print(f"Selamat datang {player_name}")

        # Memanggil nama dan pilihan player
        settings.main_choise(player_choise, player_name)

        # Memanggil pilihan computer
        settings.main_choise(computer_choise, "Komputer")

        # Menang atau Kalah
        result = settings.menang(player_choise, computer_choise)
        print(f"Anda {result}")

    else:
        print("Masukan Nomor yang benar!!!")

    # Untuk perulangan
    incontinue = input("Apakah anda ingin lanjut atau tidak? (y/n)").lower()
    if incontinue == "n":
        break
