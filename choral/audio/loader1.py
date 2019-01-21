#
# Title:loader1.py
# Description:
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#

import os

from django import forms

from django.shortcuts import render

from django.http import HttpResponse

from django.urls import reverse

from django.views import generic
from django.views import View

from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect

# import xmltodict

from .models import Artist

class LoaderView(View):


    def get(self, request, file_name):
        file_name = '/Users/guycole/desktop/choral/choral_wave/manifest.xml'

        if os.path.exists(file_name):
            print("file exists")
            with open(file_name) as fd:
                print('xxxx')
#                doc = xmltodict.parse(fd.read())
#                self.process_artist(doc)
        else:
            print("not exist")

        return HttpResponse(file_name)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
