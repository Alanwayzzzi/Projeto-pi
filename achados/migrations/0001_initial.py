import achados.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Sala",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=80, verbose_name="nome da sala")),
                ("descricao", models.CharField(blank=True, max_length=200, verbose_name="descrição")),
                ("codigo", models.CharField(default=achados.models.gerar_codigo, max_length=12, unique=True)),
                ("criada_em", models.DateTimeField(auto_now_add=True)),
                ("criador", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="salas_criadas", to=settings.AUTH_USER_MODEL)),
                ("membros", models.ManyToManyField(blank=True, related_name="salas", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-criada_em"]},
        ),
        migrations.CreateModel(
            name="Objeto",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100, verbose_name="objeto")),
                ("descricao", models.TextField(blank=True, verbose_name="descrição")),
                ("local_encontrado", models.CharField(blank=True, max_length=100, verbose_name="onde foi encontrado")),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                ("adicionado_por", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="objetos_adicionados", to=settings.AUTH_USER_MODEL)),
                ("sala", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="objetos", to="achados.sala")),
            ],
            options={"ordering": ["-criado_em"]},
        ),
    ]
