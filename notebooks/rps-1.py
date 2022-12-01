u = "c"
c = "p"
if u == "r" and c == "r":
    print("Tie")
elif u == "r" and c == "p":
    print("c wins", "comp:", c, "user:", u)
elif u == "r" and c == "s":
    print("u wins", "comp:", c, "user:", u)
elif u == "p" and c == "r":
    print("u wins", "comp:", c, "user:", u)
elif u == "p" and c == "p":
    print("Tie")
elif u == "p" and c == "s":
    print("c wins", "comp:", c, "user:", u)
elif u == "s" and c == "r":
    print("c wins", "comp:", c, "user:", u)
elif u == "s" and c == "p":
    print("u wins", "comp:", c, "user:", u)
elif u == "s" and c == "s":
    print("tie")
