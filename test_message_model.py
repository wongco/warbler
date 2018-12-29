"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py

import os
from unittest import TestCase

from models import db, User, Message, FollowersFollowee, Like

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

db.create_all()


class MessageModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        FollowersFollowee.query.delete()
        Like.query.delete()

        self.user1 = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD1")

        self.user2 = User(
            email="test2@test.com",
            username="testuser2",
            password="HASHED_PASSWORD2")

        db.session.add(self.user1)
        db.session.add(self.user2)
        db.session.commit()

        self.message1 = Message(text="GreatScott!", user_id=self.user1.id)

        self.message2 = Message(text="Bollocks!", user_id=self.user2.id)

        db.session.add(self.message1)
        db.session.add(self.message2)
        db.session.commit()

        self.client = app.test_client()

    def test_message_model(self):
        """Does basic model work?"""

        self.assertEqual(len(self.user1.messages), 1)
        self.assertEqual(len(self.user2.messages), 1)

    def test_user_repr(self):
        """Does Repr return correct format?"""

        self.assertEqual(repr(self.message1), f"<Message {self.message1.id}>")

    def test_message_relationship(self):
        """Can we access the user through the backref?"""

        u = self.message1.user
        u2 = self.message2.user
        self.assertEqual(u, self.user1)
        self.assertEqual(u2, self.user2)
