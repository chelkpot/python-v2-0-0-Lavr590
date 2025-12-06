# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    
    a, b = map(int, input().split())
    total_banks = a + b - 1
    harry_missed = total_banks - a
    larry_missed = total_banks - b
    print(harry_missed, larry_missed)

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()