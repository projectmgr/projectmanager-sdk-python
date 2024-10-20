#
# ProjectManager API for Python
#
# (c) 2023-2024 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2024 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from typing import List
import dataclasses

@dataclasses.dataclass
class ProjectFieldCreateDto:
    """
    A ProjectField is a custom field defined within your Workspace. You
    can define ProjectFields for any integration purpose that is
    important to your business. Each ProjectField has a data type as
    well as options in how it is handled. ProjectFields can be edited
    for each Project within your Workspace.
    """

    name: str | None = None
    """
    The name of this Field
    """

    type: str | None = None
    """
    The type of the Field. Attempting to create a field with any Type
    other than these will return an error. For Dropdown Field types,
    specify the list of choices in the `Options` field. Valid options
    are: * string * number * date * bool * currency * dropdown-single *
    dropdown-multi
    """

    shortId: str | None = None
    """
    The short Id of this field - human readable identity
    """

    options: List[str] | None = None
    """
    A list of options for use of this ProjectField. This is only valid
    if the `Type` value is set to `Dropdown`. When a custom TaskField of
    type `DropDown` is shown to a user in the application, they will be
    able to choose one of the `Options` in this list.
    """


