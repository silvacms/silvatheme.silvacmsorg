# -*- coding: utf-8 -*-
# Copyright (c) 2002-2010 Infrae. All rights reserved.
# $Id$

from setuptools import setup, find_packages

version = '1.0dev'

setup(name='silvatheme.silvacmsorg',
      version=version,
      description="silvacms.org website Skin",
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='skin silva',
      author='Infrae',
      author_email='info@infrae.com',
      url='http://silvacms.org',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['silvatheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'silva.core.layout',
          'silva.core.views',
          'silva.core.conf',
          'silva.resourceinclude',
          'zope.cachedescriptors',
      ],
      )
