import random
import parameters
import urllib.parse
import string

from utils import chance

# This is a list of paths from Faker, plus a ton of paths I found
# or made up (from reasonable assumptions, e.g. `secure`).
uri_paths = [
    'app', 'main', 'wp-content', 'search', 'category', 'tag', 'categories',
    'tags', 'blog', 'posts', 'list', 'explore', 'health-check', 'ops',
    'public', 'signup', 'login', 'user', 'inventory', 'template', 'address',
    'client', 'merchant', 'purchase-order', 'job', 'quote', 'discipline',
    'line-item', 'market-partner', 'service-region', 'order', 'report',
    'file-asset', 'upload', 'quote-categories', 'invoices', 'discout',
    'push-notifications', 'push-notif', 'push-notification', 'invoice',
    'consulting', 'consultations', 'types', 'type', 'campaigns', 'campaign',
    'email', 'emails', 'email-subscription', 'clients', 'leads',
    'self-serve', 'validation', 'tickets', 'quotes', 'jobs', 'payments',
    'receipts', 'upload', 'reminders', 'appointment-reminder', 'addresses',
    'users', 'resource', 'profile', 'unique', 'session', 'sessions', 'logout',
    'matches', 'swipe', 'match', 'unmatch', 'list', 'chat', 'load',
    'conversation', 'conversations', 'send', 'message', 'reload', 'command',
    'zip', 'settings', 'setting', 'portal', 'articles', 'admin', 'foo', 'bar',
    'baz', 'bax', 'extra', 'extras', 'selector', 'function', 'fn', 'env',
    'environment', 'subscribe', 'unsubscribe', 'about-us', 'donate', 'species',
    'climate', 'innovation', 'take-action', 'adopt', 'share', 'sharer',
    'social', 'element', 'elevate', 'connect', 'drop', 'ip', 'news' 'impact',
    'stories', 'fr', 'en', 'zh', 'fre', 'eng', 'de', 'deu', 'fi', 'fin', 'ru',
    'rus', 'zho', 'chi', 'da', 'dan', 'm', 'mobile', 'wiki', 'docs', 'doc',
    'en-us', 'en-ca', 'en-gb', 'custom', 'customizer', 'api', 'lib', 'src',
    'v1', 'v2', 'v3', 'rs', 'rust', 'js', 'secure', 'download', 'downloads',
    'ftp', 'file', 'transfer', 'protocol', 'socket', 'help', 'idea', 'limit',
    'data', 'data:image', 'img', 'image', 'base64', 'convert', 'run', 'activate',
    'setup', 'call', 'tutorial', 'tut', 'consume', 'bandwidth', 'cb',
    'about', 'about:blank', 'blank', 'tag', 'allow', 'cors', 'pipe', 'slack',
    'store', 'purchase', 'price', 'buy', 'verify', 'validate', 'verification',
    'web-client', 'request', 'req', 'ext', 'extension', 'phone', 'date',
    'random', 'hints', 'invite', 'wishlist', 'images', 'find', 'locate', 'dir',
    'directory', 'launch', 'create', 'gen', 'time', 'video', 'stream', 'etc',
    'misc', 'log', 'logs', 'open', 'event', 'client_event', 'pageview', 'view',
    'home', 'cache', 'bundle', 'loader', 'fatigue', 'badge', 'counter',
    'include', 'support', 'supports', 'origin', 'format', 'tools', 'tmp',
    'temp', 'index', 'register', 'faq', 'terms', 'privacy', 'author', 'all',
    'post', 'homepage', 'expand', 'terminal', 'bookings', 'book', 'book-now',
    'delete', 'restore', 'enable', 'close', 'open', 'shop', 'store', 'extract',
    'assist', 'reader', 'providers', 'provisions', 'legal'
]


def gen_uri_useable():
    chosen_chars = []

    # Chose random characters for the URI string
    for _ in range(random.randint(1, parameters.max_val['uri_folder_length'])):
        # By default, the next character will be a random letter or number
        next_char_set = string.ascii_letters + string.digits

        # Adds a 10% chance of the next character coming from the 'printable'
        # character set
        if chance(parameters.frequency['uri_use_printable_char']):
            next_char_set = string.printable

        # Choose a character and append it to the string
        chosen_chars.append(random.choice(next_char_set))

    uri_string = ''.join(chosen_chars)
    # Convert to lowercase
    uri_string = uri_string.lower()
    # URI-encodes the string. `safe=''` forces it to convert the `/` character
    # to URI encoding as well (so that it can be used in querystrings)
    return urllib.parse.quote(uri_string, safe='')


def gen_path(test_mode=False):
    path_depth = random.randint(1, parameters.max_val['uri_path_depth'])

    if test_mode:
        # If for testing, generate a realistic URI from the paths above
        return '/'.join(random.sample(uri_paths, path_depth))
    else:
        folders = []
        
        for _ in range(path_depth):
            folders.append(gen_uri_useable())

        return '/'.join(folders)


uri_extensions = [
    '.html', '.html', '.html', '.htm', '.htm', '.php', '.php', '.jsp',
    '.asp', '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.js', '.java',
    '.py', '.rs', '.json'
]
