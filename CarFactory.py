from datetime import datetime
from car import Car

class CarFactory(Car):

    def create_calliope(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_date = datetime.today()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def creat_glissade(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_date = datetime.today()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def creat_palindrome(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_date = datetime.today()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def create_rorschach(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_date = datetime.today()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def creat_thovex(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_date = datetime.today()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage



