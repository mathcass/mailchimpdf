try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="mailchimpdf",
      version="0.1.0",
      description="MailChimp DataFrames",
      long_description=("An interface to the MailChimp API "
                        "to make lists available as pandas.DataFrame"
                        "objects"),
      license="MIT",
      email="code@mathcass.com",
      install_requires=[
          "requests==2.9.1",
          "pandas==0.17.1",
          "six==1.10.0",
          "slumber==0.7.1",
      ],
      packages=[
          'mailchimpdf',
      ],
      zip_safe=False,
      entry_points={
          "console_scripts": [
              'mailchimpdf-list=mailchimpdf.list:main',
          ]
      })
