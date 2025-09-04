import triangle as tr

t = tr.Triangle.fromSirka(24)


# # f = open("soubory/mujSoubor.txt", "w")

# # f.write(t.rovnoramenny())

# # f.close()


with open("soubory/mujSoubor.txt", "w") as f:
    f.write(t.rovnoramenny())


# try:
#     f = open("soubory/mujSoubor.txt", "w")
#     f.write("Ted jsem v context-manageru!")
#     ...
# finally:
#     f.close()


# print("Jsme v pohode")



