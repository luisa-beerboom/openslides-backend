from ....models.models import Office
from ....permissions.permissions import Permissions
from ...generics.delete import DeleteAction
from ...util.default_schema import DefaultSchema
from ...util.register import register_action


@register_action("office.delete")
class OfficeDelete(DeleteAction):
    model = Office()
    schema = DefaultSchema(Office()).get_delete_schema()
    permission = Permissions.User.CAN_MANAGE
