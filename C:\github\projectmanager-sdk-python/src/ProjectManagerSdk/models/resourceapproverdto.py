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
class ResourceApproverDto:
    """
    When managing users, you can choose who will approve a person's
    Timesheets. This is a ResourceApprover. You can specify this person
    within the Resource object.
    """

    id: str | None = None
    """
    The unique identifier of this ResourceApprover
    """

    name: str | None = None
    """
    The name of this ResourceApprover
    """


