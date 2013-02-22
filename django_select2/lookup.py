from .fields import ModelResultJsonMixin


class ModelResultJson(ModelResultJsonMixin):
    queryset = None

    def __init__(self, *args, **kwargs):
        self.queryset = kwargs.get('queryset')
        self.max_results = kwargs.get('max_results', 100)  # TODO: settings
        self.to_field_name = kwargs.get('to_field_name', 'pk')
        self.search_fields = kwargs.get('search_fields', [])


class CreateModelResultJson(ModelResultJson):
    def get_results(self, request, term, page, context):
        NO_ERR_RESP, has_more, res = super(CreateModelResultJson, self).get_results(request, term, page, context)
        if len(res) == 0:
            res = [(term, term,)]
        return NO_ERR_RESP, has_more, res


class LookupChannel(object):
    def __init__(self, *args, **kwargs):
        self.modelresultjson = ModelResultJson(*args, **kwargs)

    def label_from_instance(self, obj):
        return self.label_from_instance(obj)

    def extra_data_from_instance(self, obj):
        return self.modelresultjson.extra_data_from_instance(obj)

    def prepare_qs_params(self, *args, **kwargs):
        return self.modelresultjson.prepare_qs_params(*args, **kwargs)

    def get_results(self, *args, **kwargs):
        return self.modelresultjson.get_results(*args, **kwargs)


class CreateLookupChannel(LookupChannel):
    def __init__(self, *args, **kwargs):
        self.modelresultjson = CreateModelResultJson(*args, **kwargs)