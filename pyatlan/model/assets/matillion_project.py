from __future__ import annotations

from typing import ClassVar, Optional

from pydantic.v1 import Field, validator

# from pyatlan.model.fields.atlan_fields import KeywordField, KeywordTextField, NumericField, RelationField

from .matillion import Matillion


class MatillionProject(Matillion):
    """Description"""

    type_name: str = Field("MatillionProject")  #, allow_mutation=False)

    @validator("type_name")
    def validate_type_name(cls, v):
        if v != "MatillionProject":
            raise ValueError("must be MatillionProject")
        return v

    def __setattr__(self, name, value):
        if name in MatillionProject._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # MATILLION_VERSIONS: ClassVar[KeywordField] = KeywordField(
    #     "matillionVersions", "matillionVersions"
    # )
    # """
    # List of versions in the project.
    # """
    # MATILLION_ENVIRONMENTS: ClassVar[KeywordField] = KeywordField(
    #     "matillionEnvironments", "matillionEnvironments"
    # )
    # """
    # List of environments in the project.
    # """
    # MATILLION_PROJECT_JOB_COUNT: ClassVar[NumericField] = NumericField(
    #     "matillionProjectJobCount", "matillionProjectJobCount"
    # )
    # """
    # Number of jobs in the project.
    # """
    # MATILLION_GROUP_NAME: ClassVar[KeywordTextField] = KeywordTextField(
    #     "matillionGroupName", "matillionGroupName.keyword", "matillionGroupName"
    # )
    # """
    # Simple name of the Matillion group to which the project belongs.
    # """
    # MATILLION_GROUP_QUALIFIED_NAME: ClassVar[KeywordTextField] = KeywordTextField(
    #     "matillionGroupQualifiedName",
    #     "matillionGroupQualifiedName",
    #     "matillionGroupQualifiedName.text",
    # )
    # """
    # Unique name of the Matillion group to which the project belongs.
    # """

    # MATILLION_JOBS: ClassVar[RelationField] = RelationField("matillionJobs")
    # """
    # TBC
    # """
    # MATILLION_GROUP: ClassVar[RelationField] = RelationField("matillionGroup")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "matillion_versions",
        "matillion_environments",
        "matillion_project_job_count",
        "matillion_group_name",
        "matillion_group_qualified_name",
        "matillion_jobs",
        "matillion_group",
    ]

    @property
    def matillion_versions(self) -> Optional[set[str]]:
        return None if self.attributes is None else self.attributes.matillion_versions

    @matillion_versions.setter
    def matillion_versions(self, matillion_versions: Optional[set[str]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.matillion_versions = matillion_versions

    @property
    def matillion_environments(self) -> Optional[set[str]]:
        return (
            None if self.attributes is None else self.attributes.matillion_environments
        )

    @matillion_environments.setter
    def matillion_environments(self, matillion_environments: Optional[set[str]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.matillion_environments = matillion_environments

    @property
    def matillion_project_job_count(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.matillion_project_job_count
        )

    @matillion_project_job_count.setter
    def matillion_project_job_count(self, matillion_project_job_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.matillion_project_job_count = matillion_project_job_count

    @property
    def matillion_group_name(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.matillion_group_name

    @matillion_group_name.setter
    def matillion_group_name(self, matillion_group_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.matillion_group_name = matillion_group_name

    @property
    def matillion_group_qualified_name(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.matillion_group_qualified_name
        )

    @matillion_group_qualified_name.setter
    def matillion_group_qualified_name(
        self, matillion_group_qualified_name: Optional[str]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.matillion_group_qualified_name = matillion_group_qualified_name

    @property
    def matillion_jobs(self) -> Optional[list[MatillionJob]]:
        return None if self.attributes is None else self.attributes.matillion_jobs

    @matillion_jobs.setter
    def matillion_jobs(self, matillion_jobs: Optional[list[MatillionJob]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.matillion_jobs = matillion_jobs

    @property
    def matillion_group(self) -> Optional[MatillionGroup]:
        return None if self.attributes is None else self.attributes.matillion_group

    @matillion_group.setter
    def matillion_group(self, matillion_group: Optional[MatillionGroup]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.matillion_group = matillion_group

    class Attributes(Matillion.Attributes):
        matillion_versions: Optional[set[str]] = Field(
            None, description="", alias="matillionVersions"
        )
        matillion_environments: Optional[set[str]] = Field(
            None, description="", alias="matillionEnvironments"
        )
        matillion_project_job_count: Optional[int] = Field(
            None, description="", alias="matillionProjectJobCount"
        )
        matillion_group_name: Optional[str] = Field(
            None, description="", alias="matillionGroupName"
        )
        matillion_group_qualified_name: Optional[str] = Field(
            None, description="", alias="matillionGroupQualifiedName"
        )
        matillion_jobs: Optional[list[MatillionJob]] = Field(
            None, description="", alias="matillionJobs"
        )  # relationship
        matillion_group: Optional[MatillionGroup] = Field(
            None, description="", alias="matillionGroup"
        )  # relationship

    attributes: "MatillionProject.Attributes" = Field(
        default_factory=lambda: MatillionProject.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .matillion_job import MatillionJob  # noqa: E402
from .matillion_group import MatillionGroup  # noqa: E402
