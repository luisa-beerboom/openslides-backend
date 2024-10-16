from typing import Any, Dict

import fastjsonschema

from openslides_backend.shared.schema import id_list_schema

from ..shared.mixins.user_scope_mixin import UserScopeMixin
from ..shared.schema import schema_version
from .base import BasePresenter
from .presenter import register_presenter

get_user_scope_schema = fastjsonschema.compile(
    {
        "$schema": schema_version,
        "type": "object",
        "title": "get_user_related_models",
        "description": "get user ids related models",
        "properties": {
            "user_ids": id_list_schema,
        },
        "required": ["user_ids"],
        "additionalProperties": False,
    }
)


@register_presenter("get_user_scope")
class GetUserScope(UserScopeMixin, BasePresenter):
    """
    Gets for the user_ids the user scope.
    """

    schema = get_user_scope_schema

    def get_result(self) -> Any:
        result: Dict[str, Any] = {}
        user_ids = self.data["user_ids"]
        for user_id in user_ids:
            scope, scope_id, user_oml = self.get_user_scope(user_id)
            result[str(user_id)] = {
                "collection": scope,
                "id": scope_id,
                "user_oml": user_oml,
            }
        return result
