"""
Lab 07 - Program to implement an Expert System for Weather Forecasting

A simple rule-based (forward-chaining) expert system. It gathers
facts (weather parameters), then applies a knowledge base of
IF-THEN rules to derive conclusions about the expected weather.
"""
# Lab 07 - Expert System for Weather Forecasting

class WeatherExpert:
    def __init__(self, temp, humidity, wind, sky, pressure):
        self.temp = temp
        self.humidity = humidity
        self.wind = wind
        self.sky = sky
        self.pressure = pressure

    def forecast(self):
        result = []

        if self.sky == "clear" and self.humidity < 40:
            result.append("Sunny day expected.")

        if self.sky == "cloudy" and self.humidity >= 70:
            result.append("High chance of rain.")

        if self.pressure < 1000 and self.wind > 40:
            result.append("Storm warning!")

        if self.temp > 35:
            result.append("Heatwave alert.")

        if self.temp < 5:
            result.append("Cold wave alert.")

        if self.humidity >= 40 and self.humidity < 70 and self.sky == "partly cloudy":
            result.append("Pleasant weather expected.")

        if self.wind > 60:
            result.append("High wind advisory.")

        if not result:
            result.append("Weather appears normal.")

        return result


# Case 1
weather1 = WeatherExpert(38, 30, 20, "clear", 1005)

print("Case 1:")
for r in weather1.forecast():
    print("->", r)


# Case 2
weather2 = WeatherExpert(22, 85, 65, "cloudy", 985)

print("\nCase 2:")
for r in weather2.forecast():
    print("->", r)

class WeatherExpert:
    def __init__(self, t, h, w, s, p):
        self.t, self.h, self.w, self.s, self.p = t, h, w, s, p

    def forecast(self):
        r = []

        if self.s == "clear" and self.h < 40:
            r.append("Sunny day")
        if self.s == "cloudy" and self.h >= 70:
            r.append("Rain likely")
        if self.p < 1000 and self.w > 40:
            r.append("Storm warning")
        if self.t > 35:
            r.append("Heatwave alert")
        if self.t < 5:
            r.append("Cold wave alert")
        if 40 <= self.h < 70 and self.s == "partly cloudy":
            r.append("Pleasant weather")
        if self.w > 60:
            r.append("High wind advisory")

        return r or ["Weather is normal"]


# Case 1
w1 = WeatherExpert(38, 30, 20, "clear", 1005)
print("Case 1:", w1.forecast())

# Case 2
w2 = WeatherExpert(22, 85, 65, "cloudy", 985)
print("Case 2:", w2.forecast())