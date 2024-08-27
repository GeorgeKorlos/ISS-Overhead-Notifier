# ISS Overhead Notifier: A Real-Time Notification System for ISS Sightings

This Python script notifies you via email when the International Space Station (ISS) is overhead and visible from your location. The program periodically checks the ISS's current position and compares it with your geographical location. If the ISS is within a specified range and it's currently dark outside, you will receive an email prompting you to look up at the sky.

## Features

- **Real-Time ISS Tracking:**
  - The script fetches the current position of the ISS from an API and checks if it's near your location.

- **Day/Night Check:**
  - The script also checks the local sunrise and sunset times to ensure that the ISS is visible when overhead (i.e., it’s dark outside).

- **Email Notifications:**
  - When conditions are met (ISS is overhead and it’s nighttime), an email notification is sent to alert you.

## How It Works

### 1. Fetch ISS Position
The script uses the `http://api.open-notify.org/iss-now.json` API to get the current latitude and longitude of the ISS.

### 2. Compare with User's Location
The script checks if the ISS's position is within a 5-degree range of the user's specified latitude and longitude.

### 3. Check for Darkness
Using the `https://api.sunrise-sunset.org/json` API, the script checks the current time against local sunrise and sunset times to determine if it is dark outside.

### 4. Send Email Notification
If the ISS is overhead and it is dark outside, the script sends an email notification to the user.

### Environment Variables

The script uses the following environment variables:

- `EMAIL`: Your email address used to send and receive notifications.
- `PASSWORD`: The password for your email account (note: it's recommended to use an app-specific password for security reasons).
- `LATITUDE`: Your current latitude.
- `LONGITUDE`: Your current longitude.

### Example

```python
MAIL = os.getenv('EMAIL')
PASS = os.getenv('PASSWORD')
LAT = os.getenv('LATITUDE')
LNG = os.getenv('LONGITUDE')
