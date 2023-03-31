def cls():
    """Clear REPL screen"""
    print("\033[H\033[J", end="")


def clamp(value, limits):  # moved from HD_PWM
    lower, upper = limits
    if value is None:
        return None
    elif (upper is not None) and (value > upper):
        return upper
    elif (lower is not None) and (value < lower):
        return lower
    return value
