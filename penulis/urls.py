from django.urls import path,re_path

from .views import (
    createArtikel,
    homePenulis,
    updateArtikel,
    deleteArtikel,
    loginView,
    logoutView,
    managePenulis,
    register,
    managePublishedartikel,
    publishedArtikel,
    spesialistView,
    createSpesialist,
    editSpesialist,
    deleteSpesialist,
    viewDepartement,
    createDepartement,
    editDepartement,
    deleteDepartment,
    createJadwal,
    editJadwal,
    deleteJadwal,
    jadwalManage,
    contactManage,
    lihatPengaduan,
    deletePengaduan,
)

app_name='penulis'
urlpatterns = [
    re_path(r'^delete-pengaduan/(?P<pk>\d+)/$',deletePengaduan,name='delete-pengaduan'),
    re_path(r'^detail-pengaduan/(?P<pk>\d+)/$',lihatPengaduan,name='pengaduan-view'),
    path('manage-pengaduan/',contactManage,name='manage-pengaduan'),
    re_path(r'delete-jadwal/(?P<pk>\d+)/$',deleteJadwal,name='jadwaldokter-delete'),
    re_path(r'^edit-jadwal/(?P<pk>\d+)/$',editJadwal,name='jadwaldokter-edit'),
    path('create-jadwal/',createJadwal,name='jadwaldokter-add'),
    path('manage-jadwal/',jadwalManage,name='jadwaldokter-manage'),
    re_path(r'^delete-departement/(?P<pk>\d+)/$',deleteDepartment,name='delete-departement'),
    re_path(r'^edit-departement/(?P<pk>\d+)/$',editDepartement,name='edit-departement'),
    path('create-departement/',createDepartement,name='departement-add'),
    path('manage-departement/',viewDepartement,name='manage-departement'),
    re_path(r'^delete-spesialist/(?P<pk>\d+)/$',deleteSpesialist,name='delete-spesialist'),
    re_path(r'^edit-spesialist/(?P<pk>\d+)/$',editSpesialist,name='edit-spesialist'),
    path('create-spesialist',createSpesialist,name='add-spesialist'),
    path('spesialist-manage/',spesialistView,name='manage-spesialist'),
    re_path(r'^published-artikel/(?P<pk>\d+)/$',publishedArtikel,name='published_artikel'),
    re_path(r'^delete-artikel(?P<pk>\d+)/$',deleteArtikel,name='artikel-delete'),
    re_path(r'^update-artikel/(?P<pk>\d+)/$',updateArtikel,name='artikel-update'),
    path('manage-artikel-unpublish',managePublishedartikel,name='artikel-unpublished'),
    path('register-penulis/',register,name='register-penulis'),
    path('manage-penulis',managePenulis,name='manage-penulis'),
    path('logout-penulis/',logoutView,name='logout'),
    path('login-penulis/',loginView,name='login'),
    path('create-artikel/',createArtikel,name='artikel-create'),
    path('',homePenulis,name='home-penulis'),
]
