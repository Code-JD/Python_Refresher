# name = "Bob"
# greeting = f"Hello, {name}"

# print(greeting)

# name = "Ralph"

# print(greeting)

# ---------------OUTPUT-------------
# Hello, Bob
# Hello, Bob

# name = "Bob"

# print(f"Hello, {name}")

# name = "Ralph"

# print(f"Hello, {name}")

# ---------------OUTPUT-------------
# Hello, Bob
# Hello, Ralph

# name = "Bob"
# greeting = "Hello, {}"
# with_name = greeting.format(name)
# with_name_two = greeting.format("Ralph")

# print(with_name)
# print(with_name_two)

# ---------------OUTPUT-------------
# Hello, Bob
# Hello, Ralph

longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format("Ralph", "Monday")
print(formatted)

# ---------------OUTPUT-------------
# Hello, Ralph. Today is Monday.