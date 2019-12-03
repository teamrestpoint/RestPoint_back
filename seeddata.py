location1 = Location(location_name="Starbucks on Washington", image_url="https://media.gettyimages.com/photos/exterior-of-newly-redesigned-mcdonalds-location-picture-id458133131?s=612x612",lat= 41.882, long=82.627, address="E Washington St, Chicago, IL", description="This restroom feels alright", directions="Go Left, Go Right, then Stop", has_changing_table =False, is_accessible=True, is_gender_neutral=False, is_family_bathroom=True, number_of_stalls=3)
location1.save()

location2 = Location(location_name = 'Jason’s Deli', image_url = 'https://media.gettyimages.com/photos/exterior-of-newly-redesigned-mcdonalds-location-picture-id458133131?s=612x612', lat = 41.885, long = 87.629, address = '195 N Dearborn St, Chicago, IL 60601', description = "This restroom is alright", directions = "Go Left, Go Right, then Stop", has_changing_table = False, is_accessible = True, is_gender_neutral = False, is_family_bathroom = True, number_of_stalls = 4)
location2.save()

location3 = Location(location_name = 'Qdoba Mexican Grille', image_url = "https://media.gettyimages.com/photos/exterior-of-newly-redesigned-mcdonalds-location-picture-id458133131?s=612x612", lat = 41.883, long = 87.632, address='100 N LaSalle St, Chicago, IL 60602', description = "This restroom is alright", directions = "Go Left, Go Right, then Stop",has_changing_table = False, is_accessible = True, is_gender_neutral = False, is_family_bathroom = True, number_of_stalls = 2)
location3.save()

location4 = Location(location_name = 'Intelligentsia', image_url = "https://media.gettyimages.com/photos/exterior-of-newly-redesigned-mcdonalds-location-picture-id458133131?s=612x612", long = 41.884, lat = 87.626, address = '53 E Randolph St, Chicago, IL 60601', description = "This restroom is alright", directions = "Go Left, Go Right, then Stop",has_changing_table = False, is_accessible = True, is_gender_neutral = False, is_family_bathroom = True, number_of_stalls = 2)
location4.save()

location5 = Location(location_name = 'Renaissance Hotel', image_url = "https://media.gettyimages.com/photos/exterior-of-newly-redesigned-mcdonalds-location-picture-id458133131?s=612x612", lat = 41.886, long = 82.629, address = 'W Wacker St, Chicago, IL 60601', description = "This restroom is alright", directions = "Go Left, Go Right, then Stop",has_changing_table = False, is_accessible = True, is_gender_neutral = False, is_family_bathroom = True, number_of_stalls = 3)
location5.save()


review1 = location1.reviews.create(location = 1, rating = 2, review_text = "This bathroom is terrible", is_accurate = True)
review1.save()

review2 = location2.reviews.create(location = 2, rating = 2, review_text= "This bathroom is ok", is_accurate = True)
review2.save()

review3 = location3.reviews.create(location = 3,rating = 2, review_text = "This bathroom is good", is_accurate = True)
review3.save()

review4 = location4.reviews.create(location = 4, rating = 3, review_text = "This bathroom is great",is_accurate = True)
review4.save()

review5 = location5.reviews.create(location = 5, rating = 4, review_text = "This is the best smelling restroom I’ve ever pooped inside of", is_accurate = True)
review5.save()
