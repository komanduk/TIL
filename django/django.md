1. 필드 생성방법
1-1 class (이름) (models.Model)
1-2 테이블 생성
    (테이블 타입)
  주요 Field Types : AutoField, BooleanField, CharField, DateTimeField, FileField, ImageField,TextField
  주요 Relation ship Types : ForeignKey, ManyToManyField, OneToOneField
    (필드 옵션)
    필드옵션 : 필드마다 고유 옵션이 존재, 공통 적용 옵션도 있음
  null (DB 옵션) : DB 필드에 NULL 허용 여부 (디폴트 : False)
  unique (DB 옵션) : 유일성 여부 (디폴트 : False)
  blank : 입력값 유효성 (validation) 검사 시에 empty 값 허용 여부 (디폴트 : False)
  default : 디폴트 값 지정. 값이 지정되지 않았을 때 사용
  verbose_name : 필드 레이블. 지정되지 않으면 필드명이 쓰여짐
  validators : 입력값 유효성 검사를 수행할 함수를 다수 지정
  각 필드마다 고유한 validators 들이 이미 등록되어있기도 함
  예 : 이메일만 받기, 최대길이 제한, 최소길이 제한, 최대값 제한, 최소값 제한 등
  choices (form widget 용) : select box 소스로 사용
  help_text (form widget 용) : 필드 입력 도움말
  auto_now_add : Bool, True 인 경우, 레코드 생성시 현재 시간으로 자동 저장  

2.  Migrate (필드 적용)
 python manage.py 
  makemigrations -> migrate

3. 어드민 생성
 python manage.py ctreatesuperuser
  이름설정 - 이메일(무시가능) - 패스워드

