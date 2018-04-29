from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe


class AdminImageWidget(AdminFileWidget):
    # Used in the admin screen to show images
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, 'url', None):
            url = value.url
            image = '<img style="max-height: 150px;" src="{}" />'.format(url)
            link = '<a href={} target="_blank">{}</a>'.format(url, image)
            output.append(link)
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
