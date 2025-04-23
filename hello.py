meaning = 8
print('')

if meaning > 10:
    print('right on')
else:
    print("not today")


# Ternary operator
print('Right on!') if meaning > 10 else print('Not today')

n = 5
res = "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
print(res)
