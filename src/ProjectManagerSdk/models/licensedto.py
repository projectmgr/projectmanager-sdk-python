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
class LicenseDto:
    """
    A License represents a subscription to a particular product or
    bundle of products within ProjectManager.
    """

    id: str | None = None
    """
    The unique identifier of this License.
    """

    licenseSku: str | None = None
    """
    The SKU code of this License, used for billing purposes.
    """

    bundleSku: str | None = None
    """
    The SKU code of the bundle of this License, used for billing
    purposes.
    """

    optional: bool | None = None
    """
    True if this license is optional. This field will be removed in a
    future version.
    """


