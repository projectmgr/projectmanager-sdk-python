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

    id: str | None = None
    """
    The unique identifier of this Workspace.
    """

    company: str | None = None
    """
    The name of this Workspace.
    """

    customProductDomain: str | None = None
    """
    The unique DNS domain of this Workspace.
    """

    customerId: str | None = None
    """
    TODO - What is this value?
    """

    isOwner: bool | None = None
    """
    This value is set to true if the user who retrieves this Workspace
    object via an API call is the owner of this Workspace.
    """

    organizationId: str | None = None
    """
    The organization code used for authentication systems for this
    Workspace.
    """

    color: str | None = None
    """
    The RGB color in the format `#RRGGBB` for this Workspace.
    """

    roleName: str | None = None
    """
    The role of the current user within this Workspace.
    """

    registerDate: str | None = None
    """
    The timestamp when the Workspace was created.
    """

    isInviteAccepted: bool | None = None
    """
    True if the user has accepted an invitation to this Workspace.
    """

    businessUserId: str | None = None
    """
    The unique identifier of the BusinessUser that is the owner of this
    Workspace.
    """

    isPaid: bool | None = None
    """
    True if this Workspace has an active subscription; false if this is
    a free trial.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
