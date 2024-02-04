from tyers.tyres import Tyers

class CarriganTyres(Tyers):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        for tyre in self.wear:
            if tyre >= 0.9:
                return True
        return False