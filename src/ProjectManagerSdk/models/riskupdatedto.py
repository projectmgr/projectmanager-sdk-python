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
class RiskUpdateDto:
    """
    A Risk represents an item of potential impact or uncertainty. Risks
    share many characteristics with tasks but are tracked independently
    of project execution work.
    """

    name: str | None = None
    """
    The common name of this Risk.
    """

    dueDate: str | None = None
    """
    The date when this risk is expected to be resolved.
    """

    percentComplete: int | None = None
    """
    Percentage completion (0–100).
    """

    priority: int | None = None
    """
    Priority of the risk.
    """

    impact: int | None = None
    """
    The potential effect of the risk.
    """

    likelihood: int | None = None
    """
    Probability of the risk occurring.
    """

    responseId: int | None = None
    """
    Planned or implemented response. Avoid it, Mitigate, Transfer,
    Accept
    """

    resolution: str | None = None
    """
    Actions taken or planned to address the risk.
    """

    description: str | None = None
    """
    Additional comments or observations.
    """

    assignees: List[str] | None = None
    """
    Users assigned to the risk. Replaces existing assignments when
    provided.
    """

    tagIds: List[str] | None = None
    """
    Tags applied to the risk. Replaces existing tags when provided.
    """

    riskTypeId: int | None = None
    """
    The type of risk. Risk = 1 Assumption = 2 Issue = 3 Dependency = 4
    Change = 5
    """


