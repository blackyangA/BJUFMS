#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
from django.db import models
from utils.audit_model import FullAuditMixin
from django.utils.translation import gettext_lazy as _

ProjectApprovalInformation = {
    'project_approval_id': '立项ID',
    'project_name': '项目名称',
    'application_unit': '申报单位',
    'project_fund_source': '项目资金来源',
    'project_leader': '项目负责人',
    'leader_call': '负责人电话',
    'project_location': '项目地点',
    'project_content': '项目内容',
    'project_declaration_amount': '项目申报金额',
    'project_type': '项目大类',
    'review_classification': '评审分级',
}


class ProjectApprovalInformationModel(FullAuditMixin):
    """
    立项信息表
    """
    project_approval_id = models.CharField(_('立项ID'), max_length=255, null=True)
    project_name = models.CharField(_('项目名称'), max_length=255, null=True)
    application_unit = models.CharField(_('申报单位'), max_length=255, null=True)
    project_fund_source = models.CharField(_('项目资金来源'), max_length=255, null=True)
    project_leader = models.CharField(_('项目负责人'), max_length=255, null=True)
    leader_call = models.CharField(_('负责人电话'), max_length=255, null=True)
    project_location = models.CharField(_('项目地点'), max_length=255, null=True)
    project_content = models.CharField(_('项目内容'), max_length=255, null=True)
    project_declaration_amount = models.CharField(_('项目申报金额'), max_length=255, null=True)
    project_type = models.CharField(_('项目大类'), max_length=255, null=True)
    review_classification = models.CharField(_('评审分级'), max_length=255, null=True)


BudgetInformation = {
    'budget_id': '预算ID',
    'capital_source': '资金来源',
    'meeting_minute_no': '会议纪要编号',
    'meeting_minute_name': '会议纪要名称',
    'entry_sorting': '项目排序',
    'supporting_budget': '配套预算',
    'approval_document_no': '批复文件编号',
    'approval_document_name': '批复文件名称',
    'project_type': '项目大类',
}


class BudgetInformationModel(FullAuditMixin):
    """
    预算信息表
    """
    budget_id = models.CharField(_('预算ID'), max_length=255, null=True)
    capital_source = models.CharField(_('资金来源'), max_length=255, null=True)
    meeting_minute_no = models.CharField(_('会议纪要编号'), max_length=255, null=True)
    meeting_minute_name = models.CharField(_('会议纪要名称'), max_length=255, null=True)
    entry_sorting = models.CharField(_('项目排序'), max_length=255, null=True)
    supporting_budget = models.CharField(_('配套预算'), max_length=255, null=True)
    approval_document_no = models.CharField(_('批复文件编号'), max_length=255, null=True)
    approval_document_name = models.CharField(_('批复文件名称'), max_length=255, null=True)
    project_type = models.CharField(_('项目大类'), max_length=255, null=True)


Auditinformation = {
    'audit_no': '审计编号',
    'closing_cost': '结算费用',
    'complete_time': '竣工时间',
    'review_time': '送审时间',
    'review_amount': '送审金额',
    'setting_time': '审定时间',
    'setting_amount': '审定金额',
    'audit_report_no': '审计报告编号',
}


class AuditinformationModel(FullAuditMixin):
    """
    审计信息表
    """
    audit_no = models.CharField(_('审计编号'), max_length=255, null=True)
    closing_cost = models.CharField(_('结算费用'), max_length=255, null=True)
    complete_time = models.CharField(_('竣工时间'), max_length=255, null=True)
    review_time = models.CharField(_('送审时间'), max_length=255, null=True)
    review_amount = models.CharField(_('送审金额'), max_length=255, null=True)
    setting_time = models.CharField(_('审定时间'), max_length=255, null=True)
    setting_amount = models.CharField(_('审定金额'), max_length=255, null=True)
    audit_report_no = models.CharField(_('审计报告编号'), max_length=255, null=True)


LaunchInformation = {
    'project_id': '项目ID',
    'capital_source': '资金来源',
    'project_type': '项目大类',
    'launch_time': '启动时间',
}


class LaunchInformationModel(FullAuditMixin):
    """
    启动信息表
    """
    project_id = models.CharField(_('项目ID'), max_length=255, null=True)
    capital_source = models.CharField(_('资金来源'), max_length=255, null=True)
    project_type = models.CharField(_('项目大类'), max_length=255, null=True)
    launch_time = models.CharField(_('启动时间'), max_length=255, null=True)


AcceptanceInformation = {
    'budget_id': '四方验收单编号',
    'capital_source': '四方验收日期',
    'meeting_minute_no': '特种验收单编号',
    'meeting_minute_name': '特种验收日期',
    'entry_sorting': '建委验收单编号',
    'supporting_budget': '建委验收日期',
}


class AcceptanceInformationModel(FullAuditMixin):
    """
    验收信息表
    """
    acceptance_id = models.CharField(_('四方验收单编号'), max_length=255, null=True)
    capital_source = models.CharField(_('四方验收日期'), max_length=255, null=True)
    meeting_minute_no = models.CharField(_('特种验收单编号'), max_length=255, null=True)
    meeting_minute_name = models.CharField(_('特种验收日期'), max_length=255, null=True)
    entry_sorting = models.CharField(_('建委验收单编号'), max_length=255, null=True)
    supporting_budget = models.CharField(_('建委验收日期'), max_length=255, null=True)


