from django.shortcuts import render
from .models import Zero_Product
# Create your views here.
def Zero_classification(request):
    product_info = None
    warning = None

    if request.method == 'POST':
        product_na = request.POST.get('product_name') # 사용자가 입력한 제품
        print(product_na)
        try:
            product_info = Zero_Product.objects.get(product_name=product_na)
         # product name = DB에 있는 제품명
         # Zero_Product.objects.get()
         # 데이터베이스에서 product_name이 사용자가 입력한 값과 일치하는 제품을 찾아 반환  
         # 말티톨 또는 말티톨 시럽이 포함되어 있는지 확인
            if product_info.maltitol > 0 or product_info.maltitol_syrup > 0:
                warning = "⚠️ 경고: 이 제품에는 말티톨이 포함되어 있습니다! 당뇨환자는 말티톨 섭취 시 혈당이 상승할 수 있으므로 주의가 필요합니다."
        except Zero_Product.DoesNotExist:
            product_info = None # 디비에 같은 제품이 없으면
                                # product_info = Zero_Product.objects.get(product_name=product_na)
            warning = f"'{product_name}' 제품을 데이터베이스에서 찾을 수 없습니다."

    return render(request, 'index.html', {
        'product_info': product_info,
        'warning': warning,
    })