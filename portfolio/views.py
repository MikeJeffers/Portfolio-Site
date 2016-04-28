from django.shortcuts import render
import boto3
import random
import project.settings as settings


# Create your views here.






def notHome(request):
    return render(request, 'main.html', {})


def home(request):
    s3 = boto3.session.Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                               aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    s3 = s3.resource('s3')
    bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)
    setOfImgUrls = []
    for obj in bucket.objects.all():
        if obj.key.find("tower") != -1 and ".db" not in obj.key:
            setOfImgUrls.append(obj.key)

    index = random.randint(0, len(setOfImgUrls)-1)

    context = dict()
    context['image'] = setOfImgUrls[index]
    return render(request, 'main.html', context)
