#-------------------------------------------------------------
# File : pptxmodule.py
#
# Description : View/Rem metadata of pptx 
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

#importing pptx to view metadata
from pptx import Presentation

#importing pptx to view metadata
import pptx

#Function to remove metadata
def rem_meta_pptx(pptxloc,newpptxloc='Exif_Stripped_'):
    
    if os.path.isfile(pptxloc):
        dirname = ''
        dirname,filename = os.path.split(pptxloc)
        if dirname is '':	
                dirname = str(os.getcwd())
        #Creating a temperory instance that would be deleted later on  
        newloc = os.path.join(dirname,str(newpptxloc)+'Temp_'+str(filename))

        #creating copy of the original file
        copyfile(pptxloc,newloc)
        
        pre, ext = os.path.splitext(newloc)

        #renaming the pptx file as zip to access inside
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

        zip(os.path.join(dirname,"temp_fol"),os.path.join(dirname,str(newpptxloc)+str(filename)))
       
        #Removing the older instances of temp file
        os.remove(newloc)

        #Removing the older instances of temp folder  
        rmtree(os.path.join(dirname,'temp_fol'))

        #Code segment to return if called from the dirmodule
        if newpptxloc is not 'Exif_Stripped_':

            return

        #Success message
        print("Metadata removal SUCCESS")

        sys.exit(0)
    #prompt if no location was found
    else:

        print("The file location cannot be found.")

        sys.exit(1)


#Function for viewing the metadata
def view_meta_pptx(pptxloc):

    if os.path.isfile(pptxloc):
        
        zip = ZipFile(pptxloc)

        pre, ext = os.path.splitext(pptxloc)

        os.rename(pptxloc, pre + '.zip')

        pptxloc = pre + '.zip'

        #Check If there is no metadata
        try:

                zip.getinfo(os.path.join('docProps','core.xml'))

                pre, ext = os.path.splitext(pptxloc)

                os.rename(pptxloc, pre + '.pptx')

                pptxloc = pre + '.pptx'

        except KeyError:

                print("NO METADATA")

                pre, ext = os.path.splitext(pptxloc)

                os.rename(pptxloc, pre + '.pptx')

                pptxloc = pre + '.pptx'

                sys.exit(0)

        

        presentation = Presentation(pptxloc)

        core_properties = presentation.core_properties
                        
        #displaying all metadata if any
        
        print ("Author : ",core_properties.author)
        
        print ("Category : Presentation(.pptx)",core_properties.category)

        print ("Comments : ",core_properties.comments)

        print ("Status : ",core_properties.content_status)

        print ("Created date and time : ",core_properties.created)

        print ("Identifier : ",core_properties.identifier)

        print ("Keywords : ",core_properties.keywords)

        print ("Language : ",core_properties.language)

        print ("Last modified : ",core_properties.last_modified_by)

        print ("Last printed : ",core_properties.last_printed)

        print ("Modified : ",core_properties.modified)

        print ("Revision : ",core_properties.revision)

        print ("Subject : ",core_properties.subject)

        print ("Title : ",core_properties.title)

        print ("Version : ",core_properties.version)  

        sys.exit(0)

    #prompt if loc was not found
    else:

        print("The file location cannot be found.")

        sys.exit(1)
        
	
        
