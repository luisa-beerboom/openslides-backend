from .test_account_import import (
    AccountJsonImport,
    AccountJsonImportWithIncludedJsonUpload,
)
from .test_account_json_upload import AccountJsonUpload
from .test_participant_import import (
    ParticipantImport,
    ParticipantJsonImportWithIncludedJsonUpload,
)
from .test_participant_json_upload import ParticipantJsonUpload

# TODO: DELETE this file!

class ImportTestAccountJsonUpload(AccountJsonUpload):
    pass


class ImportTestAccountJsonImport(AccountJsonImport):
    pass


class ImportTestAccountJsonImportWithIncludedJsonUpload(
    AccountJsonImportWithIncludedJsonUpload
):
    pass


class ImportTestParticipantJsonUpload(ParticipantJsonUpload):
    pass


class ImportTestParticipantJsonImport(ParticipantImport):
    pass


class ImportTestParticipantJsonImportWithIncludedJsonUpload(
    ParticipantJsonImportWithIncludedJsonUpload
):
    pass
