import os.path
import time
import pytest


# pytest可以直接获取rootdir路径
def get_rootdir(request):
    # 根目录
    rootdir = request.config.rootdir
    return rootdir


@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_name = 'logs/' + now + '.logs'

    request.config.pluginmanager.get_plugin("logging-plugin").set_log_path(os.path.join(get_rootdir(request), log_name))
