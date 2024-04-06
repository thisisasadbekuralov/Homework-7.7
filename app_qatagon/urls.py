from django.urls import path


from .views import AffectedIndividualAPIView, AffectedIndividualDetailView, AffectedIndividualsCreateView, \
    AffectedIndividualsUpdateView, AffectedIndividualsDeleteView

urlpatterns = [
    path('', AffectedIndividualAPIView().as_view()),
    path('<int:pk>/', AffectedIndividualDetailView().as_view()),
    path('create/', AffectedIndividualsCreateView.as_view()),
    path('update/<int:pk>/', AffectedIndividualsUpdateView.as_view()),
    path('delete/<int:pk>/', AffectedIndividualsDeleteView.as_view()),

]