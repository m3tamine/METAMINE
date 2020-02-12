#-------------------------------------------------------------
# File : pdfmodule.py
#
# Description : Read/Write metadata of pdf file
#
#-------------------------------------------------------------

#importing os and sys for system prompts
import os,sys

#importing PyPDF2 for pdf manipulation
from PyPDF2 import PdfFileReader,PdfFileMerger

#Function to view metadata of pdf
def view_meta_pdf(pdfloc):

    #prompt to check if path exists
    if os.path.isfile(pdfloc):

        with open(pdfloc, 'rb') as f:

                pdf = PdfFileReader(f)

                info = pdf.getDocumentInfo()

                number_of_pages = pdf.getNumPages()
        #to loop through every tag in pdf
        for f,k in info.items():

            print(f,':',k) 

        print('No. of Pages : ',number_of_pages)	

        sys.exit(0)

    else:

        print("The file location cannot be found.")

        sys.exit(1)

#function to remove metadata
def rem_meta_pdf(pdfloc,newpdfloc='Exif_Stripped_'):

    if os.path.isfile(pdfloc):

        with open(pdfloc, 'rb') as f:
                directory = ''
                directory,filename = os.path.split(pdfloc)
                merger = PdfFileMerger()
                if directory is '':
                        directory = str(os.getcwd())
                

                #reading the pdf file
                merger.append(PdfFileReader(pdfloc, 'rb'))

                #saving the new file
                merger.write(os.path.join(directory,str(newpdfloc)+str(filename)))

                #would only return if called from the dir module
                if newpdfloc is not 'Exif_Stripped_':

                   return

                #success prompt
                print("Metadata removal complete.")

        sys.exit(0)

    else:

        print("The file location cannot be found.")

        sys.exit(1)


