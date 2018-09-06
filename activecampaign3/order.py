from activecampaign3.resource import Resource


class Product(Resource):
    _resource_path = 'ecomOrderProducts'
    _valid_search_params = []
    _valid_save_params = "externalid name price quantity category".split()


class Order(Resource):
    _resource_path = 'ecomOrders'
    _valid_search_params = []
    _valid_save_params = "externalid source email orderProducts orderUrl orderDate shippingMethod totalPrice currency connectionid customerid".split()

    def _save_params(self):
        if hasattr(self, 'orderProducts'):
            self.orderProducts = [product._save_params() for product in self.orderProducts]
        return super()._save_params()
