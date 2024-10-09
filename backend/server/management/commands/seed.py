from django.core.management.base import BaseCommand
from server.models import CustomUser, EnvironmentalData  # Substitua pelo seu modelo de usuário personalizado

class Command(BaseCommand):
    help = 'Apaga todos os dados do banco de dados e popula com usuários e dados iniciais'

    def handle(self, *args, **kwargs):
        ########################################################################
        # Apaga todos os usuários existentes
        CustomUser.objects.all().delete()
        self.stdout.write(self.style.WARNING('Todos os usuários foram apagados.'))

        ########################################################################
        # Criação de 3 usuários com diferentes níveis de acesso
        CustomUser.objects.create_user(
            username='usuario',
            email='usuario@example.com',
            password='senha123',
            access_level=1  # Nível de acesso 1
        )
        CustomUser.objects.create_user(
            username='Diretor',
            email='Diretor@example.com',
            password='senha123',
            access_level=2  # Nível de acesso 2
        )
        CustomUser.objects.create_user(
            username='Ministro',
            email='Ministro@example.com',
            password='senha123',
            access_level=3  # Nível de acesso 3
        )

        ########################################################################
        # Criação de um superusuário (admin)
        CustomUser.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123',
            access_level=3  # Superusuário com nível de acesso 3
        )

        self.stdout.write(self.style.SUCCESS('Usuários inseridos com sucesso!'))


        ########################################################################
        # Apagar todas as propriedades existentes
        EnvironmentalData.objects.all().delete()
        self.stdout.write(self.style.WARNING('Todos os dados de propriedades foram apagados.'))

        ########################################################################
        # Criar propriedades com diferentes níveis de acesso
        EnvironmentalData.objects.create(
            propriedade='Fazenda Rio Claro',
            responsavel='João Silva',
            content='Propriedade com uso de pesticidas proibidos.',
            required_access_level=1
        )
        EnvironmentalData.objects.create(
            propriedade='Sítio Bela Vista',
            responsavel='Maria Souza',
            content='Propriedade com contaminação de lençol freático.',
            required_access_level=2
        )
        EnvironmentalData.objects.create(
            propriedade='Chácara Paraíso',
            responsavel='Carlos Pereira',
            content='Uso ilegal de agrotóxicos altamente tóxicos.',
            required_access_level=3
        )
        EnvironmentalData.objects.create(
            propriedade='Fazenda São Jorge',
            responsavel='Ana Oliveira',
            content='Uso de fertilizantes químicos.',
            required_access_level=1
        )
        EnvironmentalData.objects.create(
            propriedade='Sítio Esperança',
            responsavel='Rafael Mendes',
            content='Aditivos não regulamentados utilizados.',
            required_access_level=1
        )
        EnvironmentalData.objects.create(
            propriedade='Chácara do Lago',
            responsavel='Fernanda Lima',
            content='Contaminação por agrotóxicos.',
            required_access_level=2
        )
        EnvironmentalData.objects.create(
            propriedade='Fazenda Verde Vida',
            responsavel='Luiz Gomes',
            content='Uso de herbicidas proibidos.',
            required_access_level=2
        )
        EnvironmentalData.objects.create(
            propriedade='Sítio da Serra',
            responsavel='Patrícia Costa',
            content='Utilização de produtos ilegais na colheita.',
            required_access_level=3
        )
        EnvironmentalData.objects.create(
            propriedade='Fazenda do Sol',
            responsavel='Roberto Alves',
            content='Aditivos não autorizados em cultivos.',
            required_access_level=1
        )
        EnvironmentalData.objects.create(
            propriedade='Sítio da Alegria',
            responsavel='Mariana Teixeira',
            content='Uso de substâncias perigosas.',
            required_access_level=3
        )
        EnvironmentalData.objects.create(
            propriedade='Chácara do Futuro',
            responsavel='Eduardo Ribeiro',
            content='Propriedade em conformidade, mas com riscos potenciais.',
            required_access_level=2
        )

        self.stdout.write(self.style.SUCCESS('Propriedades inseridas com sucesso!'))
