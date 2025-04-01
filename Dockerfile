# Base image 설정
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일 복사
COPY app /app

# 컨테이너에서 실행할 명령어 설정
CMD ["python3", "/app/main.py"]

