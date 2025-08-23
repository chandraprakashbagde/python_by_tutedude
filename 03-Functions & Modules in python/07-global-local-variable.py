n = 1

def fn():
    global n
    n = 6
    print("in",n)

fn()
print("out",n)