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
class RiskCreateDto:
    """
    Represents the data required to create a new Risk within a Project.
    A Risk identifies a potential issue or uncertainty that may impact
    project outcomes. This DTO captures descriptive information, risk
    assessment metrics (such as impact and likelihood), and optional
    ownership via assignees.
    """

    name: str | None = None
    """
    The common name of this Risk.
    """

    description: str | None = None
    """
    A description of the work to be performed in this Risk.
    """

    percentComplete: int | None = None
    """
    The numerical percentage, from 0-100, representing the percentage
    completion for this risk. Any numbers below zero or above 100 will
    be clamped to the minimum or maximum value.
    """

    priority: int | None = None
    """
    Indicates the level of importance assigned to a risk, with 500 being
    standard priority; the higher the number, the higher the priority.
    """

    impact: int | None = None
    """
    The potential effect of the risk.
    """

    likelihood: int | None = None
    """
    Probability or chance of the risk occurring.
    """

    responseId: int | None = None
    """
    The planned or implemented response to address the identified risk.
    Avoid, Mitigate, Transfer, Accept
    """

    resolution: str | None = None
    """
    The actions or strategy planned or taken to mitigate or eliminate
    the risk.
    """

    assignees: List[str] | None = None
    """
    A list of unique identifiers of Assignees to be assigned to this
    Risk
    """

    riskTypeId: int | None = None
    """
    The type of risk. Risk = 1 Assumption = 2 Issue = 3 Dependency = 4
    Change = 5
    """


