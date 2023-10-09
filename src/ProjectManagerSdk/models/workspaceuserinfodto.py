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


from ProjectManagerSdk.models.workspacelinksdto import WorkSpaceLinksDto
from dataclasses import dataclass

@dataclass
class WorkSpaceUserInfoDto:
    """
    TODO - What is this?
    """

    links: WorkSpaceLinksDto | None = None
    """
    TODO - What is this?
    """

    emailAddress: str | None = None
    """
    TODO - What is this?
    """

    id: str | None = None
    """
    TODO - What is this?
    """

    fullName: str | None = None
    """
    TODO - What is this?
    """

    workSpaceName: str | None = None
    """
    TODO - What is this?
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
