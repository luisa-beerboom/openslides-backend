from typing import Any

from openslides_backend.action.generics.create import CreateAction
from openslides_backend.action.mixins.check_unique_name_mixin import (
    CheckUniqueInContextMixin,
)

from ....models.models import Office
from ....permissions.permissions import Permissions
from ...util.default_schema import DefaultSchema
from ...util.register import register_action


@register_action("office.create")
class OfficeCreate(CheckUniqueInContextMixin, CreateAction):
    model = Office()
    schema = DefaultSchema(Office()).get_create_schema(
        required_properties=["meeting_id", "name"],
    )
    permission = Permissions.User.CAN_MANAGE

    def validate_instance(self, instance: dict[str, Any]) -> None:
        super().validate_instance(instance)
        self.check_unique_in_context(
            "name",
            instance["name"],
            "The name of the office must be unique.",
            context_id=instance["meeting_id"],
            context_name="meeting_id",
        )
