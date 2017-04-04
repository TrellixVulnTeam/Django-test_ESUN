from django.test.utils import setup_test_environment
setup_test_environment()

from django.test import Client
# create an instance of the client for our use
client = Client()

# get a response from '/'
response = client.get('/')
# we should expect a 404 from that address
response.status_code
# 404
# on the other hand we should expect to find something at '/polls/'
# we'll use 'reverse()' rather than a hardcoded URL
from django.urls import reverse
response = client.get(reverse('polls:index'))
response.status_code
# 200
response.content
# b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#39;s up?</a></li>\n    \n    </ul>\n\n'
# If the following doesn't work, you probably omitted the call to
# setup_test_environment() described above
response.context['latest_question_list']
# <QuerySet [<Question: What's up?>]>