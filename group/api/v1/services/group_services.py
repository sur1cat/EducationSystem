from django.utils import timezone

from group.models import Group


class GroupService:
    def __init__(self):
        self.queryset = Group.objects.all()

    def distribute_users_to_groups(self, product, user):
        if product.start_date > timezone.now():
            self.rearrange_users_in_groups(product)
        else:
            groups = self.queryset.filter(product=product).order_by('users__count')

            for group in groups:
                if group.users.count() < product.max_users:
                    group.users.add(user)
                    break
            else:
                self.rearrange_users_in_groups(product)

    def rearrange_users_in_groups(self, product):
        groups = self.queryset.filter(product=product).order_by('users__count')

        prev_group = None

        for group in groups:
            if prev_group:
                diff = group.users.count() - prev_group.users.count()

                if diff > 1:
                    user_to_move = group.users.first()
                    group.users.remove(user_to_move)
                    prev_group.users.add(user_to_move)

            prev_group = group
