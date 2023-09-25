from django.db import models

from df_cards.fields import (
    AvatarImageField,
    FullImageField,
    IconImageField,
    ThumbnailImageField,
)


class DescriptionMixin:
    description = models.TextField(blank=True, default="")


class SequenceMixin:
    sequence = models.PositiveIntegerField(default=0)


class ThumbnailMixin:
    thumbnail = ThumbnailImageField()


class IconMixin:
    icon = IconImageField()


class FullImageMixin:
    full_image = FullImageField()


class AvatarMixin:
    avatar = AvatarImageField()


class BaseCard(DescriptionMixin, SequenceMixin, models.Model):
    class Meta:
        abstract = True


class NamedCard(BaseCard):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True


class TitledCard(BaseCard):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        abstract = True
