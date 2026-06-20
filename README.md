# 1. 로컬 Git 초기화 및 필수 소스 파일만 추가 (CSV 원본 데이터는 올리지 마세요)
git init
git add index.html app.py requirements.txt README.md
# 2. 커밋 생성 및 기본 브랜치를 main으로 설정
git commit -m "Deploy SVC Failure Rate Analysis Dashboard"
git branch -M main
# 3. 원격 GitHub 저장소 등록 및 최초 업로드
git remote add origin https://github.com/나의GitHub계정/저장소이름.git
git push -u origin main
