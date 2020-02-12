#-------------------------------------------------------------
# File : mp3module.py
#
# Description : Read/Write metadata of mp3 file
#
#-------------------------------------------------------------

#importing os and sys for system prompts
import os,sys

#importing mutagen for working with mp3
from mutagen.easyid3 import EasyID3

#using shutil of make a copy of original file
from shutil import copyfile

#Function to view metadata
def view_meta_audio(audloc):

    #check if file exsts
    if os.path.isfile(audloc):

        audio = EasyID3(audloc)

        #If this tag exits the no metadata
        if str(audio['artist']) != str("[u'ExifRemoved']"):

                for f,k in audio.items():

                        print(f,k)

        else:

                #success message
                print("No metadata exists.")

        sys.exit(0)

    else:
        print("The file location cannot be found.")

        sys.exit(1)

#Function to remove metadata
def rem_meta_audio(audloc,newaudloc='ExifStipped_'):

    if os.path.isfile(audloc):
        directory = ''        
        directory,filename = os.path.split(audloc)
        if directory is '':        
                directory = str(os.getcwd())
        #creating a new path for saving
        newloc = os.path.join(directory,str(newaudloc)+str(filename))
        #mutagen modifies the original mp3 file hence we create a copy
        copyfile(audloc,newloc)

        #Opening the audio itself
        audio = EasyID3(newloc)

        audio.delete()

        #as all tags are deleted we add a 'ExifRemoved' Stamp for any verifications later
        audio['artist'] = 'ExifRemoved'

        #saving the file changes
        audio.save()

        #This would only be invoked when called from dirmodule
        if newaudloc is not 'ExifStipped_':
            return

        #Code continuation if not returned
        print("Metadata Removal Complete")

        sys.exit(0)

    else:

        print("The file location cannot be found.")

        sys.exit(1)
