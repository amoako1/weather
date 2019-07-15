
import pyowm
 
owm = pyowm.OWM('8c01f3774e595e13bcd75ca3cdc912a9')
observation = owm.weather_at_place('koforidua,Ghana')
w = observation.get_weather()
 
print(w.get_wind())
print(w.get_humidity())
print(w.get_temperature())


