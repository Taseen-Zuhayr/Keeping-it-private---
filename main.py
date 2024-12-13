class x:
    __pin= 4837
    def __private(self):
        print("I am protected.")
    def display(self):
        print("I am not protected.",x.__private)


obj1 = x()
obj1.__private()
obj1.display()
print(obj1.pin)