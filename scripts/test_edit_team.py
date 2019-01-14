import unittest
import requests
import json
from base.base_action import get_url, get_params, get_res, now_time, start_log, runtime, end_log, get_team_id, \
    params_log, res_log, assert_equal, create_team, delete_team, random_team_name
from base.logger import Log


class TestEditTeam(unittest.TestCase):

    url = get_url('data', 'edit_team', 'url')
    res = get_res('data', 'edit_team', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('编辑团队接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_edit_team(self):
        u"""编辑团队接口"""
        create_team()
        teamId = get_team_id()
        team_name = random_team_name()
        new_params = dict(teamId, **team_name)
        logger.warning(params_log + str(new_params))
        r = requests.post(url=self.url, data=new_params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        delete_team(teamId)
