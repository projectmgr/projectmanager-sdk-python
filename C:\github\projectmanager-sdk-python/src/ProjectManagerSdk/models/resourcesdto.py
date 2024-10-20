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


from ProjectManagerSdk.models.resourcedto import ResourceDto
from ProjectManagerSdk.models.usererror import UserError
from typing import List
import dataclasses

@dataclasses.dataclass
class ResourcesDto:
    """
    The Resources object represents the results of a bulk Resource
    creation API call. A Resource represents a person, material, or tool
    that is used within your Projects. When you attach a Resources to
    more than one Task, the software will schedule the usage of your
    Resource so that it is not allocated to more than one Task at the
    same time. The users in your Workspace are also considered
    Resources. To invite a new User to your Workspace, create a new
    Resource for that user.
    """

    resources: List[ResourceDto] | None = None
    """
    The list of the Resources created by this API call.
    """

    errors: List[UserError] | None = None
    """
    The list of errors that occurred for Resources that could not be
    created.
    """


