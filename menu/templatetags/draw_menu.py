from django import template
from menu.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag("menu/draw_menu.html", takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    items_qs = (
        MenuItem.objects
        .select_related("menu", "parent")
        .filter(menu__name=menu_name)
    )
    items = list(items_qs)



    # items_by_id — быстрый доступ к пунктам меню по их ID.
    # children_map — словарь, где ключ — ID родителя, значение — список его дочерних пунктов.
    # Построение map для удобного обхода дерева.
    items_by_id = {item.id: item for item in items}
    children_map = {}
    for item in items:
        children_map.setdefault(item.parent_id, []).append(item)

    # Найти активный элемент (сравниваем URL)
    active_item = None
    for item in items:
        if item.get_url() == current_path:
            active_item = item
            break

    # Собираем IDs на пути от корня до активного (включая активный).
    # Используем items_by_id и parent_id чтобы не делать дополнительных запросов.
    path_ids = set()
    if active_item:
        node = active_item
        while node:
            path_ids.add(node.id)
            node = items_by_id.get(node.parent_id)  # безопасно: parent берётся из items_by_id, без запроса


    # Рекурсия вниз выполняется ТОЛЬКО для узлов, чей id есть в path_ids.
    # Это: все предки по пути + сам активный — их children будут включены.
    def build_tree(parent_id=None):
        result = []
        for child in children_map.get(parent_id, []):
            node_data = {
                "item": child,
                "is_active": (active_item is not None and child.id == active_item.id),
                "expanded": (child.id in path_ids),  # полезно в шаблоне
                "children": []
            }
            # рекурсивно включаем детей только если этого child находится на пути к активному
            if child.id in path_ids:
                node_data["children"] = build_tree(child.id)
            # если child не в path_ids — children остаются пустыми (свернуты)
            result.append(node_data)
        return result

    menu_tree = build_tree(None)

    return {
        "menu_tree": menu_tree,
        "active_item": active_item,
    }