class laptop_object():
    def __init__(self,brand,color="Black",ram="4GB",storage="256",generation="10th"):
        self.brand=brand
        self.color=color
        self.ram=ram
        self.storage=storage
        self.generation=generation
    def texting(self,message):
        print(f"{message} sent successfully")
    def gaming(self,fps):
        print(f"BGMI handled at {fps} fps")
    def browsing(self,browse):
        print(f"browsing in {browse}")
    def specifications(self,):
        print(f"{self.brand} specifics are {self.ram} Ram, {self.storage} Storage, {self.generation} Generation. ")
        print(f"It is a {self.color} Color.")
dell=laptop_object("Dell","white","8GB","512GB","13th")
dell.specifications()
dell.texting("Hello world!")
dell.gaming(120)
dell.browsing("Chrome")
print()
hp=laptop_object("HP","red","16GB","512GB","15th")
hp.specifications()
hp.texting("PythonLife")
hp.gaming(90)
hp.browsing("Microsoft Edge")