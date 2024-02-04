from tyers.tyres import Tyers

class OctoPrimeTyres(Tyers):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        sum = 0
        for tyre in self.wear:
            sum += tyre
        if sum >= 3:
            return True
        return False

