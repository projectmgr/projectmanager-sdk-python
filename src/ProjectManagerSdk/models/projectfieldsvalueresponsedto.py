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
class ProjectFieldsValueResponseDto:
    """
    A Project Field is a custom field defined within your Workspace for
    each Project. Each Project Field has a data type as well as options
    in how it is handled.
    """

    id: str | None = None
    """
    The unique identifier of this Project Field.
    """

    value: str | None = None
    """
    The value currently set for this Project Field.
    """

    name: str | None = None
    """
    The name of this Project Field.
    """

    type: str | None = None
    """
    The type of this Project Field. Valid types are the following: *
    Text * Number * Date * Checkbox * Currency * Dropdown
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
