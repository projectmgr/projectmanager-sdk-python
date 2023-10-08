#
# ProjectManager API for Python
#
# (c) 2023-2023 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2023 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from dataclasses import dataclass

@dataclass
class GetProjectFieldsResponseDto:
    """
    Represents either a ProjectField or a TaskField, depending on the
    value of the `EntityType` for this object. A ProjectField is a
    custom field defined within your Workspace. You can define
    ProjectFields for any integration purpose that is important to your
    business. Each ProjectField has a data type as well as options in
    how it is handled. ProjectFields can be edited for each Project
    within your Workspace. A TaskField is a custom field defined within
    your Workspace for a specific Project. You can define TaskFields for
    any integration purpose that is important to your business. Each
    TaskField has a data type as well as options in how it is handled.
    TaskFields can be edited for each Task inside this Project.
    """

    id: str | None = None
    name: str | None = None
    type: str | None = None
    entityType: str | None = None
    options: list[str] | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
