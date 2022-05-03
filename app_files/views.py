#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
import logging

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from utils.permission import ReadOnly
from .models import (DocumentFileModel, AccountingFileModel, PhysicalFileModel, ElectronicFileModel,
                     ProjectApprovalInformationModel, BudgetInformationModel, AuditinformationModel,
                     LaunchInformationModel, AcceptanceInformationModel, ProjectManagementModel)
from .serializers import (DocumentFileSerializer, AccountingFileSerializer, PhysicalFileSerializer, \
                          ElectronicFileSerializer, ProjectApprovalInformationSerializer, BudgetInformationSerializer,
                          AuditinformationSerializer, LaunchInformationSerializer, AcceptanceInformationSerializer,
                          ProjectManagementSerializer)

logger = logging.getLogger(__name__)


class ProjectApprovalInformationViewSet(ModelViewSet):
    """
    立项信息表
    """
    queryset = ProjectApprovalInformationModel.objects.all()
    serializer_class = ProjectApprovalInformationSerializer
    permission_classes = [permissions.IsAdminUser | (ReadOnly & permissions.IsAuthenticated)]


class BudgetInformationViewSet(ModelViewSet):
    """
    预算信息表
    """
    queryset = BudgetInformationModel.objects.all()
    serializer_class = BudgetInformationSerializer
    permission_classes = [permissions.IsAdminUser | (ReadOnly & permissions.IsAuthenticated)]


class AuditinformationViewSet(ModelViewSet):
    """
    审计信息表
    """
    queryset = AuditinformationModel.objects.all()
    serializer_class = AuditinformationSerializer
    permission_classes = [permissions.IsAdminUser | (ReadOnly & permissions.IsAuthenticated)]


class LaunchInformationViewSet(ModelViewSet):
    """
    启动信息表
    """
    queryset = LaunchInformationModel.objects.all()
    serializer_class = LaunchInformationSerializer
    permission_classes = [permissions.IsAdminUser | (ReadOnly & permissions.IsAuthenticated)]


class AcceptanceInformationViewSet(ModelViewSet):
    """
    验收信息表
    """
    queryset = AcceptanceInformationModel.objects.all()
    serializer_class = AcceptanceInformationSerializer
    permission_classes = [permissions.IsAdminUser | (ReadOnly & permissions.IsAuthenticated)]


class ProjectManagementViewSet(ModelViewSet):
    """
    工程管理表
    """
    queryset = ProjectManagementModel.objects.all()
    serializer_class = ProjectManagementSerializer
    permission_classes = [permissions.IsAdminUser | (ReadOnly & permissions.IsAuthenticated)]


class DocumentFileViewSet(ModelViewSet):
    """
    文书档案 DocumentFile
    """
    queryset = DocumentFileModel.objects.all()
    serializer_class = DocumentFileSerializer
    permission_classes = [permissions.IsAdminUser | (ReadOnly & permissions.IsAuthenticated)]

    def create(self, request, *args, **kwargs):
        print(f"create data:{request.data}")
        return super(DocumentFileViewSet, self).create(request, *args, **kwargs)


class AccountingFileViewSet(ModelViewSet):
    """
    会计档案 AccountingFile
    """
    queryset = AccountingFileModel.objects.all()
    serializer_class = AccountingFileSerializer
    permission_classes = [permissions.IsAdminUser | (ReadOnly & permissions.IsAuthenticated)]


class PhysicalFileViewSet(ModelViewSet):
    """
    实物档案 PhysicalFile
    """
    queryset = PhysicalFileModel.objects.all()
    serializer_class = PhysicalFileSerializer
    permission_classes = [permissions.IsAdminUser | (ReadOnly & permissions.IsAuthenticated)]


class ElectronicFileViewSet(ModelViewSet):
    """
    电子档案 ElectronicFile
    """
    queryset = ElectronicFileModel.objects.all()
    serializer_class = ElectronicFileSerializer
    permission_classes = [permissions.IsAdminUser | (ReadOnly & permissions.IsAuthenticated)]
