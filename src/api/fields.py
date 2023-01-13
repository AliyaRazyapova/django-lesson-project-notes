from rest_framework import serializers


class StdImageField(serializers.ImageField):
    def to_representation(self, value):
        """in api"""
        return self.get_variations_urls(value)

    def to_internal_value(self, data):
        """in python code"""
        return self.get_variations_urls(data)

    def get_variations_urls(self, object):
        return_object = {}

        if not object:
            return None

        field = object.field

        if not hasattr(field, 'variations'):
            return return_object
        variations = field.variations

        for key in variations.keys():
            if not hasattr(object, key):
                continue

            variation = getattr(object, key, None)
            if variation and hasattr(variation, 'url'):
                url = super(StdImageField, self).to_representation(variation)
                return_object[key] = url

        if hasattr(object, 'url'):
            url = super(StdImageField, self).to_representation(object)
            return_object['original'] = url

        return return_object
