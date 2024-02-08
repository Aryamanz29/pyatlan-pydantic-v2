from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .asset import Asset


class AtlasGlossaryTerm(Asset):
    """Description"""

    def _set_qualified_name_fallback(cls, values):
        if (
            "attributes" in values
            and values["attributes"]
            and not values["attributes"].qualified_name
        ):
            values["attributes"].qualified_name = values["guid"]
        return values

    def trim_to_required(self) -> AtlasGlossaryTerm:
        if self.anchor is None or not self.anchor.guid:
            raise ValueError("anchor.guid must be available")
        return self.create_for_modification(
            qualified_name=self.qualified_name or "",
            name=self.name or "",
            glossary_guid=self.anchor.guid,
        )

    # ANCHOR: ClassVar[KeywordField] = KeywordField("anchor", "__glossary")
    # """Glossary in which the term is contained, searchable by the qualifiedName of the glossary."""
    # CATEGORIES: ClassVar[KeywordField] = KeywordField("categories", "__categories")
    # """Categories in which the term is organized, searchable by the qualifiedName of the category."""

    type_name: str = Field("AtlasGlossaryTerm", allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "AtlasGlossaryTerm":
            raise ValueError("must be AtlasGlossaryTerm")
        return v

    def __setattr__(self, name, value):
        if name in AtlasGlossaryTerm._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # SHORT_DESCRIPTION: ClassVar[KeywordField] = KeywordField(
    #     "shortDescription", "shortDescription"
    # )
    # """
    # TBC
    # """
    # LONG_DESCRIPTION: ClassVar[KeywordField] = KeywordField(
    #     "longDescription", "longDescription"
    # )
    # """
    # TBC
    # """
    # EXAMPLES: ClassVar[KeywordField] = KeywordField("examples", "examples")
    # """
    # TBC
    # """
    # ABBREVIATION: ClassVar[KeywordField] = KeywordField("abbreviation", "abbreviation")
    # """
    # TBC
    # """
    # USAGE: ClassVar[KeywordField] = KeywordField("usage", "usage")
    # """
    # TBC
    # """
    # ADDITIONAL_ATTRIBUTES: ClassVar[KeywordField] = KeywordField(
    #     "additionalAttributes", "additionalAttributes"
    # )
    # """
    # TBC
    # """
    # TERM_TYPE: ClassVar[KeywordField] = KeywordField("termType", "termType")
    # """
    # TBC
    # """
    # VALID_VALUES_FOR: ClassVar[RelationField] = RelationField("validValuesFor")
    # """
    # TBC
    # """
    # VALID_VALUES: ClassVar[RelationField] = RelationField("validValues")
    # """
    # TBC
    # """
    # SEE_ALSO: ClassVar[RelationField] = RelationField("seeAlso")
    # """
    # TBC
    # """
    # IS_A: ClassVar[RelationField] = RelationField("isA")
    # """
    # TBC
    # """
    # ANTONYMS: ClassVar[RelationField] = RelationField("antonyms")
    # """
    # TBC
    # """
    # ASSIGNED_ENTITIES: ClassVar[RelationField] = RelationField("assignedEntities")
    # """
    # TBC
    # """
    # CLASSIFIES: ClassVar[RelationField] = RelationField("classifies")
    # """
    # TBC
    # """
    # PREFERRED_TO_TERMS: ClassVar[RelationField] = RelationField("preferredToTerms")
    # """
    # TBC
    # """
    # PREFERRED_TERMS: ClassVar[RelationField] = RelationField("preferredTerms")
    # """
    # TBC
    # """
    # TRANSLATION_TERMS: ClassVar[RelationField] = RelationField("translationTerms")
    # """
    # TBC
    # """
    # SYNONYMS: ClassVar[RelationField] = RelationField("synonyms")
    # """
    # TBC
    # """
    # REPLACED_BY: ClassVar[RelationField] = RelationField("replacedBy")
    # """
    # TBC
    # """
    # REPLACEMENT_TERMS: ClassVar[RelationField] = RelationField("replacementTerms")
    # """
    # TBC
    # """
    # TRANSLATED_TERMS: ClassVar[RelationField] = RelationField("translatedTerms")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "short_description",
        "long_description",
        "examples",
        "abbreviation",
        "usage",
        "additional_attributes",
        "term_type",
        "valid_values_for",
        "valid_values",
        "see_also",
        "is_a",
        "antonyms",
        "assigned_entities",
        "classifies",
        "categories",
        "preferred_to_terms",
        "preferred_terms",
        "translation_terms",
        "synonyms",
        "replaced_by",
        "replacement_terms",
        "translated_terms",
        "anchor",
    ]

    @property
    def short_description(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.short_description

    @short_description.setter
    def short_description(self, short_description: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.short_description = short_description

    @property
    def long_description(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.long_description

    @long_description.setter
    def long_description(self, long_description: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.long_description = long_description

    @property
    def examples(self) -> Optional[set[str]]:
        return None if self.attributes is None else self.attributes.examples

    @examples.setter
    def examples(self, examples: Optional[set[str]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.examples = examples

    @property
    def abbreviation(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.abbreviation = abbreviation

    @property
    def usage(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.usage

    @usage.setter
    def usage(self, usage: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.usage = usage

    @property
    def additional_attributes(self) -> Optional[dict[str, str]]:
        return (
            None if self.attributes is None else self.attributes.additional_attributes
        )

    @additional_attributes.setter
    def additional_attributes(self, additional_attributes: Optional[dict[str, str]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.additional_attributes = additional_attributes

    @property
    def valid_values_for(self) -> Optional[list[AtlasGlossaryTerm]]:
        return None if self.attributes is None else self.attributes.valid_values_for

    @valid_values_for.setter
    def valid_values_for(self, valid_values_for: Optional[list[AtlasGlossaryTerm]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.valid_values_for = valid_values_for

    @property
    def valid_values(self) -> Optional[list[AtlasGlossaryTerm]]:
        return None if self.attributes is None else self.attributes.valid_values

    @valid_values.setter
    def valid_values(self, valid_values: Optional[list[AtlasGlossaryTerm]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.valid_values = valid_values

    @property
    def see_also(self) -> Optional[list[AtlasGlossaryTerm]]:
        return None if self.attributes is None else self.attributes.see_also

    @see_also.setter
    def see_also(self, see_also: Optional[list[AtlasGlossaryTerm]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.see_also = see_also

    @property
    def is_a(self) -> Optional[list[AtlasGlossaryTerm]]:
        return None if self.attributes is None else self.attributes.is_a

    @is_a.setter
    def is_a(self, is_a: Optional[list[AtlasGlossaryTerm]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_a = is_a

    @property
    def antonyms(self) -> Optional[list[AtlasGlossaryTerm]]:
        return None if self.attributes is None else self.attributes.antonyms

    @antonyms.setter
    def antonyms(self, antonyms: Optional[list[AtlasGlossaryTerm]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.antonyms = antonyms

    @property
    def assigned_entities(self) -> Optional[list[Referenceable]]:
        return None if self.attributes is None else self.attributes.assigned_entities

    @assigned_entities.setter
    def assigned_entities(self, assigned_entities: Optional[list[Referenceable]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.assigned_entities = assigned_entities

    @property
    def classifies(self) -> Optional[list[AtlasGlossaryTerm]]:
        return None if self.attributes is None else self.attributes.classifies

    @classifies.setter
    def classifies(self, classifies: Optional[list[AtlasGlossaryTerm]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.classifies = classifies

    @property
    def categories(self) -> Optional[list[AtlasGlossaryCategory]]:
        return None if self.attributes is None else self.attributes.categories

    @categories.setter
    def categories(self, categories: Optional[list[AtlasGlossaryCategory]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.categories = categories

    @property
    def preferred_to_terms(self) -> Optional[list[AtlasGlossaryTerm]]:
        return None if self.attributes is None else self.attributes.preferred_to_terms

    @preferred_to_terms.setter
    def preferred_to_terms(self, preferred_to_terms: Optional[list[AtlasGlossaryTerm]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.preferred_to_terms = preferred_to_terms

    @property
    def preferred_terms(self) -> Optional[list[AtlasGlossaryTerm]]:
        return None if self.attributes is None else self.attributes.preferred_terms

    @preferred_terms.setter
    def preferred_terms(self, preferred_terms: Optional[list[AtlasGlossaryTerm]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.preferred_terms = preferred_terms

    @property
    def translation_terms(self) -> Optional[list[AtlasGlossaryTerm]]:
        return None if self.attributes is None else self.attributes.translation_terms

    @translation_terms.setter
    def translation_terms(self, translation_terms: Optional[list[AtlasGlossaryTerm]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.translation_terms = translation_terms

    @property
    def synonyms(self) -> Optional[list[AtlasGlossaryTerm]]:
        return None if self.attributes is None else self.attributes.synonyms

    @synonyms.setter
    def synonyms(self, synonyms: Optional[list[AtlasGlossaryTerm]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.synonyms = synonyms

    @property
    def replaced_by(self) -> Optional[list[AtlasGlossaryTerm]]:
        return None if self.attributes is None else self.attributes.replaced_by

    @replaced_by.setter
    def replaced_by(self, replaced_by: Optional[list[AtlasGlossaryTerm]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.replaced_by = replaced_by

    @property
    def replacement_terms(self) -> Optional[list[AtlasGlossaryTerm]]:
        return None if self.attributes is None else self.attributes.replacement_terms

    @replacement_terms.setter
    def replacement_terms(self, replacement_terms: Optional[list[AtlasGlossaryTerm]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.replacement_terms = replacement_terms

    @property
    def translated_terms(self) -> Optional[list[AtlasGlossaryTerm]]:
        return None if self.attributes is None else self.attributes.translated_terms

    @translated_terms.setter
    def translated_terms(self, translated_terms: Optional[list[AtlasGlossaryTerm]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.translated_terms = translated_terms

    @property
    def anchor(self) -> Optional[AtlasGlossary]:
        return None if self.attributes is None else self.attributes.anchor

    @anchor.setter
    def anchor(self, anchor: Optional[AtlasGlossary]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.anchor = anchor

    class Attributes(Asset.Attributes):
        short_description: Optional[str] = Field(
            None, description="", alias="shortDescription"
        )
        long_description: Optional[str] = Field(
            None, description="", alias="longDescription"
        )
        examples: Optional[set[str]] = Field(None, description="", alias="examples")
        abbreviation: Optional[str] = Field(None, description="", alias="abbreviation")
        usage: Optional[str] = Field(None, description="", alias="usage")
        additional_attributes: Optional[dict[str, str]] = Field(
            None, description="", alias="additionalAttributes"
        )
        valid_values_for: Optional[list[AtlasGlossaryTerm]] = Field(
            None, description="", alias="validValuesFor"
        )  # relationship
        valid_values: Optional[list[AtlasGlossaryTerm]] = Field(
            None, description="", alias="validValues"
        )  # relationship
        see_also: Optional[list[AtlasGlossaryTerm]] = Field(
            None, description="", alias="seeAlso"
        )  # relationship
        is_a: Optional[list[AtlasGlossaryTerm]] = Field(
            None, description="", alias="isA"
        )  # relationship
        antonyms: Optional[list[AtlasGlossaryTerm]] = Field(
            None, description="", alias="antonyms"
        )  # relationship
        assigned_entities: Optional[list[Referenceable]] = Field(
            None, description="", alias="assignedEntities"
        )  # relationship
        classifies: Optional[list[AtlasGlossaryTerm]] = Field(
            None, description="", alias="classifies"
        )  # relationship
        categories: Optional[list[AtlasGlossaryCategory]] = Field(
            None, description="", alias="categories"
        )  # relationship
        preferred_to_terms: Optional[list[AtlasGlossaryTerm]] = Field(
            None, description="", alias="preferredToTerms"
        )  # relationship
        preferred_terms: Optional[list[AtlasGlossaryTerm]] = Field(
            None, description="", alias="preferredTerms"
        )  # relationship
        translation_terms: Optional[list[AtlasGlossaryTerm]] = Field(
            None, description="", alias="translationTerms"
        )  # relationship
        synonyms: Optional[list[AtlasGlossaryTerm]] = Field(
            None, description="", alias="synonyms"
        )  # relationship
        replaced_by: Optional[list[AtlasGlossaryTerm]] = Field(
            None, description="", alias="replacedBy"
        )  # relationship
        replacement_terms: Optional[list[AtlasGlossaryTerm]] = Field(
            None, description="", alias="replacementTerms"
        )  # relationship
        translated_terms: Optional[list[AtlasGlossaryTerm]] = Field(
            None, description="", alias="translatedTerms"
        )  # relationship
        anchor: Optional[AtlasGlossary] = Field(
            None, description="", alias="anchor"
        )  # relationship

    attributes: AtlasGlossaryTerm.Attributes = Field(
        default_factory=lambda: AtlasGlossaryTerm.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .referenceable import Referenceable  # noqa: E402
from .atlas_glossary import AtlasGlossary  # noqa: E402
from .atlas_glossary_category import AtlasGlossaryCategory  # noqa: E402
