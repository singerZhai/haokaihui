import json
import unittest
import requests
from base.base_action import get_url, get_params, get_res, start_log, params_log, res_log, end_log, now_time, runtime, \
    assert_equal, random_device_Udid
from base.logger import Log


class TestSignInDeviceUser(unittest.TestCase):

    url = get_url('data', 'sign_in_device_user', 'url')
    params = get_params('data', 'sign_in_device_user', 'params')
    res = get_res('data', 'sign_in_device_user', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('注册设备用户接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_sign_in_device_user(self):
        u"""注册设备用户接口"""
        Udid = random_device_Udid()
        new_params = dict(Udid, **self.params)
        logger.warning(params_log + str(new_params))
        r = requests.post(url=self.url, data=new_params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
