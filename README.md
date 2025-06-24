# 🎤 Taylor Swift Lyrics Explorer

A fun and interactive **Streamlit** app that lets you:

* 🔍 Search Taylor Swift songs via the Genius API
* 📜 Display full lyrics in a readable format
* ☁️ Generate a beautiful **word cloud** to visualize frequently used words

---

## 🚀 Features

* ✅ Simple UI using Streamlit
* 🔎 Song search powered by [Genius API](https://genius.com/)
* 📄 Real-time lyrics scraping from Genius
* 🎨 Word cloud visualization using `wordcloud` and `matplotlib`

---

## 📦 Tech Stack

| Tool            | Purpose                          |
| --------------- | -------------------------------- |
| `Streamlit`     | Web UI framework                 |
| `Requests`      | API calls and HTTP requests      |
| `BeautifulSoup` | Web scraping (lyrics extraction) |
| `Matplotlib`    | Displaying the word cloud        |
| `WordCloud`     | Generating the word cloud        |
| `dotenv`        | Managing API keys securely       |

---

## 🛠️ Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/taylor-swift-lyrics-explorer.git
   cd taylor-swift-lyrics-explorer
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your `.env`**

   ```
   GENIUS_API_KEY=your_genius_api_key_here
   ```

4. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

---

## 🔐 How to Get Your Genius API Key

1. Go to [https://genius.com/developers](https://genius.com/developers)
2. Sign in and create a new API client
3. Copy the generated API key and paste it into your `.env` file as `GENIUS_API_KEY`

---
