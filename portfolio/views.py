from django.shortcuts import render
from django.http import JsonResponse
import boto3
from botocore.client import Config
import random
import project.settings as settings


# Create your views here.






def home(request):
    return render(request, 'main.html', {})


def getImage(request):
    sesh = boto3.session.Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    s3 = sesh.resource('s3')

    bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)

    setOfImgUrls = []
    for obj in bucket.objects.all():
        if obj.key.find("tower") != -1 and ".db" not in obj.key:
            setOfImgUrls.append(obj.key)
            print obj.key

    index = random.randint(0, len(setOfImgUrls) - 1)
    url = "https://" + settings.AWS_STORAGE_BUCKET_NAME + ".s3.amazonaws.com/" + setOfImgUrls[index]
    return JsonResponse({'image': url})


def getAllImages(request):
    sesh = boto3.session.Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    s3 = sesh.resource('s3')

    bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)

    setOfImgUrls = []
    for obj in bucket.objects.all():
        if obj.key.find("tower") != -1 and ".db" not in obj.key and "diagram" not in obj.key:
            url = "https://" + settings.AWS_STORAGE_BUCKET_NAME + ".s3.amazonaws.com/" + obj.key
            setOfImgUrls.append(url)

    return JsonResponse({'imageDict': setOfImgUrls})
