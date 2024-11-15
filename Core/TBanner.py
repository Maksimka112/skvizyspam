from colorama import Fore



_banner = '''
SKVIZY_SPAM = Bomber - SMS, CALL
MIX - together sms & call'''



def banner(host, port):
    print(Fore.RED + _banner)
    print(f'http://{host}:{port}')