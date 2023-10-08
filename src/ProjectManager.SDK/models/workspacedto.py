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
class WorkSpaceDto:
    """
    A Workspace represents a single business subscription to the
    ProjectManager.com service. You can be a member of multiple
    Workspaces. Each Workspace is completely separate from all other
    Workspaces and a user cannot log in to multiple Workspaces at the
    same time.
    """

    id: object | None = None
    company: object | None = None
    customProductDomain: object | None = None
    customerId: object | None = None
    isOwner: object | None = None
    organizationId: object | None = None
    color: object | None = None
    roleName: object | None = None
    registerDate: object | None = None
    isInviteAccepted: object | None = None
    businessUserId: object | None = None
    isPaid: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
