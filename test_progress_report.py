
import pytest


class Test_Progress_Report(object):
  
    
  def test_progress_report_01(self):
    assert True
    
  
  @pytest.mark.xfail(reason="passed Simply")  
  def test_progress_report_02(self):
    assert True


  @pytest.mark.skip(reason="Skip for No Reason")
  def test_progress_report_03(self):
    assert True


  @pytest.mark.xfail(reason="Failed Simply")
  def test_progress_report_04(self):
    assert False


  def test_progress_report_05(self):
    assert True is False


