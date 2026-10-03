def student_results(marks):
    passed = 0
    failed = 0

    for mark in marks:
        if mark >= 40:
            print(mark, "- Pass")
            passed += 1
        else:
            print(mark, "- Fail")
            failed += 1

    print("Total passed:", passed)
    print("Total failed:", failed)


marks = [35, 45, 67, 28, 80]

student_results(marks)