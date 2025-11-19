#技术部py第一次作业（作业一，猜数字游戏）
def guess_number_game():
    n = int(input().strip())

    low = 1
    high = 100
    guess_count = 0
    guesses = []

    while low <= high:
        mid = (low + high) // 2
        guess_count += 1
        guesses.append(mid)

        if mid == n:
            # 输出所有猜测过程
            for guess in guesses:
                print(guess)
            print(f"最终猜测{guess_count}次")
            break
        elif mid > n:
            high = mid - 1
        else:
            low = mid + 1


# 运行游戏
guess_number_game()