from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field, validator

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .sql import SQL


class Procedure(SQL):
    """Description"""

    type_name: str = Field("Procedure", allow_mutation=False)

    @validator("type_name")
    def validate_type_name(cls, v):
        if v != "Procedure":
            raise ValueError("must be Procedure")
        return v

    def __setattr__(self, name, value):
        if name in Procedure._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # DEFINITION: ClassVar[KeywordField] = KeywordField("definition", "definition")
    # """
    # SQL definition of the procedure.
    # """

    # ATLAN_SCHEMA: ClassVar[RelationField] = RelationField("atlanSchema")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "definition",
        "atlan_schema",
    ]

    @property
    def definition(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.definition

    @definition.setter
    def definition(self, definition: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.definition = definition

    @property
    def atlan_schema(self) -> Optional[Schema]:
        return None if self.attributes is None else self.attributes.atlan_schema

    @atlan_schema.setter
    def atlan_schema(self, atlan_schema: Optional[Schema]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.atlan_schema = atlan_schema

    class Attributes(SQL.Attributes):
        definition: Optional[str] = Field(None, description="", alias="definition")
        atlan_schema: Optional[Schema] = Field(
            None, description="", alias="atlanSchema"
        )  # relationship

    attributes: "Procedure.Attributes" = Field(
        default_factory=lambda: Procedure.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .schema import Schema  # noqa: E402
