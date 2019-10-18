""" World's simplest Template engine. """

import string


class SuperFormatter(string.Formatter):
    """ World's simplest Template engine. """

    def format_field(self, value, format_spec):
        if format_spec.startswith('repeat:'):
            template = format_spec.partition(':')[-1]
            if isinstance(value, dict):
                value = value.items()
            return ''.join([self.format(template, item=item) for item in value])
        if format_spec == 'call':
            return value()
        if format_spec.startswith('if:'):
            return format_spec.partition(':')[-1] if value else ''
        return super(SuperFormatter, self).format_field(value, format_spec)
