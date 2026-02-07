from drf_spectacular.renderers import OpenApiJsonRenderer


class CustomOpenApiRenderer(OpenApiJsonRenderer):
    media_type = 'application/vnd.oai.openapi'
