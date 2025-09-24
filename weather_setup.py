#!/usr/bin/env python3
"""
Weather OLED Display Setup Script
This script helps you set up the weather display with your API key
"""

import os

def setup_weather_display():
    """Setup script for weather display configuration"""

    print("🌤️  Weather OLED Display Setup")
    print("=" * 40)

    # Get the practice file
    practice_file = "oled_screen_practce.py"

    if not os.path.exists(practice_file):
        print(f"❌ Error: {practice_file} not found!")
        return

    # Get user input
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    city = input("Enter your city name: ").strip()
    units = input("Use metric (Celsius) or imperial (Fahrenheit)? [metric/imperial]: ").strip().lower()

    if units not in ['metric', 'imperial']:
        units = 'metric'

    if not api_key:
        print("❌ Error: API key is required!")
        print("   Get your free API key from: https://openweathermap.org/api")
        return

    # Read the current file
    with open(practice_file, 'r') as f:
        content = f.read()

    # Replace the configuration values
    content = content.replace('API_KEY = "YOUR_API_KEY_HERE"', f'API_KEY = "{api_key}"')
    content = content.replace('CITY = "London"', f'CITY = "{city}"')
    content = content.replace('UNITS = "metric"', f'UNITS = "{units}"')

    # Write back the updated file
    with open(practice_file, 'w') as f:
        f.write(content)

    print("✅ Configuration updated successfully!")
    print(f"   API Key: {api_key[:10]}...")
    print(f"   City: {city}")
    print(f"   Units: {units}")
    print("\n🚀 You can now run the weather display with:")
    print("   python3 oled_screen_practce.py")
    print("\n📦 Install required packages:")
    print("   pip install -r weather_requirements.txt")

if __name__ == "__main__":
    setup_weather_display()
