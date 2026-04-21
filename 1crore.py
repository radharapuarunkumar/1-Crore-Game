import random

money = 1000

while money > 0:
    print(f"\nYour balance: ₹{money}")

    a = int(input("Enter your lucky no (1-10,000): "))
    c = random.randint(1, 10000)

    if c == a:
        print("🎉🔥 JACKPOT! You won ₹1 CRORE!")
        money += 10000000
        break
    else:
        print("😢 Better luck next time bro")
        print(f"Computer random no is {c}")
        money -= 10

print("\n🏁 Game Over")
print(f"Final balance: ₹{money}")