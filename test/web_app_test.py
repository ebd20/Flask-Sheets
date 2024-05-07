
from app.models.product import Product

# tests for each page (update the tests if you change the page contents):


def test_home_page(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"<h1>Cubes and Magic: The Gathering</h1>" in response.data


def test_about_page(test_client):
    response = test_client.get("/about")
    assert response.status_code == 200
    assert b"<h1>Magic the Gathering - Cube P1P1</h1>" in response.data


def test_products_page(test_client):
    # setup (seed database with some products):
    #Product.destroy_all()
    #Product.seed()

    #products = Product.all()
    #assert len(products) == 3

    # given certain products in the database,
    # we expect to see corresponding information on the page:
    response = test_client.get("/products")
    assert response.status_code == 200
    assert b"<h1>Make your Pack 1 Pick 1 Selection</h1>" in response.data
    #I've removed the text from these cards now it's only an image that is also the button
    #assert b"Textbook" in response.data
    #assert b"Cup of Tea" in response.data
    #assert b"Strawberries" in response.data

    # clean up (clear products sheet):
    Product.destroy_all()
