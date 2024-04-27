from django.db.models import Q

from django_filters import rest_framework as filters
from django_filters import CharFilter

from project_root.product.models import CategoryAttribute, Category

class CategoryAttributeFilter(filters.FilterSet):

    def custom_category_filter(self, parameter_name, category_id):
        # get all categories that are children of the selected category including the id of the selected category
        children_categories = Category.objects.filter(Q(parent=category_id)|Q(id=category_id)).values_list('id', flat=True)
        print(self.filter(category__in=children_categories))
        return self.filter(category__in=children_categories)
    
    category = CharFilter(method=custom_category_filter)
    class Meta:
        model = CategoryAttribute
        fields = ['category']