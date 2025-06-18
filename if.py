def recommend_clothin(temperature):
    if temperature < 15:
        print(f"It's cold outside, wear a jacket!")
    elif temperature < 25:
        print(f"It's a bit chilly, wear a sweater!")
    else:
        print(f"It's warm outside, wear a t-shirt!")

temperature = int(input("Enter the temperature in Celsius: "))
recommend_clothin(temperature)

