from rest_framework.schemas.openapi import AutoSchema


class CustomAutoSchema(AutoSchema):
    def get_tags(self, path, method):
        tags = super().get_tags(path, method)
        # Customize your tags if needed
        return tags

    def get_operation(self, path, method):
        operation = super().get_operation(path, method)
        operation['tags'] = self.get_tags(path, method)
        return operation
