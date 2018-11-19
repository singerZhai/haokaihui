import unittest
import requests
from base.base_action import get_url, get_res, get_token, create_task_in_meeting_and_return_meeting_id


class TestSearchTaskInMeeting(unittest.TestCase):

    url = get_url('data', 'search_task_in_meeting', 'url')
    res = get_res('data', 'search_task_in_meeting', 'res')

    def test_search_task_in_meeting(self):
        u"""查询会议中的任务接口"""
        meetingId_dict = create_task_in_meeting_and_return_meeting_id()
        userToken = get_token()
        params = dict(userToken, **meetingId_dict)
        r = requests.post(self.url, params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])