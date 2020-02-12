#!/usr/bin/env python3
#-------------------------------------------------------------
# File : metamine.py
#
# Description : Read/Write Meta information 
#
#-------------------------------------------------------------

#importing os and sys for system prompts and argparse as a argument parser
import os,sys,argparse

def tool_banner():
     print('''%s
        \tMetamine %s: The Document Sanitizer
        %s''' % (blue, white, end))

try:
    from bin.colors import end,white,blue
    try:
        import mutagen
        import PyPDF2
        import pathlib2
        import tqdm
        import docx
        import pptx
        import openpyxl 
    except ImportError:
        tool_banner()
        print ("Some modules aren't installed, installing now.")
        os.system('pip3 install mutagen')
        os.system('pip3 install PyPDF2')
        os.system('pip3 install pathlib2')
        os.system('pip3 install tqdm')
        os.system('pip3 install python-docx')
        os.system('pip3 install python-pptx')
        os.system('pip3 install openpyxl')
        print ('Modules have been installed, restart Metamine.')
        quit()
except ImportError:
    print('Metamine isn\'t compatible with python2.\nUse python > 3.4 to run Metamine.')
    quit()


#importing the imgmodule to view/remove metadata of an image
from bin import imgmodule

#importing the mp3module to view/remove metadata of an mp3
from bin import mp3module

#importing the pdfmodule to view/remove metadata of an pdf
from bin import pdfmodule

#importing the dirmodule to remove metadata of files in a dir
from bin import dirmodule

#importing the docxmodule to view/remove metadata of a word file
from bin import docxmodule

#importing the pptxmodule to view/remove metadata of a powerpoint file
from bin import pptxmodule

#importing the xlsxmodule to view/remove metadata of a word file
from bin import xlsxmodule


#Function to only allow compatible extentions using the help of os module
def CheckExt(choices):

    class Act(argparse.Action):

        def __call__(self,parser,namespace,fname,option_string=None):

            ext = os.path.splitext(fname)[1][1:]

            if ext not in choices:

                option_string = '({})'.format(option_string) if option_string else ''

                parser.error("file doesn't end with one of {}{}".format(choices,option_string))

            else:

                setattr(namespace,self.dest,fname)

    return Act

#parser description
parser = argparse.ArgumentParser(description='This Python Scrpit is a Exif/Metadata Remover')

#positional argument to view
parser.add_argument('-v', '--view',dest="VIEW_META",help='view the exif data', action='store_true')

#positional argument for clear
parser.add_argument('-c', '--clear',dest="CLEAR_META",help='Clear Exif data from file', action='store_true')

#argument for file input and checking extension
parser.add_argument('file',action=CheckExt({'jpg','mp3','pdf','docx','pptx','xlsx',''}),help = "Input file : mp3,jpg,pdf,docx,pptx,xlsx,<dir>")



#input in command line
args = parser.parse_args()

if ((args.VIEW_META == False) and (args.CLEAR_META == False)):
    tool_banner()
    parser.print_help()
    quit()


    

#calling image module if selected
if str(args.file).endswith('.jpg'):

    if args.CLEAR_META:
        imgmodule.rem_exif_img(args.file)

    elif args.VIEW_META:
        imgmodule.view_exif_img(args.file)


#calling mp3 module if selected
elif str(args.file).endswith('.mp3'):

    if args.CLEAR_META:
        mp3module.rem_meta_audio(args.file)

    elif args.VIEW_META:
        mp3module.view_meta_audio(args.file)
        
#calling pdf module if selected
elif str(args.file).endswith('.pdf'):

    if args.CLEAR_META:
        pdfmodule.rem_meta_pdf(args.file)

    elif args.VIEW_META:
        pdfmodule.view_meta_pdf(args.file)


#calling the docxmodule if selected
elif str(args.file).endswith('.docx'):
    if args.CLEAR_META:
        docxmodule.rem_meta_docx(args.file)
    
    elif args.VIEW_META:
        docxmodule.view_meta_docx(args.file)

#calling the pptxmodule if selected
elif str(args.file).endswith('.pptx'):
    if args.CLEAR_META:
        pptxmodule.rem_meta_pptx(args.file)
    
    elif args.VIEW_META:
        pptxmodule.view_meta_pptx(args.file)

#calling the xlsxmodule if selected
elif str(args.file).endswith('.xlsx'):
    if args.CLEAR_META:
        xlsxmodule.rem_meta_xlsx(args.file)
    
    elif args.VIEW_META:
        xlsxmodule.view_meta_xlsx(args.file)
 
#calling the dirmodule if selected
elif str(args.file).endswith(''):

    if args.CLEAR_META:
        #check if only directory is entered
        if os.path.dirname(args.file):
            dirmodule.rem_every_exif(args.file)
        else:
            print("You have not chosen a directory")

    elif args.VIEW_META:
        print("Sorry, Viewing is not possible due to file being a directory")

