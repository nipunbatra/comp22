s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

out = ""
for c in s:
    if c in [" ", "'", "."]:
        out = out + c
    else:
        out = out + chr((ord(c) + 2 - ord("a")) % 26 + ord("a"))

print(out)


### Method 2
import string

inp = string.ascii_lowercase
out = inp[2:] + inp[:2]

mapping = str.maketrans(inp, out)
print("map".translate(mapping))
