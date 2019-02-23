from setuptools import setup

description = """Download subtitles from YouTube"""

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='yousub',
      version='0.0.1',
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/sinb/yousub',
      author='sinb',
      author_email='si.nb@foxmail.com',
      license='MIT',
      packages=['yousub'],
      entry_points={
          'console_scripts': [
              'yousub = yousub.__init__:main'
          ]
      },
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      platforms=['any'])
