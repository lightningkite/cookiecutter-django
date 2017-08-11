from django.core.urlresolvers import reverse
from django.views.generic import RedirectView


class UserRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('home')
