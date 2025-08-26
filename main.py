from my_random_number_generator import My_Random

# Fixed seed test (should always give the same sequence for the same seed)
r = My_Random()
r.set_seed(1234)
print(r.dice(), r.dice(), r.dice(), r.dice())

# Time-based seed test (different runs may give different sequences)
r2 = My_Random()
r2.set_seed()  # no argument -> use time-based seed
print([r2.dice() for _ in range(5)])
