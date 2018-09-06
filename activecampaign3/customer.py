from activecampaign3.resource import Resource

class Customer(Resource):
    _resource_path = 'ecomCustomers'
    _valid_save_params = "connectionid externalid email".split()

    def _save_params(self):
        return super()._save_params()
