class Container():
    def getContainer(self):
        return "container"
class Images(Container):
    def getImages(self):
        return "Images"

run = Images()
print(run.getContainer())