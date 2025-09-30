# Weather App Setup

## Configuration Setup

1. **Copy the configuration template:**

   ```bash
   cd weather_app
   cp config_template.py config.py
   ```

2. **Get your OpenWeatherMap API key:**

   - Go to https://openweathermap.org/api
   - Sign up for a free account
   - Get your API key from the dashboard

3. **Edit config.py:**

   - Open `config.py` in your editor
   - Replace `"your_openweathermap_api_key_here"` with your actual API key
   - Update `CITY_NAME` if needed (currently set to "Burbank")
   - Update `COUNTRY_CODE` if needed (currently set to "US")

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   python sense_hat_monitor.py
   ```

## Security Note

The `config.py` file is ignored by git to keep your API keys secure. Never commit API keys to version control!

## File Structure

- `config_template.py` - Template for configuration (committed to git)
- `config.py` - Your actual configuration with API keys (ignored by git)
- `sense_hat_monitor.py` - Main application file

