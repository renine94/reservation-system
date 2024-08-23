from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    """
    전역 에러 핸들러 필요하면 사용
    """
    pass
    # # 기본 exception handler를 호출하여 응답을 가져옵니다
    # response = exception_handler(exc, context)
    #
    # # 만약 예외가 처리되지 않았다면 기본 500 에러를 반환합니다
    # if response is None:
    #     return Response({
    #         "error": "An unexpected error occurred."
    #     }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    #
    # # 응답에 추가 정보를 포함시킵니다
    # if response is not None:
    #     response.data['status_code'] = response.status_code
    #
    #     if 'detail' in response.data:
    #         response.data['message'] = response.data['detail']
    #         del response.data['detail']
    #     else:
    #         response.data['message'] = "An error occurred."
    #
    # return response
