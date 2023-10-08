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
class CreateProjectFieldDto:
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
    The type of the Field. Valid types are the following: * Text *
    Number * Date * Currency * Dropdown Attempting to create a field
    with any Type other than these will return an error. For Dropdown
    Field, specify the list of choices in the `Options` field. TODO -
    This object needs to support a list of options, in case dropdown is
    selected
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
