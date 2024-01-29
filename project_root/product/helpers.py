def category_restructure_in_parent_child_format(parent_categories, queryset):
    for c in parent_categories:
        children = queryset.filter(parent=c.id)
        if children:
            c.children = children
            category_restructure_in_parent_child_format(children, queryset)
        else:
            c.children = None
    return parent_categories