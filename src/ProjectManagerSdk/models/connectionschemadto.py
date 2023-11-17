#
# ProjectManager API for Python
#
# (c) 2023-2023 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2023 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from dataclasses import dataclass

@dataclass
class ConnectionSchemaDto:
    """
    This class contains the URL or AuthScheme to use to authenticate
    with the Integration Provider.
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


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
