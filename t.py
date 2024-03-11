def get_name(first, last):
    return first + ' ' + last


# ⛔️ calling the function with keyword arguments
print(get_name(first='bobby', last='hadz'))

# ✅ calling the function with positional arguments
print(get_name('bobby', 'hadz'))