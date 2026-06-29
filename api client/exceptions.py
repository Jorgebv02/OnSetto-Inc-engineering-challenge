"""
I think perhaps this module can be re-used later somehow, for now it just contains the exceptions that the API client can raise.
"""
class AuthenticationError(Exception):
    pass

class MFAError(Exception):
    pass

class ValidationError(Exception):
    pass

class RateLimitError(Exception):
    pass