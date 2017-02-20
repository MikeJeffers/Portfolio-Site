from django.shortcuts import render, redirect
from django.http import JsonResponse
import boto3
import random
import project.settings as settings

ACCEPTABLE_IMG_FILES = ['.png', '.jpg', '.gif']
MAX_IMGS_PER_PAGE = 15


def home(request):
    sesh = boto3.session.Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    s3 = sesh.resource('s3')
    bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)

    setOfImgUrls = []

    for obj in bucket.objects.filter(Prefix="portfolio/media/Splash/"):
        if isValidImgKey(obj.key):
            url = "https://" + settings.AWS_STORAGE_BUCKET_NAME + ".s3.amazonaws.com/" + obj.key
            setOfImgUrls.append(url)

    if len(setOfImgUrls) == 0:
        return render(request, 'main.html', {'splashUrl': ''})

    index = random.randint(0, len(setOfImgUrls) - 1)
    imgUrl = setOfImgUrls[index]

    return render(request, 'main.html', {'splashUrl': imgUrl})


def cv(request):
    return render(request, 'cv.html', {})


def arch(request):
    return render(request, 'arch.html', {'years': [1, 2, 3, 4, 5]})


def thesis(request):
    return render(request, 'thesis.html', {})


def mastersThesis(request):
    return render(request, 'masters-thesis.html', {})


def about(request):
    return render(request, 'about.html', {})


def code(request):
    return redirect('https://github.com/mikejeffers')


def research(request):
    return redirect('https://vimeo.com/iosignals')


def proj(request, id=0):
    return render(request, 'proj.html', {})


def getAllImages(request):
    sesh = boto3.session.Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    s3 = sesh.resource('s3')

    bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)

    setOfImgUrls = []
    for obj in bucket.objects.all():
        if isValidImgKey(obj.key):
            url = "https://" + settings.AWS_STORAGE_BUCKET_NAME + ".s3.amazonaws.com/" + obj.key
            setOfImgUrls.append(url)
    setOfImgUrls = listMaxSize(setOfImgUrls)
    return JsonResponse({'imageDict': setOfImgUrls})


def getAllProjects(request):
    sesh = boto3.session.Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    s3 = sesh.resource('s3')
    bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)

    setOfImgUrls = []
    for obj in bucket.objects.filter(MaxKeys=3, Delimiter=".png"):
        if obj.key.find("year") != -1 and isValidImgKey(obj.key):
            url = "https://" + settings.AWS_STORAGE_BUCKET_NAME + ".s3.amazonaws.com/" + obj.key
            setOfImgUrls.append(url)
    setOfImgUrls = listMaxSize(setOfImgUrls)
    return JsonResponse({'imageDict': setOfImgUrls})


def getProjectByYear(request, year=5):
    sesh = boto3.session.Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    s3 = sesh.resource('s3')
    bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)

    setOfImgUrls = set()

    for obj in bucket.objects.filter(Prefix="portfolio/media/Year" + year).limit(40):
        if obj.key.find("year") != -1 and isValidImgKey(obj.key):
            url = "https://" + settings.AWS_STORAGE_BUCKET_NAME + ".s3.amazonaws.com/" + obj.key
            setOfImgUrls.add(url)
    listOfUrls = list(setOfImgUrls)
    random.shuffle(listOfUrls)
    listOfUrls = listMaxSize(listOfUrls)
    return JsonResponse({'imageDict': listOfUrls})


def getThesisTopics(request):
    sesh = boto3.session.Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    s3 = sesh.resource('s3')
    bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)

    topicSet = set()
    for obj in bucket.objects.filter(Prefix="portfolio/media/THESIS_IMGS/"):
        if obj.key.find(".db") == -1:
            topicSet.add(obj.key.split('/')[3])  # adds subfolder name only

    return JsonResponse({'topics': list(topicSet)})


def getThesisTopic(request, topic):
    sesh = boto3.session.Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    s3 = sesh.resource('s3')
    bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)

    setOfImgUrls = set()

    for obj in bucket.objects.filter(Prefix="portfolio/media/THESIS_IMGS/" + topic + "/").limit(40):
        if isValidImgKey(obj.key):
            url = "https://" + settings.AWS_STORAGE_BUCKET_NAME + ".s3.amazonaws.com/" + obj.key
            setOfImgUrls.add(url)
    listOfUrls = list(setOfImgUrls)
    random.shuffle(listOfUrls)
    listOfUrls = listMaxSize(listOfUrls)
    return JsonResponse({'imageDict': listOfUrls})


def getMastersImages(request):
    sesh = boto3.session.Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    s3 = sesh.resource('s3')
    bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)

    setOfImgUrls = set()

    for obj in bucket.objects.filter(Prefix="portfolio/media/MSCD_THESIS_IMGS/").limit(40):
        if isValidImgKey(obj.key):
            url = "https://" + settings.AWS_STORAGE_BUCKET_NAME + ".s3.amazonaws.com/" + obj.key
            setOfImgUrls.add(url)
    listOfUrls = list(setOfImgUrls)
    random.shuffle(listOfUrls)
    listOfUrls = listMaxSize(listOfUrls)
    return JsonResponse({'imageDict': listOfUrls})


def listMaxSize(collection, limit=MAX_IMGS_PER_PAGE):
    if len(collection) > limit:
        return collection[0:limit]
    return collection


def isValidImgKey(url, formats=ACCEPTABLE_IMG_FILES):
    if len(formats) > 0:
        for format in formats:
            if format in url:
                return True
    return False