ProjectManagement = {
    'engineering_record_sheet_no': '工程记录单编号',
    'engineering_record_sheet_name': '工程记录单名称',
    'engineering_record_sheet_amount': '工程记录单数量',
    'engineering_record_sheet_money': '工程记录单金额',
    'major_design_no': '重大决策文件编号',
    'supervision_information': '监理资料编号',
    'flow_sheet_filed': '流程单是否归档',
}


class ProjectManagementModel(FullAuditMixin):
    """
    工程管理表
    """
    engineering_record_sheet_no = models.CharField(_('工程记录单编号'), max_length=255, null=True)
    engineering_record_sheet_name = models.CharField(_('工程记录单名称'), max_length=255, null=True)
    engineering_record_sheet_amount = models.CharField(_('工程记录单数量'), max_length=255, null=True)
    engineering_record_sheet_money = models.CharField(_('工程记录单金额'), max_length=255, null=True)
    major_design_no = models.CharField(_('重大决策文件编号'), max_length=255, null=True)
    supervision_information = models.CharField(_('监理资料编号'), max_length=255, null=True)
    flow_sheet_filed = models.CharField(_('流程单是否归档'), max_length=255, null=True)


class DocumentFileModel(FullAuditMixin):
    """
    文书档案 DocumentFile
    """

    text = models.TextField(_('原文'), null=True, )
    file_no = models.CharField(_('案卷级档号'), max_length=255, null=True, )
    title = models.CharField(_('题名'), max_length=255, null=True, )
    all_sovereign = models.IntegerField(_('全宗号'), null=True, default=0)
    ecn = models.CharField(_('实体分类号'), max_length=255, null=True, )
    catalogue_no = models.IntegerField(_('目录号'), null=True, default=0)
    case_file_no = models.IntegerField(_('案卷号'), null=True, default=0)
    start_dt = models.DateField(_('文件开始时间'), null=True)
    end_dt = models.DateField(_('文件结束时间'), null=True)
    total_pages = models.IntegerField(_('文件总页数'), null=True, default=0)
    poc = models.CharField(_('保管期限'), max_length=255, null=True, )

    class Meta:
        ordering = ('-id',)


class AccountingFileModel(FullAuditMixin):
    """
    会计档案 AccountingFile
    """

    text = models.TextField(_('原文'), null=True, )
    file_no = models.CharField(_('案卷级档号'), max_length=255, null=True, )
    title = models.CharField(_('题名'), max_length=255, null=True, )
    all_sovereign = models.IntegerField(_('全宗号'), null=True, default=0)
    ecn = models.CharField(_('实体分类号'), max_length=255, null=True, )
    catalogue_no = models.IntegerField(_('目录号'), null=True, default=0)
    case_file_no = models.IntegerField(_('案卷号'), null=True, default=0)
    start_dt = models.DateField(_('文件开始时间'), null=True)
    end_dt = models.DateField(_('文件结束时间'), null=True)
    total_pages = models.IntegerField(_('文件总页数'), null=True, default=0)
    poc = models.CharField(_('保管期限'), max_length=255, null=True, )

    class Meta:
        ordering = ('-id',)


class PhysicalFileModel(FullAuditMixin):
    """
    实物档案 PhysicalFile
    """

    text = models.TextField(_('原文'), null=True, )
    file_no = models.CharField(_('案卷级档号'), max_length=255, null=True, )
    title = models.CharField(_('题名'), max_length=255, null=True, )
    all_sovereign = models.IntegerField(_('全宗号'), null=True, default=0)
    ecn = models.CharField(_('实体分类号'), max_length=255, null=True, )
    catalogue_no = models.IntegerField(_('目录号'), null=True, default=0)
    case_file_no = models.IntegerField(_('案卷号'), null=True, default=0)
    start_dt = models.DateField(_('文件开始时间'), null=True)
    end_dt = models.DateField(_('文件结束时间'), null=True)
    total_pages = models.IntegerField(_('文件总页数'), null=True, default=0)
    poc = models.CharField(_('保管期限'), max_length=255, null=True, )

    class Meta:
        ordering = ('-id',)


class ElectronicFileModel(FullAuditMixin):
    """
    电子档案 ElectronicFile
    """

    text = models.TextField(_('原文'), null=True, )
    file_no = models.CharField(_('案卷级档号'), max_length=255, null=True, )
    title = models.CharField(_('题名'), max_length=255, null=True, )
    all_sovereign = models.IntegerField(_('全宗号'), null=True, default=0)
    ecn = models.CharField(_('实体分类号'), max_length=255, null=True, )
    catalogue_no = models.IntegerField(_('目录号'), null=True, default=0)
    case_file_no = models.IntegerField(_('案卷号'), null=True, default=0)
    start_dt = models.DateField(_('文件开始时间'), null=True)
    end_dt = models.DateField(_('文件结束时间'), null=True)
    total_pages = models.IntegerField(_('文件总页数'), null=True, default=0)
    poc = models.CharField(_('保管期限'), max_length=255, null=True, )

    class Meta:
        ordering = ('-id',)
