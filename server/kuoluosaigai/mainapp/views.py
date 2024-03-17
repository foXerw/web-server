from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache


# Create your views here.
def nothing_view(request):
    # 获取或设置API调用计数
    count_key = 'api_call_count'
    call_count = cache.get(count_key)
    if call_count is None:
        call_count = 1
    else:
        call_count += 1
    cache.set(count_key, call_count, timeout=60*60*24)  # 设置缓存过期时间为一天

    # 返回JSON响应，包含API调用次数
    response_data = {'count': call_count}
    return JsonResponse(response_data)


