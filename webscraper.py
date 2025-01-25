import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
from urllib.parse import urljoin

# URL of the website
url = 'https://www.welding-alloys.com/'

# List of filler words to exclude
filler_words = set([
    'the', 'a', 'an', 'and', 'but', 'or', 'for', 'nor', 'so', 'yet', 'to', 'of', 'in',
    'on', 'at', 'by', 'with', 'about', 'as', 'from', 'into', 'like', 'through', 'after',
    'over', 'between', 'out', 'against', 'during', 'before', 'under', 'around', 'among',
    'since', 'within', 'without', 'upon', 'along', 'except', 'across', 'off', 'above',
    'below', 'near', 'behind', 'beneath', 'beside', 'next to', 'are', 'we', 'very',
    'really', 'just', 'be', 'that', 'have', 'it', 'not', 'would', 'there', 'or', 'an',
    'so', 'what', 'get', 'request', 'quote', 'sign', 'up', 'out', 'well', 'good', 'people',
    'team', 'these', 'give', 'because', 'any', 'us', 'even', 'can', 'company', 'business',
    'more', 'see', 'details', 'alloys', 'sugar', 'locations', 'our', 'product', 'products',
    'engineered', 'cement', 'contact', 'your', '2024', 'thoughtcorp', '2022', 'applications',
    'industry', 'food', 'mining', 'oil', 'gas', 'petrochemical', 'power', 'pulp', 'paper',
    'railways', 'recycling', 'making', 'news', 'learn', 'link', 'ceramic', 'https', 'www',
    'wp', 'content', 'uploads', '18', 'kit', 'hard', 'advanced', 'industries', 'case',
    'studies', 'innovative', 'than', 'reduce', '19', '03', 'wa', 'top', 'calculator',
    'meet', 'careers', 'menu', 'sustainability', 'range', 'dedicated'
])


def get_subdirectories(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    subdirectories = []

    for link in soup.find_all('a'):
        href = link.get('href')

        # Ensure it's not None and is a proper url
        if href and not href.startswith('#') and not href.startswith('mailto:') and not href.startswith('tel:'):
            # Join the URL if it's relative (not starting with http:// or https://)
            href = urljoin(url, href)
            subdirectories.append(href)

    return subdirectories


def get_text(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text from the webpage
        text = ' '.join(soup.stripped_strings)

        return text
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return ""


def count_words(text):
    # Use regular expressions to find words
    words = re.findall(r'\b\w+\b', text.lower())

    # Filter out filler words and count occurrences of the rest
    filtered_words = [
        word for word in words if word not in filler_words and not word.isdigit() and len(word) > 1]
    word_counts = Counter(filtered_words)

    return word_counts


# Get the subdirectories
subdirectories = get_subdirectories(url)

# Initialize a counter
word_counts = Counter()

# Go through all the subdirectories
for subdir in subdirectories:
    text = get_text(subdir)
    word_counts += count_words(text)

# Get the top 100 most common words
top_100_words = word_counts.most_common(100)

for word, count in top_100_words:
    print(f'{word}: {count}')
