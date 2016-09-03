from distutils.core import setup
from os import path

import pypandoc

# Constants
VERSION = '1.0.0'
THIS_DIR_ABS_PATH = path.abspath(path.dirname(__file__))
README_ABS_PATH = path.join(THIS_DIR_ABS_PATH, 'README.md')

# Tools to convert README from Github Markdown (MD) to RST format.
def try_download_pandoc():
  '''
    @description
    Try downloading pandoc if it's not already on the system.

    @return True if we successfully downloaded pandoc, False otherwise
  '''
  try:
    pypandoc.pandoc_download.download_pandoc()
    return True
  except:
    return False

def try_convert_to_rst(path):
  '''
    @description
    Convert the file at the given absolute path to RST format.

    @param path
    Absolute path of the file that we want to convert to RST format.

    @return the contents of the specified file in RST format. 
  '''
  file_contents = ''
  try:
    file_contents = pypandoc.convert(path, 'rst')
  except:
    file_contents = pypandoc.convert(path, 'rst') if try_download_pandoc() else ''
  finally:
    return file_contents

# PyPI Package Configuration
setup(
  # Basic Package Details
  name = 'randomwordgenerator',
  packages = ['randomwordgenerator'],
  version = VERSION,

  # Package Overview and Extended Description (README)
  description = 'Python 3 Random Word Generator Library',
  long_description = try_convert_to_rst(README_ABS_PATH),

  # Dependencies
  install_requires = [
    'requests'
  ],

  # Author Details
  author = 'Sairam Krishnan',
  author_email = 'sairambkrishnan@gmail.com',
  
  # Github Repo Details
  url = 'https://github.com/SaiWebApps/RandomWordGenerator',
  download_url = 'https://github.com/SaiWebApps/RandomWordGenerator/tarball/' + VERSION,
  
  # Misc Details
  license = 'MIT',
  keywords = ['Python', 'random-word']
)