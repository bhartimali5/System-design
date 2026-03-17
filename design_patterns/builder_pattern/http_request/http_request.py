class HttpRequest:
    def __init__(self):
        self.method = None
        self.url = None
        self.headers = {}
        self.query_params = {}      
        self.body = None

    def __str__(self):
        return (
            f"HttpRequest [\n"
            f"  method: {self.method},\n"
            f"  url: {self.url},\n"
            f"  headers: {self.headers},\n"
            f"  params: {self.query_params},\n"
            f"  body: {self.body}\n"
            f"]"
        )
