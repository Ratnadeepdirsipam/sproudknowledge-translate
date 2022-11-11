from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from googletrans import Translator
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

import pyrebase
config={
 'apiKey': 'AIzaSyALpZXvAbi0RyU1z60QFKaTZEM26ax4AzM',
 'authDomain': 'sproudknowledgechat.firebaseapp.com',
 'projectId': 'sproudknowledgechat',
 'storageBucket': 'sproudknowledgechat.appspot.com',
 'messagingSenderId': '747518791451',
 'appId': '1:747518791451:web:6a22c09a0a1707d82e0dbe',
 'measurementId': 'G-LZHZ5J6QRK',
 'databaseURL' : 'https://sproudknowledgechat-default-rtdb.firebaseio.com'
}

def index(request):
    print(lnguage_translate('i love you',LANGUAGESCODES[0]))
    return HttpResponse('successfully uploaded mail')

def translate(request):
    print(lnguage_translate('i love you',LANGUAGESCODES[0]))
    return HttpResponse('successfully translate')

def post(request):    
    return HttpResponse('successfully uploaded')
def get(request):    
    return HttpResponse('successfully fetched data')

def send_mail_deepu():
    subject = 'welcome to sproudknowledge'
    message = "you are selected as frontend developer for sproudknowledge if you want to work with our company please send a mail like dukudu ani type chesi mahesh babu ki sms chesi bigboss ki vote veyandi"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ssidhusidhu828@gmail.com','ratnadeepdirsipam@gmail.com']
    #,'haripriya.k@rockinterview.in','sneha.j@rockinterview.in','venkata.i@rockinterview.in'
    send_mail( subject, message, email_from, recipient_list )
    print('send mail successfully')

def lnguage_translate(text,lnge):
    translator = Translator()
    translations = translator.translate([text], dest=lnge)
    for translation in translations:
        return translation.text

LANGUAGESCODES = [
    'te','af','sq','am','ar','hy','az','eu','be','bn','bs','bg','ca','ceb','ny','zh-cn','zh-tw','co','hr','cs','da','nl','en',
    'eo','et','tl','fi','fr','fy','gl','ka','de','el','gu','ht','ha','haw','iw','he','hi','hmn','hu','is','ig','id','ga',
    'it','ja','jw','kn','kk','km','ko','ku','ky','lo','la','lv','lt','lb','mk','mg','ms','ml','mt','mi','mr','mn','my',
    'ne','no','or','ps','fa','pl','pt','pa','ro','ru','sm','gd','sr','st','sn','sd','si','sk','sl','so','es','su','sw',
    'sv','tg','ta','th','tr','uk','ur','ug','uz','vi','cy','xh','yi','yo','zu'
  ]