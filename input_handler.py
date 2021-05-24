import os
import traceback


class InputHandler:

    IMAGES_PARENT_FOLDER = './images'

    def __init__(self):
        filesList = []

    def listFiles(self,path=''):
        if path != '':
            self.IMAGES_PARENT_FOLDER = path
        
        try:
            self.listFiles = [os.path.join(self.IMAGES_PARENT_FOLDER,imageFile) for imageFile in os.listdir(self.IMAGES_PARENT_FOLDER)\
                            if os.path.isfile(os.path.join(self.IMAGES_PARENT_FOLDER,imageFile))]
        except:
            print(traceback.print_exec())
        
        return self.listFiles

if __name__ == '__main__':
    obj = InputHandler()
    print(obj.listFiles())