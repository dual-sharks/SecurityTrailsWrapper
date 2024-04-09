# src/securitytrails_wrapper/domain/domain_api.py

from ..base import SecurityTrailsBase
import time
import pandas as pd

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
        if response:
            return response.get('subdomains', [])
        return []

    def get_ips_for_subdomains(self, domain):
        subdomains = self.list_subdomains(domain)
        rows = []
        for subdomain in subdomains:
            time.sleep(.1)
            sub = f'{subdomain}.{domain}'
            print(sub)
            data = self.get_domain_details(sub)
            if not data['current_dns']['a'] == {}:
                vals = data['current_dns']['a']
                row_data = {
                    'first_seen': vals['first_seen'],
                    'domain': domain,
                    'subdomain': subdomain,
                    'ip': vals['values'][0]['ip'],
                    'ip_org': vals['values'][0]['ip_organization'],

                }
                rows.append(row_data)
            else:
                row_data = {
                    'first_seen': None,
                    'ip': None,
                    'ip_org': None,
                }
                rows.append(row_data)
        # TODO: assert the amount of rows is equal to the amount of subdomains -- len(subdomains) == len(rows)
        return pd.DataFrame(rows)