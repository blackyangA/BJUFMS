#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'document', views.DocumentFileViewSet)
router.register(r'account', views.AccountingFileViewSet)
router.register(r'physical', views.PhysicalFileViewSet)
router.register(r'electronic', views.ElectronicFileViewSet)
router.register(r'approval', views.ProjectApprovalInformationViewSet)
router.register(r'budget', views.BudgetInformationViewSet)
router.register(r'audit', views.AuditinformationViewSet)
router.register(r'launch', views.LaunchInformationViewSet)
router.register(r'acceptance', views.AcceptanceInformationViewSet)
router.register(r'management', views.ProjectManagementViewSet)

"""
approval 立项信息
budget 预算信息表
audit 审计信息
launch 启动信息
acceptance 验收信息
management 工程管理
"""

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
