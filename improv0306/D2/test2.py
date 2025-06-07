import triangle as tr

t = tr.Triangle.fromSirka(35)

# f = open("trojuhelniky.txt", "w")
# try:
#     f.write(t.pravouhly())
#     f.write("\n")
#     f.write(t.rovnoramenny())
# finally:
#     f.close()


with open("trojuhelniky.txt", "w") as f:
    f.write(t.pravouhly())
    f.write("\n\n")
    f.write(t.rovnoramenny())