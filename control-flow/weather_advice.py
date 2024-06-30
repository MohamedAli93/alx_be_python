weather_s = str(input("What's the weather like today? (sunny/rainy/cold):"))
if weather_s == "sunny":
    print ("Wear a t-shirt and sunglasses.")
elif weather_s == "rainy":
    print ("Don't forget your umbrella and a raincoat.")
elif weather_s == "cold":
    print ("Make sure to wear a warm coat and a scarf.")
else:
    print ("Sorry, I don't have recommendations for this weather.")