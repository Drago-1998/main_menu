from django import template
from django.core.cache import cache
from django.template.loader import render_to_string

from menu.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name=None):
    if menu_name:
        menu_items = get_menu_items()
        selected_menu = next((item for item in menu_items if item.slug == menu_name), None)
        if not selected_menu:
            return ''
        context = {'selected_menu': selected_menu, 'childes': selected_menu.children_items}
    else:
        menu_list = MenuItem.objects \
            .select_related().prefetch_related('children') \
            .filter(parent__isnull=True)
        context = {'menu_list': menu_list}
    return render_to_string('extra/menu.html', context)


def get_menu_items():
    menu_items = {
        _menu.id: _menu
        for _menu in MenuItem.objects.all()
    }

    def menu_getter(menu_item):
        menu_item.parent_instance = menu_items.get(menu_item.parent_id, None)
        menu_item.children_items = [
            _menu_item
            for _menu_item in menu_items.values()
            if _menu_item.parent_id == menu_item.id
        ]
        return menu_item

    menu_list = [
        menu_getter(menu_item)
        for menu_item in menu_items.values()
    ]
    return menu_list
