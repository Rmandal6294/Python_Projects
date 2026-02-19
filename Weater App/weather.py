import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime
import json

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        
        self.api_key = "4d8fb5b93d4af21d66a2948710284366"  
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        self.setup_ui()
    
    def setup_ui(self):
        
        bg_color = "#2c3e50"
        fg_color = "#ecf0f1"
        button_color = "#3498db"
        
        self.root.configure(bg=bg_color)
        
        
        title_label = tk.Label(
            self.root,
            text="🌤️ Weather App",
            font=("Arial", 24, "bold"),
            bg=bg_color,
            fg=fg_color
        )
        title_label.pack(pady=20)
        
        #
        search_frame = tk.Frame(self.root, bg=bg_color)
        search_frame.pack(pady=10)
        
        self.city_entry = tk.Entry(
            search_frame,
            font=("Arial", 14),
            width=25,
            relief=tk.FLAT,
            bg="#34495e",
            fg=fg_color,
            insertbackground=fg_color
        )
        self.city_entry.pack(side=tk.LEFT, padx=5, ipady=8)
        self.city_entry.insert(0, "Enter city name")
        self.city_entry.bind("<FocusIn>", self.clear_placeholder)
        self.city_entry.bind("<Return>", lambda e: self.get_weather())
        
        search_button = tk.Button(
            search_frame,
            text="Search",
            font=("Arial", 12, "bold"),
            bg=button_color,
            fg=fg_color,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.get_weather,
            padx=20,
            pady=8
        )
        search_button.pack(side=tk.LEFT, padx=5)
        
      
        self.info_frame = tk.Frame(self.root, bg=bg_color)
        self.info_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        
        self.city_label = tk.Label(
            self.info_frame,
            text="",
            font=("Arial", 22, "bold"),
            bg=bg_color,
            fg=fg_color
        )
        self.city_label.pack(pady=10)
        
        self.temp_label = tk.Label(
            self.info_frame,
            text="",
            font=("Arial", 48, "bold"),
            bg=bg_color,
            fg=fg_color
        )
        self.temp_label.pack(pady=10)
        
        self.desc_label = tk.Label(
            self.info_frame,
            text="",
            font=("Arial", 16),
            bg=bg_color,
            fg=fg_color
        )
        self.desc_label.pack(pady=5)
        
        details_frame = tk.Frame(self.info_frame, bg=bg_color)
        details_frame.pack(pady=20)
        
        self.humidity_label = tk.Label(
            details_frame,
            text="",
            font=("Arial", 12),
            bg=bg_color,
            fg=fg_color
        )
        self.humidity_label.grid(row=0, column=0, padx=20, pady=5)
        
        self.wind_label = tk.Label(
            details_frame,
            text="",
            font=("Arial", 12),
            bg=bg_color,
            fg=fg_color
        )
        self.wind_label.grid(row=0, column=1, padx=20, pady=5)
        
        self.pressure_label = tk.Label(
            details_frame,
            text="",
            font=("Arial", 12),
            bg=bg_color,
            fg=fg_color
        )
        self.pressure_label.grid(row=1, column=0, padx=20, pady=5)
        
        self.feels_label = tk.Label(
            details_frame,
            text="",
            font=("Arial", 12),
            bg=bg_color,
            fg=fg_color
        )
        self.feels_label.grid(row=1, column=1, padx=20, pady=5)
        
        footer_label = tk.Label(
            self.root,
            text="Powered by OpenWeatherMap",
            font=("Arial", 9),
            bg=bg_color,
            fg="#95a5a6"
        )
        footer_label.pack(side=tk.BOTTOM, pady=10)
    
    def clear_placeholder(self, event):
        if self.city_entry.get() == "Enter city name":
            self.city_entry.delete(0, tk.END)
    
    def get_weather(self):
        city = self.city_entry.get()
        
        if not city or city == "Enter city name":
            messagebox.showwarning("Warning", "Please enter a city name!")
            return
        
        if self.api_key == "YOUR_API_KEY_HERE":
            messagebox.showerror(
                "API Key Required",
                "Please get a free API key from:\nhttps://openweathermap.org/api\n\n"
                "Then replace 'YOUR_API_KEY_HERE' in the code with your key."
            )
            return
        
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                self.display_weather(data)
            elif response.status_code == 404:
                messagebox.showerror("Error", "City not found!")
                self.clear_display()
            elif response.status_code == 401:
                messagebox.showerror("Error", "Invalid API key!")
            else:
                messagebox.showerror("Error", f"Error fetching weather data: {response.status_code}")
                
        except requests.exceptions.Timeout:
            messagebox.showerror("Error", "Request timed out. Please try again.")
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Error", "No internet connection!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def display_weather(self, data):
        city_name = data['name']
        country = data['sys']['country']
        temp = round(data['main']['temp'])
        feels_like = round(data['main']['feels_like'])
        description = data['weather'][0]['description'].title()
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        
        weather_id = data['weather'][0]['id']
        icon = self.get_weather_icon(weather_id)
        
        self.city_label.config(text=f"{city_name}, {country}")
        self.temp_label.config(text=f"{icon} {temp}°C")
        self.desc_label.config(text=description)
        self.humidity_label.config(text=f"💧 Humidity: {humidity}%")
        self.wind_label.config(text=f"💨 Wind: {wind_speed} m/s")
        self.pressure_label.config(text=f"🔽 Pressure: {pressure} hPa")
        self.feels_label.config(text=f"🌡️ Feels like: {feels_like}°C")
    
    def get_weather_icon(self, weather_id):
        if weather_id < 300:
            return "⛈️"  # Thunderstorm
        elif weather_id < 400:
            return "🌧️"  # Drizzle
        elif weather_id < 600:
            return "🌧️"  # Rain
        elif weather_id < 700:
            return "❄️"  # Snow
        elif weather_id < 800:
            return "🌫️"  # Atmosphere (fog, mist, etc.)
        elif weather_id == 800:
            return "☀️"  # Clear
        else:
            return "☁️"  # Clouds
    
    def clear_display(self):
        self.city_label.config(text="")
        self.temp_label.config(text="")
        self.desc_label.config(text="")
        self.humidity_label.config(text="")
        self.wind_label.config(text="")
        self.pressure_label.config(text="")
        self.feels_label.config(text="")


def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()