class dog:
    def __init__(self, legs = 4, tail = 1,  *args, **kwargs):
        self.legs = legs
        self.tail = tail
    
    def bark(self):
        return('Woof')
        
morzsi = dog(4,1)
print(morzsi.bark())

class lab(dog):
    def __init__(self, smart = True, *args, **kwargs):
        self.smart = smart
        
        super(lab, self).__init__(*args, **kwargs)

fido = lab(smart = True, legs =2)
print(fido.legs)
print(fido.smart)
print(fido.bark())
