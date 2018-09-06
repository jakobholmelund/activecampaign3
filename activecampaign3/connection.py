from activecampaign3.resource import Resource

class Connection(Resource):
    _resource_path = 'connections'
    _valid_save_params = "service externalid name logoUrl linkUrl".split()

    def _save_params(self):
        return super()._save_params()
