# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

final_range = []
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            final_range.append(i)
            break

print(f'Всего кратных любому из диапазона от 2 до 9:  {len(final_range)} чисел')
