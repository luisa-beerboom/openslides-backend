from typing import Any

from openslides_backend.action.generics.update import UpdateAction
from openslides_backend.action.mixins.check_unique_name_mixin import (
    CheckUniqueInContextMixin,
)

from ....models.models import Office
from ....permissions.permissions import Permissions
from ...util.default_schema import DefaultSchema
from ...util.register import register_action


@register_action("office.update")
class OfficeUpdate(CheckUniqueInContextMixin, UpdateAction):
    model = Office()
    schema = DefaultSchema(Office()).get_update_schema(
        required_properties=["name"],
    )
    permission = Permissions.User.CAN_MANAGE

    def validate_instance(self, instance: dict[str, Any]) -> None:
        super().validate_instance(instance)
        self.check_unique_in_context(
            "name",
            instance["name"],
            "The name of the office must be unique.",
            instance["id"],
            "meeting_id",
            self.get_meeting_id(instance),
        )
