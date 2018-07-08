import pytest


@pytest.mark.bashcomp(
    ignore_env=r"^[+-]_scp_path_esc=",
)
class TestSshfs(object):

    @pytest.mark.complete("sshfs ./")
    def test_1(self, completion):
        assert completion.list
