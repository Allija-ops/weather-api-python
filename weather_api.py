
###How to get your api key??? ---> open this link https://openweathermap.org/ and create an account
###Then it's just simple..

###This is just an simple project with API's nothing special...

import os 
import requests as req

def conversion(temperature):
    toggle = input("C or F? ")

    if toggle == "C" or toggle =="c":
        print(f"Temperature: {temperature} degrees celsius.")
        
    elif toggle == "F" or toggle =="f":
        fahrenheit = (float(temperature) * 9/5) + 32
        print(f"Temperature: {round(fahrenheit,3)} degrees fahrenheit.")
        

    


while True:
    try:
        print("====== WEATHER API ======")
        city = input("Input the city that you want the basic information for/(input quit to exit): ")
        print("")

        api_key = os.getenv("OPENWEATHER_API_KEY")

        params = {
            "q": city,
            "appid":api_key,
            "units":"metric",
        }

        url = "https://api.openweathermap.org/data/2.5/weather"
        
        if city =="quit":
            print("GOODBYE!")
            break

        response = req.get(url,params=params)
        data = response.json()
        response.raise_for_status()
        
        temperature = data["main"]["temp"]
        
        print(f"City: {city}")

        if "clear" in data["weather"][0]["description"]:
            emoji = "☀️"
            print(f"Description: {emoji}")

        elif "clouds" in data["weather"][0]["description"]:
            emoji ="☁️"
            print(f"Description: {emoji}")
        
        elif "rain" in data["weather"][0]["description"] or "storm" in data["weather"][0]["description"]:
            emoji ="🌧️"
            print(f"Description: {emoji}")
        
        else:
            print(f"Description: {data["weather"][0]["description"]}")


        conversion(temperature)
        print(f"Humidity: {data["main"]["humidity"]}%")
        print("")

    except req.HTTPError as e:
        if response.status_code == 404:
            print("City not found:",e) #HTTPError if you input in a wrong city
            print("")
        
        else:
            print("HTTP error:",data.get("message",response.status_code))
            print("")

    except req.RequestException as e: #RequestException if the URL is wrong
        print("Network/request error:",e)
        print("")

