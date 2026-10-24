import random
secret = random.randint(1, 50)

hearts = 5

guess = int(input("Guess the secret number: "))
while guess != secret:
    if guess > secret:
        if guess - secret <= 3:
            hint = "🔥HOT!"
        if guess - secret >= 21:
            hint = "🧊ICE COLD!"
        if guess - secret >= 4:
            hint = "🌡️WARM!"
        if guess - secret >= 12:
                hint = "🥶COLD!"
    else:
        if secret - guess <= 3:
            hint = "🔥HOT!"
        if secret - guess >= 21:
            hint = "🧊ICE COLD!"
        if secret - guess >= 4:
            hint = "🌡️WARM!"
        if secret - guess >= 12:
            hint = "🥶COLD!"

    for i in range(1, 6):
        if guess != secret:
            hearts -= 1
            break
    print("❤️" * hearts)

    if hearts == 0:
        print("GAME OVER!","Number was", secret)
        break

    print(hint)
    guess = int(input("RETRY! Guess the secret number again: "))

if guess == secret:
    print("YOU WIN!")