def grade_value(grade):
    result = None

    if 2 <= grade_data <= 2.99:
        result = "Fail"
    elif 3 <= grade_data <= 3.49:
        result = "Poor"
    elif 3.50 <= grade_data <= 4.49:
        result = "Good"
    elif 4.50 <= grade_data <= 5.49:
        result = "Very Good"
    else:
        result = "Excellent"

    return result


grade_data = float(input())
print(grade_value(grade_data))
