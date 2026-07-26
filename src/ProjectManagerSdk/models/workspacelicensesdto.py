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
class WorkspaceLicensesDto:
    """
    A summary of the paid user licenses for the workspace the current
    user is logged on to.
    """

    purchased: int | None = None
    """
    The number of paid user licenses purchased for this workspace.
    """

    used: int | None = None
    """
    The number of paid user licenses currently in use by active
    (non-guest) users.
    """

    guestUsed: int | None = None
    """
    The number of active guest users in this workspace.
    """

    remaining: int | None = None
    """
    The number of purchased licenses still available. This can be
    negative when the workspace has more active users than purchased
    licenses.
    """


