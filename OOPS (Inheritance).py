# Parent Class
class Hero:
    def __init__(self, name):
        self.name = name
    def intro(self):
        print(f"Main ek super-hero hoon aur mera naam {self.name} hai!")

# Child 1
class FlyingHero(Hero):
    def fly(self): # Yahan se 'name' hata diya
        print(f"{self.name} aasmaan mein ud raha hai! ☁️") # self.name use kiya

# Child 2
class StrongHero(Hero):
    def lift_weight(self): # Yahan se bhi 'name' hata diya
        print(f"{self.name} ne 1000kg wazan utha liya hai! 💪") # self.name use kiya

# Objects
h1 = FlyingHero('Superman')
h2 = StrongHero('Hulk')

# Calling methods
h1.intro()      # Parent ka talent
h1.fly()        # Apna talent

print("---")

h2.intro()      # Parent ka talent
h2.lift_weight() # Apna talent
