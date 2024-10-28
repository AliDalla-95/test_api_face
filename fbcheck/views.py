from django.shortcuts import render
from django.http import JsonResponse
import facebook

def check_user_membership(request):
    page_id = 'your_page_id'  # استبدل 'your_page_id' بمعرف الصفحة (مثلًا banias)
    user_name = 'Ali Dalla'   # اسم المستخدم الذي تبحث عنه
    access_token = 'your_access_token'  # ضع توكن الوصول هنا

    try:
        # إنشاء كائن Facebook Graph API باستخدام التوكن
        graph = facebook.GraphAPI(access_token=access_token)

        # الحصول على قائمة المستخدمين الذين تفاعلوا مع الصفحة
        members = graph.get_connections(id=page_id, connection_name='likes')

        # البحث عن المستخدم في قائمة الأعضاء باستخدام الاسم
        is_member = any(member['name'] == user_name for member in members['data'])

        # إرجاع النتيجة كـ JSON
        return JsonResponse({"is_member": is_member})
    
    except facebook.GraphAPIError as e:
        # في حالة حدوث خطأ، إرجاعه كـ JSON
        return JsonResponse({"error": str(e)})
