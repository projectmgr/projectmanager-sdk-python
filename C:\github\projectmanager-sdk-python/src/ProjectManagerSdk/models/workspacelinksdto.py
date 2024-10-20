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
class WorkSpaceLinksDto:
    """
    A shortcut link within the currently logged in Workspace.
    """

    project: str | None = None
    """
    The name of the project for this link.
    """

    workSpaceApi: str | None = None
    """
    This is the link to the api for this business. Some endpoints may
    need this value.
    """


