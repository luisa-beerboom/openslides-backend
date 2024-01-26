from typing import Any, Dict

from ....models.models import Speaker
from ....permissions.permissions import Permissions
from ....shared.patterns import fqid_from_collection_and_id
from ...action import ActionException
from ...generics.delete import DeleteAction
from ...util.default_schema import DefaultSchema
from ...util.register import register_action
from ..structure_level_list_of_speakers.delete import (
    StructureLevelListOfSpeakersDeleteAction,
)


@register_action("speaker.delete")
class SpeakerDeleteAction(DeleteAction):
    model = Speaker()
    schema = DefaultSchema(Speaker()).get_delete_schema()
    permission = Permissions.ListOfSpeakers.CAN_MANAGE
    speaker: Dict[str, Any]

    def check_permissions(self, instance: Dict[str, Any]) -> None:
        self.speaker = self.datastore.get(
            fqid_from_collection_and_id(self.model.collection, instance["id"]),
            ["meeting_user_id", "structure_level_list_of_speakers_id"],
            lock_result=False,
        )
        if self.speaker.get("meeting_user_id"):
            meeting_user = self.datastore.get(
                fqid_from_collection_and_id(
                    "meeting_user", self.speaker["meeting_user_id"]
                ),
                ["user_id"],
            )

            if meeting_user.get("user_id") == self.user_id:
                return
        super().check_permissions(instance)

    def update_instance(self, instance: Dict[str, Any]) -> Dict[str, Any]:
        if self.speaker.get("structure_level_list_of_speakers_id"):
            sllos = self.datastore.get(
                fqid_from_collection_and_id(
                    "structure_level_list_of_speakers",
                    self.speaker["structure_level_list_of_speakers_id"],
                ),
                [
                    "speaker_ids",
                    "remaining_time",
                    "initial_time",
                    "additional_time",
                    "current_start_time",
                ],
                lock_result=False,
            )
            if len(sllos["speaker_ids"]) == 1 and (
                (
                    sllos.get("initial_time", 0) + sllos.get("additional_time", 0)
                    == sllos.get("remaining_time", 0)
                )
                and not sllos.get("current_start_time")
            ):
                if sllos["speaker_ids"][0] != instance["id"]:
                    raise ActionException(
                        "Couldn't delete speaker because of corrupt structure_level speaking time data"
                    )
                self.execute_other_action(
                    StructureLevelListOfSpeakersDeleteAction,
                    [{"id": self.speaker["structure_level_list_of_speakers_id"]}],
                )
        return super().update_instance(instance)
