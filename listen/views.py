# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import os
from pyaudioanalysis import audioTrainTest as aT
# Create your views here.

def homepage(request) :
	return render(request,"index.html",{})


def delete_path_silently(file) :

	try:
		os.remove(file)
	except OSError:
		pass


def upload(request):

	customHeader = request.META['HTTP_MYCUSTOMHEADER']

	# obviously handle correct naming of the file and place it somewhere like media/uploads/
	if request.user.is_anonymous() :
		link = settings.MEDIA_ROOT + "/" +str(0)
		if not os.path.exists(link) :
			os.mkdir(link)
		file = link + "/recording.wav"
	else :
		link = settings.MEDIA_ROOT + "/" + str(request.user)
		if not os.path.exists(link) :
			os.mkdir(link)
		file = link +"/recording.wav"
	# file =  "recording.wav"


	uploadedFile = open(file, "wb")
	# the actual file is in request.body
	uploadedFile.write(request.body)
	uploadedFile.close()
	# put additional logic like creating a model instance or something like this here
	return HttpResponse("Uploaded")


def detectemotion(request) :
	if request.user.is_anonymous() :
		file = settings.MEDIA_ROOT + "/" +str(0) + "/recording.wav"
	else :
		file = settings.MEDIA_ROOT + "/" + str(request.user) +"/recording.wav"
	classifier = os.path.join(settings.BASE_DIR, "classifiers") + "/svmforemotions"
	Result, P, classNames = aT.fileClassification(file, classifier, "svm")
	print Result
	print P
	print classNames
	msg =  "The emotion is : " + classNames[int(Result)]
	return JsonResponse({"msg":msg})