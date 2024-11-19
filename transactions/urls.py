from django.urls import path
from .views import TransactionListCreate, TransactionDetailUpdate

urlpatterns = [
    path('api/transactions/', TransactionListCreate.as_view(), name='transaction-list-create'),
    path('api/transactions/<int:transaction_id>/', TransactionDetailUpdate.as_view(), name='transaction-detail-update'),
]
