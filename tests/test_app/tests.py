import io
import shutil
import tempfile
from typing import Tuple

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from PIL import Image

from df_cards.specs import ThumbnailImageSpec
from tests.test_app.models import Post


class PostModelTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.temp_dir = tempfile.mkdtemp()
        settings.MEDIA_ROOT = f"{self.temp_dir}/media/"

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)
        super().tearDown()
        settings.MEDIA_ROOT = ""

    def create_image(self, size: Tuple[int, int] = (2000, 2000)) -> SimpleUploadedFile:
        """Create a new image and return it."""
        img = Image.new("RGB", size)
        img_io = io.BytesIO()
        img.save(img_io, format="JPEG")
        img_content = img_io.getvalue()
        return SimpleUploadedFile(name="test.jpg", content=img_content)

    def test_thumbnail_resized_properly(self) -> None:
        # Replace below settings with actual thumbnail size setting

        # Create a new Post instance with an uploaded image
        uploaded_image = self.create_image()
        post = Post.objects.create(
            title="Test Post",
            thumbnail=uploaded_image,
        )

        # Open the saved thumbnail and check its size
        saved_thumbnail = Image.open(post.thumbnail.path)
        self.assertEqual(
            saved_thumbnail.size[0], ThumbnailImageSpec.processors[0].width
        )
        self.assertEqual(
            saved_thumbnail.size[1], ThumbnailImageSpec.processors[0].height
        )
