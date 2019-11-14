from django.contrib import admin
from .models import ImageUploadModel
# Register your models here.
class Image_upload_Admin(admin.ModelAdmin):
    list_display = ('description', 'document','uploaded_at') # 웹페이지의 데이터 리스트 목록 (1,2,3,4)
    list_filter = ['uploaded_at']
    search_fields = ['document']

admin.site.register(ImageUploadModel, Image_upload_Admin) # 모델 보여줄 때, 뒤에 admin사용해서 보여줘라
