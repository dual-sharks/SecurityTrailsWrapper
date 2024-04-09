# src/securitytrails_wrapper/dns/dns_api.py

from ..base import SecurityTrailsBase
from datetime import datetime
import pandas as pd


class DNSAPI(SecurityTrailsBase):
    def list_dns_records(self, domain, record_type="a"):
        """Lists DNS records for a given domain and record type."""
        return self.make_request("GET", f"history/{domain}/dns/{record_type}")

    @staticmethod
    def _get_current_date_iso():
        """Helper method to get the current date in ISO format."""
        return datetime.utcnow().date().isoformat()

    def process_dns_records(self, dns_records):
        """Process DNS records to find and normalize the most recent record."""
        if dns_records and dns_records['records']:
            last_seen_record = dns_records['records'][0]['last_seen']
            current_date = self._get_current_date_iso()

            if last_seen_record >= current_date:
                record = dns_records['records'][0]
            else:
                record = None

            if record:
                df = pd.json_normalize(record, record_path=['values'],
                                       meta=['first_seen', 'last_seen', 'organizations', ['type']])
                df = df.explode('organizations')
                return df
        return None

    def get_current_dns(self, domain):
        dns_records = self.list_dns_records(domain)
        return self.process_dns_records(dns_records)
