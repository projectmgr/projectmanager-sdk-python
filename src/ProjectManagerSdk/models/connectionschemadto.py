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
class ConnectionSchemaDto:
    """
    This class contains the URL or AuthScheme to use to authenticate
    with the Integration Provider.
    """

    connected: bool | None = None
    """
    Whether or not the Integration Provider is connected.
    """

    url: str | None = None
    """
    The URL to use to authenticate with the Integration Provider.
    """

    authScheme: object | None = None
    """
    This class contains the AuthScheme to use to authenticate with the
    Integration Provider.
    """


