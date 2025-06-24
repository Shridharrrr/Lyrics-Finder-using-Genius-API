import streamlit as st
from dotenv import load_dotenv
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import os

st.set_page_config(page_title="Taylor Swift Lyrics Explorer", page_icon="🎤")
st.title("🎤 Taylor Swift Lyrics Explorer")
st.write("Discover lyrics and visualize word patterns in Taylor Swift songs")

load_dotenv()
GENIUS_API_KEY = os.getenv("GENIUS_API_KEY")
GENIUS_API_URL = "https://api.genius.com"

def search_song(title, artist="Taylor+Swift"):
    headers = {"Authorization": f"Bearer {GENIUS_API_KEY}"}
    params = {"q": f"{title}+{artist}"}
    response = requests.get(f"{GENIUS_API_URL}/search", headers=headers, params=params)
    return response.json()

import requests
from bs4 import BeautifulSoup

def get_lyrics(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        page = requests.get(url, headers=headers)
        page.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(page.content, 'html.parser')
        
        lyrics_containers = soup.find_all("div", class_="Lyrics__Container-sc-3d1d18a3-1 bjajog")
        
        if not lyrics_containers:
            return "Lyrics not found."
        
        lyrics = []
        for container in lyrics_containers:
            verse = container.get_text(separator='\n')
            cleaned_verse = '\n'.join(line.strip() for line in verse.split('\n') if line.strip())
            lyrics.append(cleaned_verse)
        
        return '\n\n'.join(lyrics)
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching lyrics: {str(e)}"

def generate_wordcloud(text):
    
    if not text or text == "Lyrics not found.":
        return None
    
    # Customize the word cloud
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        colormap='viridis',
        stopwords={'oh', 'ohh', 'ah', 'la', 'ha', 'hey', 'ooh', 'mm', 'mmm'}
    ).generate(text)
    
    # Display the word cloud
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

song_title = st.text_input("Enter a Taylor Swift song title:", placeholder="e.g. Love Story, Blank Space...")    

if st.button("Get Lyrics") and song_title:
    with st.spinner(f"Searching for '{song_title}'..."):
        search_results = search_song(song_title)
        
        if 'response' not in search_results:
            st.error("Error accessing Genius API. Please try again later.")
            st.stop()
            
        hits = search_results['response']['hits']
        
        if not hits:
            st.warning(f"No results found for '{song_title}'. Please check the spelling.")
            st.stop()
            
        song_info = hits[0]['result']
        song_url = song_info['url']
        
        with st.spinner(f"Fetching lyrics for '{song_info['title']}'..."):
            lyrics = get_lyrics(song_url)
            
           
            if lyrics:
                
                st.subheader(song_info['title'])
                if 'primary_artist' in song_info:
                    st.caption(f"by {song_info['primary_artist']['name']}")
                
                # Display lyrics in a text box
                st.text_area("Lyrics:", value=lyrics, height=300, key="lyrics_display")
                
                # Generate word cloud
                try:
                    st.subheader("Word Cloud")
                    generate_wordcloud(lyrics)
                except Exception as e:
                    st.warning(f"Could not generate word cloud: {str(e)}")
            else:
                st.warning("Could not retrieve lyrics for this song.")