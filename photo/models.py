from django.db import models

from django.conf import settings
from django.contrib.auth.models import User  # 장고 기본 사용자 모델
from django.urls import reverse #get_absolute_url

# Create your models here.

class Photo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_photos')
    '''
    장고 사용자모델은 settings.AUTH_USER_MODEL로 사용할것 
    유저모델이 다른모델로 바뀌어도 설정은 항상 따라가기 때문
    '''
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', default='photo/no_image.png')
    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # 모델 정렬 지정
    class Meta:
        ordering = ['-updated']  # 글 수정시간의 내림차순으로 정렬

    def __str__(self):
        return self.author.username+" "+self.created.strftime("%Y-%m-%d|%H:%M:%S")


    def get_absolute_url(self): #주소를 호출해서 detail뷰로 이동한다
        return reverse('photo:photo_detail', args=[str(self.id)])


