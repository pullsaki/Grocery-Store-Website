from django.contrib import admin
from .models import Category,Product,CartOrder,CartOrderItems,ProductReview,UserAddressBook

class CategoryAdmin(admin.ModelAdmin):
	list_display=('title',)
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','price','category', 'status','is_featured')
    list_editable=('status','is_featured')
admin.site.register(Product,ProductAdmin)

# Order
class CartOrderAdmin(admin.ModelAdmin):
	list_editable=('paid_status','order_status')
	list_display=('user','total_amt','paid_status','order_dt','order_status')
admin.site.register(CartOrder,CartOrderAdmin)

class CartOrderItemsAdmin(admin.ModelAdmin):
	list_display=('invoice_no','item','qty','price','total')
admin.site.register(CartOrderItems,CartOrderItemsAdmin)


class ProductReviewAdmin(admin.ModelAdmin):
	list_display=('user','product','review_text','get_review_rating')
admin.site.register(ProductReview,ProductReviewAdmin)


class UserAddressBookAdmin(admin.ModelAdmin):
	list_display=('user','address','status')
admin.site.register(UserAddressBook,UserAddressBookAdmin)