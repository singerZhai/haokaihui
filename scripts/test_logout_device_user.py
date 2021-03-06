import json
import unittest
import requests
from base.base_action import get_url, get_res, get_user_id, start_log, params_log, res_log, end_log, now_time, runtime, \
    assert_equal
from base.logger import Log


class TestLogoutDeviceUser(unittest.TestCase):

    url = get_url('data', 'logout_device_user', 'url')
    res = get_res('data', 'logout_device_user', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('注销设备用户接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_logout_device_user(self):
        u"""注销设备用户接口"""
        userid = get_user_id()
        logger.warning(params_log + str(userid))
        r = requests.post(self.url, userid)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
