import socks


api_id = 964617
api_hash = '68247a39c2c9de1dba45a8d576370b0c'


test_group_id = -213997592
dev_group_id = -1001280812832


proxies = [
    dict(proxy_type=socks.HTTP,
         addr='138.128.90.153',
         port=8000,
         username='Qu5nBm',
         password='1b1CsD'),
    (socks.HTTP, '51.158.68.133', 8811),
    (socks.SOCKS5, '46.161.40.104', 9001),
    (socks.SOCKS5, '69.4.86.194', 65082),
    (socks.SOCKS5, '35.198.187.178', 4444),
    (socks.SOCKS5, '192.169.249.15', 33972),
    (socks.SOCKS5, '35.246.215.166', 4444),
    (socks.SOCKS5, '35.198.109.101', 4444),
    (socks.SOCKS5, '35.198.121.110', 4444),
    (socks.SOCKS5, '35.246.171.18', 4444),
    (socks.SOCKS5, '35.246.255.14', 4444),
    (socks.SOCKS5, '136.244.81.26', 30766)
]


mime_types = {
    'rar': 'application/x-rar',
    'zip': 'application/zip',
    '7z': 'application/x-7z-compressed'
}


download_dir = 'downloads'