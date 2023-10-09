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
class GetTaskFieldsResponseDto:
    """
    A TaskField is a custom field defined within your Workspace for a
    specific Project. You can define TaskFields for any integration
    purpose that is important to your business. Each TaskField has a
    data type as well as options in how it is handled. TaskFields can be
    edited for each Task inside this Project.
    """

    id: str | None = None
    """
    The unique identifier of this TaskField
    """

    name: str | None = None
    """
    The name of this TaskField
    """

    type: str | None = None
    """
    The type of this TaskField. Valid types are the following: * Text *
    Number * Date * Checkbox * Currency * Dropdown Attempting to create
    a field with any Type other than these will return an error. For
    Dropdown TaskFields, specify the list of choices in the `Options`
    field.
    """

    options: list[str] | None = None
    """
    A list of options for use of this TaskField. This is only valid if
    the `Type` value is set to `Dropdown`. When a custom TaskField of
    type `DropDown` is shown to a user in the application, they will be
    able to choose one of the `Options` in this list.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
