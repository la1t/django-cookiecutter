from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema as YasgSwaggerAutoSchema
from rest_framework import status


def get_error_schema():
    return openapi.Schema(
        type=openapi.TYPE_ARRAY,
        items=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "code": openapi.Schema(type=openapi.TYPE_STRING),
                "detail": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
    )


class SwaggerAutoSchema(YasgSwaggerAutoSchema):
    def get_response_schemas(self, response_serializers):
        responses = super().get_response_schemas(response_serializers)

        default_serializer = self.get_view_serializer()
        if default_serializer:
            error_schema = self.get_error_schema(default_serializer)
            responses.setdefault(
                str(status.HTTP_400_BAD_REQUEST),
                openapi.Response(description="", schema=error_schema),
            )

        return responses

    def get_error_schema(self, serializer):
        schema_ref = self.serializer_to_schema(serializer)
        schema = schema_ref.resolve(self.components)

        error_properties = {
            property_key: get_error_schema() for property_key in schema.properties
        }
        error_properties.setdefault("non_field_errors", get_error_schema())

        error_schema = openapi.Schema(
            description="", type=openapi.TYPE_OBJECT, properties=error_properties
        )
        return error_schema
