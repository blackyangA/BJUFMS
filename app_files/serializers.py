#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
import logging

from rest_framework import serializers

from utils.audit_serializer import AuditSerializer
from .models import DocumentFileModel, AccountingFileModel, PhysicalFileModel, ElectronicFileModel

logger = logging.getLogger(__name__)


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
