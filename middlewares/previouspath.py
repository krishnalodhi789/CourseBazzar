class PreviousPathMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Store the current path as the previous path in the session
        request.session['previous_path'] = request.path
        response = self.get_response(request)
        return response