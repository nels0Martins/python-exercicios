print()
hr = float(input("Digite a hora: "))
min = float(input("Digite os minutos: "))
a_m = hr*60
total_min = a_m + min
s = total_min * 60
print(f'''a) {a_m :.0f}min
b) {total_min :.0f}min
c) {s :.0f}s''')
print()
