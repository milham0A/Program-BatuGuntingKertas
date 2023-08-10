# Fungsi penampung inputan user
def main_choise(choise, name="Tamu"):
    menu = ["Batu", "Gunting", "Kertas"]
    print(f"{name} Memilih {menu[choise]}")


# Fungsi validasi pilihan user
def validate(choise):
    if choise < 0 or choise > 2:
        return False
    else:
        return True


# Fungsi penentuan menang atau kalah
def menang(player, computer):
    if player == computer:
        return "Seri"
    elif player == 0 and computer == 2:
        return "kalah"
    elif player == 1 and computer == 0:
        return "kalah"
    elif player == 2 and computer == 1:
        return "kalah"
    else:
        return "Menang"
