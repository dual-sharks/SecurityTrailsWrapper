from src.securitytrails_wrapper.utils.helpers import _read_csv, _column_to_list, _drop_na
import ipaddress
import pandas as pd


def get_recon_data(csv_file, column_name):
    df = _drop_na(_read_csv(csv_file), column_name)
    return df


def scan_host_list(host_list, dns):
    results = []

    for idx, row in host_list.iterrows():
        current_ip = str(row['ip']).strip()
        host = row['Host']

        try:
            ipaddress.ip_address(host)
            continue
        except ValueError:
            pass

        df = dns.get_current_dns(host)
        if df is not None and not df.empty and 'ip' in df.columns and len(df['ip']) > 0:
            fetched_ip = str(df['ip'].iloc[0]).strip()
            if current_ip != fetched_ip:
                results.append({'Host': host, 'Old IP': current_ip, 'New IP': fetched_ip})
        else:
            results.append({'Host': host, 'Old IP': current_ip, 'New IP': 'No data returned'})

    results_df = pd.DataFrame(results)
    return results_df
