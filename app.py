import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request

app = Flask(__name__)

BASE_URL = "https://hianime.to/search"

def fetch_anime_details(anime_name):
    # Construct the search URL using the `keyword` query parameter
    search_url = f"{BASE_URL}?keyword={anime_name.replace(' ', '+')}"
    
    # Send request to the search URL
    response = requests.get(search_url)
    
    if response.status_code != 200:
        return None  # Return None if there was an error fetching the page
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Initialize a list to store multiple anime details if available
    anime_list = []

    # Find all anime entries in the search results
    anime_cards = soup.find_all('div', class_='flw-item')
    for anime_card in anime_cards:
        anime_details = {}
        
        # Extract title
        title_tag = anime_card.find('h3', class_='film-name').find('a')
        anime_details['title'] = title_tag.get_text() if title_tag else "No Title"
        
        # Extract video link
        link_tag = anime_card.find('a', class_='film-poster-ahref')
        anime_details['video_link'] = f"https://hianime.to{link_tag['href']}" if link_tag else "No Link"
        
        # Extract image URL
        image_tag = anime_card.find('img', class_='film-poster-img')
        anime_details['image_url'] = image_tag['data-src'] if image_tag else "No Image"
        
        # Extract type (e.g., "Special") and duration
        info_tags = anime_card.find('div', class_='fd-infor')
        if info_tags:
            info_items = info_tags.find_all('span', class_='fdi-item')
            anime_details['type'] = info_items[0].get_text() if len(info_items) > 0 else "No Type"
            anime_details['duration'] = info_items[1].get_text() if len(info_items) > 1 else "No Duration"
        
        # Extract episode number from "tick-item tick-sub"
        episode_tag = anime_card.find('div', class_='tick-item tick-sub')
        anime_details['episodes'] = episode_tag.get_text().strip() if episode_tag else "No Episode Number"

        # Append the extracted details to the list
        anime_list.append(anime_details)

    return anime_list

# Flask route to fetch anime details
@app.route('/anime', methods=['GET'])
def get_anime_details():
    anime_name = request.args.get('name')
    if not anime_name:
        return jsonify({"error": "Anime name is required"}), 400

    # Fetch anime details
    anime_details = fetch_anime_details(anime_name)
    
    if not anime_details:
        return jsonify({"error": "Anime not found"}), 404
    
    return jsonify(anime_details)

if __name__ == '__main__':
    app.run(debug=True)
