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
class ProjectCustomerCreateDto:
    """
    A ProjectCustomer is a code used to identify costs within your
    Projects. Each ProjectCustomer has a name and a unique identifier.
    ChargeCodes are defined per Workspace and are shared among Projects.
    """

    name: str | None = None
    """
    The name of this ProjectCustomer
    """


