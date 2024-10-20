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
class MasterConnectionSchemeDto:
    """
    Master Connection Scheme for Providers
    """

    value: str | None = None
    """
    The value of the property
    """

    type: str | None = None
    """
    The type of the property
    """

    sendToClient: bool | None = None
    """
    Send to the client true/false
    """


