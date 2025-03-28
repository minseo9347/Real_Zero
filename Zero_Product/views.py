from django.shortcuts import render
from .models import Zero_Product

def Zero_classification(request):
    product_info = None
    warning = None

    if request.method == 'POST':
        product_na = request.POST.get('product_name')  # 사용자가 입력한 제품명
        print(product_na)
        
        try:
            # 데이터베이스에서 제품명으로 제품 조회
            product_info = Zero_Product.objects.get(product_name=product_na)
            # product name = DB에 있는 제품명
             # Zero_Product.objects.get()
            # 데이터베이스에서 product_name이 사용자가 입력한 값과 일치하는 제품을 찾아 반환  
            
            # 원재료(ingredients)에 "말티톨" 또는 "maltitol"이 포함되어 있는지 확인
            Raw_materials = product_info.Raw_materials.lower()  # 대소문자 구분 없이 검색하기 위해 소문자로 변환
            if "말티톨" in Raw_materials or "maltitol" in Raw_materials:
                warning = "⚠️ 경고: 이 제품에는 말티톨이 포함되어 있습니다! 당뇨환자는 말티톨 섭취 시 혈당이 상승할 수 있으므로 주의가 필요합니다."
        
        except Zero_Product.DoesNotExist:
            product_info = None  # 데이터베이스에 제품이 없으면
            warning = f"'{product_na}' 제품을 데이터베이스에서 찾을 수 없습니다."

    return render(request, 'index.html', {
        'product_info': product_info,
        'warning': warning,
    })