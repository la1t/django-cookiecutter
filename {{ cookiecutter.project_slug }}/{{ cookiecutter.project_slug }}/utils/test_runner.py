from django.conf import settings
from django.test.runner import DiscoverRunner
from celery import current_app


def _set_eager():
    settings.CELERY_TASK_ALWAYS_EAGER = True
    current_app.conf.CELERY_TASK_ALWAYS_EAGER = True
    settings.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
    current_app.conf.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True


class CeleryTestSuiteRunner(DiscoverRunner):

    def setup_test_environment(self, **kwargs):
        _set_eager()
        super().setup_test_environment(**kwargs)
