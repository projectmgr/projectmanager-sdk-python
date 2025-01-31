# API client
from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient
from ProjectManagerSdk.tools import remove_empty_elements
# API categories
from ProjectManagerSdk.clients.apikeyclient import ApiKeyClient
from ProjectManagerSdk.clients.changesetclient import ChangesetClient
from ProjectManagerSdk.clients.dashboardclient import DashboardClient
from ProjectManagerSdk.clients.discussionclient import DiscussionClient
from ProjectManagerSdk.clients.fileclient import FileClient
from ProjectManagerSdk.clients.holidayclient import HolidayClient
from ProjectManagerSdk.clients.homefileclient import HomeFileClient
from ProjectManagerSdk.clients.integrationcategoryclient import IntegrationCategoryClient
from ProjectManagerSdk.clients.integrationclient import IntegrationClient
from ProjectManagerSdk.clients.integrationproviderclient import IntegrationProviderClient
from ProjectManagerSdk.clients.licenseclient import LicenseClient
from ProjectManagerSdk.clients.meclient import MeClient
from ProjectManagerSdk.clients.notificationclient import NotificationClient
from ProjectManagerSdk.clients.nptfilesclient import NptFilesClient
from ProjectManagerSdk.clients.projectchargecodeclient import ProjectChargeCodeClient
from ProjectManagerSdk.clients.projectclient import ProjectClient
from ProjectManagerSdk.clients.projectcustomerclient import ProjectCustomerClient
from ProjectManagerSdk.clients.projectfieldclient import ProjectFieldClient
from ProjectManagerSdk.clients.projectfileclient import ProjectFileClient
from ProjectManagerSdk.clients.projectfolderclient import ProjectFolderClient
from ProjectManagerSdk.clients.projectmembersclient import ProjectMembersClient
from ProjectManagerSdk.clients.projectpriorityclient import ProjectPriorityClient
from ProjectManagerSdk.clients.projectstatusclient import ProjectStatusClient
from ProjectManagerSdk.clients.projecttemplateclient import ProjectTemplateClient
from ProjectManagerSdk.clients.projectversionclient import ProjectVersionClient
from ProjectManagerSdk.clients.resourceclient import ResourceClient
from ProjectManagerSdk.clients.resourceskillclient import ResourceSkillClient
from ProjectManagerSdk.clients.resourceteamclient import ResourceTeamClient
from ProjectManagerSdk.clients.riskclient import RiskClient
from ProjectManagerSdk.clients.tagclient import TagClient
from ProjectManagerSdk.clients.taskassigneeclient import TaskAssigneeClient
from ProjectManagerSdk.clients.taskclient import TaskClient
from ProjectManagerSdk.clients.taskfieldclient import TaskFieldClient
from ProjectManagerSdk.clients.taskfileclient import TaskFileClient
from ProjectManagerSdk.clients.taskmetadataclient import TaskMetadataClient
from ProjectManagerSdk.clients.taskstatusclient import TaskStatusClient
from ProjectManagerSdk.clients.tasktagclient import TaskTagClient
from ProjectManagerSdk.clients.tasktodoclient import TaskTodoClient
from ProjectManagerSdk.clients.teamsclient import TeamsClient
from ProjectManagerSdk.clients.timesheetclient import TimesheetClient
from ProjectManagerSdk.clients.userroleclient import UserRoleClient
from ProjectManagerSdk.clients.workspaceclient import WorkSpaceClient
# Data models
from ProjectManagerSdk.models.apikeycreatedto import ApiKeyCreateDto
from ProjectManagerSdk.models.apikeydto import ApiKeyDto
from ProjectManagerSdk.models.assigneeupsertdto import AssigneeUpsertDto
from ProjectManagerSdk.models.astroerror import AstroError
from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.authenticationdto import AuthenticationDto
from ProjectManagerSdk.models.authenticationstatusdto import AuthenticationStatusDto
from ProjectManagerSdk.models.changesetdto import ChangeSetDto
from ProjectManagerSdk.models.changesetstatusdto import ChangeSetStatusDto
from ProjectManagerSdk.models.connectionschemadto import ConnectionSchemaDto
from ProjectManagerSdk.models.countryholidaydto import CountryHolidayDto
from ProjectManagerSdk.models.createresourceskilldto import CreateResourceSkillDto
from ProjectManagerSdk.models.createresourceteamdto import CreateResourceTeamDto
from ProjectManagerSdk.models.createtaskfielddto import CreateTaskFieldDto
from ProjectManagerSdk.models.dashboardsettingcreatedto import DashboardSettingCreateDto
from ProjectManagerSdk.models.dashboardsettingdto import DashboardSettingDto
from ProjectManagerSdk.models.directlinkdto import DirectLinkDto
from ProjectManagerSdk.models.discussioncommentcreatedto import DiscussionCommentCreateDto
from ProjectManagerSdk.models.discussioncommentcreateresponsedto import DiscussionCommentCreateResponseDto
from ProjectManagerSdk.models.discussioncommentdto import DiscussionCommentDto
from ProjectManagerSdk.models.discussioncommentfiledto import DiscussionCommentFileDto
from ProjectManagerSdk.models.discussionemoji import DiscussionEmoji
from ProjectManagerSdk.models.exportdto import ExportDto
from ProjectManagerSdk.models.exportduedatefilterdto import ExportDueDateFilterDto
from ProjectManagerSdk.models.exportpriorityfilterdto import ExportPriorityFilterDto
from ProjectManagerSdk.models.filedto import FileDto
from ProjectManagerSdk.models.globalholidaydto import GlobalHolidayDto
from ProjectManagerSdk.models.iddto import IdDto
from ProjectManagerSdk.models.integrationauthsetupdto import IntegrationAuthSetupDto
from ProjectManagerSdk.models.integrationcategorydto import IntegrationCategoryDto
from ProjectManagerSdk.models.integrationconnectionschemeobjectdto import IntegrationConnectionSchemeObjectDto
from ProjectManagerSdk.models.integrationdto import IntegrationDto
from ProjectManagerSdk.models.integrationinstancedto import IntegrationInstanceDto
from ProjectManagerSdk.models.integrationproviderdto import IntegrationProviderDto
from ProjectManagerSdk.models.licensedto import LicenseDto
from ProjectManagerSdk.models.masterconnectionschemedto import MasterConnectionSchemeDto
from ProjectManagerSdk.models.namedto import NameDto
from ProjectManagerSdk.models.notificationdatadto import NotificationDataDto
from ProjectManagerSdk.models.notificationdto import NotificationDto
from ProjectManagerSdk.models.notificationresponsedto import NotificationResponseDto
from ProjectManagerSdk.models.notificationtimestampdto import NotificationTimestampDto
from ProjectManagerSdk.models.notificationtotalcountdto import NotificationTotalCountDto
from ProjectManagerSdk.models.notificationunreadcountdto import NotificationUnreadCountDto
from ProjectManagerSdk.models.permissionoptionsdto import PermissionOptionsDto
from ProjectManagerSdk.models.projectchangestatusdto import ProjectChangeStatusDto
from ProjectManagerSdk.models.projectchargecodedto import ProjectChargeCodeDto
from ProjectManagerSdk.models.projectcreateaccessdto import ProjectCreateAccessDto
from ProjectManagerSdk.models.projectcreateaccessmemberdto import ProjectCreateAccessMemberDto
from ProjectManagerSdk.models.projectcreatedto import ProjectCreateDto
from ProjectManagerSdk.models.projectcustomercreatedto import ProjectCustomerCreateDto
from ProjectManagerSdk.models.projectcustomerdto import ProjectCustomerDto
from ProjectManagerSdk.models.projectdto import ProjectDto
from ProjectManagerSdk.models.projectfieldcreatedto import ProjectFieldCreateDto
from ProjectManagerSdk.models.projectfielddto import ProjectFieldDto
from ProjectManagerSdk.models.projectfieldvaluedto import ProjectFieldValueDto
from ProjectManagerSdk.models.projectfiledto import ProjectFileDto
from ProjectManagerSdk.models.projectfilefolderdto import ProjectFileFolderDto
from ProjectManagerSdk.models.projectfiletaskdto import ProjectFileTaskDto
from ProjectManagerSdk.models.projectfolderdto import ProjectFolderDto
from ProjectManagerSdk.models.projectmanagerdto import ProjectManagerDto
from ProjectManagerSdk.models.projectmemberdto import ProjectMemberDto
from ProjectManagerSdk.models.projectmemberroledto import ProjectMemberRoleDto
from ProjectManagerSdk.models.projectprioritydto import ProjectPriorityDto
from ProjectManagerSdk.models.projectstatusdto import ProjectStatusDto
from ProjectManagerSdk.models.projecttemplatecategorydto import ProjectTemplateCategoryDto
from ProjectManagerSdk.models.projecttemplatedto import ProjectTemplateDto
from ProjectManagerSdk.models.projectupdatedto import ProjectUpdateDto
from ProjectManagerSdk.models.projectversionchangedatadto import ProjectVersionChangeDataDto
from ProjectManagerSdk.models.projectversiondto import ProjectVersionDto
from ProjectManagerSdk.models.reactgridlayoutdto import ReactGridLayoutDto
from ProjectManagerSdk.models.reactgridlayoutitemdto import ReactGridLayoutItemDto
from ProjectManagerSdk.models.resourceapproverdto import ResourceApproverDto
from ProjectManagerSdk.models.resourcecreatedto import ResourceCreateDto
from ProjectManagerSdk.models.resourcedto import ResourceDto
from ProjectManagerSdk.models.resourceholidaydto import ResourceHolidayDto
from ProjectManagerSdk.models.resourcescreatedto import ResourcesCreateDto
from ProjectManagerSdk.models.resourcesdto import ResourcesDto
from ProjectManagerSdk.models.resourceskilldto import ResourceSkillDto
from ProjectManagerSdk.models.resourceteamdto import ResourceTeamDto
from ProjectManagerSdk.models.resourceupdatedto import ResourceUpdateDto
from ProjectManagerSdk.models.riskexportprogressfilterdto import RiskExportProgressFilterDto
from ProjectManagerSdk.models.riskexportsettingsdto import RiskExportSettingsDto
from ProjectManagerSdk.models.tagcreatedto import TagCreateDto
from ProjectManagerSdk.models.tagdto import TagDto
from ProjectManagerSdk.models.tagupdatedto import TagUpdateDto
from ProjectManagerSdk.models.taskassigneedto import TaskAssigneeDto
from ProjectManagerSdk.models.taskcreatedto import TaskCreateDto
from ProjectManagerSdk.models.taskdto import TaskDto
from ProjectManagerSdk.models.taskfielddto import TaskFieldDto
from ProjectManagerSdk.models.taskfieldprojectdto import TaskFieldProjectDto
from ProjectManagerSdk.models.taskfieldvaluedto import TaskFieldValueDto
from ProjectManagerSdk.models.taskfieldvaluetaskdto import TaskFieldValueTaskDto
from ProjectManagerSdk.models.taskfiledto import TaskFileDto
from ProjectManagerSdk.models.taskmetadatasearchdto import TaskMetadataSearchDto
from ProjectManagerSdk.models.taskmetadataupdatedto import TaskMetadataUpdateDto
from ProjectManagerSdk.models.taskprioritydto import TaskPriorityDto
from ProjectManagerSdk.models.taskprojectdto import TaskProjectDto
from ProjectManagerSdk.models.taskstatuscreatedto import TaskStatusCreateDto
from ProjectManagerSdk.models.taskstatusdto import TaskStatusDto
from ProjectManagerSdk.models.taskstatusupdatedto import TaskStatusUpdateDto
from ProjectManagerSdk.models.tasktagdto import TaskTagDto
from ProjectManagerSdk.models.tasktodocreatedto import TaskTodoCreateDto
from ProjectManagerSdk.models.tasktododto import TaskTodoDto
from ProjectManagerSdk.models.tasktodoupdatedto import TaskTodoUpdateDto
from ProjectManagerSdk.models.taskupdatedto import TaskUpdateDto
from ProjectManagerSdk.models.timesheetadmintypedto import TimesheetAdminTypeDto
from ProjectManagerSdk.models.timesheetcreaterequestdto import TimesheetCreateRequestDto
from ProjectManagerSdk.models.timesheetdto import TimesheetDto
from ProjectManagerSdk.models.timesheetfiledto import TimesheetFileDto
from ProjectManagerSdk.models.timesheetprojectdto import TimeSheetProjectDto
from ProjectManagerSdk.models.timesheetresourcedto import TimesheetResourceDto
from ProjectManagerSdk.models.timesheetresponsedto import TimesheetResponseDto
from ProjectManagerSdk.models.timesheettaskdto import TimesheetTaskDto
from ProjectManagerSdk.models.timesheetupdaterequestdto import TimesheetUpdateRequestDto
from ProjectManagerSdk.models.updateprojectfieldvaluedto import UpdateProjectFieldValueDto
from ProjectManagerSdk.models.updaterequestdto import UpdateRequestDto
from ProjectManagerSdk.models.updateresourceskilldto import UpdateResourceSkillDto
from ProjectManagerSdk.models.updateresourceteamdto import UpdateResourceTeamDto
from ProjectManagerSdk.models.updatetaskfieldvaluedto import UpdateTaskFieldValueDto
from ProjectManagerSdk.models.usererror import UserError
from ProjectManagerSdk.models.userroledto import UserRoleDto
from ProjectManagerSdk.models.workspacedto import WorkSpaceDto
from ProjectManagerSdk.models.workspacejoindto import WorkSpaceJoinDto
from ProjectManagerSdk.models.workspacelinksdto import WorkSpaceLinksDto
from ProjectManagerSdk.models.workspacepermissionsdto import WorkSpacePermissionsDto
from ProjectManagerSdk.models.workspaceuserinfodto import WorkSpaceUserInfoDto
