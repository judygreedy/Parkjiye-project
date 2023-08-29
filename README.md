# Parkjiye-project
## 프로젝트 구조 소개
boardApp: 게시판과 게시글에 대한 모델, 뷰, 템플릿, URL 등이 정의되어 있는 앱
models.py: Board와 Post 모델 정의
serializers.py: 모델을 JSON으로 직렬화/역직렬화하기 위한 Serializer 클래스 정의
views.py: 게시판과 게시글의 CRUD 기능을 위한 API 뷰 구현
urls.py: URL 패턴 및 라우팅 설정

## 구현 방법에 대한 설명
Django와 Django REST Framework를 사용하여 API를 구현했습니다.
ListView, DetailView 등 제네릭 뷰를 활용하여 코드를 간결하게 유지했습니다.
게시글 목록은 페이징과 필터링 기능을 제공합니다.

## 개발 환경
Python: 3.11.2
Django: 4.2.4
Django REST Framework: (버전)
Database: SQLite (개발용)

## 빌드 & 실행 방법
가상 환경 설정 및 활성화

1.bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

2.의존성 설치
pip install -r requirements.txt

3.데이터베이스 마이그레이션
python manage.py migrate

4.서버 실행
python manage.py runserver

## API 주소
게시판 리스트와 생성: [http://localhost:8000/com/mailplug/homework/api/boards/]
특정 게시판의 세부 정보: [http://localhost:8000/com/mailplug/homework/api/boards/[게시판 id]
특정 게시글의 세부 정보: [http://localhost:8000/com/mailplug/homework/api/posts/[게시글 id]
Swagger 문서: [도메인 혹은 localhost]/swagger/
ReDoc 문서: [http://localhost:8000/redoc/]
