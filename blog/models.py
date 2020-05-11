from django.db import models

# Create your models here.
class Post(models.Model):
    #각 field의 default값은 'null=Flase'로 지정되어 있다. 따라서 admin/사용자 페이지에서
    #데이터를 입력할 때 빈칸으로 남겨두면 자동으로 required(필수입력)미시지를 띄운다.

    title = models.CharField(max_length=100, help_text='최대 100자 내로 입력가능합니다.')
    choices=(
            ('제목1', '제목1 레이블'),
            ('제목2', '제목2 레이블'),
            ('제목3', '제목3 레이블'),
        )
    author = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    #사용자가 직접 입력하지 않아도 자동으로 시간 받아오기
    content = models.TextField()
    #길이 제한이 없는 문자열
    #content 필드에서 빈칸을 허용하려면 null=True로 할 수도 있다. 
    #하지만 나중에 처리하는데 값이 없으면 어려움이 있을까봐 default=''로 놔서 ''(space한 칸)만큼
    #데이터가 기본으로 들어가있게 했다.

    # created_at = models.DateTimeField(auto_now_add=True)
    # #해당 레코드 생성 시 현재 시간 자동 저장
    # updated_at = models.DateTimeField(auto_now=True)
    # #해당 레코드 갱신 시 현재 시간 자동 저장

    #DB에서는 길이제한 유무에 따라서 문자열 필드타입이 다르다.
    #길이 제한이 없는 문자열을 많이 쓰면 성능이 좋지 않다.

    def __str__(self):
        return self.title
    #title : 사용자가 입력한대로 string 불러오기
    #__str__함수를 쓰면 제목을 띄울 때 사용자에게 입력받은 문자열을 그대로 나타나게 한다.
    #이걸 지정해주지 않으면 admin페이지에서 django default 설정대로 일괄적으로 부여된 게시물 넘버가 나온다.
