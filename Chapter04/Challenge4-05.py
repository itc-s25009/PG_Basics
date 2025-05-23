def x(masami):
    """
    2024を少数にする
    """
    try:
        return float(masami)
    except ValueError:
        print("error")
a=x("2024")
print(a)
