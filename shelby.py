from src.securitytrails_wrapper.utils.helpers import _read_csv, _column_to_list, _drop_na
import ipaddress


def get_recon_data(csv_file, column_name):
    df = _drop_na(_read_csv(csv_file), column_name)
    return df


def scan_host_list(host_list, dns_api):
    for idx, row in host_list.iterrows():
        current_ip = str(row['ip']).strip()
        host = row['Host']
        try:
            ipaddress.ip_address(host)
            print(f"Skipping IP address: {host}")
            continue
        except ValueError:
            pass

        df = dns_api.dns_bot(host)

        if df is not None and not df.empty and 'ip' in df.columns and len(df['ip']) > 0:
            fetched_ip = str(df['ip'].iloc[0]).strip()
            if current_ip == fetched_ip:
                pass
            else:
                print(f'Host: {host}')
                print(f'Old IP: {current_ip} New IP: {fetched_ip}')
                print('-----------------------------------')
        else:
            print(f"No data returned for host: {host}")
