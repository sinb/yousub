from setuptools import setup

description = """Download subtitles from YouTube"""


setup(name='yousub',
      version='0.1',
      description=description,
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
      zip_safe=False)
