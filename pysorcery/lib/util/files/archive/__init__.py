# Libraries
#
#-------------------------------------------------------------------------------

# System Libraries
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
from pysorcery.lib.system import logging
from pysorcery.lib.system import shutil
# Other Application Libraries
from pysorcery.lib.sorcery import files
from pysorcery.lib.util import text


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
class CZipFile(files.BaseFile):
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
        logger.debug("Xfile: "+ str(self.filename))

        file_dir, basename, ext = CompressedFile.pne(self)

        logger.debug("File_dir: " + str(file_dir))
        logger.debug("File name: " + str(basename))
        logger.debug("Extention: " + str(ext))
    
        try:
            zip_file = zipfile.ZipFile(self.filename)
            for name in zip_file.namelist():
                zip_file.extractall(basename)
            logger.info("Extracted file: " + str(self.filename))
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
class CTarFile(files.BaseFile):
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
        logger.debug("Xfile: " + str(self.filename))

        file_dir, basename, ext = files.BaseFile.pne(self)

        logger.debug("File_dir: " + str(file_dir))
        logger.debug("File name: " + str(basename))
        logger.debug("Extention: " + str(ext))
    
        try:
            tar_file = tarfile.open(self.filename)
            for name in tar_file.getnames():
                tar_file.extractall(basename)
#                logger.info2(name)
#            logger.info1("Extracted file: " + str(self.filename))
        except zipfile.BadZipFile:
            logger.error("Unk Extraction Error")
            pass
        except IOError:
            logger.error("IO Error")
            pass
        except:
            logger.error("Unknown Error")
            
        return

    def list_files(self):
        logger.debug("Begin Function")

        try:
            tar_file = tarfile.open(self.filename)
            for name in tar_file.getnames():
                logger.info1(name)
            logger.info("Extracted file: " + str(self.filename))
        except zipfile.BadZipFile:
            logger.error("Unk Extraction Error")
            pass
        except IOError:
            logger.error("IO Error")
            pass
        except:
            logger.error("Unknown Error")

        logger.debug('End Function')
        return

    def compress(self,source):
        logger.debug("Begin Function")
        
        try:
            tar_file = tarfile.open(self.filename)
            tar_file.add(source)

            logger.info("Added file: " + str(self.source))
        except zipfile.BadZipFile:
            logger.error("Unk Extraction Error")
            pass
        except IOError:
            logger.error("IO Error")
            pass
        except:
            logger.error("Unknown Error")

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
class CLZMAFile(files.BaseFile):
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
        
        logger.debug("Xfile: "+ str(self.filename))            
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
class CGZFile(files.BaseFile):
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
        logger.debug("Xfile: "+ str(self.filename))

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
class CBZ2File(files.BaseFile):
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
        logger.debug("Xfile: "+ str(self.filename))

        file_dir, basename, ext = CompressedFile.pne(self)

        logger.debug("File_dir: " + str(file_dir))
        logger.debug("File name: " + str(basename))
        logger.debug("Extention: " + str(ext))
    
        try:
            zip_file = zipfile.ZipFile(self.filename)
            for name in zip_file.namelist():
                zip_file.extractall(basename)
            logger.info("Extracted file: " + str(self.filename))
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

