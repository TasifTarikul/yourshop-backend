from collections import Counter

def category_restructure_in_parent_child_format(parent_categories, queryset):
    for c in parent_categories:
        children = queryset.filter(parent=c.id)
        if children:
            c.children = children
            category_restructure_in_parent_child_format(children, queryset)
        else:
            c.children = None
    return parent_categories

def find_duplicate_strings(lst):
    lowercase_strings = [s.lower() for s in lst]
    # Use Counter to count occurrences of each string
    string_counts = Counter(lowercase_strings)
    # Find strings with counts greater than 1 (indicating duplicates)
    duplicates = [string for string, count in string_counts.items() if count > 1]
    return duplicates