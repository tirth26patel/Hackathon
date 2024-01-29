
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name='home'),
    path("home",views.index,name='home'),
    path("login",views.login_in,name='login'),
    path("log-out",views.log_out,name='log-out'),
    path("register",views.registration,name='registration'),
    path("index1",views.index1,name='index1'),
    path("profile",views.profile,name='profile'),
    path("profile1",views.profile1,name='profile1'),
    path("admin_page",views.admin_page,name='admin_page'),
    path("admin_details/<str:details>/",views.admin_details,name='admin_details'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("forget",views.forget,name='forget'),

#About-scheme
    path("scheme-page",views.scheme_page,name='scheme-page'),
    path("scheme01",views.scheme01,name='scheme01'),
    path("scheme02",views.scheme02,name='scheme02'),
    path("scheme03",views.scheme03,name='scheme03'),
    path("scheme04",views.scheme04,name='scheme04'),
    path("scheme05",views.scheme05,name='scheme05'),
    path("scheme06",views.scheme06,name='scheme06'),
    path("scheme07",views.scheme07,name='scheme07'),
#About-scheme-end


#schemes-apply
    path("adiwasi",views.adiwasi,name='adiwasi'),
    path("ashram",views.ashram,name='ashram'),
    path("eklavya",views.eklavya,name='eklavya'),
    path("tribal_d",views.tribal_d,name='tribal_d'),
    path("tribal_y",views.tribal_y,name='tribal_y'),
    path("van",views.van,name='van'),
    path("vanbandhu",views.vanbandhu,name='vanbandhu'),
#schemes-apply_end


#About-scholarship
    path("scholarship-page",views.scholarship_page,name='scholarship-page'),
    path("scholarship1",views.scholarship1,name='scholarship1'),
    path("scholarship2",views.scholarship2,name='scholarship2'),
    path("scholarship3",views.scholarship3,name='scholarship3'),
    path("scholarship4",views.scholarship4,name='scholarship4'),
    path("scholarship5",views.scholarship5,name='scholarship5'),
#About-scholarship-end


#scholarship-apply
    path("gujarat",views.gujarat,name='scholarship'),
    path("mukhyamantri",views.mukhyamantri,name='scholarship'),
    path("national",views.national_over,name='scholarship'),
    path("pe-matric",views.pe_matric,name='scholarship'),
    path("post-matric",views.post_matric,name='scholarship'),
#scholarship-apply_end
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
