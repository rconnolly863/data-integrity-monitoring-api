from compare import compare_data

def test_compare_data_finds_issues():
    issues = compare_data()
    assert len(issues) >= 1