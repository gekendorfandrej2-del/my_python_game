# Игра "Угадай число"
import random                          # подключаем модуль случайных чисел

secret = random.randint(1, 10)         # загадываем число от 1 до 10
attempts = 0                           # счётчик попыток

print("Я загадал число от 1 до 10.")

while True:                            # бесконечный цикл, пока не угадаем
    guess = int(input("Твой вариант: "))
    attempts += 1                      # увеличиваем счётчик на 1

    if guess < secret:
        print("Больше!")
    elif guess > secret:
        print("Меньше!")
    else:
        print(f"Угадал! Попыток: {attempts}")
        break                          # выходим из цикла
