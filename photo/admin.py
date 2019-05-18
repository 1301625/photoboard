from django.contrib import admin

# Register your models here.
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','author','created','updated'] #목록에 보일 필드 설정
    raw_id_fields = ['author'] #ForeignKey 또는 ManyToManyField에 대한 입력 위젯으로 변경하려는 필드의 목록
    list_filter = ['created', 'updated', 'author']
    search_fields = ['text', 'created']
    ordering = ['-updated'] #모델 기본 정렬값이 아닌 어드민사이트 기본 사용될 정렬값


admin.site.register(Photo, PhotoAdmin)