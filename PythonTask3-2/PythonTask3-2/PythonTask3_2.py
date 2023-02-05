def generate_squares(num):
    return{a: a ** 2 for a in range(num+1) if a>0}

print(generate_squares(5))