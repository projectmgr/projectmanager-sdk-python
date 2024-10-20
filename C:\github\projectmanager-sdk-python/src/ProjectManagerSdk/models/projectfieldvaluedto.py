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
class ProjectFieldValueDto:
    """
    A model that contains the value for a ProjectField.
    """

    id: str | None = None
    """
    The unique identifier of this Project Field.
    """

    shortId: str | None = None
    """
    The unique Short Id of this Project Field.
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

    value: str | None = None
    """
    The value currently set for this Project Field Value.
    """

    createdDate: str | None = None
    """
    Date and time (in UTC) that this TaskField was created.
    """

    modifiedDate: str | None = None
    """
    Date and time (in UTC) that this TaskField was last modified.
    """


