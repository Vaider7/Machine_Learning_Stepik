import random
from numba import jit


@jit(nopython=True)
def probability():
    sum_1_20 = 0
    sum_1_10 = 0
    sum_1_5 = 0
    total_sum = 0
    count = 0
    count_20 = 0
    count_10 = 0
    count_5 = 0
    while True:
        rand_int = random.randint(1, 7)

        if rand_int < 6:
            rand_val = random.randint(0, 19)
            total_sum += rand_val
            sum_1_20 += rand_val
            count_20 += 1
        elif rand_int == 6:
            rand_val = random.randint(0, 9)
            total_sum += rand_val
            sum_1_10 += rand_val
            count_10 += 1
        elif rand_int == 7:
            rand_val = random.randint(0, 4)
            total_sum += rand_val
            sum_1_5 += rand_val
            count_5 += 1

        count += 1
        if count % 1_000_000_000 == 0:
            print('Общее', total_sum / count, total_sum, count)
            print(sum_1_20/count_20, sum_1_10/count_10, sum_1_5/count_5)


@jit(nopython=True)
def task_10():
    count = 0
    successful = 0
    while True:
        success = True
        time = random.randint(1, 60)
        temperature = random.randint(1, 100)
        salt = random.randint(1, 25)
        meat = random.randint(1, 400)
        if time > 30 and success:
            if not(salt > 10) and success:
                success = False
        elif temperature > 80 and success:
            if not(meat < 300) and success:
                success = False
        elif temperature <= 80 and success:
            success = False

        if (20 < time <= 45) and success:
            if temperature > 50 and success:
                if not(salt <= 20) and success:
                    success = False
            else:
                success = False
        elif not(meat > 150) and success:
            success = False

        if success:
            successful += 1
        count += 1
        if count % 100_000_000 == 0:
            print(successful/count, successful, count)

task_10()
