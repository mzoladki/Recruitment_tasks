def fight(army, even, odd):
    for soldier in army:
        soldier = "{0:b}".format(soldier)
        even_counter = 0
        odd_counter = 0
        if int(soldier) == 0:
            pass
        elif int(soldier) % 2 == 1:
            for a in soldier:
                if a == "1":
                    odd_counter += 1
            if soldier[0] == "-":
                odd.append(int(odd_counter) * (-1))
            else:
                odd.append(int(odd_counter))
        else:
            for a in soldier:
                if a == "0":
                    even_counter += 1
            if soldier[0] == "-":
                even.append(int(even_counter) * (-1))
            else:
                even.append(int(even_counter))


def result(even, odd):
    odd_strength = 0
    even_strength = 0
    for a in even:
        even_strength += a
    for a in odd:
        odd_strength += a
    if even_strength > odd_strength:
        print("evens win")
    elif even_strength < odd_strength:
        print("odds win")
    else:
        print("tie")


even_stats = []
odd_stats = []
battle = [0, 0, 1, -2, 2, -1, 0, 8, 7]

fight(battle, even_stats, odd_stats)
result(even_stats, odd_stats)
