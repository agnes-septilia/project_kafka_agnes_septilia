from random import SystemRandom

def open_home():
    return {
        "page_type": "home",
        "page_url": "http://www.ecommerce.com"
    }

def open_product():
    product_id = SystemRandom().randint(0, 300)
    return {
        "page_type": "product",
        "page_url": f"http://www.ecommerce.com/products/{product_id}",

    }

def open_checkout():
    return {
        "page_type": "checkout",
        "page_url": f"http://www.ecommerce.com/checkout"
    }

def open_payment():
    return {
        "page_type": "checkout",
        "page_url": f"http://www.ecommerce.com/payment"
    }