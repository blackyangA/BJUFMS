#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
import logging

from rest_framework import serializers

from utils.audit_serializer import AuditSerializer
from .models import (DocumentFileModel, AccountingFileModel, PhysicalFileModel, ElectronicFileModel,
                     ProjectApprovalInformationModel, BudgetInformationModel, AuditinformationModel,
                     LaunchInformationModel, AcceptanceInformationModel, ProjectManagementModel)

logger = logging.getLogger(__name__)


class ProjectApprovalInformationSerializer(AuditSerializer, serializers.ModelSerializer):
    class Meta:
        model = ProjectApprovalInformationModel
        fields = "__all__"


class BudgetInformationSerializer(AuditSerializer, serializers.ModelSerializer):
    class Meta:
        model = BudgetInformationModel
        fields = "__all__"


class AuditinformationSerializer(AuditSerializer, serializers.ModelSerializer):
    class Meta:
        model = AuditinformationModel
        fields = "__all__"


class LaunchInformationSerializer(AuditSerializer, serializers.ModelSerializer):
    class Meta:
        model = LaunchInformationModel
        fields = "__all__"


class AcceptanceInformationSerializer(AuditSerializer, serializers.ModelSerializer):
    class Meta:
        model = AcceptanceInformationModel
        fields = "__all__"


class ProjectManagementSerializer(AuditSerializer, serializers.ModelSerializer):
    class Meta:
        model = ProjectManagementModel
        fields = "__all__"


class DocumentFileSerializer(AuditSerializer, serializers.ModelSerializer):
    class Meta:
        model = DocumentFileModel
        fields = "__all__"


class AccountingFileSerializer(AuditSerializer, serializers.ModelSerializer):
    class Meta:
        model = AccountingFileModel
        fields = '__all__'


class PhysicalFileSerializer(AuditSerializer, serializers.ModelSerializer):
    class Meta:
        model = PhysicalFileModel
        fields = '__all__'


class ElectronicFileSerializer(AuditSerializer, serializers.ModelSerializer):
    class Meta:
        model = ElectronicFileModel
        fields = '__all__'
