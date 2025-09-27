l = [(10, 'a'), (20, 'b'), (30, 'c')]

# 1. First elements of each tuple as a list
first_elements_list = [x[0] for x in l]
print("First elements as list:", first_elements_list)  # [10, 20, 30]

# 2. Second elements of each tuple as a tuple
second_elements_tuple = tuple(x[1] for x in l)
print("Second elements as tuple:", second_elements_tuple)  # ('a', 'b', 'c')

# 3. Print only the first elements of each tuple in a single line
print("First elements printed in one line:", end=' ')
for x in l:
    print(x[0], end=' ')
print()  # for newline

# 4. First elements as a list using tuple unpacking (alternative)
firsts = [a for a, b in l]
print("First elements using unpacking:", firsts)  # [10, 20, 30]

# 5. Bonus: Using zip to separate first and second elements
a_list, b_list = zip(*l)
print("Using zip - firsts as list:", list(a_list))   # [10, 20, 30]
print("Using zip - seconds as tuple:", tuple(b_list))  # ('a', 'b', 'c')