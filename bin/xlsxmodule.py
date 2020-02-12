#-------------------------------------------------------------
# File : xlsxmodule.py
#
# Description : View/Rem metadata of xlsx 
#
#-------------------------------------------------------------

#importing os and sys for system prompts
import os,sys

#importing shutil to copyfile and remove directory
from shutil import copyfile,rmtree

#importing zipfile to work with zip
from zipfile import ZipFile

#importing zipfile to work with zip
import zipfile

#importing xlsx to view metadata
from openpyxl import load_workbook

#importing xlsx to view metadata
import openpyxl

#Function to remove metadata
def rem_meta_xlsx(xlsxloc,newxlsxloc='Exif_Stripped_'):
    
    if os.path.isfile(xlsxloc):
        dirname = ''
        dirname,filename = os.path.split(xlsxloc)
        if dirname is '':	
            dirname = str(os.getcwd())

        #Creating a temperory instance that would be deleted later on  
        newloc = os.path.join(dirname,str(newxlsxloc)+'Temp_'+str(filename))

        #creating copy of the original file
        copyfile(xlsxloc,newloc)

        pre, ext = os.path.splitext(newloc)

        #renaming the xlsx file as zip to access inside
        os.rename(newloc, pre + '.zip')
        
        
        #creating a temp folder to extract metadata
        os.mkdir(os.path.join(dirname,'temp_fol'))

        newloc = pre + '.zip'

        with ZipFile(newloc, 'r') as newzip:
           #extracting all zip data in a temp folder
           newzip.extractall(os.path.join(dirname,'temp_fol', ''))

        #deleting file that contain metadta 
        if os.path.isfile(os.path.join(dirname,'temp_fol','docProps','app.xml')):

            os.remove(os.path.join(dirname,'temp_fol','docProps','app.xml'))

        if os.path.isfile(os.path.join(dirname,'temp_fol','docProps','core.xml')):

            os.remove(os.path.join(dirname,'temp_fol','docProps','core.xml'))

        #Making an archive of the extracted again into a zip
        def zip(src, dst):

            zf = zipfile.ZipFile("%s" % (dst), "w", zipfile.ZIP_DEFLATED)

            abs_src = os.path.abspath(src)

            for dirname, subdirs, files in os.walk(src):

                for filename in files:

                    absname = os.path.abspath(os.path.join(dirname, filename))

                    arcname = absname[len(abs_src) + 1:]

                    zf.write(absname, arcname)

            zf.close()

        zip(os.path.join(dirname,"temp_fol"),os.path.join(dirname,str(newxlsxloc)+str(filename)))

        #Removing the older instances of temp file
        os.remove(newloc)

        #Removing the older instances of temp folder  
        rmtree(os.path.join(dirname,'temp_fol'))

        #Code segment to return if called from the dirmodule
        if newxlsxloc is not 'Exif_Stripped_':

            return

        #Success message
        print("Metadata removal SUCCESS")

        sys.exit(0)
    #prompt if no location was found
    else:

        print("The file location cannot be found.")

        sys.exit(1)

#Function for viewing the metadata
def view_meta_xlsx(xlsxloc):

    if os.path.isfile(xlsxloc):
        
        zip = ZipFile(xlsxloc)

        pre, ext = os.path.splitext(xlsxloc)

        os.rename(xlsxloc, pre + '.zip')

        xlsxloc = pre + '.zip'

        #Check If there is no metadata
        try:

                zip.getinfo(os.path.join('docProps','core.xml'))

                pre, ext = os.path.splitext(xlsxloc)

                os.rename(xlsxloc, pre + '.xlsx')

                xlsxloc = pre + '.xlsx'

        except KeyError:

                print("NO METADATA")

                pre, ext = os.path.splitext(xlsxloc)

                os.rename(xlsxloc, pre + '.xlsx')

                xlsxloc = pre + '.xlsx'

                sys.exit(0)

        wb = load_workbook(xlsxloc)
        properties = wb.properties
        #displaying all metadata if any

        print ("Author: ",properties.creator)

        print ("Title: ",properties.title)

        print ("Description: ",properties.description)

        print ("Subject: ",properties.subject)

        print ("Identifier: ",properties.identifier)

        print ("Language: ",properties.language)

        print ("Modified: ",properties.modified)

        print ("Last Modified by: ",properties.lastModifiedBy)

        print ("Category: ",properties.category)

        print ("Contentstatus: ",properties.contentStatus)

        print ("Version: ",properties.version)

        print ("Keyboards: ",properties.keywords)

        print ("Revision: ",properties.revision)

        print ("LastPrinted: ",properties.lastPrinted)

        sys.exit(0)

    #prompt if loc was not found
    else:

        print("The file location cannot be found.")

        sys.exit(1)
        
        
        
