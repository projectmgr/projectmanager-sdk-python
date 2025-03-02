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
class StateDto:
    """
    Represents a state with its details.
    """

    id: int | None = None
    """
    Gets or sets the unique identifier for the state.
    """

    stateCode: str | None = None
    """
    Gets or sets the code of the state.
    """

    name: str | None = None
    """
    Gets or sets the name of the state.
    """


