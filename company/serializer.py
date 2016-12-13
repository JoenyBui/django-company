
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
    public_id = serializers.UUIDField(default=uuid.uuid4, read_only=True)

    name = serializers.CharField(max_length=255)
    street = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    zipcode = serializers.IntegerField(default=12345)
    website = serializers.URLField(allow_blank=True, allow_null=True, required=False)
    picture = serializers.ImageField(allow_empty_file=True, use_url=False)

    def to_representation(self, instance):
        ret = super(CompanySerializer, self).to_representation(instance)

        return ret

    def create(self, validated_data):
        """
        Create a new file entry.

        User must provide a valid folder UUID.
        """
        name = validated_data.get('name')
        street = validated_data.get('street')
        city = validated_data.get('city')
        state = validated_data.get('state')
        zipcode = validated_data.get('zipcode')
        website = validated_data.get('website')
        # picture = validated_data.get('picture')

        return Company.objects.create(name=name, street=street, city=city, state=state, zipcode=zipcode, website=website)


class EmployeeSerializer(serializers.Serializer):
    """
    Window analysis module input file serializer.
    """
    public_id = serializers.UUIDField(default=uuid.uuid4, read_only=True)
    company_id = serializers.UUIDField()
    # user_id = serializers.UUIDField()

    privilege = serializers.IntegerField(default=1)

    def to_representation(self, instance):
        ret = super(EmployeeSerializer, self).to_representation(instance)

        if not ret:
            return None

        if instance.company:
            ret["company_id"] = instance.company.public_id
        else:
            ret["company_id"] = None

        return ret

    def create(self, validated_data):
        """
        Create a new file entry.

        User must provide a valid folder UUID.
        """
        company_id = validated_data.get('company_id')
        public_id = validated_data.get('public_id')

        try:
            company = Company.objects.filter(public_id=company_id).first()
        except ObjectDoesNotExist as e:
            company = None

        try:
            user = User.objects.filter(public_id=public_id).first()
        except ObjectDoesNotExist as e:
            user = None

        if company and user:
            user = self.context['request'].user

            return Employee.objects.create(company=company,
                                           user=user)
        else:
            return None
