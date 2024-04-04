# src/securitytrails_wrapper/domain/domain_api.py

from ..base import SecurityTrailsBase


class DomainAPI(SecurityTrailsBase):
    def get_domain_details(self, domain):
        """Fetches detailed information about a given domain."""
        return self.make_request("GET", f"domain/{domain}")

    def list_subdomains(self, domain):
        """
        List subdomains for a given domain.

        Parameters:
        - domain: The domain for which to list subdomains.

        Returns:
        - A response object containing the list of subdomains.
        """
        endpoint = f"domain/{domain}/subdomains"
        response = self.make_request("GET", endpoint)
        return response
