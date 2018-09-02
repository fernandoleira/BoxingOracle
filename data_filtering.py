fi = open("boxing.csv", "r+")
fo = open("data.csv", "a")

temp = fi.read().splitlines()

stances_names = []
stances_nums = []

for x in range(1, len(temp)):
    ln = temp[x].split(',')
    stanceA = ln[6]
    stanceB = ln[7]
    res = ln[-1]

    is_orthodox_A = 0
    is_orthodox_B = 0
    is_southpaw_A = 0
    is_southpaw_B = 0
    result = 0

    if '' not in ln:
        # Stances
        if stanceA == "orthodox":
            is_orthodox_A = 1
        else:
            is_southpaw_A = 1

        if stanceB == "orthodox":
            is_orthodox_B = 1
        else:
            is_southpaw_B = 1

        # Result
        if res == 'win_A':
            result = 1
        elif res == 'win_B':
            result = 2
        else:
            result = 0

        # Append
        final_ln = ",".join(ln[0:6] + [str(is_orthodox_A), str(is_orthodox_B), str(is_southpaw_A), str(is_southpaw_B)] + ln[8:18] + [str(result)])
        print(final_ln)
        fo.write("\n{}".format(final_ln))

fi.close()
fo.close()
