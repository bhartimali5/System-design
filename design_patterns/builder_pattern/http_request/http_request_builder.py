## Using method chaining:
"""
Depends on the following factors:
1. construction sequence
2. repeated standard patterns(all params are same every time)
3. caller
"""
from design_patterns.builder_pattern.http_request.http_request import HttpRequest

class HttpRequestBuilder:
    VALID_METHODS = {"GET", "POST", "PUT", "DELETE"}
    BODY_ALLOWED = {"POST", "PUT"}           # ✅ body only for these

    def __init__(self):
        self._request = HttpRequest()

    def method(self, method: str) -> "HttpRequestBuilder":
        if method.upper() not in self.VALID_METHODS:
            raise ValueError(f"Invalid method: {method}")
        self._request.method = method.upper()
        return self                            # ✅ return self for chaining

    def url(self, url: str) -> "HttpRequestBuilder":
        self._request.url = url
        return self                            # ✅

    def header(self, key: str, value: str) -> "HttpRequestBuilder":
        self._request.headers[key] = value     # ✅ adds one header at a time
        return self

    def query_param(self, key: str, value: str) -> "HttpRequestBuilder":
        self._request.query_params[key] = value
        return self

    def body(self, body: dict) -> "HttpRequestBuilder":
        # validate body only allowed on POST and PUT
        if self._request.method not in self.BODY_ALLOWED:
            raise ValueError(
                f"Body not allowed for {self._request.method} requests. "
                f"Only {self.BODY_ALLOWED} can have a body."
            )
        self._request.body = body
        return self

    def build(self) -> HttpRequest:
        self._validate()
        return self._request

    def _validate(self):
        if not self._request.method:
            raise ValueError("Method is required")
        if not self._request.url:
            raise ValueError("URL is required")
