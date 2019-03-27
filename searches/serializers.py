from rest_framework import serializers
from .models import Complaint, Searchee, SearcheeSample, Search, SearchResult


class ComplaintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Complaint
        fields = (
            'url',
            'name',
            'doi',
            'poi',
            'fir',
            'status',
            'status_msg',
            'created_at',
            'updated_at',
            'submitter',
            'searchees')


class SearcheeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Searchee
        fields = (
            'url',
            'full_name',
            'dob',
            'sex',
            'height_cm',
            'weight_kg',
            'skin_tone',
            'created_at',
            'updated_at',
            'complaint',
            'samples',
            'searches'
        )


class SearcheeSampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SearcheeSample
        fields = serializers.ALL_FIELDS


class SearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Search
        fields = (
            'url',
            'name',
            'video',
            'location',
            'lat',
            'long',
            'status',
            'progress',
            'created_at',
            'updated_at',
            'searchee',
            'results'
        )


class SearchResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SearchResult
        fields = serializers.ALL_FIELDS
