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
class RolePermissionFeatureDto:
    """
    One cell in the workspace role permissions matrix: grant state plus
    subscription / feature metadata when the action is Chargebee-gated.
    """

    isGranted: bool | None = None
    """
    Whether this permission is granted for the role in the workspace
    (persisted access).
    """

    isEntitled: bool | None = None
    """
    Whether the current workspace subscription entitles this action. May
    be false while isGranted is true for legacy data.
    """

    isFeatureEnabled: bool | None = None
    """
    Whether the feature flag for this permission is enabled for the
    workspace (display / upsell context).
    """

    featureId: str | None = None
    """
    Primary Chargebee feature id used for entitlement (e.g.
    print-and-export), when applicable.
    """

    featureName: str | None = None
    """
    Human-readable feature name for UI or documentation, when
    applicable.
    """


