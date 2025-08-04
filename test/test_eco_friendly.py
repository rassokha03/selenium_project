def test_all_el(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.accept_cookie()
    eco_friendly.check_number_of_products_on_a_page()


def test_open_card_product(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.accept_cookie()
    eco_friendly.scroll_400_px()
    eco_friendly.check_open_card_product()


def test_sorted_by_price(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.accept_cookie()
    eco_friendly.check_sort_by_price()
