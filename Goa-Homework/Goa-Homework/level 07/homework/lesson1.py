# მომხმარებლისგან რიცხვის მიღება
n = int(input("შეიყვანეთ რიცხვი: "))

# გამყოფების გამოთვლა
print(f"რიცხვის {n} გამყოფები არიან:")

for i in range(1, n + 1):  # გადავდივართ 1-დან n-მდე
    if n % i == 0:  # თუ n იყოფა i-თ უნაშთოდ
        print(i)