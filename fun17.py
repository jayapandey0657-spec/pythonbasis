marks = [35, 45, 67, 28, 80]

passed = 0
failed = 0

for mark in marks:
    if mark >= 40:
        passed += 1
    else:
        failed += 1

print("Students passed:", passed)
print("Students failed:", failed)