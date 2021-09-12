try:
    import json
except ImportError:
    import simplejson as json
import urllib.request
from functools import reduce


def reducer(stats, lang):
    if lang:
        stats[lang] = stats.setdefault(lang, 0) + 1
    return stats


user = "saultyevil"
repos = json.loads(urllib.request.urlopen(
    u'https://api.github.com/users/%s/repos?per_page=100' % user).read())
lang_stats = reduce(reducer, (repo["language"] for repo in repos), {})
for lang in sorted(lang_stats, key=lambda l: lang_stats[l], reverse=True):
    print("{:18} {:18}".format(lang, str(lang_stats[lang])))
