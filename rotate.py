


def clock(v):
    new = []
    new.append(v[6])
    new.append(v[3])
    new.append(v[0])
    new.append(v[7])
    new.append(v[4])
    new.append(v[1])
    new.append(v[8])
    new.append(v[5])
    new.append(v[2])
    print("Rotating Clockwise...")
    return new

def counter(v):
    new = []
    new.append(v[2])
    new.append(v[5])
    new.append(v[8])
    new.append(v[1])
    new.append(v[4])
    new.append(v[7])
    new.append(v[0])
    new.append(v[3])
    new.append(v[6])
    print("Rotating Counter Clockwise...")
    return new

def pMat(v):
    s = ""
    s += v[0] + " "
    s += v[1] + " "
    s += v[2] + " "
    print(s)
    s = ""
    s += v[3] + " "
    s += v[4] + " "
    s += v[5] + " "
    print(s)
    s = ""
    s += v[6] + " "
    s += v[7] + " "
    s += v[8] + " "
    print(s)
    return

if __name__ == "__main__":
    v = ["0","1","2","3","4","5","6","7","8"]

    pMat(v)
    v = clock(v)
    pMat(v)
    v = counter(v)
    pMat(v)
    
