from django.db.models import Aggregate, CharField


class GroupConcat(Aggregate):
    function = 'ARRAY_AGG'
    template = '%(function)s(%(distinct)s%(expressions)s%(order_by)s)'

    def __init__(self, expression, distinct=False, order_by=False, **extra):
        super(GroupConcat, self).__init__(
            expression,
            distinct='DISTINCT ' if distinct else '',
            output_field=CharField(),
            order_by=' ORDER BY {}'.format(order_by) if order_by else '',
            **extra)
