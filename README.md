# METAMINE

Metamine is a full-featured command-line application for reading and removing meta information in a wide variety of files, without   compromising the data in file.

It was born from the lack of existing tool that was completely written in Python and had very simple commands to execute.

For the time, It supports the following file types:
	
* .jpg  
* .mp3
* .pdf
* .docx
* .pptx
* .xlsx

Further more it supports batch-processing where you can put all your files in a folder and remove metadata at once.

# RUNNING

This tool can be run directly. You just have to run the metamine.py along with the file type you want to view/remove metadata.
For example,
* WINDOWS:<br />
        py -3 metamine.py `file_location` -v <br />
* LINUX:<br />
        python3 metamine.py `file_location` -v 

The script won't work if the modules along with metamine.py are not in the same directory so you need to ensure that they remain in bin.

# DEPENDENCIES

Python 3 or later is required alongwith the following libraries:
- [PyPDF2](https://github.com/mstamy2/PyPDF2)
- [mutagen](https://github.com/mutagen-io/mutagen) 
- [pathlib2](https://github.com/mcmtroffaes/pathlib2)
- [tqdm](https://github.com/tqdm/tqdm)
- [python-docx](https://github.com/python-openxml/python-docx)
- [python-pptx](https://github.com/scanny/python-pptx) 
- [openpyxl](https://github.com/chronossc/openpyxl)

# AUTHORS
- **Aditya Ramesh** - [aditya-dk7](https://github.com/aditya-dk7)
- **Sanchit Bajaj**
- **Riten Bhagra**
- **Aditia Sharma**
