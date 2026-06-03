import random


class Spectator:
    def __init__(self, arrival, target=False):
        self.arrival = arrival
        self.target = target


def one_simulation(N, m, T, t1, x):
    spectators = []

    # Наш глядач
    spectators.append(Spectator(T - x, True))

    # Інші глядачі
    for _ in range(N - 1):
        arrival_time = random.uniform(0, T)
        spectators.append(Spectator(arrival_time))

    # Сортуємо за часом приходу
    spectators.sort(key=lambda s: s.arrival)

    # Час звільнення кожного турнікета
    turnstiles = [0.0] * m

    for s in spectators:

        # Знаходимо найшвидший турнікет
        best = turnstiles.index(min(turnstiles))

        # Коли людина реально почне проходити
        start_time = max(s.arrival, turnstiles[best])

        # Випадковий час проходження
        service_time = random.uniform(1, t1)

        finish_time = start_time + service_time

        # Оновлюємо час зайнятості турнікета
        turnstiles[best] = finish_time

        # Якщо це наш глядач
        if s.target:
            return finish_time <= T

    return False


def probability(N, m, T, t1, x, experiments=10000):
    success = 0

    for _ in range(experiments):
        if one_simulation(N, m, T, t1, x):
            success += 1

    return success / experiments


def find_min_time(N, m, T, t1):

    left = 0
    right = T

    for _ in range(40):

        mid = (left + right) / 2

        p = probability(N, m, T, t1, mid)

        if p >= 0.9:
            right = mid
        else:
            left = mid

    return right


# ---------------- MAIN ----------------

N = int(input("Кількість глядачів N: "))
m = int(input("Кількість турнікетів m: "))
T = float(input("За скільки часу відкривають турнікети T: "))
t1 = float(input("Максимальний час проходу t1: "))

result = find_min_time(N, m, T, t1)

print("\nМінімальний час приходу:")
print(round(result, 2))

final_probability = probability(N, m, T, t1, result)

print("Ймовірність пройти:")
print(round(final_probability, 4))