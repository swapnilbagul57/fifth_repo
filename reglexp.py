
import re
pat = "sw+"

def searchstring(st, pat):
    if re.match(pat, st):
        return True
    else:
        return False

st = input(" Enter any string ")
flag = searchstring(st, pat)

if flag:
    print("Match Found in String ")
else:
    print("Match not found ")
