#-------------------------------------------------------------
# File : imgmodule.py
#
# Description : View/Rem metadata of jpg 
#
#-------------------------------------------------------------

#importing os and sys for system prompts
import os,sys

#importing the Image class from PILLOW module
import PIL.Image

#importing the ExifTags class from PILLOW module
from PIL.ExifTags import TAGS

#Function to remove metadata
def rem_exif_img(imgloc,newimgloc='Cleared_EXIF_' ):

    #check if path exists
    if os.path.isfile(imgloc):
        directory = ''
        directory, filename = os.path.split(imgloc)
        if directory is '':
                directory = str(os.getcwd())
        
        #opening the image itself
        image = PIL.Image.open(imgloc)

        #getting all the info from image
        data = list(image.getdata())

        #creating a new Image containg old data from above but void of metadata
        image_new = PIL.Image.new(image.mode, image.size)

        image_new.putdata(data)

        #saving the image
        image_new.save(os.path.join(directory,str(newimgloc)+str(filename)))

        #return to the dirmodule if called
        if newimgloc is not 'Cleared_EXIF_':
            return

        #continuing code if not called from dirmodule
        print("File saved success")
        
        sys.exit(0)
    else:
        print("The file location cannot be found.")
        sys.exit(1)

#function to view the metadata
def view_exif_img(imgloc):

     #check if path exists
     if os.path.isfile(imgloc):
        ret = {}
        i = PIL.Image.open(imgloc)
        info = i._getexif()
        #check if tags exists or not
        if info is not None:

                #looping through the tags to display metadata
                for tag, value in info.items():

                         decoded = TAGS.get(tag, tag)

                         print(decoded,value)
        #prompt if no exif data exists
        else:

                print("The file has no exif data.")

                sys.exit(0)            

     else:

       		print("The file location cannot be found.")

       		sys.exit(1)

