from garpixcms.urls import *  # noqa
import debug_toolbar

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns  # noqa
