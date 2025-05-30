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
class ApiKeyDto:
    """
    Represents api access key entity
    """

    id: str | None = None
    """
    Internal access token id
    """

    createdBy: str | None = None
    """
    Created by user id
    """

    expires: str | None = None
    """
    Expires date
    """

    apiKey: str | None = None
    """
    Bearer Key
    """

    name: str | None = None
    """
    Name of token
    """


