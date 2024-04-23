def loud(text):
    return text.upper()
def quite(text):
    return text.lower()


def high_ordered_functions(func):
    result = func(input('So\'z kiriting '))
    return result


print(high_ordered_functions(loud))