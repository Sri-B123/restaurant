import requests
from app import create_app, db
from app.models import Restaurant

app = create_app()

# Yelp API key
API_KEY = 'QnhNd6ILRPgKCP5c0oMv1wBQKEUh_-eNpdetiQphmWVnbVkLd-XGpOQc5bYe5RRK34iDeNE6a4fkPxiDA2qzFIj1p-pqwrKXBHQT0fz4rcMc0eTBbMQ8k13x9P56ZnYx'
headers = {'Authorization': f'Bearer {API_KEY}'}

def fetch_and_store_restaurants(location):
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'location': location, 'categories': 'restaurants', 'limit': 50}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    with app.app_context():
        for business in data['businesses']:
            restaurant = Restaurant(
                id=business['id'],
                name=business['name'],
                rating=business['rating'],
                address=", ".join(business['location']['display_address']),
                phone=business.get('display_phone', 'N/A')
            )
            db.session.merge(restaurant)  # Use merge to handle duplicates
        db.session.commit()

if __name__ == "__main__":
    fetch_and_store_restaurants("New York, NY")
