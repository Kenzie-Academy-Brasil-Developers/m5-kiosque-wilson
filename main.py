from management import menu_report, add_product, get_product_by_id, get_products_by_type, calculate_tab
from menu import products

if __name__ == "__main__":
    # Seus prints de teste aqui
    menu_report()
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "description": "Sanduiche de Python",
        "type": "fast-food",
        "rating": 5
    }
    new_list = []
    add_product([], **new_product)
    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    calculate_tab(table_1)
    
    ...
