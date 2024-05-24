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

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.updaterequestdto import UpdateRequestDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class FileClient:
    """
    API methods related to File
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def download_file(self, documentId: str, type: str) -> AstroResult[bytes]:
        """
        Downloads the contents of a file that was previously uploaded to
        ProjectManager.com. ProjectManager allows you to store Files
        connected to other elements of your Workspace such as a Project,
        a Task, or Home. Files are maintained separately based on the
        location where the file was stored. When you upload a File,
        please allow a few moments for the File to be processed and
        verified. ProjectManager may reject File uploads that contain
        problems such as malware. Once a File has completed the upload
        the process, you may retrieve it using the DownloadFile API. If
        successful, this API returns the file contents as an
        octet-stream (raw bytes). If an error occurs, you will receive a
        JSON result with error information.

        Parameters
        ----------
        documentId : str
            The unique identifier of the document to download
        type : str
            If you specify a type of `html`, processes the file using
            text encoding, otherwise binary
        """
        path = f"/api/data/files/{documentId}/download"
        queryParams = {}
        if type:
            queryParams['type'] = type
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[bytes](None, True, False, result.status_code, result.content)
        else:
            response = AstroResult[bytes](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def download_a_thumbnail_image(self, documentId: str) -> AstroResult[bytes]:
        """
        Downloads a thumbnail image associated with a document that was
        previously uploaded to ProjectManager.com. ProjectManager allows
        you to store files linked to various elements within your
        Workspace, such as Projects, Tasks, or your Home. Files are
        organized based on their storage location. When uploading a
        file, please allow some time for the file to undergo processing
        and verification. ProjectManager may reject file uploads
        containing issues such as malware. Once a file has completed the
        upload process, you can retrieve its associated thumbnail using
        the DownloadThumbnail API. If successful, this API returns the
        file contents as an octet-stream (raw bytes). If an error
        occurs, you will receive a JSON result with error information.

        Parameters
        ----------
        documentId : str
            The unique identifier of the document for which to download
            the thumbnail.
        """
        path = f"/api/data/files/{documentId}/thumbnail"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[bytes](None, True, False, result.status_code, result.content)
        else:
            response = AstroResult[bytes](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_file(self, fileId: str, body: UpdateRequestDto) -> AstroResult[object]:
        """
        Updates information about a File uploaded to your Workspace.
        ProjectManager allows you to store Files connected to other
        elements of your Workspace such as a Project, a Task, or Home.
        Files are maintained separately based on the location where the
        file was stored. When you upload a File, please allow a few
        moments for the File to be processed and verified.
        ProjectManager may reject File uploads that contain problems
        such as malware. Once a File has completed the upload the
        process, you may retrieve it using the DownloadFile API. This
        API returns a JSON response indicating success or failure.

        Parameters
        ----------
        fileId : str
            The unique identifier of the File to update
        body : UpdateRequestDto
            Information to change about the File and its location
        """
        path = f"/api/data/files/{fileId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_file(self, fileId: str, hard: bool) -> AstroResult[object]:
        """
        In case of soft delete moves file to trash folder. For hard
        delete completely deletes file's metadata from pm database as
        well as from amazon storage This API returns a JSON response
        indicating success or failure.

        Parameters
        ----------
        fileId : str
            The unique identifier of the File to delete
        hard : bool
            Param indicates that file should be hard deleted
        """
        path = f"/api/data/files/{fileId}"
        queryParams = {}
        if hard:
            queryParams['hard'] = hard
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
