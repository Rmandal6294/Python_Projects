# ====================== WEB SCRAPER ================================
import requests
from bs4 import BeautifulSoup

print("""
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                        🌐 Basic Web Scraper Application 🌐
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.\n""")

def fetch_siteData(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"✅  Connected to '{url}' successfully.")
        return response.text
    
    except requests.exceptions.ConnectionError:
        print("⚠️ Error: Invalid URL or No internet Connection ")
    except Exception as e:
        print("❌Something wrong: ", e)
        
def scrape_headlines(url):
    data = fetch_siteData(url)
    soup = BeautifulSoup(data, "html.parser")
    headlines = soup.find_all(['h1', 'h2', 'h3'])
    
    if not headlines:
        print(f"⚠️ No Headlines Found From {url}::: 🤳 Try Another URL...")
        return
    
    print("\n🥇 ===============>> Latest Headlines <<================= 🥇\n")
    
    for i, headline in enumerate(headlines[:15], start=1):  #! limit to 15
            text = headline.get_text(strip=True)
            if text:
                print(f"{i}. {text}")
        
# =======================================================================
while True:
    print ("""
           ---------------------------------------------
           |          1.) For Seeing Headlines          |
           |          2.) Exit                          |
           ---------------------------------------------
           """)
    
    choice = int(input("🤏 Enter Your Choice (1 / 2): "))
    
    if choice == 1:
        url = input("🔗 Enter An Valid URL (ex: 'https://www.google.com'): ")
        scrape_headlines(url)
    elif choice == 2:
        print("👋 ====== GOODBY ==========")
        break
    else:
        print("⚠️ Enter a valid Choice Between 1 and 2")
    
    