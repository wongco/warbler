"""User model tests."""

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

db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        FollowersFollowee.query.delete()

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

        self.client = app.test_client()

    def test_user_model(self):
        """Does basic model work?"""

        # User should have no messages & no followers
        self.assertEqual(len(self.user1.messages), 0)
        self.assertEqual(len(self.user1.followers), 0)

    def test_user_repr(self):
        """Does Repr return correct format?"""

        self.assertEqual(
            repr(self.user1),
            f"<User #{self.user1.id}: testuser, test@test.com>")

    def test_is_following_method(self):
        """Assert user is following another user."""

        # Append User1 to User2 followers
        self.user2.followers.append(self.user1)

        # user1 is following user2 should be True
        self.assertEqual(self.user1.is_following(self.user2), True)

        # user2 is following user1 should be False
        self.assertEqual(self.user2.is_following(self.user1), False)

    def test_is_followed_by_method(self):
        """Assert that user1.is_following(user2)."""

        # Append User1 to User2 followers
        self.user2.followers.append(self.user1)

        # user1 is following user2 should be True
        self.assertEqual(self.user2.is_followed_by(self.user1), True)

        # user2 is following user1 should be False
        self.assertEqual(self.user1.is_followed_by(self.user2), False)

    def test_user_signup_classmethod_success(self):
        """Test User.signup() classmethod succeeds."""

        u = User.signup(
            email="test3@test.com",
            username="testuser3",
            password="HASHED_PASSWORD3",
            image_url="/static/images/default-pic.png")

        test_user = User.query.filter_by(username="testuser3").first()

        self.assertEqual(u, test_user)
        # self.assertIn("testuser3", repr(u))

    def test_user_authenticate_classmethod(self):
        """Test User.authenticate() classmethod."""

        u = User.signup(
            email="test3@test.com",
            username="testuser3",
            password="HASHED_PASSWORD3",
            image_url="/static/images/default-pic.png")

        # Assert authentication with proper credentials succeeds
        self.assertEqual(User.authenticate("testuser3", "HASHED_PASSWORD3"), u)
        # Assert authentication with wrong usearname returns False
        self.assertEqual(
            User.authenticate("testuser5", "HASHED_PASSWORD3"), False)
        # Assert authentication with wrong password returns False
        self.assertEqual(
            User.authenticate("testuser3", "HASHED_PASSWORD2"), False)
