dict = {}
k =4
while(k):
    # FavLang = input("Favourite language: ")
    dict.update( {input("Name: ") : input("Favourite language: ") })
    k = k-1
print(dict)