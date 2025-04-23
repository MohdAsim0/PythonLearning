
def full_name(first_name, last_name):
    full_name = first_name+last_name
    return full_name


print(full_name('asim', 'khan'))


def full_name_type(first_name: str, last_name: str):
    full_name = first_name.capitalize()+last_name.capitalize()
    return full_name


print(full_name_type('asim', 'khan'))


def sumt(a: int, b: int):
    ans = a + b
    return ans


print(sumt(1, 2))
