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
class CountryDto:
    """
    Represents a country with its details.
    """

    id: str | None = None
    """
    Gets or sets the unique identifier for the country. This should
    translate to the ISO2 code for that country.
    """

    name: str | None = None
    """
    Gets or sets the name of the country.
    """


