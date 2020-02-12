#!/usr/bin/env python3
#-------------------------------------------------------------
# File : dirmodule.py
#
# Description : Remove metadata of files in a directory
#
#-------------------------------------------------------------

#importing os and sys for system prompts
import os,sys

#importing the imgmodule to remove metadata of image
from bin import imgmodule

#importing the mp3module to remove metadata of mp3
from bin import mp3module

#importing the pdfmodule to remove metadata of pdf
from bin import pdfmodule

#imporing the docxmodule to remove metadata of docx
from bin import docxmodule

#imporing the pptxmodule to remove metadata of pptx
from bin import pptxmodule

#imporing the xlsxmodule to remove metadata of xlsx
from bin import xlsxmodule

#importing the tqdm module for percentage bar
from tqdm import tqdm

#import this to see path
from pathlib2 import Path


#Function to remove the metadata
def rem_every_exif(dirloc):
    #check if the path is really a directory
    if os.path.dirname(dirloc):
        path = Path(dirloc)
        dname = path.parent
        if str(dname) == '.':
            dname = os.getcwd()
        filename = path.name
        directory = os.path.join(dname,filename,'')
	
        #check if folder is empty
        if len(os.listdir(directory)) is not 0:

            #creating directory for saving pdf files after metadata removal
            if 'stripped_pdf' not in os.listdir(directory):
                    os.mkdir(os.path.join(directory,'stripped_pdf', ''))

            #creating directory for saving image files after metadata removal
            if 'stripped_jpg' not in os.listdir(directory):
                    os.mkdir(os.path.join(directory,'stripped_jpg', ''))

            #creating directory for saving mp3 files after metadata removal
            if 'stripped_mp3' not in os.listdir(directory):
                    os.mkdir(os.path.join(directory,'stripped_mp3', ''))
	    
	    #creating directory for saving docx files after metadata removal
            if 'stripped_docx' not in os.listdir(directory):
                    os.mkdir(os.path.join(directory,'stripped_docx', ''))
	    
	    #creating directory for saving pptx files after metadata removal
            if 'stripped_pptx' not in os.listdir(directory):
                    os.mkdir(os.path.join(directory,'stripped_pptx', ''))
             
            #creating directory for saving docx files after metadata removal
            if 'stripped_xlsx' not in os.listdir(directory):
                    os.mkdir(os.path.join(directory,'stripped_xlsx', ''))

            #changing to the entered folder
            os.chdir(directory)

            files_dir = os.getcwd()

            #initializing count as 0 to count incompatible files
            count = 0

            #for loop to loop through every file
            for r in tqdm(os.listdir(files_dir)):
                    if r.split('.')[-1] == 'jpg':

                        imgmodule.rem_exif_img(directory+r,os.path.join('stripped_jpg','Exif_Stripped_'))

                    elif r.split('.')[-1] == 'mp3':
                       
                        mp3module.rem_meta_audio(directory+r,os.path.join('stripped_mp3','Exif_Stripped_'))

                    elif r.split('.')[-1] == 'pdf':

                        pdfmodule.rem_meta_pdf(directory+r,os.path.join('stripped_pdf','Exif_Stripped_'))

                    elif r.split('.')[-1] == 'docx':
			
                        docxmodule.rem_meta_docx(directory+r,os.path.join('stripped_docx','Exif_Stripped_'))
                    
                    elif r.split('.')[-1] == 'pptx':
                        
                        pptxmodule.rem_meta_pptx(directory+r,os.path.join('stripped_pptx','Exif_Stripped_'))

                    elif r.split('.')[-1] == 'xlsx':
                        
                        xlsxmodule.rem_meta_xlsx(directory+r,os.path.join('stripped_xlsx','Exif_Stripped_'))

                    else:

                        count = count + 1

            count = count - 6
            
            #displaying the count of incompatible files
            if count is not 0:
                print(str(count) + " files were ignored due to incompatibility.")    

        #prompt if dir is empty
        else:

            print("The directory location you entered is completely empty")            

        sys.exit(0)

    #prompt if there is no directory as entered
    else:

        print("The directory location cannot be found.")

        sys.exit(1)
