import json
import unittest
import requests
from base.base_action import get_url, get_res, get_params, start_log, params_log, res_log, end_log, now_time, \
    assert_equal, runtime
from base.logger import Log


class TestLogin(unittest.TestCase):

    login_url = get_url('data', 'login', 'url')
    login_params = get_params('data', 'login', 'params')
    login_res = get_res('data', 'login', 'res')
    fast_login_url = get_url('data', 'fast_login', 'url')
    fast_login_params = get_params('data', 'fast_login', 'params')
    fast_login_res = get_res('data', 'fast_login', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('用户登录接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_login(self):
        u"""用户登录接口"""
        logger.warning(params_log + str(self.login_params))
        r = requests.post(self.login_url, self.login_params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.login_res['status'])
        assert_equal(res['msg'], self.login_res['msg'])

    @unittest.skipIf(condition=True, reason='万能验证码')
    def test_fast_login(self):
        u"""快速登录接口"""
        r = requests.post(self.fast_login_url, self.fast_login_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.fast_login_res['status'])
        self.assertEqual(res['msg'], self.fast_login_res['msg'])
