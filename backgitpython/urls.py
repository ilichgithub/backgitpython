from django.urls import include, path
from rest_framework import routers
from backgitpython.quickstart import views 
from backgitpython.branch import views as branch_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/branch', branch_views.BranchesAPIView.as_view(), name='branch'),
    path('api/v1/branch/<slug:branch>/commits/', branch_views.CommitsBranchAPIView.as_view(), name='branchCommits'),
    path('api/v1/clone', branch_views.CloneRepoAPIView.as_view(), name='clone'),
    path('api/v1/', include('prs.urls')),
]