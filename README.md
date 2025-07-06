# MyShop

Django로 만든 쇼핑몰 프로젝트입니다.

## 설치 방법

1. 저장소를 클론합니다:
```bash
git clone <repository-url>
cd myshop
```

2. 가상환경을 생성하고 활성화합니다:
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# 또는
venv\Scripts\activate  # Windows
```

3. 의존성을 설치합니다:
```bash
pip install -r requirements.txt
```

4. 데이터베이스를 마이그레이션합니다:
```bash
python manage.py migrate
```

5. 개발 서버를 실행합니다:
```bash
python manage.py runserver
```

6. 브라우저에서 http://127.0.0.1:8000/ 에 접속합니다.

## 프로젝트 구조

- `myshop/`: Django 프로젝트 설정
- `products/`: 상품 관련 앱
- `manage.py`: Django 관리 스크립트

## 기능

- 상품 관리
- 쇼핑몰 기능 (추후 개발 예정) 