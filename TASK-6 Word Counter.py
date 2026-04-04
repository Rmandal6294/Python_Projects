from collections import Counter

print("""
      =======================================================================
                            🧮 Word Counter Tool 🧮
      =======================================================================
    """)

print(""" 🔰 Features:
      1.) Showing how many lines and word and character have on this file
      2.) Showing top most used words with count on this file
      -----------------------[WELCOME]----------------------------------------
""")

def read_fileData(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            text = f.read()
            
        lines = text.splitlines()
        words = text.split()
        characters = len(text)
        
        word_freq = (word.strip('.,!?;:"()').lower() for word in words)
        word_counter = Counter(word_freq)
        
        if "" in word_counter:
            del word_counter[""]
            
        mostCommon = word_counter.most_common(10)
        
        print("\n===== FILE ANALYSIS =====")
        print(f"🔖 Total Lines : {len(lines)}")
        print(f"📒 Total Words : {len(words)}")
        print(f"🏷️ Total Characters : {characters}")
        
        print("\n📈 ------->>> Top 10 Words <<<-------- 📈")
        for word, count in mostCommon:
            print(f"{word} : {count}")
        
    except FileNotFoundError:
        print("⚠️ File Not Found")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print("Error:", e)


filename = input("📁 Enter file name (e.g., sample.txt): ")
read_fileData(filename)
print("\n================================ ooo =======================================")