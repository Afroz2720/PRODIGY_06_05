import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h2', class_='entry-title')  # Adjust the selector as needed
        
        for title in titles:
            print(title.get_text(strip=True))
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def main():
    url = 'https://example-blog.com'  # Replace with the target website
    scrape_titles(url)

if __name__ == "__main__":
    main()
