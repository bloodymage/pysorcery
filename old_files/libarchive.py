# Libraries
#
#-------------------------------------------------------------------------------

# System Libraries
import sys
import os
import tarfile
import zipfile
import zlib
import lzma
import gzip
import bz2


# Other Libraries
# Only Load if module rarfile available.
# If not, error, ask if user wants to install
# import rarfile


# Application Libraries
# System Library Overrides
from pysorcery.lib import logging
# Other Application Libraries
from pysorcery.lib import libfiles
from pysorcery.lib import libtext


# Other Optional Libraries

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)

#-------------------------------------------------------------------------------
#
# Classes
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Class CZipFile
#
#-------------------------------------------------------------------------------
class CZipFile(libfiles.BaseFile):
    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def extract(self):
        logger.debug("Begin Function")
        logger.debug("Xfile: "+ str(self.name))

        file_dir, basename, ext = CompressedFile.pne(self)

        logger.debug("File_dir: " + str(file_dir))
        logger.debug("File name: " + str(basename))
        logger.debug("Extention: " + str(ext))
    
        try:
            zip_file = zipfile.ZipFile(self.name)
            for name in zip_file.namelist():
                zip_file.extractall(basename)
            logger.info("Extracted file: " + str(self.name))
        except zipfile.BadZipFile:
            logger.error("Unk Extraction Error")
            pass
        except IOError:
            logger.error("IO Error")
            pass
        except:
            logger.error("Unknown Error")
            
        return 0

    def list_files(self):
        logger.debug("Begin Function")
        
        logger.debug('End Function')
        return

    def compress(self):
        logger.debug("Begin Function")
        
        logger.debug('End Function')
        return
    
    def test(self):
        logger.debug("Begin Function")
        
        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class TarFile
#
#-------------------------------------------------------------------------------
class CTarFile(libfiles.BaseFile):
    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def extract(self):
        logger.debug("Begin Function")
        logger.debug("Xfile: " + str(self.name))

        file_dir, basename, ext = CompressedFile.pne(self)

        logger.debug("File_dir: " + str(file_dir))
        logger.debug("File name: " + str(basename))
        logger.debug("Extention: " + str(ext))
    
        try:
            tar_file = tarfile.open(self.name)
            for name in tar_file.getnames():
                tar_file.extractall(basename)
            logger.info("Extracted file: " + str(self.name))
        except zipfile.BadZipFile:
            logger.error("Unk Extraction Error")
            pass
        except IOError:
            logger.error("IO Error")
            pass
        except:
            logger.error("Unknown Error")
            
        return 0

    def list_files(self):
        logger.debug("Begin Function")
        
        logger.debug('End Function')
        return

    def compress(self):
        logger.debug("Begin Function")
        
        logger.debug('End Function')
        return
    
    def test(self):
        logger.debug("Begin Function")
        
        logger.debug('End Function')
        return


#-------------------------------------------------------------------------------
#
# Class CZipFile
#
#-------------------------------------------------------------------------------
class CLZMAFile(libfiles.BaseFile):
    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def extract(self):
        logger.debug("Begin Function")
        
        logger.debug("Xfile: "+ str(self.name))            
        return 0

    def list_files(self):
        logger.debug("Begin Function")
        
        logger.debug('End Function')
        return

    def compress(self):
        logger.debug("Begin Function")
        
        logger.debug('End Function')
        return
    
    def test(self):
        logger.debug("Begin Function")
        
        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class CZipFile
#
#-------------------------------------------------------------------------------
class CGZFile(libfiles.BaseFile):
    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def extract(self):
        logger.debug("Begin Function")
        logger.debug("Xfile: "+ str(self.name))

        logger.debug('End Function')            
        return 0

    def list_files(self):
        logger.debug("Begin Function")
        
        logger.debug('End Function')
        return

    def compress(self):
        logger.debug("Begin Function")
        
        logger.debug('End Function')
        return
    
    def test(self):
        logger.debug("Begin Function")
        
        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class CZipFile
#
#-------------------------------------------------------------------------------
class CBZ2File(libfiles.BaseFile):
    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def extract(self):
        logger.debug("Begin Function")
        logger.debug("Xfile: "+ str(self.name))

        file_dir, basename, ext = CompressedFile.pne(self)

        logger.debug("File_dir: " + str(file_dir))
        logger.debug("File name: " + str(basename))
        logger.debug("Extention: " + str(ext))
    
        try:
            zip_file = zipfile.ZipFile(self.name)
            for name in zip_file.namelist():
                zip_file.extractall(basename)
            logger.info("Extracted file: " + str(self.name))
        except zipfile.BadZipFile:
            logger.error("Unk Extraction Error")
            pass
        except IOError:
            logger.error("IO Error")
            pass
        except:
            logger.error("Unknown Error")
            
        return 0

    def list_files(self):
        logger.debug("Begin Function")
        
        logger.debug('End Function')
        return

    def compress(self):
        logger.debug("Begin Function")
        
        logger.debug('End Function')
        return
    
    def test(self):
        logger.debug("Begin Function")
        
        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class CompressedFile
# 
#
#-------------------------------------------------------------------------------
class CompressedFile(libfiles.BaseFile):
    #-------------------------------------------------------------------------------
    #
    # Function id_type
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def __init__(self,name):
        logger.debug("Begin Function")
        libfiles.BaseFile.__init__(self,name)
        
        if (self.name.endswith('tar') or
            self.name.endswith('tar.gz') or
            self.name.endswith('tar.bz2') or
            self.name.endswith('tar.xz') or
            self.name.endswith('tgz') or
            self.name.endswith('tbz2')):
            if tarfile.is_tarfile(self.name):
                self.cfile = CTarFile(self.name)
        elif self.name.endswith('zip') and zipfile.is_zipfile(self.name):
            self.cfile = CZipFile(self.name)
        elif self.name.endswith('gz'):
            self.cfile = GZFile(self.name)
        elif self.name.endswith('bz2'):
            self.cfile = BZ2file(self.name)
        elif self.name.endswith('lzma') or self.name.endswith('xz'):
            self.cfile = LZMAfile(self.name)
        #    elif self.name.endswith('.Z'):
        #        extract_zlibfile(self.name)
        #    elif self.name.endswith('7z'):
        #        extract_7zfile(self.name)
        #    elif self.name.endswith('rar'):
        #        extract_rarfile(self.name)
        #    elif self.name.endswith('exe'):
        #       extract_exefile(self.name)
        else:
            logger.error("Invalid: " + str(self.name))

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def extract(self):
        logger.debug("Begin Function")


        self.cfile.extract()

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def list_files(self):
        logger.debug("Begin Function")

        self.cfile.list_files()

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def compress(self):
        logger.debug("Begin Function")

        self.cfile.extract()

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def test(self):
        logger.debug("Begin Function")

        self.cfile.extract()

        logger.debug("End Function")
        return

