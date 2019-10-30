# -*- coding: utf-8 -*-
from django.test import TestCase
from .views import check_time


class CheckTimeTrueTest(TestCase):
    def test_check_time_true(self):
        '''
        강의 시간이 겹치지 않는 경우 확인 테스트 케이스
        '''
        self.assertTrue(check_time(9, 10, 10, 11),
                        "등록된 강의의 종료시간과 등록 할 강의의 시작시간이 겹치는 경우")

        self.assertTrue(check_time(9, 10, 15, 16),
                        "등록된 강의가 먼저 종료하고 겹치지 않는 경우")
        self.assertTrue(check_time(13, 15, 12, 13),
                        "등록된 강의의 시작시간과 등록 할 강의의 종료시간이 겹치는 경우")
        self.assertTrue(check_time(13, 15, 9, 10),
                        "등록된 강의가 나중에 종료하고 겹치지 않는 경우")

    def test_check_time_false(self):
        '''
        강의 시간이 겹치는 경우 확인 테스트 케이스
        '''
        self.assertFalse(check_time(9, 12, 10, 11),
                         "등록된 강의 중간에 등록할 강의가 시작하는 경우")
        self.assertFalse(check_time(10, 12, 10, 12),
                         "등록된 강의와 등록된 강의의 시간이 같은 경우")


if __name__ == "__main__":
    unittest.main()
