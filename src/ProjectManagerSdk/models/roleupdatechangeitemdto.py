#
# ProjectManager API for Python
#
# (c) ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from typing import List
import dataclasses

@dataclasses.dataclass
class RoleUpdateChangeItemDto:
    """
    One property change when updating a business role (batch change-set
    item).
    """

    property: str | None = None
    """
    Field to change: name, description, or permissions.
    """

    value: object | None = None
    """
    New value for the field; for permissions, a JSON object in the role
    permissions matrix shape.
    """

    id: str | None = None
    """
    Optional identifier when the change targets a nested or keyed item.
    """


