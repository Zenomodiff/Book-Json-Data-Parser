import requests,json

for i in range(501,1001):
    page_number = (i)
    data_list = []

    url = f"https://www.ebooks.com/api/search/?ResultOrder=Popularity&pageNumber={page_number}&CountryCode=IN&Filter.DrmFree=True"

    req = requests.get(url)
    res = req.json()

    Book = res['books']
    for i in Book:
        Book_name = (i['title'])
        Price = (i['price'])
        Image = (i['image_url'])
        Subtitle = (i['subtitle'])
        Publication_Year = (i['publication_year'])
        Publisher = (i['publisher'])
        Written_By = (i['authors'])
        Book = (i['book_url'])
        Data = "https://www.ebooks.com"
        Book_Link = str(Data) + str(Book)


        if Subtitle == "":
            Subtitle = "None"

        for j in Written_By:
            Author = (j['author_name'])
            Author_Link = (j['author_url'])
            Data = "https://www.ebooks.com"

            Author_Data = str(Data) + str(Author_Link)

            data = {
                    'Book_name': Book_name,
                    'Book_Link' : Book_Link,
                    'Price' : Price,
                    'Image': Image,
                    'Subtitle': Subtitle,
                    'Publication_Year': Publication_Year,
                    'Author': Author,
                    'Author_Data': Author_Data,
                    'Publisher': Publisher
                   }

            data_list.append(data)
            New_List = json.dumps(data_list, indent =2)
            with open(f"page_number{page_number}.json", "w", encoding="utf-8") as file:
                file.write(str(New_List))
                print(New_List)
