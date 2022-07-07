import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='TierraCrossSection',
     version='1.0',
     scripts=['HAPILite.py'] ,
     author="Prajwal Niraula",
     author_email="prajwalniraula@gmail.com",

     description="Reduced library for generating atomic cross-sections",
     long_description=long_description,

     long_description_content_type="text/markdown",
     url="https://github.com/disruptiveplanets/tierraCrossSection",
     packages=setuptools.find_packages(),

     classifiers=[
         "Programming Language :: Python :: >3.5",
         "License :: MIT License",
         "Operating System :: LINUX",
     ],

 )
