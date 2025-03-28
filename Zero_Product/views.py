from django.shortcuts import render
from .models import Zero_Product

# Create your views here.
def Zero_classification(request):
    product_info = None
    warning = None

    if request.method == 'POST':
        product_na = request.POST.get('product_name')  # 사용자가 입력한 제품
        print(product_na)
        
        try:
            product_info = Zero_Product.objects.get(product_name=product_na)
            # product name = DB에 있는 제품명
            # Zero_Product.objects.get()으로 데이터베이스에서 product_name이 사용자가 입력한 값과 일치하는 제품을 찾아 반환  
                     # product name = DB에 있는 제품명
         # Zero_Product.objects.get()
         # 데이터베이스에서 product_name이 사용자가 입력한 값과 일치하는 제품을 찾아 반환  
         # 말티톨 또는 말티톨 시럽이 포함되어 있는지 확인
            
            # maltitol과 maltitol_syrup 값 처리
            maltitol_value = product_info.maltitol if product_info.maltitol else 0
            maltitol_syrup_value = product_info.maltitol_syrup if product_info.maltitol_syrup else 0
            
            # 빈 값 또는 변환 불가능한 값은 0으로 처리
            try:
                maltitol_value = float(maltitol_value) if maltitol_value != '' else 0
            except ValueError:
                maltitol_value = 0
            
            try:
                maltitol_syrup_value = float(maltitol_syrup_value) if maltitol_syrup_value != '' else 0
            except ValueError:
                maltitol_syrup_value = 0

            # 말티톨 또는 말티톨 시럽 값이 0보다 큰지 확인
            if maltitol_value > 0 or maltitol_syrup_value > 0:
                warning = "⚠️ 경고: 이 제품에는 말티톨이 포함되어 있습니다! 당뇨환자는 말티톨 섭취 시 혈당이 상승할 수 있으므로 주의가 필요합니다."
        
        except Zero_Product.DoesNotExist:
            product_info = None  # 디비에 같은 제품이 없으면
            warning = f"'{product_na}' 제품을 데이터베이스에서 찾을 수 없습니다."
             # 디비에 같은 제품이 없으면
                                # product_info = Zero_Product.objects.get(product_name=product_na)

    return render(request, 'index.html', {
        'product_info': product_info,
        'warning': warning,
    })
