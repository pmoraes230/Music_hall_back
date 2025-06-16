from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Setores, Cadeiras, Evento

@receiver(post_save, sender=Setores)
def create_chairs(sender, instance, created, **kwargs):
    if created:
        evento = instance.id_evento
        total_cadeiras = sum(setor.qtd_cadeira for setor in evento.setores_set.all())
        if total_cadeiras > evento.capacidade_pessoas:
            instance.delete()
            raise ValidationError(
                f"A soma de cadeiras ({total_cadeiras}) excede a capacidade do evento ({evento.capacidade_pessoas})."
            )

        qtd_cadeira = instance.qtd_cadeira
        rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']  # Extended row labels
        cols_per_row = max(1, (qtd_cadeira // len(rows)) + (1 if qtd_cadeira % len(rows) else 0))

        for i in range(qtd_cadeira):
            row = rows[i // cols_per_row] if i // cols_per_row < len(rows) else rows[-1]
            column = (i % cols_per_row) + 1
            Cadeiras.objects.create(
                id_setor=instance,
                status='available',
                row_assent=row,
                column_assent=str(column)
            )