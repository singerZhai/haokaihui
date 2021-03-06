import json
import unittest
import requests
from base.base_action import get_url, get_params, get_res, start_log, params_log, res_log, end_log, now_time, runtime, \
    assert_equal
from base.logger import Log


class TestSignIn(unittest.TestCase):

    url = get_url('data', 'sign_in', 'url')
    params = get_params('data', 'sign_in', 'params')
    res = get_res('data', 'sign_in', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('用户注册接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    @unittest.skipIf(condition=True, reason='万能验证码')
    def test_sign_in(self):
        u"""用户注册接口"""
        logger.warning(params_log + str(self.params))
        r = requests.post(self.url, self.params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
