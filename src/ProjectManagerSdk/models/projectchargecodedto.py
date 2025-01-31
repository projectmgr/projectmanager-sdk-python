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
class ProjectChargeCodeDto:
    """
    A ChargeCode is a code used to identify costs within your Projects.
    Each ChargeCode has a name and a unique identifier. ChargeCodes are
    defined per Workspace and are shared among Projects.
    """

    id: str | None = None
    """
    The unique identifier of this ChargeCode
    """

    name: str | None = None
    """
    The name of this ChargeCode
    """


