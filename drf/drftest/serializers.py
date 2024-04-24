import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = "__all__"






# def encode():
#     model = WomenModel('Анджелина Джоли', 'Content: Анджелина Джоли')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"\xd0\x90\xd0\xbd\xd0\xb4\xd0\xb6\xd0\xb5\xd0\xbb\xd0\xb8\xd0\xbd\xd0\xb0 \xd0\x94\xd0\xb6\xd0\xbe\xd0\xbb\xd0\xb8","content":"Content: \xd0\x90\xd0\xbd\xd0\xb4\xd0\xb6\xd0\xb5\xd0\xbb\xd0\xb8\xd0\xbd\xd0\xb0 \xd0\x94\xd0\xb6\xd0\xbe\xd0\xbb\xd0\xb8"}')
#     data = JSONParser().parse(stream)
#     serializers = WomenSerializer(data=data)
#     serializers.is_valid()
#     print(serializers.validated_data)
