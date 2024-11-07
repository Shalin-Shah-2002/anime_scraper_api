Here's a basic documentation and README file to help guide users through setting up and using this API.

---

### Git Documentation and README

#### Project Structure
- **app.py**: Main API server with Flask that fetches anime details from the website.
- **README.md**: Detailed setup instructions and usage examples.

---

## README.md

```markdown
# Anime Details Scraper API

This API scrapes anime details (title, video link, image URL, type, duration, and episode number) from the website [hianime.to](https://hianime.to). It provides an endpoint that returns search results for any given anime name.

## Features

- Fetches anime titles, video links, images, type, duration, and episode numbers.
- Simple to set up and easy to use via a single endpoint.

---

## Prerequisites

- Python 3.x
- `Flask` and `BeautifulSoup4` libraries

Install the required packages:
```bash
pip install flask beautifulsoup4 requests
```

---

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. **Run the API server:**

    ```bash
    python app.py
    ```

3. **Access the API:**

   Once running, the API will be accessible at:
   ```
   http://127.0.0.1:5000/anime?name=<anime_name>
   ```
   Replace `<anime_name>` with your desired anime title (e.g., `naruto`).

---

## Usage Example

To fetch anime details, make a GET request to the `/anime` endpoint with the `name` parameter:

```bash
curl http://127.0.0.1:5000/anime?name=naruto
```

### Sample Response

```json
[
    {
        "title": "Naruto OVA3: Hidden Leaf Village Grand Sports Festival",
        "video_link": "https://hianime.to/watch/naruto-ova3-hidden-leaf-village-grand-sports-festival-4136",
        "image_url": "https://cdn.noitatnemucod.net/thumbnail/300x400/100/b4bb0d2caaa9591fdb3c442738d7f87a.jpg",
        "type": "Special",
        "duration": "11m",
        "episode_number": "1"
    }
]
```

---

## API Endpoints

### `GET /anime`

Fetches a list of anime details based on the search term.

- **Parameters**:
  - `name` (string): Name of the anime to search.

- **Response**:
  - A JSON array of objects, each containing:
    - `title`: Title of the anime.
    - `video_link`: Link to the anime on the website.
    - `image_url`: URL to the anime's image.
    - `type`: Type (e.g., "Special", "OVA").
    - `duration`: Duration of the anime.
    - `episode_number`: Episode number or subtitle indicator.

- **Example**:
  ```
  http://127.0.0.1:5000/anime?name=naruto
  ```

---

## Contributing

Feel free to open issues or submit pull requests if you'd like to contribute.

---

