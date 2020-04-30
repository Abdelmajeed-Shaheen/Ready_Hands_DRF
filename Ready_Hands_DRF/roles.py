from rolepermissions.roles import AbstractUserRole

class Client(AbstractUserRole):
    available_permissions = {
    'is_client': True,
    }

class Worker(AbstractUserRole):
    available_permissions = {
    'is_worker': True,
    }
