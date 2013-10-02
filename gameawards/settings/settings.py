# Django settings for gameawards project.

import os, socket, ayah
from django.core.mail import send_mail

from gameawards.settings.common import *

#Initialization of Are you human
ayah.configure("15aaa63b65ead6b11342d1c7f349c68e875a3f16","5d736518475d70a969d57bf2caadb32ce7160500")

if socket.gethostname() == ("TheMatrix" or "Virus" or "xishan"):
    from gameawards.settings.dev import *
    
else:
    from gameawards.settings.prod import *
