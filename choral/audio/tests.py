from django.test import TestCase

from .models import Artist

import uuid

class ArtistModelTests(TestCase):

    def test_000(self):
        first_name = str(uuid.uuid4())
        last_name = str(uuid.uuid4())
        music_brainz_id = str(uuid.uuid4())

        candidate = Artist(first_name = first_name, last_name = last_name, mb_id = music_brainz_id)
        self.assertEqual(candidate.first_name, first_name)
        self.assertEqual(candidate.last_name, last_name)
        self.assertEqual(candidate.mb_id, music_brainz_id)

        print(candidate)
