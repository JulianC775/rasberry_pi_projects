# 🌤️ Weather OLED Display

A Python script to display real-time weather information on a 128x64 OLED display using Raspberry Pi.

## Features

- **Current Temperature** - Real-time temperature display
- **Feels Like Temperature** - Apparent temperature considering wind chill/heat index
- **Weather Conditions** - Current weather description (Sunny, Cloudy, Rainy, etc.)
- **Humidity** - Relative humidity percentage
- **Pressure** - Atmospheric pressure in hPa
- **Wind Speed & Direction** - Wind speed in m/s with compass direction
- **Cycling Display** - Automatically cycles through different weather views
- **Error Handling** - Graceful handling of network/API errors

## Hardware Requirements

- Raspberry Pi (any model with GPIO pins)
- 128x64 OLED display (SSD1306 controller)
- I2C connection between Raspberry Pi and OLED display

## Software Requirements

Install the required Python packages:

```bash
pip install -r weather_requirements.txt
```

Or install manually:

```bash
pip install luma.oled requests psutil
```

## Setup Instructions

### 1. Get OpenWeatherMap API Key

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Generate a free API key
4. Copy the API key for use in the configuration

### 2. Configure Your Location

Run the setup script to configure your API key and location:

```bash
python3 weather_setup.py
```

This will prompt you to enter:

- Your OpenWeatherMap API key
- Your city name
- Temperature units (metric/Celsius or imperial/Fahrenheit)

### 3. Run the Weather Display

```bash
python3 oled_screen_practce.py
```

The display will cycle through three different views every 3 seconds:

1. **Main Weather**: Temperature, feels-like, humidity, wind speed
2. **Detailed Info**: Weather description, pressure, wind direction, timestamp
3. **Status View**: System status, city name, basic temperature and conditions

## Configuration

You can manually edit the configuration in `oled_screen_practce.py`:

```python
# Weather API configuration
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key
CITY = "London"                # Change to your city
UNITS = "metric"              # Use "imperial" for Fahrenheit
```

## Troubleshooting

### Common Issues

1. **"Network Error"**: Check your internet connection
2. **"API Error"**: Verify your API key is correct
3. **"No Data"**: Check that your city name is spelled correctly
4. **OLED not displaying**: Verify I2C connection and address (0x3C)

### I2C Setup on Raspberry Pi

If you haven't enabled I2C yet:

```bash
sudo raspi-config
```

Go to: Interfacing Options → I2C → Enable

### Testing OLED Connection

```bash
i2cdetect -y 1
```

You should see device `3C` in the output.

## API Usage Limits

- **Free Tier**: 1,000 API calls per day
- **Rate Limit**: 60 calls per minute
- The script makes one API call every 9 seconds (when cycling through 3 displays)

## File Structure

- `oled_screen_practce.py` - Main weather display script
- `oled_screen.py` - Original system stats display (for reference)
- `weather_requirements.txt` - Python dependencies
- `weather_setup.py` - Configuration setup script
- `weather_readme.md` - This documentation

## Customization

You can modify the display cycle by editing the `displays` list in the `display_weather_cycle()` function to show different information or change the timing.

## License

This project is open source and available under the MIT License.
