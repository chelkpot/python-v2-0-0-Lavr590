# tasks/task2.py

def solve():
# Ниже пишите решение задачи

    x, y, z = map(int, input().split())
    total_cost = x * 3 + y * 5 + z * 12
    print(total_cost)

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()