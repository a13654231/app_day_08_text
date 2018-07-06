import pytest,allure

class Test_001:

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_002(self):
        assert 2

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_003(self):
        assert 3

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_004(self):
        assert 4

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_005(self):
        assert 2

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="测试步骤001")
    def test_001_1(self):
        allure.attach("我是描述","我是描述内容")
        assert 0

    @allure.step(title="测试步骤002")
    def test_001_2(self):
        assert 1