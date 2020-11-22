from setuptools import setup

with open('README.md') as f:
   readme = f.read()

setup(name = 'tkvideo',
      version = '0.1.0',
      description = 'Python module for playing videos (without sound) inside tkinter Label widget using Pillow and imageio',
      long_description = readme,
      long_description_content_type = "text/markdown",
      classifiers = [
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.9',
          'Topic :: Multimedia :: Video :: Display'
      ],
      keywords = 'tkvideo tkinter video display label pillow imageio huskee',      
      url = 'https://github.com/huskeee/tkvideo',
      author = 'Xenofon Konitsas (huskee)',
      author_email = 'konitsasx@gmail.com',
      license = 'MIT',
      packages = ['tkvideo'],
      install_requires = [
          'imageio',
          'imageio-ffmpeg',
          'pillow'
      ],
      include_package_data = True,
      zip_safe = False
)
