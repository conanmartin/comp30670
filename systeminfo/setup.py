from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic inforation for COMP30670",
      url="",
      author="Conan Martin",
      author_email="conan.martin@ucdconnecte",
      licence="GPL3",
      packages=['systeminfo'],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
          }
      )