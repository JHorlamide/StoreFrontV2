from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

# Parent Domain Routes
router.register("products", views.ProductViewSet, basename="products")
router.register("collections", views.CollectionViewSet)
router.register("carts", views.CartViewSet, basename="cart")
router.register("customers", views.CustomerViewSet)
router.register("orders", views.OrderViewSet, basename="orders")

# Product Child Router
products_router = routers.NestedDefaultRouter(router, "products", lookup="product")
products_router.register("reviews", views.ReviewViewSet, basename="product-reviews")

# Cart Child Router
carts_router = routers.NestedDefaultRouter(router, "carts", lookup="cart")
carts_router.register("items", views.CartItemViewSet, basename="cart-items")

# URLConf
urlpatterns = router.urls + products_router.urls + carts_router.urls

# urlpatterns = [
#   path("", include(router.urls)),
#   path("products/", views.ProductList.as_view()),
#   path("products/<int:pk>/", views.ProductDetails.as_view()),
#   path("collections/", views.CollectionList.as_view()),
#   path("collections/<int:pk>", views.CollectionDetails.as_view())
# ] 