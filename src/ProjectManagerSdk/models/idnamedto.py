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
class IdNameDto:
    """
    A lightweight reference that pairs a unique identifier with a
    display name. To determine what the identifier and name represent,
    see the field to which this value is attached in the parent object.
    """

    id: str | None = None
    """
    A unique identifier. To determine the meaning of this unique
    identifier, see the field to which this value is attached.
    """

    name: str | None = None
    """
    A name. To determine the meaning of this name, see the field to
    which this value is attached in the parent object.
    """


