import os
import json
from django.shortcuts import render
from google.cloud import vision
import io

# Google Cloud Vision API 인증 설정
credentials_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ocr-text-extraction_api_key.json")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

# JSON 파일 유효성 검사
if credentials_path and os.path.exists(credentials_path):
    try:
        with open(credentials_path, 'r') as file:
            data = json.load(file)
        required_keys = ["type", "project_id"]
        missing_keys = [key for key in required_keys if key not in data]
        if not missing_keys:
            print("JSON 파일이 올바릅니다.")
        else:
            print(f"JSON 파일에서 누락된 키가 있습니다 {missing_keys}")
    except json.JSONDecodeError as e:
        print(f"JSON 파일을 해석하는 중 오류 발생:  {e}")
else:
    print(f"GOOGLE_APPLICATION_CREDENTIALS 환경 변수가 설정되지 않았거나, 파일이 존재하지 않습니다: {credentials_path}")

# 텍스트 감지 함수 (OCR)
def detect_text(image_content):
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=image_content)
    # image_content → 사용자가 올린 사진 데이터를 가져온다.
    response = client.text_detection(image=image)
    # 사진속 텍스트 감지
    texts = response.text_annotations
    # 찾은 글자 정보 가져와 texts에 담는다.
    if not texts:
        return {"text": "text=x", "warning": None}
    
    # OCR 결과에서 첫 번째 요소가 전체 텍스트 (이후의 요소들은 개별 단어 정보)
    extracted_text = texts[0].description if texts else ""


    blacklist = ["말티톨","우유", "복숭아", "말티톨시럽"]
    ingredients = []
    print("extracted_text",extracted_text)
        # 모든 blacklist 단어를 빨간색으로 표시
    highlighted_text = extracted_text  # 원본 텍스트 유지
    for ingredient in blacklist:
        if ingredient in extracted_text:
            highlighted_text = highlighted_text.replace(
                ingredient, f"<span class='text-danger'>{ingredient}</span>"
            )
            ingredients.append(ingredient)  # 감지된 성분 추가

    # 경고 메시지 추가 (검출된 성분이 있을 때만)
    warning_message = None
    if ingredients:
        warning_message = (
            "⚠ 경고: 이 제품에는 혈당을 올리는 성분이 포함되어 있습니다. "
            "과량 섭취 시 설사를 유발할 수 있습니다."
        )

    return {"text": highlighted_text, "warning": warning_message}

# 업로드 페이지 뷰
def upload_page(request):
    return render(request, 'upload.html')

# 이미지 업로드 및 텍스트 추출 뷰
def upload_image(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return render(request, 'upload.html', {'error': '파일을 업로드하지 않았습니다.'})
        
        file = request.FILES['file']
        if not file:
            return render(request, 'upload.html', {'error': '파일은 있지만 선택되지 않았습니다.'})
        
        # 업로드된 이미지 읽기
        image_content = file.read()
        
        # 텍스트 추출 및 경고 메시지 확인
        result = detect_text(image_content)
        
        # 결과 페이지 렌더링
        return render(request, 'result.html', {'text': result["text"], 'warning': result["warning"]})
    
    return render(request, 'upload.html')
