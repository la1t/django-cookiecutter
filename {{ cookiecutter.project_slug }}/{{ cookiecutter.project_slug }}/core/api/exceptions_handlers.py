from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import set_rollback


def render_exception_detail(exc_detail):
    if isinstance(exc_detail, list):
        return [render_exception_detail(detail) for detail in exc_detail]
    elif isinstance(exc_detail, dict):
        return {key: render_exception_detail(exc_detail[key]) for key in exc_detail}

    assert isinstance(exc_detail, exceptions.ErrorDetail)
    return {
        "code": exc_detail.code,
        "detail": exc_detail,
    }


def exception_handler(exc, context):
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, "auth_header", None):
            headers["WWW-Authenticate"] = exc.auth_header
        if getattr(exc, "wait", None):
            headers["Retry-After"] = "%d" % exc.wait

        data = render_exception_detail(exc.detail)

        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)

    return None
