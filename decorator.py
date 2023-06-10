def uppercase_decorator(function):
    def wrap():
        text = function()
        return text.upper()

    return wrap

@uppercase_decorator
def hellow_world():
    return 'hello world!'

print(hellow_world())
