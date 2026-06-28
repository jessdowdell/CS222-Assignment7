def calculate_grade(score):
    # Checks data type
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be an int or float.")
    
    # Checks range
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    
    
    # Determines letter grade
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"