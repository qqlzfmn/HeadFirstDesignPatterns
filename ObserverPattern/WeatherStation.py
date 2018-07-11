class Subject(object):
    def register_observer(self, observer):
        pass

    def remove_observer(self, observer):
        pass

    def notify_observers(self):
        pass


class Observer(object):
    def update(self, temperature, humidity, pressure):
        pass


class DisplayElement(object):
    def display(self):
        pass


class WeatherData(Subject):
    observers = []
    temperature = 0
    humidity = 0
    pressure = 0

    def __int__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()


class CurrentConditionsDisplay(Observer, DisplayElement):
    temperature = 0
    humidity = 0
    weather_data = Subject()

    def __init__(self, weather_data):
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: %.1f°F and %.1f%% humidity" %
              (self.temperature, self.humidity))


class StatisticsDisplay(Observer, DisplayElement):
    max_temp = 0
    min_temp = 200
    temp_sum = 0
    num_readings = 0
    weather_data = WeatherData()

    def __init__(self, weather_data):
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temp_sum += temperature
        self.num_readings += 1
        if temperature > self.max_temp:
            self.max_temp = temperature
        if temperature < self.min_temp:
            self.min_temp = temperature
        self.display()

    def display(self):
        print("Avg/Max/Min temperature = %.1f/%.1f/%.1f" %
              (self.temp_sum / self.num_readings, self.max_temp, self.min_temp))


class ForecastDisplay(Observer, DisplayElement):
    current_pressure = 29.92
    last_pressure = 0
    weather_data = WeatherData()

    def __init__(self, weather_data):
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.last_pressure = self.current_pressure
        self.current_pressure = pressure
        self.display()

    def display(self):
        print("Forecast: ", end='')
        if self.current_pressure > self.last_pressure:
            print("Improving weather on the way!")
        elif self.current_pressure == self.last_pressure:
            print("More of the same.")
        else:
            print("Watch out for cooler, rainy weather.")


class HeatIndexDisplay(Observer, DisplayElement):
    heat_index = 0
    weather_data = WeatherData()

    def __init__(self, weather_data):
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.heat_index = self.compute_heat_index(temperature, humidity)
        self.display()

    @staticmethod
    def compute_heat_index(t, rh):
        index = float(16.923 +
                      0.185212 * t +
                      5.37941 * rh -
                      0.100254 * t * rh +
                      0.00941695 * t ** 2 +
                      0.00728898 * rh ** 2 +
                      0.000345372 * t ** 2 * rh -
                      0.000814971 * t * rh ** 2 +
                      0.0000102102 * t ** 2 * rh ** 2 -
                      0.000038646 * t ** 3 +
                      0.0000291583 * rh ** 3 +
                      0.00000142721 * t ** 3 * rh +
                      0.000000197483 * t * rh ** 3 -
                      0.0000000218429 * t ** 3 * rh ** 2 +
                      0.000000000843296 * t ** 2 * rh ** 3 -
                      0.0000000000481975 * t ** 3 * rh ** 3)
        return index

    def display(self):
        print("Heat index is %.5f" % self.heat_index)


if __name__ == '__main__':
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)
    heat_index_display = HeatIndexDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)
