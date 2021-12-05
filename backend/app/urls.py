from garpixcms.urls import *  # noqa
import debug_toolbar
from django.urls import include, path


urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns  # noqa
