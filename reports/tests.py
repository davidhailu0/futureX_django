from django.test import TestCase
from unittest.mock import patch

class SummaryReportTests(TestCase):
    @patch("reports.services.requests.get")
    def test_summary_ok(self, mock_get):
        mock_get.side_effect = [
            type("r", (), {"json": lambda: [{"id":1,"name":"A","email":"a@x"}], "raise_for_status": lambda: None}),
            type("r", (), {"json": lambda: [
                {"id":1,"userId":1,"title":"T1","category":"CatA"},
                {"id":2,"userId":1,"title":"T2","category":"CatA"},
                {"id":3,"userId":1,"title":"T3","category":"CatB"},
            ], "raise_for_status": lambda: None})
        ]
        res = self.client.get("/report/summary")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["totalUsers"], 1)
        self.assertEqual(res.json()["totalVideos"], 3)
        self.assertEqual(res.json()["topCategories"][0]["category"], "CatA")
        self.assertEqual(res.json()["topCategories"][0]["count"], 2)
    @patch("reports.services.requests.get")
    def test_user_report_found(self, mock_get):
        # First call: /users, Second: /videos
        mock_get.side_effect = [
            type("r", (), {"json": lambda: [{"id":2,"name":"B","email":"b@x"}], "raise_for_status": lambda: None}),
            type("r", (), {"json": lambda: [
                {"id":1,"userId":2,"title":"T1","category":"CatA"},
                {"id":2,"userId":3,"title":"T2","category":"CatA"},
            ], "raise_for_status": lambda: None})
        ]
        res = self.client.get("/report/user/2")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["user"]["id"], 2)
        self.assertEqual(res.json()["totals"]["videoCount"], 1)

    @patch("reports.services.requests.get")
    def test_user_report_not_found(self, mock_get):
        mock_get.side_effect = [
            type("r", (), {"json": lambda: [{"id":5,"name":"E","email":"e@x"}], "raise_for_status": lambda: None}),
            type("r", (), {"json": lambda: [], "raise_for_status": lambda: None})
        ]
        res = self.client.get("/report/user/999")
        self.assertEqual(res.status_code, 404)
    
    @patch("reports.services.requests.get")
    def test_summary_upstream_fail(self, mock_get):
        mock_get.side_effect = requests.RequestException("Upstream error")
        res = self.client.get("/report/summary")
        self.assertEqual(res.status_code, 502)
        self.assertIn("error", res.json())

