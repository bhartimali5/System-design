from design_patterns.builder_pattern.http_request.http_request_builder import HttpRequestBuilder

if __name__ == "__main__":

    # GET request
    get_request = (
        HttpRequestBuilder()
        .method("GET")
        .url("https://api.example.com/users")
        .header("Authorization", "Bearer token123")
        .query_param("page", "1")
        .query_param("limit", "10")
        .build()
    )
    print(get_request)

    # POST request
    post_request = (
        HttpRequestBuilder()
        .method("POST")
        .url("https://api.example.com/users")
        .header("Content-Type", "application/json")
        .body({"name": "Rahul", "email": "rahul@example.com"})
        .build()
    )
    print(post_request)

    # DELETE request
    delete_request = (
        HttpRequestBuilder()
        .method("DELETE")
        .url("https://api.example.com/users/1")
        .header("Authorization", "Bearer token123")
        .build()
    )
    print(delete_request)

    # Invalid — body on GET 
    try:
        invalid = (
            HttpRequestBuilder()
            .method("GET")
            .url("https://api.example.com/users")
            .body({"name": "Rahul"})
            .build()
        )
    except ValueError as e:
        print(f"\nCaught error: {e}")

    # Invalid — no URL 
    try:
        invalid = (
            HttpRequestBuilder()
            .method("POST")
            .build()
        )
    except ValueError as e:
        print(f"Caught error: {e}")