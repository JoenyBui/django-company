"""
 *  PROTECTION ENGINEERING CONSULTANTS CONFIDENTIAL
 *
 *  [2014] - [2015] Protection Engineering Consultants
 *  All Rights Reserved.
 *
 * NOTICE:  All information contained herein is, and remains
 * the property of Protection Engineering Consultants and its suppliers,
 * if any.  The intellectual and technical concepts contained
 * herein are proprietary to Protection Engineering Consultants
 * and its suppliers and may be covered by U.S. and Foreign Patents,
 * patents in process, and are protected by trade secret or copyright law.
 * Dissemination of this information or reproduction of this material
 * is strictly forbidden unless prior written permission is obtained
 * from Protection Engineering Consultants.
"""

import uuid

from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers

from .models import Company, Employee

__author__ = 'jbui'


class UserSerializer(serializers.Serializer):
    """
    User serializer model.
    """
    username = serializers.CharField(allow_blank=False)
    first_name = serializers.CharField(max_length=30, allow_blank=True)
    last_name = serializers.CharField(max_length=30, allow_blank=True)
    email = serializers.EmailField(allow_blank=False)


class CompanySerializer(serializers.Serializer):
    """
    Window analysis module input file serializer.
    """
    public_id = serializers.UUIDField(default=uuid.uuid4)

    name = serializers.CharField(max_length=255)
    street = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=2)
    zipcode = serializers.IntegerField(default=12345)
    website = serializers.URLField(allow_blank=True)
    picture = serializers.ImageField()

    def to_representation(self, instance):
        ret = super(CompanySerializer, self).to_representation(instance)

        return ret

    def create(self, validated_data):
        """
        Create a new file entry.

        User must provide a valid folder UUID.
        """
        folder_id = validated_data.get('folder_id')
        name = validated_data.get('name')
        data = validated_data.get('data')
        file = validated_data.get('file')
        public_id = validated_data.get('public_id')

        try:
            folder = Company.objects.filter(public_id=folder_id).first()
        except ObjectDoesNotExist as e:
            folder = None

        if folder:
            user = self.context['request'].user

            return Company.objects.create(name=name,
                                           public_id=public_id,
                                           user=user,
                                           folder=folder,
                                           data=data,
                                           file=file)
        else:
            return None


class EmployeeSerializer(serializers.Serializer):
    """
    Window analysis module input file serializer.
    """
    public_id = serializers.UUIDField(default=uuid.uuid4)
    company_id = serializers.UUIDField()
    user_id = serializers.UUIDField()

    privilege = serializers.IntegerField(default=1)

    def to_representation(self, instance):
        ret = super(Employee, self).to_representation(instance)

        if instance.folder:
            ret["folder_id"] = instance.folder.public_id
        else:
            ret["folder_id"] = None

        return ret

    def create(self, validated_data):
        """
        Create a new file entry.

        User must provide a valid folder UUID.
        """
        company_id = validated_data.get('company_id')
        user_id = validated_data.get('user_id')
        public_id = validated_data.get('public_id')

        try:
            company = Company.objects.filter(public_id=company_id).first()
        except ObjectDoesNotExist as e:
            company = None

        try:
            user = User.objects.filter(public_id=user_id).first()
        except ObjectDoesNotExist as e:
            user = None

        if company and user:
            user = self.context['request'].user

            return Employee.objects.create(company=company,
                                           user=user)
        else:
            return None
