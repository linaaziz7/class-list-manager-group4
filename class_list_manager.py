# Class List Manager - Group 4
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# ===== Each student adds her function BELOW this line =====


# Written by: Lina Alfaadhel (task 6)
def to_upper(names):
    upper_names = []
    for name in names:
        upper_names.append(name.upper())
    return upper_names
  
# ===== Each student adds her function ABOVE this line =====


def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)

    # Each student calls her function here

    print("Uppercase names:", to_upper(names))
main()
  
