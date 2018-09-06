from activecampaign3.connection import Connection
from activecampaign3.contact import Contact
from activecampaign3.customer import Customer
from activecampaign3.order import Order, Product


def test_clean_old_connections():
    connections = Connection.search()
    for connection in connections:
        connection.delete()


def test_clean_old_customers():
    customers = Customer.search()
    for customer in customers:
        customer.delete()


def test_clean_old_orders():
    orders = Order.search()
    for order in orders:
        order.delete()


def test_create_connection():
    connection = Connection(
        service="SOAT",
        externalid=1,
        name="SOATTEST",
        logoUrl="https://www.example.com/static/images/bb7907e90.jpg",
        linkUrl="https://www.example.com"
    )
    connection.save()
    return connection.resource_id


def test_list_connections():
    connections = Connection.search()
    assert connections.total == 1


def test_create_customer(connectionid):


    customer = Customer(
        connectionid=connectionid,
        externalid=1,
        email="jakob@example.com"
    )
    customer.save()
    return customer.resource_id


def test_list_customers():
    customers = Customer.search()
    assert customers.total == 1


def test_create_order():
    connectionid = test_create_connection()
    customerid = test_create_customer(connectionid)

    products = []

    products.append(Product(
        externalid=4,
        name="Pogo Stick",
        price=5000,
        quantity=1,
        category="Stuff"
    ))

    products.append(Product(
        externalid=5,
        name="Banana",
        price=5000,
        quantity=2,
        category="Stuff"
    ))

    order = Order(
        externalid=1,
        source=0,
        email="jakob@example.com",
        orderProducts=products,
        orderUrl="https://www.example.com/accounts/profile/order/1",
        orderDate="2016-09-13T17:41:39-04:00",
        shippingMethod="UPS Ground",
        totalPrice=100000,
        currency="USD",
        connectionid=connectionid,
        customerid=customerid
    )
    order.save()


def test_list_orders():
    orders = Order.search()
    assert orders.total == 1
