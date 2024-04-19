from openslides_backend.datastore.shared.postgresql_backend.create_schema import (
    create_schema,
)
from openslides_backend.datastore.writer.services import register_services


def main() -> None:
    register_services()
    create_schema()


if __name__ == "__main__":
    main()
