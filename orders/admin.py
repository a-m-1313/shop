
from django.contrib import admin
from .models import Order, OrderItem
from jalali_date import datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    field = ('order', 'product', 'quantity', 'price', )
    extra = 0


@admin.register(Order)
class PageAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    model = Order
    list_display = ('user',  'first_name', 'last_name', 'get_created_jalali', 'is_paid')
    inlines = [OrderItemInline]

    @admin.display(description='تاریخ ایجاد', ordering='created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.date_created).strftime('%d / %m / %Y  | %H:%M:%S')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ('order', 'product', 'quantity', 'price',)


