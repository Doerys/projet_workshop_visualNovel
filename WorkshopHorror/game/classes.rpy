init python:

# Classe Item
    class Item:
        def __init__(self, name, image, selectImage, specialAttribute):
            self.name = name
            self.image = image
            self.selectImage = selectImage
            self.selected = False
            self.specialAttribute = specialAttribute

        def setSelected(self,bool):
            self.selected = bool

        def getSelected(self):
            return self.selected

        def getImage(self):
            return self.image

# Classe Inventaire
    class Inventory:
        def __init__(self, max):
            self.slots = []
            self.max = max

        def getInv(self):
            return self.slots

        def addItem(self, item):
            if (len(self.slots) > self.max):
                return False
            
            else :
                self.slots.append(item)
                return True

        def removeItem(self,item):
            self.slots.remove(item)
            
        def selectItem(self,index):
            for item in self.slots:
                item.setSelected(False)

            self.slots[index].setSelected(True)

# Initialisation de l'inventaire
    inventory = Inventory(7)