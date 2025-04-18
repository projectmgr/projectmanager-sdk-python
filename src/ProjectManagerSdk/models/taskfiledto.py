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
class TaskFileDto:
    """
    Represents a file associated with a Task in project manager
    """

    id: str | None = None
    """
    The identifier for this file
    """

    name: str | None = None
    """
    The name of the file
    """

    url: str | None = None
    """
    The url of the file which can be used for downloading
    """


