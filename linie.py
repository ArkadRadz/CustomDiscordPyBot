t = [["g2", "g2", "r2", "g2", "g2"],
     ["g2", "g2", "g2", "b", "g2"],
     ["g2", "g2", "b2", "b", "g2"]]


def check(b, t, w):
    d3 = {"r": 0.2, "g": 0.2, "b": 0.2, "r2": 1, "g2": 0.5, "b2": 0.5, "j": 2}
    d4 = {"r": 0.5, "g": 0.5, "b": 0.5, "r2": 2, "g2": 1, "b2": 1, "j": 6}
    d5 = {"r": 2, "g": 1.5, "b": 1, "r2": 10, "g2": 5, "b2": 4, "j": 40}
    w = [[True for i in range(9)] for i in range(3)]
    total = 0
    sum = 0
    last_sum = 0
    spin = True
    git
    if w[0][2]:
        if t[0][0] == t[0][1] == t[0][2] == t[0][3] == t[0][4]:
            sum += b * d5[t[0][0]]
            w[0][2] = False
            w[0][1] = False
            w[0][0] = False
    if w[0][1]:
        if t[0][0] == t[0][1] == t[0][2] == t[0][3]:
            sum += b * d4[t[0][0]]
            w[0][1] = False
            w[0][0] = False
    if w[0][0]:
        if t[0][0] == t[0][1] == t[0][2]:
            sum += b * d3[t[0][0]]
            w[0][0] = False

    if w[0][5]:
        if t[1][0] == t[1][1] == t[1][2] == t[1][3] == t[1][4]:
            sum += b * d5[t[1][0]]
            w[0][5] = False
            w[0][4] = False
            w[0][3] = False
    if w[0][4]:
        if t[1][0] == t[1][1] == t[1][2] == t[1][3]:
            sum += b * d4[t[1][0]]
            w[0][4] = False
            w[0][3] = False
    if w[0][3]:
        if t[1][0] == t[1][1] == t[1][2]:
            sum += b * d3[t[1][0]]
            w[0][3] = False

    if w[0][8]:
        if t[2][0] == t[2][1] == t[2][2] == t[2][3] == t[2][4]:
            sum += b * d5[t[2][0]]
            w[0][8] = False
            w[0][7] = False
            w[0][6] = False
    if w[0][7]:
        if t[2][0] == t[2][1] == t[2][2] == t[2][3]:
            sum += b * d4[t[2][0]]
            w[0][7] = False
            w[0][6] = False
    if w[0][6]:
        if t[2][0] == t[2][1] == t[2][2]:
            sum += b * d3[t[2][0]]
            w[0][6] = False

    if w[1][2]:
        if t[0][0] == t[1][1] == t[2][2] == t[1][3] == t[0][4]:
            sum += b * d5[t[0][0]]
            w[1][2] = False
            w[1][1] = False
            w[1][0] = False
    if w[1][1]:
        if t[0][0] == t[1][1] == t[2][2] == t[1][3]:
            sum += b * d4[t[0][0]]
            w[1][1] = False
            w[1][0] = False
    if w[1][0]:
        if t[0][0] == t[1][1] == t[2][2]:
            sum += b * d3[t[0][0]]
            w[1][0] = False

    if w[1][5]:
        if t[2][0] == t[1][1] == t[0][2] == t[1][3] == t[2][4]:
            sum += b * d5[t[2][0]]
            w[1][5] = False
            w[1][4] = False
            w[1][3] = False
    if w[1][4]:
        if t[2][0] == t[1][1] == t[0][2] == t[1][3]:
            sum += b * d4[t[2][0]]
            w[1][4] = False
            w[1][3] = False
    if w[1][3]:
        if t[2][0] == t[1][1] == t[0][2]:
            sum += b * d3[t[2][0]]
            w[1][3] = False

    if w[1][8]:
        if t[1][0] == t[0][1] == t[0][2] == t[0][3] == t[1][4]:
            sum += b * d5[t[1][0]]
            w[1][8] = False
            w[1][7] = False
            w[1][6] = False
    if w[1][7]:
        if t[1][0] == t[0][1] == t[0][2] == t[0][3]:
            sum += b * d4[t[1][0]]
            w[1][7] = False
            w[1][6] = False
    if w[1][6]:
        if t[1][0] == t[0][1] == t[0][2]:
            sum += b * d3[t[1][0]]
            w[1][6] = False

    if w[2][2]:
        if t[1][0] == t[2][1] == t[2][2] == t[2][3] == t[1][4]:
            sum += b * d5[t[1][0]]
            w[2][2] = False
            w[2][1] = False
            w[2][0] = False
    if w[2][1]:
        if t[1][0] == t[2][1] == t[2][2] == t[2][3]:
            sum += b * d4[t[1][0]]
            w[2][1] = False
            w[2][0] = False
    if w[2][0]:
        if t[1][0] == t[2][1] == t[2][2]:
            sum += b * d3[t[1][0]]
            w[2][0] = False

    if w[2][5]:
        if t[0][0] == t[1][1] == t[1][2] == t[1][3] == t[0][4]:
            sum += b * d5[t[0][0]]
            w[2][5] = False
            w[2][4] = False
            w[2][3] = False
    if w[2][4]:
        if t[0][0] == t[1][1] == t[1][2] == t[1][3]:
            sum += b * d4[t[0][0]]
            w[2][4] = False
            w[2][3] = False
    if w[2][3]:
        if t[0][0] == t[1][1] == t[1][2]:
            sum += b * d3[t[0][0]]
            w[2][3] = False

    if w[2][8]:
        if t[2][0] == t[1][1] == t[1][2] == t[1][3] == t[2][4]:
            sum += b * d5[t[2][0]]
            w[2][8] = False
            w[2][7] = False
            w[2][6] = False
    if w[2][7]:
        if t[2][0] == t[1][1] == t[1][2] == t[1][3]:
            sum += b * d4[t[2][0]]
            w[2][7] = False
            w[2][6] = False
    if w[2][6]:
        if t[2][0] == t[1][1] == t[1][2]:
            sum += b * d3[t[2][0]]
            w[2][6] = False

    if sum > 0:
        total += sum
        spin = True
    else:
        spin = False
        total += last_sum

    return [total, w, spin]


