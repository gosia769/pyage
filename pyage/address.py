from pyage.inject import Inject

class AddressProvider(object):
    def __init__(self):
        super(AddressProvider, self).__init__()

    def generate_address(self, obj):
        return str(hash(obj))


class Addressable(object):
    @Inject("address_provider")
    def __init__(self):
        super(Addressable, self).__init__()
        self.address = self.address_provider.generate_address(self)