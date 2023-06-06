from api.models import Project, Role, RoleMapping, User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Non-interactively create a rolemapping'

    @classmethod
    def add_arguments(cls, parser):
        parser.add_argument('--rolename', default=None,
                            help='The name of the role.')
        parser.add_argument('--username', default=None,
                            help='The name of the user.')
        parser.add_argument('--projectname', default=None,
                            help='The name of the project.')

    def handle(self, *args, **options):
        rolename = options.get('rolename')
        username = options.get('username')
        projectname = options.get('projectname')

        if not rolename or not username or not projectname:
            raise CommandError('--rolename  --projectname  --username are required for the rolemapping')

        try:
            role = Role.objects.get(name=rolename)
            user = User.objects.get(username=username)
            project = Project.objects.get(name=projectname)
            rolemapping = RoleMapping.objects.create(role_id=role.id, user_id=user.id, project_id=project.id)
        except Exception as ex:
            self.stderr.write(
                self.style.ERROR(
                    f'Error occurred while creating rolemapping "{ex}"'
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f'Rolemapping created successfully "{rolemapping.id}"'
                )
            )
