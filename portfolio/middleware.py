"""Baca bahasa pilihan dari session, taruh di request.LANG ('id' default)."""


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = request.session.get('lang', 'id')
        request.LANG = lang if lang in ('id', 'en') else 'id'
        return self.get_response(request)
