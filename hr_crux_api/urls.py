from django.urls import include, path

urlpatterns = [
    path("auth/", include("hr_crux_api.api_urls.auth.urls")),
    path("asset/", include("hr_crux_api.api_urls.asset.urls")),
    path("base/", include("hr_crux_api.api_urls.base.urls")),
    path("employee/", include("hr_crux_api.api_urls.employee.urls")),
    path("notifications/", include("hr_crux_api.api_urls.notifications.urls")),
    path("payroll/", include("hr_crux_api.api_urls.payroll.urls")),
    path("attendance/", include("hr_crux_api.api_urls.attendance.urls")),
    path("leave/", include("hr_crux_api.api_urls.leave.urls")),
]
