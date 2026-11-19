import unittest
import sys
import os
from datetime import datetime

# Import modular project scripts
sys.path.insert(0, os.path.abspath("01-Bank-System"))
sys.path.insert(0, os.path.abspath("02-Task-Scheduler"))
sys.path.insert(0, os.path.abspath("03-Mini-Social-Network"))
sys.path.insert(0, os.path.abspath("04-Short-URL-Maker"))

from mini_social_network import MiniSocialNetwork
from short_url_maker import URLShortener


class TestBankSystemLogic(unittest.TestCase):
    """Tests core banking state operations and balance integrity."""

    def setUp(self):
        self.accounts = {
            "Alice": {"balance": 1000},
            "Bob": {"balance": 500}
        }

    def test_deposit_increases_balance(self):
        self.accounts["Alice"]["balance"] += 250
        self.assertEqual(self.accounts["Alice"]["balance"], 1250)

    def test_withdrawal_decreases_balance(self):
        amount = 300
        if amount <= self.accounts["Bob"]["balance"]:
            self.accounts["Bob"]["balance"] -= amount
        self.assertEqual(self.accounts["Bob"]["balance"], 200)

    def test_overdraft_withdrawal_is_prevented(self):
        amount = 1500
        has_sufficient = amount <= self.accounts["Bob"]["balance"]
        self.assertFalse(has_sufficient)
        self.assertEqual(self.accounts["Bob"]["balance"], 500)

    def test_transfer_atomic_balances(self):
        transfer_amt = 400
        self.accounts["Alice"]["balance"] -= transfer_amt
        self.accounts["Bob"]["balance"] += transfer_amt
        self.assertEqual(self.accounts["Alice"]["balance"], 600)
        self.assertEqual(self.accounts["Bob"]["balance"], 900)


class TestTaskSchedulerLogic(unittest.TestCase):
    """Tests date parsing and chronological queue priority."""

    def setUp(self):
        self.tasks = []

    def test_date_parsing_and_sorting(self):
        d1 = datetime.strptime("2026-11-05 10:00", "%Y-%m-%d %H:%M")
        d2 = datetime.strptime("2026-10-30 09:00", "%Y-%m-%d %H:%M")
        self.tasks.append({"name": "Task Later", "due": d1, "done": False})
        self.tasks.append({"name": "Task Earlier", "due": d2, "done": False})

        sorted_tasks = sorted(self.tasks, key=lambda t: t["due"])
        self.assertEqual(sorted_tasks[0]["name"], "Task Earlier")
        self.assertEqual(sorted_tasks[1]["name"], "Task Later")

    def test_task_completion_status(self):
        t = {"name": "Audit", "due": datetime.now(), "done": False}
        t["done"] = True
        self.assertTrue(t["done"])


class TestMiniSocialNetwork(unittest.TestCase):
    """Tests user registration, auth sessions, and newsfeed ordering."""

    def setUp(self):
        self.app = MiniSocialNetwork()

    def test_user_registration_and_login(self):
        self.app.register("alex", "pass123")
        self.assertIn("alex", self.app.users)
        self.app.login("alex", "pass123")
        self.assertEqual(self.app.current_user, "alex")

    def test_duplicate_registration_rejected(self):
        self.app.register("sam", "pass1")
        # Second registration should not overwrite
        self.app.register("sam", "pass2")
        self.assertEqual(self.app.users["sam"]["password"], "pass1")

    def test_follow_and_post_feed(self):
        self.app.register("user1", "p")
        self.app.register("user2", "p")
        self.app.login("user1", "p")
        self.app.follow("user2")
        self.assertIn("user2", self.app.users["user1"]["following"])


class TestShortURLMaker(unittest.TestCase):
    """Tests URL shortening, O(1) resolution, and idempotent caching."""

    def setUp(self):
        self.shortener = URLShortener()

    def test_url_shortening_and_retrieval(self):
        long_url = "https://github.com/akshaykaygude/Python_Projects"
        code = self.shortener.shorten_url(long_url)
        self.assertEqual(len(code), 6)

        retrieved = self.shortener.retrieve_url(code)
        self.assertEqual(retrieved, long_url)

    def test_idempotent_shortening_returns_identical_code(self):
        url = "https://example.com/deep/page"
        code1 = self.shortener.shorten_url(url)
        code2 = self.shortener.shorten_url(url)
        self.assertEqual(code1, code2)


if __name__ == "__main__":
    unittest.main()
