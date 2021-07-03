# name = input("Enter your name: ")
# print(name)

# ---------------OUTPUT-------------
# Enter your name: ralph
# ralph


# size_input = input("How big is your house (in square feet): ")
# square_feet = int(size_input)
# square_meters = square_feet / 10.8
# print(f"{square_feet} square feet is {square_meters} square meters.")

# ---------------OUTPUT-------------
# How big is your house (in square feet): 500
# 500 square feet is 46.29629629629629 square meters.

size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(f"{square_feet} square feet is {square_meters:.2f} square meters.")

# ---------------OUTPUT-------------
# How big is your house (in square feet): 500
# 500 square feet is 46.30 square meters.