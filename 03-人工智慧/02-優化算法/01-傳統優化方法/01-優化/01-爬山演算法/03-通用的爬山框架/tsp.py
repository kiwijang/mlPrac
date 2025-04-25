from random import randint

citys = [
    (0,3),(0,0),
    (0,2),(0,1),
    (1,0),(1,3),
    (2,0),(2,3),
    (3,0),(3,3),
    (3,1),(3,2)
]

#path = [i for i in range(len(citys))]
l = len(citys)
path = [(i+1)%l for i in range(l)]
print(path)

def distance(p1, p2):
    # print('p1=', p1)
    x1, y1 = p1
    x2, y2 = p2
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def pathLength(p):
    dist = 0
    plen = len(p)
    for i in range(plen):
        # dist += distance(citys[p[i]], citys[p[(i+1)%plen]])
        dist += distance(citys[i], citys[p[i]])
    return dist

print('pathLength=', pathLength(path))

def randCity() :
    return randint(0, l-1)

def neighbor(path):
    new_path = path.copy()
    
    # 避免 i == j（對調同一個城市沒有意義）
    while True:
        i = randCity()
        j = randCity()
        if i != j:
            break

    # 對調位置 i 和 j
    new_path[i], new_path[j] = new_path[j], new_path[i]
    return new_path

def hillClimbing(x, pathLength, neighbor, max_fail=10000):
    fail = 0
    print('--- start! ---')
    while True:
        nx = neighbor(x)
        if pathLength(nx)>pathLength(x):
            x = nx
            fail = 0
        else:
            fail += 1
            if fail > max_fail:
                
                print("solution: ", pathLength(x))
                print("path: ", x)
                return x

# 執行爬山演算法
# hillClimbing(path, pathLength, neighbor, max_fail=10000)

# 🧪 多次嘗試取最佳解
def multiHillClimb(times=10):
    best_path = None
    best_len = float('inf')

    for i in range(times):
        print(f"\n🔁 Run {i+1}")
        initial_path = [(i+1)%l for i in range(l)]
        result = hillClimbing(initial_path, pathLength, neighbor, max_fail=10000)
        length = pathLength(result)

        if length < best_len:
            best_len = length
            best_path = result

    print("\n🌟 最佳解")
    print("最短距離(solution):", best_len)
    print("最佳路徑(path):", best_path)

multiHillClimb(times=10)
