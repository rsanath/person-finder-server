from rest_framework import viewsets
from .serializers import (
    ComplaintSerializer,
    SearcheeSerializer,
    SearcheeSampleSerializer,
    SearchSerializer,
    SearchResultSerializer
)
from .models import Complaint, Searchee, SearcheeSample, Search, SearchResult
from rest_framework.response import Response
from rest_framework.decorators import action
from cloud_storage.storage import upload_sample_image, upload_fir



class ComplaintViewSet(viewsets.ModelViewSet):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()

    @action(detail=False, methods=['POST'])
    def upload_fir(self, request, *args, **kwargs):
        file = request.data['image']
        url = upload_fir(file)
        return Response(url, 201)


class SearcheeViewSet(viewsets.ModelViewSet):
    serializer_class = SearcheeSerializer
    queryset = Searchee.objects.all()

    @action(detail=True, methods=['POST'])
    def upload_sample(self, request, *args, **kwargs):
        searchee = self.get_object()
        try:
            file = request.data['image']
            url = upload_sample_image(file)
            sample = SearcheeSample(searchee=searchee, image_url=url)
            sample.save()
        except KeyError:
            raise ParseError('Request has no resource file attached')
        return Response('uploaded', 200)

    @action(detail=True, methods=['GET'])
    def searches(self, request, *args, **kwargs):
        searchee = self.get_object()
        serializer = SearchSerializer(searchee.searches.all(), many=True, context={'request': request})
        
        return Response(serializer.data, 200)

    @action(detail=True, methods=['GET'])
    def samples(self, request, *args, **kwargs):
        searchee = self.get_object()
        searchee_samples = searchee.samples.all().values_list('image_url', flat=True)
        searchee_samples = list(searchee_samples)
        return Response(searchee_samples, 200)


class SearcheeSampleViewSet(viewsets.ModelViewSet):
    serializer_class = SearcheeSampleSerializer
    queryset = SearcheeSample.objects.all()


class SearchViewSet(viewsets.ModelViewSet):
    serializer_class = SearchSerializer
    queryset = Search.objects.all()

    @action(detail=True, methods=['GET'])
    def results(self, request, *args, **kwargs):
        search = self.get_object()
        results = search.results.all()
        
        serializer = SearchResultSerializer(results, many=True, context={'request': request})
        return Response(serializer.data, 200)


class SearchResultViewSet(viewsets.ModelViewSet):
    serializer_class = SearchResultSerializer
    queryset = SearchResult.objects.all()
