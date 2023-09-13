from df_cards.models import FullImageMixin, ThumbnailMixin, TitledCard


class Post(ThumbnailMixin, FullImageMixin, TitledCard):  # type: ignore
    pass
