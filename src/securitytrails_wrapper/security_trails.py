from src.securitytrails_wrapper.domain.domain_api import DomainAPI
from src.securitytrails_wrapper.dns.dns_api import DNSAPI

class SecurityTrails:
    def __init__(self, api_key):
        self.domain = DomainAPI(api_key=api_key)
        self.dns = DNSAPI(api_key=api_key)

    def get_domain_details(self, domain):
        return self.domain.get_domain_details(domain)

    def get_current_dns(self, domain):
        return self.dns.get_current_dns(domain)