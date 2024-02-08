from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field, validator

# from pyatlan.model.fields.atlan_fields import KeywordField, KeywordTextField, RelationField

from .dbt import Dbt


class DbtTest(Dbt):
    """Description"""

    type_name: str = Field("DbtTest", allow_mutation=False)

    @validator("type_name")
    def validate_type_name(cls, v):
        if v != "DbtTest":
            raise ValueError("must be DbtTest")
        return v

    def __setattr__(self, name, value):
        if name in DbtTest._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # DBT_TEST_STATUS: ClassVar[KeywordField] = KeywordField(
    #     "dbtTestStatus", "dbtTestStatus"
    # )
    # """
    # Details of the results of the test. For errors, it reads "ERROR".
    # """
    # DBT_TEST_STATE: ClassVar[KeywordField] = KeywordField(
    #     "dbtTestState", "dbtTestState"
    # )
    # """
    # Test results. Can be one of, in order of severity, "error", "fail", "warn", "pass".
    # """
    # DBT_TEST_ERROR: ClassVar[KeywordField] = KeywordField(
    #     "dbtTestError", "dbtTestError"
    # )
    # """
    # Error message in the case of state being "error".
    # """
    # DBT_TEST_RAW_SQL: ClassVar[KeywordTextField] = KeywordTextField(
    #     "dbtTestRawSQL", "dbtTestRawSQL", "dbtTestRawSQL.text"
    # )
    # """
    # Raw SQL of the test.
    # """
    # DBT_TEST_COMPILED_SQL: ClassVar[KeywordField] = KeywordField(
    #     "dbtTestCompiledSQL", "dbtTestCompiledSQL"
    # )
    # """
    # Compiled SQL of the test.
    # """
    # DBT_TEST_RAW_CODE: ClassVar[KeywordTextField] = KeywordTextField(
    #     "dbtTestRawCode", "dbtTestRawCode", "dbtTestRawCode.text"
    # )
    # """
    # Raw code of the test (when the test is defined using Python).
    # """
    # DBT_TEST_COMPILED_CODE: ClassVar[KeywordField] = KeywordField(
    #     "dbtTestCompiledCode", "dbtTestCompiledCode"
    # )
    # """
    # Compiled code of the test (when the test is defined using Python).
    # """
    # DBT_TEST_LANGUAGE: ClassVar[KeywordField] = KeywordField(
    #     "dbtTestLanguage", "dbtTestLanguage"
    # )
    # """
    # Language in which the test is written, for example: SQL or Python.
    # """

    # DBT_SOURCES: ClassVar[RelationField] = RelationField("dbtSources")
    # """
    # TBC
    # """
    # SQL_ASSETS: ClassVar[RelationField] = RelationField("sqlAssets")
    # """
    # TBC
    # """
    # DBT_MODELS: ClassVar[RelationField] = RelationField("dbtModels")
    # """
    # TBC
    # """
    # DBT_MODEL_COLUMNS: ClassVar[RelationField] = RelationField("dbtModelColumns")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "dbt_test_status",
        "dbt_test_state",
        "dbt_test_error",
        "dbt_test_raw_s_q_l",
        "dbt_test_compiled_s_q_l",
        "dbt_test_raw_code",
        "dbt_test_compiled_code",
        "dbt_test_language",
        "dbt_sources",
        "sql_assets",
        "dbt_models",
        "dbt_model_columns",
    ]

    @property
    def dbt_test_status(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.dbt_test_status

    @dbt_test_status.setter
    def dbt_test_status(self, dbt_test_status: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.dbt_test_status = dbt_test_status

    @property
    def dbt_test_state(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.dbt_test_state

    @dbt_test_state.setter
    def dbt_test_state(self, dbt_test_state: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.dbt_test_state = dbt_test_state

    @property
    def dbt_test_error(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.dbt_test_error

    @dbt_test_error.setter
    def dbt_test_error(self, dbt_test_error: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.dbt_test_error = dbt_test_error

    @property
    def dbt_test_raw_s_q_l(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.dbt_test_raw_s_q_l

    @dbt_test_raw_s_q_l.setter
    def dbt_test_raw_s_q_l(self, dbt_test_raw_s_q_l: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.dbt_test_raw_s_q_l = dbt_test_raw_s_q_l

    @property
    def dbt_test_compiled_s_q_l(self) -> Optional[str]:
        return (
            None if self.attributes is None else self.attributes.dbt_test_compiled_s_q_l
        )

    @dbt_test_compiled_s_q_l.setter
    def dbt_test_compiled_s_q_l(self, dbt_test_compiled_s_q_l: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.dbt_test_compiled_s_q_l = dbt_test_compiled_s_q_l

    @property
    def dbt_test_raw_code(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.dbt_test_raw_code

    @dbt_test_raw_code.setter
    def dbt_test_raw_code(self, dbt_test_raw_code: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.dbt_test_raw_code = dbt_test_raw_code

    @property
    def dbt_test_compiled_code(self) -> Optional[str]:
        return (
            None if self.attributes is None else self.attributes.dbt_test_compiled_code
        )

    @dbt_test_compiled_code.setter
    def dbt_test_compiled_code(self, dbt_test_compiled_code: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.dbt_test_compiled_code = dbt_test_compiled_code

    @property
    def dbt_test_language(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.dbt_test_language

    @dbt_test_language.setter
    def dbt_test_language(self, dbt_test_language: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.dbt_test_language = dbt_test_language

    @property
    def dbt_sources(self) -> Optional[list[DbtSource]]:
        return None if self.attributes is None else self.attributes.dbt_sources

    @dbt_sources.setter
    def dbt_sources(self, dbt_sources: Optional[list[DbtSource]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.dbt_sources = dbt_sources

    @property
    def sql_assets(self) -> Optional[list[SQL]]:
        return None if self.attributes is None else self.attributes.sql_assets

    @sql_assets.setter
    def sql_assets(self, sql_assets: Optional[list[SQL]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.sql_assets = sql_assets

    @property
    def dbt_models(self) -> Optional[list[DbtModel]]:
        return None if self.attributes is None else self.attributes.dbt_models

    @dbt_models.setter
    def dbt_models(self, dbt_models: Optional[list[DbtModel]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.dbt_models = dbt_models

    @property
    def dbt_model_columns(self) -> Optional[list[DbtModelColumn]]:
        return None if self.attributes is None else self.attributes.dbt_model_columns

    @dbt_model_columns.setter
    def dbt_model_columns(self, dbt_model_columns: Optional[list[DbtModelColumn]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.dbt_model_columns = dbt_model_columns

    class Attributes(Dbt.Attributes):
        dbt_test_status: Optional[str] = Field(
            None, description="", alias="dbtTestStatus"
        )
        dbt_test_state: Optional[str] = Field(
            None, description="", alias="dbtTestState"
        )
        dbt_test_error: Optional[str] = Field(
            None, description="", alias="dbtTestError"
        )
        dbt_test_raw_s_q_l: Optional[str] = Field(
            None, description="", alias="dbtTestRawSQL"
        )
        dbt_test_compiled_s_q_l: Optional[str] = Field(
            None, description="", alias="dbtTestCompiledSQL"
        )
        dbt_test_raw_code: Optional[str] = Field(
            None, description="", alias="dbtTestRawCode"
        )
        dbt_test_compiled_code: Optional[str] = Field(
            None, description="", alias="dbtTestCompiledCode"
        )
        dbt_test_language: Optional[str] = Field(
            None, description="", alias="dbtTestLanguage"
        )
        dbt_sources: Optional[list[DbtSource]] = Field(
            None, description="", alias="dbtSources"
        )  # relationship
        sql_assets: Optional[list[SQL]] = Field(
            None, description="", alias="sqlAssets"
        )  # relationship
        dbt_models: Optional[list[DbtModel]] = Field(
            None, description="", alias="dbtModels"
        )  # relationship
        dbt_model_columns: Optional[list[DbtModelColumn]] = Field(
            None, description="", alias="dbtModelColumns"
        )  # relationship

    attributes: "DbtTest.Attributes" = Field(
        default_factory=lambda: DbtTest.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .dbt_source import DbtSource  # noqa: E402
from .sql import SQL  # noqa: E402
from .dbt_model import DbtModel  # noqa: E402
from .dbt_model_column import DbtModelColumn  # noqa: E402
