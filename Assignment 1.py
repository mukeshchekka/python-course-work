# Task: Collect Netflix Application Content Details from User

show_id = int(input("Enter Show ID (unique integer): "))
show_title = input("Enter Show Title (e.g., Stranger Things): ")
subscription_price = float(input("Enter Subscription Price (₹): "))
genres_input = input("Enter Genres (comma-separated, e.g., Thriller,Drama,Sci-Fi): ")
genres = [genre.strip() for genre in genres_input.split(',')]
available_streams = int(input("Enter Number of Available Streams (licenses): "))
times_watched = int(input("Enter Times Watched: "))
watch_stats = (available_streams, times_watched)
discount_percent = float(input("Enter Discount Percentage on Subscription (e.g., 15.0): "))
# 7. Show Features (like HD, 4K, Dolby Audio, etc.)
features_input = input("Enter Unique Show Features (comma-separated, e.g., 4K,HD,Dolby Audio): ")
show_features = {feature.strip() for feature in features_input.split(',')}
studio_name = input("Enter Production Studio Name: ")
studio_contact = input("Enter Studio Contact Number: ")
studio_location = input("Enter Studio Location: ")
studio_details = {
    "Studio Name": studio_name,
    "Contact": studio_contact,
    "Location": studio_location
}
print("\n--- Netflix Show/Content Details ---")
print(f"Show ID: {show_id}")
print(f"Title: {show_title}")
print(f"Subscription Price: ₹{subscription_price}")
print(f"Genres: {genres}")
print(f"Watch Stats (Available Streams, Times Watched): {watch_stats}")
print(f"Discount: {discount_percent}%")
print(f"Features: {show_features}")
print(f"Studio Info: {studio_details}")
