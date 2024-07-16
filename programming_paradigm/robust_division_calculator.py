def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return f"The result of the division is {result:.1f}"
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except ValueError:
        return "Error: Please enter numeric values only."