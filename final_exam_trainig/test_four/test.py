match = ["@###Val1d1teM@###"]
grps = ""
for sym in match[0]:
    if sym.isdigit():
        grps += sym
print(grps)