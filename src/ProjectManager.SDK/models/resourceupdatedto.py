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
class ResourceUpdateDto:
    """
    A Resource represents a person, material, or tool that is used
    within your Projects. When you attach a Resources to more than one
    Task, the software will schedule the usage of your Resource so that
    it is not allocated to more than one Task at the same time. The
    users in your Workspace are also considered Resources. To invite a
    new User to your Workspace, create a new Resource for that user.
    """

    firstName: object | None = None
    lastName: object | None = None
    email: object | None = None
    hourlyRate: object | None = None
    phone: object | None = None
    city: object | None = None
    state: object | None = None
    countryCode: object | None = None
    notes: object | None = None
    roleId: object | None = None
    teamIds: list[object] | None = None
    skillIds: list[object] | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
