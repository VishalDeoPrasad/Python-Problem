x = {1: 2, 3: 4, 4: 3, 2: 4, 0: 4}
print(x)
sorted_x = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
print(sorted_x)

