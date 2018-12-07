"""User View tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py

import os

from unittest import TestCase

from models import db, User, Message, FollowersFollowee

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

CURR_USER_KEY = "curr_user"


class UserViewTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        FollowersFollowee.query.delete()

        self.user = User.signup(
            email="test3@test.com",
            username="testuser3",
            password="HASHED_PASSWORD3",
            image_url="/static/images/default-pic.png")

        db.session.commit()

        self.client = app.test_client()
        app.config['Testing'] = True

    def test_homepage(self):
        """Test homepage."""

        with self.client:
            response = self.client.get("/")

            # test for successful response code
            self.assertEqual(response.status_code, 200)

            # test for homepage for anonymous user
            self.assertIn(b'<a href="/signup">Sign up</a>', response.data)

    def test_homepage_for_logged_in_user(self):

        with self.client:
            with self.client.session_transaction() as s:

                # create a fake session and store user id into current user key
                s[CURR_USER_KEY] = self.user.id
                print(f"\n\n\nKEY: {s[CURR_USER_KEY]}\n\n\n")
                print(f"\n\n\nUSER: {self.user}\n\n\n")

            response = self.client.get("/")

            # test for homepage for logged in user
            self.assertIn(b'<a href="/logout">Log out</a>', response.data)
