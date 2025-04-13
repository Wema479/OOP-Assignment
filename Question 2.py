class dolphin:
    def move(self):
        return "swim deep"

class eagle:
    def move(self):
        return "fly's high!"
    
class Cow:
    def move(self):
        return "walks slowly"    


for animal in [dolphin(), eagle(), Cow()]:
    print(animal.move())

