import time

i = 0
l = []

print("Ait pmst lood nii, ütled mis viimase tunni jooksul tegid, ma panen kirja ja pärast vaatame, mis sinuga teeme.")

while True:
      print("1 - mitte sittagi (yt, fb, ig, minesweeper jne)\n"
            "2 - hooldustööd (koristamine, nõude pesemine, söögi tegemine jne)\n"
            "3 - õppimine (mv)\n"
            "4 - tubli pela gf-i, poiste, Trumpiga (omaette warthunder ei loe)\n"
            "kui sa tra midagi muud kirjutad kui selle numbri ss see mf proge läheb katki ja sina oled süüdi\n")
      x = input()
      l.append(x)
      i += 1
      if i >= 16:
            break
s = "".join(l)
f = open("bsArchive.txt", "a")
f.write(s + "\n")
f.close()

print("Tänane seeria:\n")
with open('bsArchive.txt') as f:
    for line in f:
        pass
    last_line = line
print(last_line)
f.close()