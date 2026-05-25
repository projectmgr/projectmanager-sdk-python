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
class EntitlementDto:
    """
    Represents a single entitlement for the current Workspace.
    """

    shortId: str | None = None
    """
    The unique identifier for this entitlement.
    """

    name: str | None = None
    """
    The human-readable name of the entitlement.
    """

    type: str | None = None
    """
    Indicates whether this is a boolean toggle ("switch") or a numeric
    cap ("limit").
    """

    enabled: bool | None = None
    """
    For switch-type entitlements, indicates whether the feature is
    enabled. Null for limit-type entitlements.
    """

    limit: float | None = None
    """
    For limit-type entitlements, the numeric cap value. Null for
    switch-type entitlements.
    """


